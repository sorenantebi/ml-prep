"""Challenge 14 - LoRA Adapters: Zero Init, Merging, Multi-Adapter Serving (Medium)

PROBLEM
-------
Implement LoRA (Hu et al., 2021) for a single linear layer, plus the batched
dispatch that lets one copy of the base weights serve many fine-tunes at once.

    LoRALinear(W, r, alpha, seed)
        W       base weight of shape (d, k), frozen
        A       shape (d, r), drawn from N(0, 1/r): variance 1/r, scale 1/sqrt(r)
        B       shape (r, k), all zeros
        scaling alpha / r

    forward(x) -> x @ W + (alpha / r) * (x @ A) @ B
        Keep the two thin matmuls. Forming A @ B here materialises a d x k
        matrix on every step and throws away the whole point of the method.
    merge() -> a single (d, k) matrix, W + (alpha / r) * A @ B, leaving W alone.
    trainable_params() -> entries in A and B
    param_ratio()      -> trainable_params() / W.size

    apply_adapters(x, base_W, adapters, request_ids) -> (batch, k)
        Batched multi-adapter serving, the S-LoRA idea. x is (batch, d) and
        request_ids is a (batch,) array of indices into `adapters`, where -1
        means "base model, no adapter". Run the base projection ONCE for the
        whole batch, then add each adapter's low-rank delta to the rows that
        asked for it, gathered by adapter id. A per-request Python loop over
        the base matmul is the wrong answer.

Constraints: numpy and the standard library only, float64, seeded throughout.

INTERVIEW NOTES
---------------
A strong solution demonstrates:
- Why B starts at zero and A does not. At step 0 the delta is exactly zero, so
  the adapted layer reproduces the pretrained one bit for bit. But dL/dB is
  proportional to (x @ A) transposed, so zeroing A as well would leave B with
  no gradient forever. One side zero, one side random. The exact distribution
  of A matters far less: the paper says Gaussian, Hugging Face PEFT defaults to
  Kaiming-uniform, and N(0, 1/r) here is simply a fixed, testable choice.
- Why the update is scaled by alpha / r rather than alpha. The paper's aim is
  that, with Adam, changing r should not force a fresh learning-rate sweep, so
  it fixes alpha and tunes r. Practitioners often set alpha = 2r instead, which
  pins the scaling at 2. rsLoRA (Kalajdzievski, 2023) shows alpha / r shrinks
  the update too much at high rank and argues for alpha / sqrt(r); PEFT
  exposes it as use_rslora.
- The cost model: r(d + k) trainable entries against d*k frozen ones. At
  d = k = 4096 and r = 8 that is under 0.4 percent of the layer. Gradients and
  optimizer state shrink with it. In mixed-precision Adam fine-tuning each
  parameter costs ~16 bytes: 2 for the bf16 weight, 2 for its gradient and 12
  for the fp32 master copy and two moments, so LoRA drops ~14 of those 16 on
  every frozen weight. Activations do not shrink, so long sequences still need
  checkpointing.
- Merging is a deployment decision, not a correctness one. The merged matrix is
  one matmul of the original shape, so inference overhead is zero, but it now
  serves exactly one tenant. Left unmerged you pay two thin matmuls per token
  and buy hot-swapping: one base copy, many adapters batched together.
- Merging into a quantized base is lossy. The base sits on a discrete grid and
  the delta does not, so you dequantize, add, and requantize, and that rounding
  is not the rounding the adapter trained against (QLoRA trains the adapter
  against the quantized base). Keep it unmerged, or merge before quantizing.
Common mistakes: random B, which corrupts the model on step 0; scaling by alpha
alone or dropping the scaling; computing A @ B inside forward; leaving W
trainable; looping request by request in the serving path; expecting merged and
unmerged to agree bit for bit in fp16, or merging to be undone by subtraction.
Follow-ups: DoRA, which splits the update into magnitude and direction; QLoRA
with an NF4 base and higher-precision adapters; which projections to adapt and
how that trades against r; rank scheduling, as in AdaLoRA; stacking several
adapters and the interference that follows; paged adapter memory (S-LoRA) and
segmented gather kernels such as Punica's SGMV for the gathered low-rank matmul
in a real server, the approach behind multi-LoRA serving in vLLM and SGLang.
"""

from typing import Sequence

import numpy as np


# --------------------------------------------------------------------------- layer

