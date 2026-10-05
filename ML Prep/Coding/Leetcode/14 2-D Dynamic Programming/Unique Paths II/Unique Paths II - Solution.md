---
topic: "2-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/unique-paths-ii/
neetcode: https://neetcode.io/problems/unique-paths-ii
---
# Unique Paths II - Solution

**Question:** [[Unique Paths II - Question]] · **Difficulty:** Medium

## Intuition

Same recurrence as Unique Paths — paths into a cell = paths from above + paths from the left — except an obstacle cell contributes `0` paths. Rolling the DP into one row keeps space linear.

## Approach

1. Let `dp` be an array of length `n`, with `dp[0] = 1` if the start is free (else 0).
2. For every row, sweep the columns left to right:
   - If the cell is an obstacle, set `dp[c] = 0`.
   - Otherwise, if `c > 0`, add the left neighbour: `dp[c] += dp[c-1]` (`dp[c]` already holds the value from above).
3. Return `dp[-1]`.

## Code

```python
from typing import List


class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
		n = len(obstacleGrid[0])
		dp = [0] * n
		dp[0] = 1 if obstacleGrid[0][0] == 0 else 0
		for row in obstacleGrid:
			for c in range(n):
				if row[c] == 1:
					dp[c] = 0          # no path goes through an obstacle
				elif c > 0:
					dp[c] += dp[c - 1]  # from above (old dp[c]) + from left
		return dp[-1]
```

## Complexity

- **Time:** `O(m * n)` — each cell is visited once.
- **Space:** `O(n)` — one rolling row.

## Other Approaches

- **Full 2-D DP table:** same recurrence stored in an `m x n` table — Time `O(m * n)`, Space `O(m * n)`.
- **Memoized DFS from the start:** recurse right/down, returning 0 on obstacles — Time `O(m * n)`, Space `O(m * n)`.

## Key Takeaway

Obstacles in grid DP are handled by forcing that cell's count to zero; the rest of the recurrence is unchanged.
