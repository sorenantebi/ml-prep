---
topic: "Advanced Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/path-with-minimum-effort/
neetcode: https://neetcode.io/problems/path-with-minimum-effort
---
# Path with Minimum Effort - Solution

**Question:** [[Path with Minimum Effort - Question]] · **Difficulty:** Medium

## Intuition

This is a shortest-path problem where the "length" of a path is the maximum edge weight on it rather than the sum. Dijkstra still works because the cost is monotone: extending a path can never decrease its max-edge cost. So we pop the cell with the smallest effort-so-far from a min-heap; the first time we pop the target, that effort is optimal.

## Approach

1. Keep `dist[r][c]` = best known effort to reach `(r, c)`, initialised to infinity except `dist[0][0] = 0`.
2. Push `(0, 0, 0)` (effort, row, col) into a min-heap.
3. Pop the smallest-effort cell. If it is the target, return its effort. Skip stale entries whose effort exceeds `dist`.
4. For each neighbour, the new effort is `max(effort, |h[nr][nc] - h[r][c]|)`. If it improves `dist`, update and push.

## Code

```python
from typing import List
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dist = [[float("inf")] * cols for _ in range(rows)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]  # (effort so far, row, col)

        while heap:
            effort, r, c = heapq.heappop(heap)
            if (r, c) == (rows - 1, cols - 1):
                return effort
            if effort > dist[r][c]:
                continue  # stale heap entry
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    # path cost is the max single step, not the sum
                    new_effort = max(effort, abs(heights[nr][nc] - heights[r][c]))
                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))
        return 0
```

## Complexity

- **Time:** `O(R·C·log(R·C))` — each cell is pushed a bounded number of times (once per incoming edge) and heap operations cost `log`.
- **Space:** `O(R·C)` — the `dist` grid and the heap.

## Other Approaches

- **Binary search + BFS/DFS:** binary search the effort limit `E` in `[0, 10^6]` and check reachability using only steps with difference `<= E` — Time `O(R·C·log(maxH))`, Space `O(R·C)`.
- **Kruskal / Union-Find:** sort all adjacent-cell edges by weight and union them until start and end are connected; the last weight added is the answer — Time `O(R·C·log(R·C))`, Space `O(R·C)`.

## Key Takeaway

Dijkstra works for any path cost that is monotone non-decreasing as the path grows, including "minimise the maximum edge" (minimax) objectives — just replace `+` with `max`.
