---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/number-of-islands/
neetcode: https://neetcode.io/problems/count-number-of-islands
---
# Number of Islands - Solution

**Question:** [[Number of Islands - Question]] · **Difficulty:** Medium

## Intuition

Treat the grid as a graph where land cells are nodes and adjacent land cells share an edge. The number of islands is the number of connected components. Scan the grid; whenever an unvisited land cell is found, it starts a new island, and a flood fill (BFS/DFS) marks the entire island as visited.

## Approach

1. Loop over every cell.
2. When a cell is `'1'`, increment the island count and flood-fill from it.
3. The flood fill (iterative BFS here, to avoid recursion limits) turns every reachable `'1'` into `'0'` so it is never counted again.
4. Return the count.

## Code

```python
from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(sr: int, sc: int) -> None:
            q = deque([(sr, sc)])
            grid[sr][sc] = "0"  # mark visited when enqueued
            while q:
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)
        return islands
```

## Complexity

- **Time:** `O(m * n)` — each cell is enqueued/visited at most once.
- **Space:** `O(min(m, n))` to `O(m * n)` — the BFS queue in the worst case; the grid is modified in place instead of using a visited set.

## Other Approaches

- **Recursive DFS:** same idea with recursion — Time `O(m * n)`, Space `O(m * n)` recursion stack (may hit Python's recursion limit on large grids).
- **Union-Find:** union adjacent land cells and count distinct roots — Time `O(m * n * α(mn))`, Space `O(m * n)`.

## Key Takeaway

"Count groups of connected cells" = count connected components: scan + flood fill, marking cells visited as soon as they are enqueued.
