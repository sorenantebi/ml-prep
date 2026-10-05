---
topic: "2-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/interleaving-string/
neetcode: https://neetcode.io/problems/interleaving-string
---
# Interleaving String - Solution

**Question:** [[Interleaving String - Question]] · **Difficulty:** Medium

## Intuition

Let `dp[i][j]` mean "the first `i` chars of `s1` and first `j` chars of `s2` can form the first `i + j` chars of `s3`". The last character of that prefix of `s3` must come from either `s1[i-1]` or `s2[j-1]`, so `dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])`. One row of the table suffices.

## Approach

1. If `len(s1) + len(s2) != len(s3)`, return `False`.
2. Keep `dp` of length `len(s2) + 1`; row `i = 0` is filled using only `s2`.
3. For each `i` from 0 to `len(s1)`, and each `j` from 0 to `len(s2)`, compute `dp[j]` from `dp[j]` (the row above: take from `s1`) and `dp[j-1]` (the left: take from `s2`).
4. Return `dp[len(s2)]`.

## Code

```python
class Solution:
	def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
		m, n = len(s1), len(s2)
		if m + n != len(s3):
			return False
		dp = [False] * (n + 1)
		for i in range(m + 1):
			for j in range(n + 1):
				if i == 0 and j == 0:
					dp[j] = True
					continue
				k = i + j - 1  # index in s3 of the char being placed
				from_s1 = i > 0 and dp[j] and s1[i - 1] == s3[k]        # dp[j] = row above
				from_s2 = j > 0 and dp[j - 1] and s2[j - 1] == s3[k]    # dp[j-1] = current row
				dp[j] = from_s1 or from_s2
		return dp[n]
```

## Complexity

- **Time:** `O(m * n)` — each `(i, j)` state is computed once.
- **Space:** `O(n)` — a single row of the DP table.

## Other Approaches

- **Memoized DFS on `(i, j)`:** try taking the next char from `s1` or `s2` — Time `O(m * n)`, Space `O(m * n)`.
- **Plain backtracking:** without memoization the branching explodes — Time `O(2^(m+n))`, Space `O(m + n)`.

## Key Takeaway

When the state of a merge can be described by "how much of each input has been consumed", a 2-D DP over `(i, j)` captures it; the index into the output is implied as `i + j`.
