"""Challenge 15 - Beam Search with Length Normalization (Medium)

PROBLEM
-------
Implement beam search over an injected next-token function, with the language
model mocked out so decoding is deterministic and testable.

Model protocol - `step_fn(prefix) -> np.ndarray` of shape (V,), the
log-probabilities of the next token given the token list `prefix`.

Implement:

    beam_search(step_fn, start_token, beam_width, max_len, eos_id,
                length_penalty=0.0) -> list[tuple[list[int], float]]

    - a beam is the token list generated after start_token; the prefix handed
      to step_fn is [start_token] + tokens
    - carry a CUMULATIVE LOG-PROBABILITY per beam: add log-probs, never
      multiply probabilities
    - each step scores all B * V continuations at once and keeps the best B
      via np.argpartition (O(B*V), not a full O(B*V log(B*V)) sort)
    - a beam whose new token is eos_id is parked in a `completed` list and
      never expanded again; the survivors carry on, and beams still alive at
      max_len are completed as they stand
    - the reported score is the GNMT length normalization (Wu et al., 2016),
      with len the number of generated tokens:
          score = logp / ((5 + len) / 6) ** length_penalty
    - return at most beam_width (tokens, score) pairs, best score first
    - an eos_id outside the vocabulary disables early stopping

INTERVIEW NOTES
---------------
A strong solution demonstrates:
- Why decoding lives in log space: 800 tokens at an average probability of
  0.25 each is 0.25**800 ~ 2e-482, far below float64's smallest subnormal
  (~5e-324), so the product is exactly 0.0. Sums stay representable,
  products do not.
- Beam width is one dial, greedy decode at one end (B=1) and exhaustive search
  at the other (B >= V**max_len). Everything between is a heuristic with no
  optimality guarantee, so a wider beam can still score worse on the metric
  you care about.
- Beam search is biased towards short sequences: every extra token adds a
  negative log-prob, so EOS looks attractive early. Length normalization
  divides that bias out, and alpha is a real tuning knob.
- Finished beams are results, not candidates. Parking them leaves the live set
  free for hypotheses that can still improve. This version lets the live set
  shrink as beams finish; Hugging Face transformers instead keeps the top 2B
  candidates per step so B beams stay alive, a trade of compute for recall.
Common mistakes: multiplying probabilities and underflowing to zero;
re-expanding a beam that already emitted EOS, which puts EOS mid-output;
killing the whole search when the top beam finishes; ranking raw log-probs
against normalized scores in the same list; sorting all B*V candidates when a
partition suffices; quoting a length_penalty value without saying which
formula it feeds (transformers divides by len**alpha, not the GNMT form).
Follow-ups: the GNMT coverage penalty; diverse beam search; batching all B
prefixes through one forward pass with a shared, copy-on-write KV cache;
min_len by masking EOS; why search suits closed-ended tasks (translation, ASR) while
open-ended generation samples instead, since high-likelihood text degenerates
into repetition (Holtzman et al., 2020); why chat LLM serving rarely offers
beam search (up to B times the KV cache, poor fit with continuous batching).
"""

import itertools
import math
from typing import Callable

import numpy as np


# --------------------------------------------------------------------------- mock LM

class MockLM:
    """Stand-in for a forward pass: a seeded (V, V) table of bigram log-probs,
    so every test below is reproducible without a model or a network call."""

    def __init__(self, vocab_size: int, seed: int = 0, sharpness: float = 1.0):
        rng = np.random.default_rng(seed)
        logits = rng.normal(size=(vocab_size, vocab_size)) * sharpness
        logits -= logits.max(axis=-1, keepdims=True)          # stable log_softmax
        self.table = logits - np.log(np.exp(logits).sum(axis=-1, keepdims=True))
        self.calls = 0

    def __call__(self, prefix: list[int]) -> np.ndarray:
        self.calls += 1
        return self.table[prefix[-1]]

    def logp(self, start_token: int, tokens: list[int]) -> float:
        """Cumulative log-prob of `tokens`, used as an independent reference."""
        total, last = 0.0, start_token
        for token in tokens:
            total += float(self.table[last][token])
            last = token
        return total


# --------------------------------------------------------------------------- search

def length_penalty_factor(length: int, alpha: float) -> float:
    """GNMT normalizer ((5 + len) / 6) ** alpha; exactly 1.0 when alpha == 0."""
    return ((5.0 + length) / 6.0) ** alpha


