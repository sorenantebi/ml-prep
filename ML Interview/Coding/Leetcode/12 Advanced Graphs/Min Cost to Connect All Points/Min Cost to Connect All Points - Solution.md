---
topic: "Advanced Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/min-cost-to-connect-all-points/
neetcode: https://neetcode.io/problems/min-cost-to-connect-points
---
# Min Cost to Connect All Points - Solution

**Question:** [[Min Cost to Connect All Points - Question]] · **Difficulty:** Medium

## Intuition

We need a minimum spanning tree of a complete graph where every pair of points is an edge. Because the graph is dense (`~n^2/2` edges), the array-based version of **Prim's algorithm** is ideal: it runs in `O(n^2)` without ever materialising the edges or using a heap.

## Approach

1. Keep `min_dist[i]` = cheapest known edge connecting point `i` to the growing tree (start: `inf`, and `0` for point 0).
2. Repeat `n` times: pick the unvisited point with the smallest `min_dist`, add that cost to the total, and mark it visited.
3. Relax: for every unvisited point `j`, set `min_dist[j] = min(min_dist[j], manhattan(cur, j))`.
4. Return the total.

## Code

```python
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_dist = [float("inf")] * n
        min_dist[0] = 0
        in_tree = [False] * n
        total = 0

        for _ in range(n):
            # pick the closest point not yet in the tree
            cur = min((i for i in range(n) if not in_tree[i]), key=lambda i: min_dist[i])
            in_tree[cur] = True
            total += min_dist[cur]
            x1, y1 = points[cur]
            for j in range(n):
                if not in_tree[j]:
                    d = abs(x1 - points[j][0]) + abs(y1 - points[j][1])
                    if d < min_dist[j]:
                        min_dist[j] = d
        return total
```

## Complexity

- **Time:** `O(n^2)` — `n` rounds, each scanning all points.
- **Space:** `O(n)` — the `min_dist` and `in_tree` arrays.

## Other Approaches

- **Kruskal + Union-Find:** generate all `n^2/2` edges, sort, union greedily — Time `O(n^2 log n)`, Space `O(n^2)`.
- **Prim with a heap:** lazy heap of `(cost, point)` — Time `O(n^2 log n)`, Space `O(n^2)` (worse than array Prim on dense graphs).

## Key Takeaway

For MST on a dense/complete graph, array-based Prim (`O(V^2)`) beats heap-based Prim and Kruskal; for sparse graphs prefer Kruskal or heap Prim.
