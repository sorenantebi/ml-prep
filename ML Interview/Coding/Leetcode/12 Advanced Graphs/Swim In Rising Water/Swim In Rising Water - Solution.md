---
topic: "Advanced Graphs"
difficulty: Hard
leetcode: https://leetcode.com/problems/swim-in-rising-water/
neetcode: https://neetcode.io/problems/swim-in-rising-water
---
# Swim In Rising Water - Solution

**Question:** [[Swim In Rising Water - Question]] · **Difficulty:** Hard

## Intuition

The time needed for a path is the highest elevation along it (including start and end). We want the path minimising that maximum — a minimax shortest path. Dijkstra with `max` instead of `+` solves it: always expand the reachable cell with the lowest elevation seen so far.

## Approach

1. Min-heap of `(time_needed, r, c)` starting with `(grid[0][0], 0, 0)`; mark `(0, 0)` visited.
2. Pop the lowest entry. If it is the bottom-right cell, return its time.
3. For each unvisited neighbour, mark visited and push `(max(time, grid[nr][nc]), nr, nc)`.

## Code

```python
from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]  # (water level needed so far, row, col)
        visited = {(0, 0)}

        while heap:
            t, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return t
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))  # safe: heap pops cells in non-decreasing t
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))
        return -1
```

## Complexity

- **Time:** `O(n^2 log n)` — each of the `n^2` cells is pushed once; heap ops cost `log(n^2)`.
- **Space:** `O(n^2)` — heap and visited set.

## Other Approaches

- **Binary search + BFS:** binary search `t` in `[grid[0][0], n^2 - 1]` and check reachability through cells `<= t` — Time `O(n^2 log n)`, Space `O(n^2)`.
- **Union-Find by elevation:** add cells in increasing elevation order, union with already-added neighbours, stop when corners are connected — Time `O(n^2 α(n))` after sorting, Space `O(n^2)`.

## Key Takeaway

"Minimise the bottleneck (max) along a path" is solved by Dijkstra with `max`, by binary search on the answer + BFS, or by Kruskal-style union-find — all three are worth recognising.
