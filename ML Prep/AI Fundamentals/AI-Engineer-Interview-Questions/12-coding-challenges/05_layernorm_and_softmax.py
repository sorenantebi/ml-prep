"""Challenge 05 - Numerically stable softmax, LayerNorm, RMSNorm (Easy).

PROBLEM
-------
Numpy only:

1. softmax(x, axis=-1) -> np.ndarray
   Must not overflow for logits like 1e4 (naive exp(1e4) = inf -> nan).

2. log_softmax(x, axis=-1) -> np.ndarray
   Computed directly, NOT as np.log(softmax(x)) - that underflows to
   log(0) = -inf for strongly negative logits.

3. layer_norm(x, gamma, beta, eps=1e-5) -> np.ndarray
   Normalize over the LAST axis to zero mean / unit variance (biased
   variance, as in PyTorch), then scale and shift:
       y = (x - mean) / sqrt(var + eps) * gamma + beta

4. rms_norm(x, gamma, eps=1e-6) -> np.ndarray
   Llama-style: no mean subtraction, no beta:
       y = x / sqrt(mean(x^2) + eps) * gamma

INTERVIEW NOTES
---------------
A strong solution: subtracts the row max in softmax and explains WHY it is
exact (softmax is shift-invariant: exp(x-c)/sum(exp(x-c)) == softmax(x));
puts eps INSIDE the sqrt; uses the biased variance (ddof=0); knows RMSNorm
drops mean-centring because re-centring empirically adds little while the
mean reduction costs an extra pass - one reason Llama, Mistral, Qwen and
most current open-weight LLMs use it.

Common mistakes: eps outside the sqrt (subtly different, breaks checkpoint
parity); normalizing over the wrong axis (batch instead of features - that's
BatchNorm: outputs then depend on what else is in the batch, and in a causal
LM, statistics over the batch and time axes leak future tokens during
training); log(softmax(x)) instead of a fused log-softmax; forgetting
gamma/beta entirely.

Follow-up variations: pre-norm vs post-norm transformer blocks (pre-norm
keeps a clean residual path and tolerates little or no warmup; post-norm was
the original and is harder to train deep); why a pre-norm stack needs a
final norm before the LM head (the residual stream itself is never
normalized); QK-norm to tame attention logit growth; norms placed after the
sublayer as well as, or instead of, before it in some recent open models;
where float16 overflows first and why norms usually run in float32 even in
mixed-precision training.
"""
from __future__ import annotations

import numpy as np


def softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    x_max = np.max(x, axis=axis, keepdims=True)
    e = np.exp(x - x_max)  # largest exponent is exp(0) = 1: cannot overflow
    return e / np.sum(e, axis=axis, keepdims=True)


def log_softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    x_max = np.max(x, axis=axis, keepdims=True)
    shifted = x - x_max
    # log-sum-exp trick: logsumexp(x) = max + log(sum(exp(x - max)))
    return shifted - np.log(np.sum(np.exp(shifted), axis=axis, keepdims=True))


def layer_norm(
    x: np.ndarray, gamma: np.ndarray, beta: np.ndarray, eps: float = 1e-5
) -> np.ndarray:
    mean = x.mean(axis=-1, keepdims=True)
    var = x.var(axis=-1, keepdims=True)  # biased (ddof=0), matches PyTorch
    return (x - mean) / np.sqrt(var + eps) * gamma + beta


def rms_norm(x: np.ndarray, gamma: np.ndarray, eps: float = 1e-6) -> np.ndarray:
    rms = np.sqrt(np.mean(x * x, axis=-1, keepdims=True) + eps)
    return x / rms * gamma


if __name__ == "__main__":
    rng = np.random.default_rng(0)

    # --- softmax: stability with huge and tiny logits ---
    s = softmax(np.array([1e4, 1e4 + 1, 1e4 + 2]))
    assert np.all(np.isfinite(s)) and np.isclose(s.sum(), 1.0)
    assert np.allclose(s, softmax(np.array([0.0, 1.0, 2.0])))  # shift-invariant
    s = softmax(np.array([-1e4, -1e4 + 1]))
    assert np.all(np.isfinite(s)) and np.isclose(s.sum(), 1.0)
    # hand-computed: softmax([0, log 3]) = [1/4, 3/4]
    assert np.allclose(softmax(np.array([0.0, np.log(3.0)])), [0.25, 0.75])
    # rows of a matrix normalize independently
    m = rng.normal(size=(4, 10))
    assert np.allclose(softmax(m).sum(axis=-1), 1.0)

    # --- log_softmax: stable where log(softmax) is not ---
    x = np.array([0.0, -2000.0])
    ls = log_softmax(x)
    assert np.all(np.isfinite(ls)) and np.isclose(ls[1], -2000.0, atol=1e-6)
    with np.errstate(divide="ignore"):  # provoke the naive path on purpose
        naive = np.log(softmax(x))
    assert np.isinf(naive[1]), "naive path underflows - that's the point"
    # agrees with log(softmax) in the well-behaved regime
    y = rng.normal(size=(3, 5))
    assert np.allclose(log_softmax(y), np.log(softmax(y)))
    assert np.allclose(np.exp(log_softmax(y)).sum(axis=-1), 1.0)

    # --- layer_norm: statistics and affine parameters ---
    d = 64
    x = rng.normal(loc=5.0, scale=3.0, size=(8, d))
    ones, zeros = np.ones(d), np.zeros(d)
    y = layer_norm(x, ones, zeros)
    assert np.allclose(y.mean(axis=-1), 0.0, atol=1e-7)
    assert np.allclose(y.var(axis=-1), 1.0, atol=1e-3)  # eps makes it ~1
    y2 = layer_norm(x, 2 * ones, 3 * ones)
    assert np.allclose(y2, 2 * y + 3)
    # invariant to per-row shift and positive scale of the input
    assert np.allclose(layer_norm(4.0 * x + 7.0, ones, zeros), y, atol=1e-6)
    # hand-computed: [1, 2, 3] has mean 2 and BIASED var 2/3, so the output is
    # [-sqrt(1.5), 0, sqrt(1.5)]. Unbiased var (1.0) would give [-1, 0, 1].
    ln3 = layer_norm(np.array([1.0, 2.0, 3.0]), np.ones(3), np.zeros(3), eps=0.0)
    assert np.allclose(ln3, [-np.sqrt(1.5), 0.0, np.sqrt(1.5)])

    # --- rms_norm: hand-computed value, scale-invariance, NO shift-invariance ---
    # [2, -2, 2, -2] has mean(x^2) = 4, rms = 2; gamma then scales per feature.
    r4 = rms_norm(np.array([2.0, -2.0, 2.0, -2.0]), np.array([1.0, 2.0, 3.0, 4.0]), eps=0.0)
    assert np.allclose(r4, [1.0, -2.0, 3.0, -4.0])
    g = np.ones(d)
    r = rms_norm(x, g)
    assert np.allclose(np.sqrt(np.mean(r**2, axis=-1)), 1.0, atol=1e-3)
    assert np.allclose(rms_norm(5.0 * x, g), r, atol=1e-6)      # scale-invariant
    assert not np.allclose(rms_norm(x + 10.0, g), r, atol=1e-2)  # shift matters
    # rms_norm == layer_norm when the input is already zero-mean
    xc = x - x.mean(axis=-1, keepdims=True)
    assert np.allclose(rms_norm(xc, g), layer_norm(xc, g, zeros), atol=1e-4)

    print("All tests passed.")
