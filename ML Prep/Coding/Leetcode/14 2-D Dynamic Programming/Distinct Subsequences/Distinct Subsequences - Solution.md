---
topic: "2-D Dynamic Programming"
difficulty: Hard
leetcode: https://leetcode.com/problems/distinct-subsequences/
neetcode: https://neetcode.io/problems/count-subsequences
---
# Distinct Subsequences - Solution

**Question:** [[Distinct Subsequences - Question]] · **Difficulty:** Hard

## Intuition

Let `dp[j]` = number of ways the processed prefix of `s` can form `t[:j]`. When we read a new character `c` of `s`, every `j` with `t[j-1] == c` gains `dp[j-1]` new ways (use `c` as the `j`-th char of `t`); skipping `c` keeps the old count. Iterating `j` **backwards** ensures each `s` character is used at most once per subsequence.

## Approach

1. `dp = [1] + [0] * len(t)` — the empty `t` is formed in exactly one way.
2. For each character `c` of `s`, for `j` from `len(t)` down to 1: if `t[j-1] == c`, `dp[j] += dp[j-1]`.
3. Return `dp[len(t)]`.

## Code

```python
class Solution:
	def numDistinct(self, s: str, t: str) -> int:
		n = len(t)
		dp = [1] + [0] * n  # dp[j]: ways to form t[:j] from the prefix of s seen so far
		for c in s:
			for j in range(n, 0, -1):  # backwards so dp[j-1] is still the old value
				if t[j - 1] == c:
					dp[j] += dp[j - 1]
		return dp[n]
```

## Complexity

- **Time:** `O(m * n)` — `m = len(s)`, `n = len(t)`.
- **Space:** `O(n)` — one row indexed by `t` prefix length.

## Other Approaches

- **2-D DP `dp[i][j]`:** `dp[i][j] = dp[i+1][j] + (s[i]==t[j]) * dp[i+1][j+1]` — Time `O(mn)`, Space `O(mn)`.
- **Memoized DFS on `(i, j)`:** skip or use `s[i]` — Time `O(mn)`, Space `O(mn)`.

## Key Takeaway

Counting subsequence embeddings: each source char either skips or matches; a reverse inner loop gives the 0/1 "use once" semantics in a 1-D table.
