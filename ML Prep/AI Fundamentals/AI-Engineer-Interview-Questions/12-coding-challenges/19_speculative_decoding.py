"""Challenge 19 - Speculative Decoding: Draft, Verify, Accept (Hard)

PROBLEM
-------
A small draft model proposes gamma tokens, the large target model verifies all
of them in one forward pass, and the accept/reject rule keeps the output
distribution exactly equal to the target's. Implement it, then prove by test
that it is lossless. Both models here are seeded probability tables, so the
tests are deterministic:
    draft_probs_fn(prefix) -> array (V,), one sequential step
    target_probs_fn(prefix, continuation) -> array (len(continuation) + 1, V),
        ONE forward pass scoring every position at once: row i is the target's
        distribution for the token following prefix + continuation[:i]

Implement:

    draft_tokens(draft_probs_fn, prefix, gamma, rng) -> (tokens, q_probs)
        sample gamma tokens autoregressively from the draft, returning the
        tokens and the distribution used at each position (keep them:
        re-running the draft to recover q defeats the point)

    speculative_step(target_probs_fn, draft_probs_fn, prefix, gamma, rng)
        -> (accepted_tokens, n_target_calls)
        - draft gamma tokens, then call the target exactly once
        - accept each drafted x_i, in order, with prob min(1, p_i(x_i)/q_i(x_i))
        - on the first rejection emit one token from the residual
          norm(max(p_i - q_i, 0)) and stop, discarding the rest of the draft
        - if all gamma are accepted, emit a bonus token from p_gamma, which
          that same forward pass already paid for
        - output length is n_accepted + 1, always in [1, gamma + 1], and
          n_target_calls is 1 for any gamma, gamma = 0 included (that case
          degenerates to plain autoregressive sampling)

    residual_distribution(p, q) -> array (V,)
        max(p - q, 0) renormalised, falling back to p if the residual mass is
        zero (unreachable after a real rejection, but do not divide by zero)

INTERVIEW NOTES
---------------
A strong solution demonstrates:
- WHY it is lossless, in one line. P(emit t at the drafted position)
  = q(t) * min(1, p(t)/q(t)) + P(reject) * residual(t) = min(p(t), q(t))
  + (p(t) - q(t))+ = p(t), since P(reject) is exactly sum_t (p(t) - q(t))+,
  the normaliser the residual divides by. No approximation, no quality knob.
- WHY it is a memory-bandwidth win, not a FLOPs win. Batch-1 decoding streams
  every weight from HBM to produce one token, roughly one multiply-accumulate
  per weight loaded, so the arithmetic units idle while memory works. Verifying
  gamma + 1 positions in one pass reads those weights once and does gamma + 1
  times the arithmetic on them: total FLOPs go UP (rejected drafts are wasted
  work), wall-clock latency goes down.
- The crossover where it stops paying. With i.i.d. acceptance rate a, expected
  output per step is (1 - a^(gamma+1)) / (1 - a), saturating in gamma while
  draft cost stays linear in it, so there is an optimal gamma per model pair.
  Raising the batch size makes the target pass compute-bound, the spare
  arithmetic disappears and the wasted work becomes real time: a latency
  optimisation for small-batch serving that can cut throughput on a saturated
  server. The exception is long context, where KV-cache reads keep even large
  batches memory-bound and speculation can pay again. Too big a draft pays its
  own latency gamma times per step; too weak a draft drives a towards zero.
  Serving engines therefore tune gamma per workload or adapt it at runtime.
Common mistakes: resampling from p rather than the residual after a rejection
(nothing crashes, output silently drifts towards what the draft over-proposes);
accepting on argmax agreement, defensible only at temperature 0 and still
biased once you sample; forgetting the bonus token; not rolling back BOTH KV
caches past the rejected position; measuring the win in FLOPs.
Follow-ups: tree or multi-candidate drafting; n-gram or prompt-lookup drafting
with no draft model at all; self-speculation via early-exit layers; draft
heads on the target's own hidden states (Medusa, EAGLE) and multi-token
prediction heads trained with the model (DeepSeek-V3), both of which often
replace a separate draft model in production; lenient acceptance
thresholds that buy speed by giving up exactness; ragged batching when
sequences accept different numbers of tokens. References: Leviathan et
al., 2023, "Fast Inference from Transformers via Speculative Decoding"; Chen
et al., 2023, "Accelerating Large Language Model Decoding with Speculative
Sampling".
"""

from typing import Callable, Sequence

import numpy as np

Probs = np.ndarray
DraftFn = Callable[[Sequence[int]], Probs]
TargetFn = Callable[[Sequence[int], Sequence[int]], Probs]


# ----------------------------------------------------------------- primitives

def sample_token(probs: Probs, rng: np.random.Generator) -> int:
    """Inverse-CDF categorical sample: cheaper and more predictable than choice()."""
    idx = int(np.searchsorted(np.cumsum(probs), rng.random(), side="right"))
    return min(idx, probs.shape[0] - 1)  # guard against a cumsum ending at 1-eps