class LoRALinear:
    """A frozen linear layer with a trainable rank-r update."""

    def __init__(self, W: np.ndarray, r: int, alpha: float, seed: int = 0):
        W = np.asarray(W, dtype=np.float64)
        if W.ndim != 2:
            raise ValueError("W must be 2-D, shape (d, k)")
        d, k = W.shape
        if not 1 <= r <= min(d, k):
            raise ValueError(f"require 1 <= r <= min(d, k) = {min(d, k)}, got {r}")

        self.W = W                      # frozen, never written to
        self.r = int(r)
        self.alpha = float(alpha)
        self.scaling = self.alpha / self.r
        rng = np.random.default_rng(seed)
        self.A = rng.normal(0.0, 1.0 / np.sqrt(self.r), size=(d, self.r))
        self.B = np.zeros((self.r, k))  # zero init: the delta starts at exactly 0

    def forward(self, x: np.ndarray) -> np.ndarray:
        x = np.asarray(x, dtype=np.float64)
        # (x @ A) @ B, left to right: two thin matmuls, no d x k intermediate.
        return x @ self.W + self.scaling * (x @ self.A) @ self.B

    def delta(self) -> np.ndarray:
        """The full (d, k) weight update. Fine offline, never in the hot path."""
        return self.scaling * (self.A @ self.B)

    def merge(self) -> np.ndarray:
        return self.W + self.delta()    # a new array; self.W is untouched

    def trainable_params(self) -> int:
        return self.A.size + self.B.size

    def param_ratio(self) -> float:
        return self.trainable_params() / self.W.size


# --------------------------------------------------------------------------- serving

def apply_adapters(x: np.ndarray, base_W: np.ndarray,
                   adapters: Sequence[LoRALinear],
                   request_ids: Sequence[int]) -> np.ndarray:
    """Run one batch through one base weight and per-request LoRA adapters."""
    x = np.asarray(x, dtype=np.float64)
    ids = np.asarray(request_ids, dtype=np.int64)
    if x.ndim != 2:
        raise ValueError("x must be 2-D, shape (batch, d)")
    if ids.shape != (x.shape[0],):
        raise ValueError("request_ids must have one entry per row of x")

    y = x @ base_W                      # one shared matmul for the whole batch
    for adapter_id in np.unique(ids):
        if adapter_id < 0:
            continue                    # base model, no delta
        if adapter_id >= len(adapters):
            raise ValueError(f"no adapter with id {int(adapter_id)}")
        rows = np.flatnonzero(ids == adapter_id)
        adapter = adapters[int(adapter_id)]
        # Gather the rows for this adapter, apply its rank-r delta, scatter back.
        y[rows] += adapter.scaling * (x[rows] @ adapter.A) @ adapter.B
    return y


