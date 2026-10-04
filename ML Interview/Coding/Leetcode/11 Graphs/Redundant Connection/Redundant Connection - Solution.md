---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/redundant-connection/
neetcode: https://neetcode.io/problems/redundant-connection
---
# Redundant Connection - Solution

**Question:** [[Redundant Connection - Question]] · **Difficulty:** Medium

## Intuition

Add edges one by one with **Union-Find**. The first edge whose endpoints are already connected closes the (only) cycle. Since the graph has exactly one cycle and every cycle edge is processed before or at that moment, the edge that closes it is the last cycle edge in the input — exactly the edge the problem asks for.

## Approach

1. Initialize Union-Find over nodes `1..n`.
2. For each edge `[a, b]` in order: if `find(a) == find(b)`, return `[a, b]`.
3. Otherwise union the two sets.

## Code

```python
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra == rb:
                return [a, b]  # a and b already connected -> this edge closes the cycle
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
        return []
```

## Complexity

- **Time:** `O(n * α(n))` — one find/union per edge.
- **Space:** `O(n)` — parent and rank arrays.

## Other Approaches

- **DFS per edge:** before adding each edge, DFS to check whether `a` can already reach `b` — Time `O(n^2)`, Space `O(n)`.
- **Find the cycle, then pick the last cycle edge:** DFS to extract cycle nodes, then scan edges backwards for the last one on the cycle — Time `O(n)`, Space `O(n)`.

## Key Takeaway

In an incrementally built undirected graph, "this edge connects two already-connected nodes" is the Union-Find signature of a cycle.