def residual_distribution(p: Probs, q: Probs) -> Probs:
    """norm(max(p - q, 0)): the mass the target still owes after the draft's share."""
    residual = np.clip(p - q, 0.0, None)
    total = residual.sum()
    if total <= 0.0:  # p == q, so no rejection can reach here; stay safe anyway
        return np.asarray(p, dtype=float) / np.sum(p)
    return residual / total


class TableModel:
    """Toy autoregressive model: next-token distribution keyed on the last token.

    Two call protocols, because that is how the models really run: the draft
    one step at a time, the target once over a whole block.
    """

    def __init__(self, table: np.ndarray):
        self.table = table
        self.calls = 0

    @classmethod
    def random(cls, vocab_size: int, seed: int) -> "TableModel":
        logits = np.random.default_rng(seed).normal(size=(vocab_size, vocab_size))
        e = np.exp(logits - logits.max(axis=1, keepdims=True))
        return cls(e / e.sum(axis=1, keepdims=True))

    def next_probs(self, prefix: Sequence[int]) -> Probs:
        self.calls += 1
        return self.table[prefix[-1]]

    def batch_probs(self, prefix: Sequence[int], continuation: Sequence[int]) -> Probs:
        self.calls += 1  # one forward pass, however long the continuation
        return self.table[[prefix[-1], *continuation]]


def interpolate(draft: TableModel, target: TableModel, alpha: float) -> TableModel:
    """Mix a draft towards the target: alpha=0 leaves it alone, alpha=1 matches it."""
    return TableModel((1.0 - alpha) * draft.table + alpha * target.table)


# ----------------------------------------------------------------- the sampler

def draft_tokens(draft_probs_fn: DraftFn, prefix: Sequence[int], gamma: int,
                 rng: np.random.Generator) -> tuple[list[int], list[Probs]]:
    """Sample gamma tokens from the draft, keeping the distribution used at each."""
    tokens, q_probs, context = [], [], list(prefix)
    for _ in range(gamma):
        q = np.asarray(draft_probs_fn(context), dtype=float)
        tokens.append(sample_token(q, rng))
        q_probs.append(q)
        context.append(tokens[-1])  # the draft conditions on its own guesses
    return tokens, q_probs


def speculative_step(target_probs_fn: TargetFn, draft_probs_fn: DraftFn,
                     prefix: Sequence[int], gamma: int,
                     rng: np.random.Generator) -> tuple[list[int], int]:
    """One draft-and-verify round. Returns (tokens emitted, target calls used)."""
    drafted, q_probs = draft_tokens(draft_probs_fn, prefix, gamma, rng)
    p_probs = target_probs_fn(prefix, drafted)  # the single expensive call
    out: list[int] = []
    for i, token in enumerate(drafted):
        p, q = p_probs[i], q_probs[i]
        if rng.random() >= min(1.0, p[token] / q[token]):  # rejected: correct and stop
            return out + [sample_token(residual_distribution(p, q), rng)], 1
        out.append(token)
    return out + [sample_token(p_probs[gamma], rng)], 1  # bonus token, already paid for


def naive_greedy_step(target_probs_fn: TargetFn, draft_probs_fn: DraftFn,
                      prefix: Sequence[int], gamma: int,
                      rng: np.random.Generator) -> tuple[list[int], int]:
    """WRONG ON PURPOSE: accept when the draft token matches the target's argmax.

    The plausible variant candidates reach for, kept so the tests can show it
    failing the distributional check that the real rule passes."""
    drafted, _ = draft_tokens(draft_probs_fn, prefix, gamma, rng)
    p_probs = target_probs_fn(prefix, drafted)
    out: list[int] = []
    for i, token in enumerate(drafted):
        if token != int(np.argmax(p_probs[i])):
            return out + [sample_token(p_probs[i], rng)], 1
        out.append(token)
    return out + [sample_token(p_probs[gamma], rng)], 1


