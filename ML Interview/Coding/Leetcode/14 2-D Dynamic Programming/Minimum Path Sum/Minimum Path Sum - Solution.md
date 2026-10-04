---
topic: "2-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/minimum-path-sum/
neetcode: https://neetcode.io/problems/minimum-path-sum
---
# Minimum Path Sum - Solution

**Question:** [[Minimum Path Sum - Question]] · **Difficulty:** Medium

## Intuition

The cheapest way to reach cell `(r, c)` must come through either the cell above or the cell to its left, so `best(r, c) = grid[r][c] + min(best(r-1, c), best(r, c-1))`. Only the previous row is needed, so a 1-D array suffices.

## Approach

1. Initialize `dp = [inf] * n` and set `dp[0] = 0` as a virtual "entry" value.
2. For each row, sweep left to right: `dp[c] = grid[r][c] + min(dp[c], dp[c-1])`, where `dp[c]` is the value from above and `dp[c-1]` from the left (skip the left term for `c == 0`).
3. Return `dp[-1]`.

## Code

```python
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        dp = [float("inf")] * n
        dp[0] = 0  # lets the first cell take just its own value
        for row in grid:
            dp[0] += row[0]  # first column: only reachable from above
            for c in range(1, n):
                dp[c] = row[c] + min(dp[c], dp[c - 1])  # above vs left
        return dp[-1]
```

## Complexity

- **Time:** `O(m * n)` — each cell processed once.
- **Space:** `O(n)` — one rolling row (or `O(1)` if the grid may be modified in place).

## Other Approaches

- **In-place 2-D DP:** overwrite `grid` with the prefix minima — Time `O(m * n)`, Space `O(1)` extra.
- **Dijkstra:** treat cells as nodes with non-negative weights — Time `O(mn log mn)`, Space `O(mn)`; overkill since moves are restricted to right/down (a DAG).

## Key Takeaway

For right/down-only grid problems the grid is a DAG in row-major order, so a simple min-over-predecessors DP replaces any shortest-path algorithm.
