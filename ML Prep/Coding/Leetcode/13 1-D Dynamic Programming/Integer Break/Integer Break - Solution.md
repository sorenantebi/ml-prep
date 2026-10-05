---
topic: "1-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/integer-break/
neetcode: https://neetcode.io/problems/integer-break
---
# Integer Break - Solution

**Question:** [[Integer Break - Question]] · **Difficulty:** Medium

## Intuition

Any part `>= 5` can be split into `2 + (k - 2)` or `3 + (k - 3)` with a larger product, and `4 = 2 + 2` gives the same product, so an optimal split uses only 2s and 3s. Three 2s (product 8) lose to two 3s (product 9), so use as many 3s as possible — except never leave a remainder of 1 (turn `3 + 1` into `2 + 2`). Small `n` (2 or 3) must still be split, so they are special-cased.

## Approach

1. If `n <= 3`, return `n - 1` (forced split: `1+1` or `1+2`).
2. Let `q, r = divmod(n, 3)`.
3. If `r == 0` return `3^q`; if `r == 1` return `3^(q-1) · 4`; if `r == 2` return `3^q · 2`.

## Code

```python
class Solution:
	def integerBreak(self, n: int) -> int:
		if n <= 3:
			return n - 1  # must split into at least two parts
		q, r = divmod(n, 3)
		if r == 0:
			return 3 ** q
		if r == 1:
			return 3 ** (q - 1) * 4  # replace 3 + 1 with 2 + 2
		return 3 ** q * 2
```

## Complexity

- **Time:** `O(log n)` — exponentiation by squaring (effectively `O(1)` for `n <= 58`).
- **Space:** `O(1)`.

## Other Approaches

- **1-D DP:** `dp[i] = max over j of max(j, dp[j]) * max(i - j, dp[i - j])`, i.e. each part is either kept whole or broken further — Time `O(n^2)`, Space `O(n)`.

## Key Takeaway

Know both: the DP ("keep a part whole or break it further") generalises, while the math insight (use 3s, avoid a leftover 1) is the optimal closed form.