def greedy_decode(step_fn: Callable[[list[int]], np.ndarray], start_token: int,
                  max_len: int, eos_id: int) -> tuple[list[int], float]:
    """Reference decoder: always take the argmax. Beam search at B=1 must match."""
    prefix, tokens, total = [start_token], [], 0.0
    for _ in range(max_len):
        logprobs = np.asarray(step_fn(prefix), dtype=np.float64)
        token = int(np.argmax(logprobs))
        total += float(logprobs[token])
        tokens.append(token)
        prefix.append(token)
        if token == eos_id:
            break
    return tokens, total


def beam_search(step_fn: Callable[[list[int]], np.ndarray], start_token: int,
                beam_width: int, max_len: int, eos_id: int,
                length_penalty: float = 0.0) -> list[tuple[list[int], float]]:
    if beam_width < 1:
        raise ValueError("beam_width must be >= 1")
    if max_len < 1:
        raise ValueError("max_len must be >= 1")

    live: list[tuple[list[int], float]] = [([], 0.0)]
    completed: list[tuple[list[int], float]] = []

    for step in range(max_len):
        if not live:
            break
        rows = np.stack([np.asarray(step_fn([start_token] + toks), dtype=np.float64)
                         for toks, _ in live])
        running = np.array([logp for _, logp in live], dtype=np.float64)[:, None]
        candidates = rows + running          # addition, never multiplication
        flat = candidates.ravel()
        vocab = candidates.shape[1]

        # Partition the B*V candidates, then order only the k survivors.
        k = min(beam_width, flat.size)
        top = np.argpartition(-flat, k - 1)[:k]
        top = top[np.argsort(-flat[top], kind="stable")]

        survivors: list[tuple[list[int], float]] = []
        for idx in top:
            beam_index, token = divmod(int(idx), vocab)
            tokens = live[beam_index][0] + [token]
            logp = float(flat[idx])
            if token == eos_id or step == max_len - 1:
                completed.append((tokens, logp))   # parked, never expanded again
            else:
                survivors.append((tokens, logp))
        live = survivors

    scored = [(toks, logp / length_penalty_factor(len(toks), length_penalty))
              for toks, logp in completed]
    scored.sort(key=lambda pair: -pair[1])
    return scored[:beam_width]