class _MatmulCounter(np.ndarray):
    """Test scaffolding: an ndarray that records every matmul it takes part in."""
    calls: list = []

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        if ufunc is np.matmul:
            _MatmulCounter.calls.append(1)
        plain = tuple(np.asarray(i) if isinstance(i, _MatmulCounter) else i
                      for i in inputs)
        return getattr(ufunc, method)(*plain, **kwargs)


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    d, k, r = 64, 48, 8
    W = rng.normal(0.0, 1.0 / np.sqrt(d), size=(d, k))
    x = rng.normal(size=(6, d))

    # 1. Zero-init B: at step 0 the adapted layer IS the base layer, exactly.
    lora = LoRALinear(W, r=r, alpha=16, seed=1)
    assert lora.A.shape == (d, r) and lora.B.shape == (r, k)
    assert np.array_equal(lora.forward(x), x @ W)          # bit for bit, not allclose
    assert np.count_nonzero(lora.B) == 0                   # B is zeroed
    assert np.count_nonzero(lora.A) == lora.A.size         # A breaks the symmetry

    # The killer: a plausible-looking random B corrupts the pretrained model
    # before a single gradient step, which is why B is zeroed and A is not.
    broken = LoRALinear(W, r=r, alpha=16, seed=1)
    broken.B = rng.normal(0.0, 0.05, size=broken.B.shape)
    assert not np.allclose(broken.forward(x), x @ W, atol=1e-3)

    # Zeroing A as well would be worse than useless: dL/dB = s (x @ A).T @ dY,
    # so the adapter would sit at zero gradient forever.
    dY = rng.normal(size=(6, k))

    def grad_B(a: np.ndarray) -> np.ndarray:
        return lora.scaling * (x @ a).T @ dY

    assert np.max(np.abs(grad_B(lora.A))) > 1e-6           # trainable from step 0
    assert np.array_equal(grad_B(np.zeros_like(lora.A)), np.zeros((r, k)))

    # 2. Merged and unmerged compute the same function.
    trained = LoRALinear(W, r=r, alpha=16, seed=2)
    trained.B = rng.normal(0.0, 0.05, size=trained.B.shape)   # stand-in for training
    merged = trained.merge()
    assert merged.shape == (d, k)
    assert np.max(np.abs(trained.forward(x) - x @ merged)) < 1e-12
    assert np.array_equal(trained.W, W)                    # merge must not touch W
    assert np.max(np.abs(merged - W)) > 1e-3               # the test is not vacuous

    # 3. The scaling really is alpha / r, not alpha and not 1.
    a1 = LoRALinear(W, r=8, alpha=8, seed=5)               # scaling 1.0
    a2 = LoRALinear(W, r=8, alpha=16, seed=5)              # scaling 2.0, same A
    assert np.array_equal(a1.A, a2.A) and a1.scaling == 1.0 and a2.scaling == 2.0
    trained_B = rng.normal(0.0, 0.05, size=a1.B.shape)
    a1.B, a2.B = trained_B, trained_B.copy()
    delta_1, delta_2 = a1.forward(x) - x @ W, a2.forward(x) - x @ W
    assert np.max(np.abs(delta_1)) > 1e-3                  # not vacuous
    assert np.max(np.abs(delta_2 - 2.0 * delta_1)) < 1e-12
    assert np.max(np.abs(delta_2 - (16 / 8) * (x @ a2.A @ a2.B))) < 1e-12

    # 4. Parameter budget: d = k = 4096, r = 8 is well under one percent.
    W_big = np.zeros((4096, 4096))
    r8, r32 = LoRALinear(W_big, 8, 16, seed=3), LoRALinear(W_big, 32, 16, seed=3)
    assert r8.trainable_params() == 8 * (4096 + 4096) == 65536
    assert r8.param_ratio() < 0.01
    assert abs(r8.param_ratio() - 65536 / 4096 ** 2) < 1e-15
    assert abs(r32.param_ratio() - 4 * r8.param_ratio()) < 1e-15  # linear in r

    # 5. The delta is rank-limited by construction: rank <= r, whatever alpha is.
    assert np.linalg.matrix_rank(trained.delta()) == r
    assert np.linalg.matrix_rank(merged - W) <= r
    assert np.linalg.matrix_rank(W) == min(d, k)           # the base is full rank
    rank_one = LoRALinear(W, r=1, alpha=8, seed=4)
    rank_one.B = rng.normal(0.0, 0.05, size=rank_one.B.shape)
    assert np.linalg.matrix_rank(rank_one.delta()) == 1

    # 6. Batched multi-adapter dispatch matches a per-request loop.
    base = rng.normal(0.0, 1.0 / np.sqrt(d), size=(d, k))
    adapters = []
    for i in range(3):
        ad = LoRALinear(base, r=r, alpha=16, seed=10 + i)
        ad.B = rng.normal(0.0, 0.05, size=ad.B.shape)      # each tenant trained apart
        adapters.append(ad)
    batch = rng.normal(size=(9, d))
    ids = np.array([0, 2, 1, 1, -1, 0, 2, -1, 1])
    # Adapters must be distinguishable, otherwise dispatch cannot be tested.
    assert not np.allclose(adapters[0].forward(batch[0]), adapters[1].forward(batch[0]))

    out = apply_adapters(batch, base, adapters, ids)
    expected = np.stack([batch[i] @ base if ids[i] < 0
                         else adapters[ids[i]].forward(batch[i])
                         for i in range(len(ids))])
    assert out.shape == (9, k) and np.max(np.abs(out - expected)) < 1e-12
    assert np.max(np.abs(out[4] - batch[4] @ base)) < 1e-12       # id -1 is untouched
    assert np.max(np.abs(out[0] - batch[0] @ base)) > 1e-3        # id 0 is not

    # The point of batched dispatch: one base matmul, however many adapters and
    # rows are in flight. A per-request loop passes the check above and fails here.
    _MatmulCounter.calls.clear()
    counted = base.view(_MatmulCounter)
    out2 = apply_adapters(batch, counted, adapters, ids)
    assert len(_MatmulCounter.calls) == 1
    assert np.max(np.abs(out2 - expected)) < 1e-12

    # 7. Init statistics and reproducibility.
    W_sq = np.zeros((512, 512))
    stats, same = LoRALinear(W_sq, 8, 8, seed=7), LoRALinear(W_sq, 8, 8, seed=7)
    other = LoRALinear(W_sq, 8, 8, seed=8)
    assert abs(np.var(stats.A) - 1.0 / 8) < 0.02 and abs(np.mean(stats.A)) < 0.03
    assert np.array_equal(stats.A, same.A) and not np.array_equal(stats.A, other.A)

    # 8. Input validation.
    for bad_rank in (0, -1, min(d, k) + 1):
        try:
            LoRALinear(W, r=bad_rank, alpha=16, seed=0)
            assert False, f"rank {bad_rank} should be rejected"
        except ValueError:
            pass
    for bad_ids in (np.array([0, 1]), np.array([0, 1, 9] + [0] * 6)):
        try:
            apply_adapters(batch, base, adapters, bad_ids)
            assert False, "bad request_ids should be rejected"
        except ValueError:
            pass

    print("All tests passed.")