if __name__ == "__main__":
    VOCAB, PREFIX, GAMMA, TRIALS = 6, (0, 3), 4, 200_000
    target = TableModel.random(VOCAB, seed=1)
    base_draft = TableModel.random(VOCAB, seed=2)
    p_row, q_row = target.table[PREFIX[-1]], base_draft.table[PREFIX[-1]]

    def first_token_counts(step_fn, draft: TableModel) -> np.ndarray:
        """Histogram of the token emitted at the drafted position, gamma=1."""
        rng = np.random.default_rng(7)
        counts = np.zeros(VOCAB, dtype=np.int64)
        for _ in range(TRIALS):
            out, n_calls = step_fn(target.batch_probs, draft.next_probs, PREFIX, 1, rng)
            assert n_calls == 1 and 1 <= len(out) <= 2
            counts[out[0]] += 1  # out[1], if present, belongs to another context
        return counts

    def z_scores(counts: np.ndarray) -> np.ndarray:
        """Per-token deviation from the target distribution, in binomial sigmas."""
        return np.abs(counts - TRIALS * p_row) / np.sqrt(TRIALS * p_row * (1.0 - p_row))

    # 1. Losslessness: 200k single-token steps reproduce the TARGET distribution
    #    to within 3 sigma, even though every proposal came from the draft.
    z_spec = z_scores(first_token_counts(speculative_step, base_draft))
    assert z_spec.max() < 3.0, f"output is not target-distributed: {z_spec}"

    #    The argmax variant fails the same test by a mile, over-emitting the
    #    target's top token by exactly q(top) * (1 - p(top)).
    naive = first_token_counts(naive_greedy_step, base_draft)
    assert z_scores(naive).max() > 10.0, "naive variant should fail 3 sigma"
    top = int(np.argmax(p_row))
    assert abs(naive[top] / TRIALS - (q_row[top] + (1 - q_row[top]) * p_row[top])) < 0.01

    #    Position 1 with gamma=2 goes through accept/reject too, so it checks that
    #    row i of the target pass is paired with draft step i. Given an accepted
    #    first token x, the second must follow p(. | x) = target.table[x]. Pairing
    #    every drafted token with row 0 passes the test above and fails this one.
    rng = np.random.default_rng(29)
    obs, expect, var = np.zeros(VOCAB), np.zeros(VOCAB), np.zeros(VOCAB)
    for _ in range(60_000):
        out, _ = speculative_step(target.batch_probs, base_draft.next_probs, PREFIX, 2, rng)
        if len(out) >= 2:
            p_next = target.table[out[0]]
            obs[out[1]] += 1
            expect += p_next
            var += p_next * (1.0 - p_next)
    assert obs.sum() > 20_000  # enough accepted first tokens to mean something
    assert (np.abs(obs - expect) / np.sqrt(var)).max() < 3.0

    def acceptance_rate(draft: TableModel, steps: int = 4000) -> float:
        """Fraction of gamma=1 proposals accepted, so output length 2 not 1."""
        rng = np.random.default_rng(11)
        return sum(len(speculative_step(target.batch_probs, draft.next_probs, PREFIX,
                                        1, rng)[0]) - 1 for _ in range(steps)) / steps

    # 2. Interpolating the draft towards the target raises acceptance monotonically,
    #    and every point lands on the theoretical 1 - TV(p, q).
    alphas = (0.0, 0.25, 0.5, 0.75, 1.0)
    total_variation = 0.5 * np.abs(p_row - q_row).sum()
    assert total_variation > 0.2  # the draft really is a poor match to start with
    rates = [acceptance_rate(interpolate(base_draft, target, a)) for a in alphas]
    assert all(rates[i] + 0.01 < rates[i + 1] for i in range(len(alphas) - 1)), rates
    for alpha, rate in zip(alphas, rates):
        assert abs(rate - (1.0 - (1.0 - alpha) * total_variation)) < 0.02

    # 3. Draft == target: acceptance is 1.0 and every step yields gamma + 1.
    twin, rng = TableModel(target.table.copy()), np.random.default_rng(13)
    calls_before, emitted = target.calls, 0
    for _ in range(300):
        out, n = speculative_step(target.batch_probs, twin.next_probs, PREFIX, GAMMA, rng)
        assert len(out) == GAMMA + 1 and n == 1  # nothing is ever rejected
        emitted += len(out)
    # gamma + 1 tokens per forward pass, and one forward pass per step, not five.
    assert emitted / (target.calls - calls_before) == GAMMA + 1

    # 4. Target calls per emitted token beat the gamma=0 baseline.
    good_draft = interpolate(base_draft, target, 0.7)

    def calls_per_token(gamma: int, steps: int = 2000) -> float:
        rng, tokens = np.random.default_rng(17), 0
        for _ in range(steps):
            out, n_calls = speculative_step(target.batch_probs, good_draft.next_probs,
                                            PREFIX, gamma, rng)
            assert n_calls == 1 and 1 <= len(out) <= gamma + 1
            tokens += len(out)
        return steps / tokens  # exactly one target call per step, whatever gamma is

    assert calls_per_token(0) == 1.0  # gamma=0 degenerates to plain autoregression
    assert calls_per_token(GAMMA) < 0.45

    # 5. The residual is a valid distribution wherever a rejection can land.
    hand = residual_distribution(np.array([0.5, 0.3, 0.2]), np.array([0.2, 0.1, 0.7]))
    assert np.allclose(hand, [0.6, 0.4, 0.0])
    rng = np.random.default_rng(23)
    for _ in range(500):
        p, q = rng.dirichlet(np.full(VOCAB, 0.4)), rng.dirichlet(np.full(VOCAB, 0.4))
        r = residual_distribution(p, q)
        assert abs(r.sum() - 1.0) < 1e-12 and (r >= 0.0).all() and r.max() > 0.0
        assert np.clip(p - q, 0.0, None).sum() > 0.0  # a rejection needs p(x) < q(x)
    assert abs(residual_distribution(p_row, p_row.copy()).sum() - 1.0) < 1e-12  # no 0/0

    print("All tests passed.")