if __name__ == "__main__":
    NO_EOS = -1  # an id outside the vocabulary, so nothing terminates early

    # 1. beam_width=1 reproduces greedy decode exactly, token for token.
    lm = MockLM(vocab_size=6, seed=3)
    greedy_tokens, greedy_logp = greedy_decode(lm, 5, max_len=12, eos_id=0)
    greedy_calls, lm.calls = lm.calls, 0
    beams = beam_search(lm, 5, beam_width=1, max_len=12, eos_id=0)
    assert len(beams) == 1 and beams[0][0] == greedy_tokens
    assert abs(beams[0][1] - greedy_logp) < 1e-12
    assert lm.calls == greedy_calls          # one forward pass per step, none wasted

    # 2. Exhaustive check: V=4, max_len=5, brute-force all 4**5 sequences.
    V, L, START = 4, 5, 0
    lm = MockLM(vocab_size=V, seed=10)
    brute = [(list(s), lm.logp(START, list(s)))
             for s in itertools.product(range(V), repeat=L)]
    brute.sort(key=lambda pair: -pair[1])
    exhaustive = beam_search(lm, START, beam_width=V ** L, max_len=L, eos_id=NO_EOS)
    assert len(brute) == len(exhaustive) == V ** L       # every sequence retained
    assert brute[0][1] > brute[1][1]                     # the argmax is unique
    assert exhaustive[0][0] == brute[0][0]               # and beam search finds it
    # Permuted transition multisets tie under a bigram table: rank scores, set sequences.
    for (_, got), (_, want) in zip(exhaustive, brute):
        assert abs(got - want) < 1e-12
    assert {tuple(t) for t, _ in exhaustive} == {tuple(t) for t, _ in brute}

    # A narrow beam is a heuristic: it beats greedy here and still misses the argmax.
    narrow = beam_search(lm, START, beam_width=2, max_len=L, eos_id=NO_EOS)
    _, greedy_score = greedy_decode(lm, START, max_len=L, eos_id=NO_EOS)
    assert greedy_score < narrow[0][1] < brute[0][1]

    # 3. Length penalty flips the winner: EOS now (p=0.6) versus a long, nearly
    #    free run of token 1 that ends with EOS at length 8.
    first = np.log(np.array([0.6, 0.4]))
    keep = np.log(np.array([0.01, 0.99]))
    stop = np.log(np.array([0.99, 0.01]))

    def length_bias_step(prefix: list[int]) -> np.ndarray:
        generated = len(prefix) - 1
        if generated == 0:
            return first
        return keep if generated < 7 else stop

    short = beam_search(length_bias_step, 1, 2, 8, eos_id=0, length_penalty=0.0)
    long = beam_search(length_bias_step, 1, 2, 8, eos_id=0, length_penalty=1.0)
    assert short[0][0] == [0]                            # raw log-prob stops early
    assert long[0][0] == [1, 1, 1, 1, 1, 1, 1, 0]        # normalized score does not
    assert long[1][0] == [0]                             # the order actually swapped
    # The flip comes from the divisor, not from a better raw log-prob.
    long_raw = float(first[1] + 6 * keep[1] + stop[0])   # ln .4 + 6 ln .99 + ln .99
    short_raw = float(first[0])                          # ln .6
    assert long_raw < short_raw < 0.0
    assert abs(short[0][1] - short_raw) < 1e-12          # alpha=0 divides by 1.0
    assert abs(long[0][1] - long_raw / (13.0 / 6.0)) < 1e-12   # (5 + 8) / 6
    assert abs(long[1][1] - short_raw) < 1e-12
    assert abs(length_penalty_factor(4, 0.5) - math.sqrt(1.5)) < 1e-12
    assert length_penalty_factor(8, 0.0) == 1.0 == length_penalty_factor(1, 1.0)

    # 4. EOS parks one beam without truncating the others. Row 0 makes staying
    #    in EOS almost free, so re-expanding a finished beam is impossible to miss.
    eos_table = np.log(np.array([
        [0.997, 0.001, 0.001, 0.001],   # after EOS (a correct search never reads this)
        [0.62, 0.21, 0.13, 0.04],
        [0.06, 0.23, 0.59, 0.12],
        [0.04, 0.51, 0.31, 0.14],       # start row
    ]))
    results = beam_search(lambda p: eos_table[p[-1]], 3, 3, max_len=4, eos_id=0)
    assert len(results) == 3 and results[0][0] == [1, 0]   # best beam stops at len 2
    assert abs(results[0][1] - float(eos_table[3][1] + eos_table[1][0])) < 1e-12
    for tokens, _ in results:
        assert 0 not in tokens[:-1]                      # no EOS mid-sequence
        assert tokens[-1] == 0 or len(tokens) == 4       # ended, or ran to max_len
    assert any(len(tokens) == 4 for tokens, _ in results)  # others were not cut short

    # 5. Beams come back sorted by normalized score, and it is the normalized
    #    ordering: sorting on raw log-prob would put [0] first here.
    ranked = beam_search(length_bias_step, 1, 5, 8, eos_id=0, length_penalty=0.9)
    assert [s for _, s in ranked] == sorted((s for _, s in ranked), reverse=True)
    raw = [s * length_penalty_factor(len(t), 0.9) for t, s in ranked]
    assert raw != sorted(raw, reverse=True)

    lm = MockLM(vocab_size=6, seed=11)
    ranked = beam_search(lm, 2, 4, max_len=9, eos_id=1, length_penalty=0.6)
    assert len(ranked) == 4
    assert [s for _, s in ranked] == sorted((s for _, s in ranked), reverse=True)
    for tokens, score in ranked:
        want = lm.logp(2, tokens) / length_penalty_factor(len(tokens), 0.6)
        assert abs(score - want) < 1e-12

    # 6. Log space is not optional: 800 steps of ~1e-1 tokens is 0.0 as a product.
    lm = MockLM(vocab_size=8, seed=5, sharpness=0.3)
    deep = beam_search(lm, 0, beam_width=2, max_len=800, eos_id=NO_EOS)
    total = deep[0][1]
    assert math.isfinite(total) and total < -745.0   # below float64 exp underflow
    assert float(np.exp(total)) == 0.0               # multiplying probs gives 0.0
    assert abs(total - lm.logp(0, deep[0][0])) < 1e-9

    # 7. Argument validation.
    for bad in ({"beam_width": 0}, {"max_len": 0}):
        try:
            beam_search(lm, 0, eos_id=NO_EOS, **{"beam_width": 2, "max_len": 4, **bad})
            assert False, f"should have rejected {bad}"
        except ValueError:
            pass

    print("All tests passed.")
