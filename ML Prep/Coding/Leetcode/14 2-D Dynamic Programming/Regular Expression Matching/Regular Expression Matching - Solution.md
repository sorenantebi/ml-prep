---
topic: "2-D Dynamic Programming"
difficulty: Hard
leetcode: https://leetcode.com/problems/regular-expression-matching/
neetcode: https://neetcode.io/problems/regular-expression-matching
---
# Regular Expression Matching - Solution

**Question:** [[Regular Expression Matching - Question]] · **Difficulty:** Hard

## Intuition

Let `dp[i][j]` = "does `s[i:]` match `p[j:]`?". If the next pattern token is `x*`, we can either skip it entirely (`dp[i][j+2]`) or, if `s[i]` matches `x`, consume one character of `s` and stay on the same token (`dp[i+1][j]`). Otherwise the current characters must match and both advance (`dp[i+1][j+1]`). Filling from the end gives a bottom-up DP.

## Approach

1. Create `dp` of size `(m+1) x (n+1)` with `dp[m][n] = True` (empty matches empty).
2. Iterate `i` from `m` down to 0 and `j` from `n - 1` down to 0:
   - `first = i < m and p[j] in (s[i], '.')`.
   - If `j + 1 < n and p[j+1] == '*'`: `dp[i][j] = dp[i][j+2] or (first and dp[i+1][j])`.
   - Else: `dp[i][j] = first and dp[i+1][j+1]`.
3. Return `dp[0][0]`.

## Code

```python
class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		m, n = len(s), len(p)
		dp = [[False] * (n + 1) for _ in range(m + 1)]
		dp[m][n] = True  # empty string matches empty pattern
		for i in range(m, -1, -1):          # i == m: s exhausted (still need x* skipping)
			for j in range(n - 1, -1, -1):
				first = i < m and p[j] in (s[i], ".")
				if j + 1 < n and p[j + 1] == "*":
					# skip "x*" entirely, or use it to eat s[i] and stay on it
					dp[i][j] = dp[i][j + 2] or (first and dp[i + 1][j])
				else:
					dp[i][j] = first and dp[i + 1][j + 1]
		return dp[0][0]
```

## Complexity

- **Time:** `O(m * n)` — each `(i, j)` state is computed in `O(1)`.
- **Space:** `O(m * n)` — the DP table (reducible to `O(n)` with two rows).

## Other Approaches

- **Top-down memoized recursion on `(i, j)`:** same transitions, often easier to write in an interview — Time `O(mn)`, Space `O(mn)`.
- **Plain backtracking:** without memoization, patterns like `a*a*a*...` cause exponential blow-up — Time exponential, Space `O(m + n)`.

## Key Takeaway

Treat `x*` as one token with two choices — "zero more copies" (skip the token) or "one more copy" (consume a char, keep the token) — and memoize on `(i, j)`.
