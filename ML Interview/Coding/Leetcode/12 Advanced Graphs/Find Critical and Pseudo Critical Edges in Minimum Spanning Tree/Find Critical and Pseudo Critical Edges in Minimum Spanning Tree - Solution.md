---
topic: "Advanced Graphs"
difficulty: Hard
leetcode: https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/
neetcode: https://neetcode.io/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree
---
# Find Critical and Pseudo Critical Edges in Minimum Spanning Tree - Solution

**Question:** [[Find Critical and Pseudo Critical Edges in Minimum Spanning Tree - Question]] · **Difficulty:** Hard

## Intuition

Compute the MST weight once with Kruskal. Then test each edge in two ways: (1) build the MST **without** it — if the weight goes up (or the graph can't be spanned), the edge is critical; (2) otherwise build the MST **forcing** it in first — if the weight still equals the optimum, the edge belongs to some MST and is pseudo-critical. With at most 200 edges, running Kruskal `2E` times is cheap.

## Approach

1. Sort edge indices by weight (keeping original indices).
2. `mst(skip, force)`: a Kruskal run with Union-Find that optionally pre-unions edge `force` and ignores edge `skip`; returns total weight, or `inf` if fewer than `n - 1` edges were used.
3. `base = mst(-1, -1)`.
4. For each edge `i`: if `mst(skip=i) > base` it is critical; elif `mst(force=i) == base` it is pseudo-critical.

## Code

```python
from typing import List


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        order = sorted(range(len(edges)), key=lambda i: edges[i][2])

        def mst(skip: int, force: int) -> float:
            parent = list(range(n))

            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]  # path halving
                    x = parent[x]
                return x

            def union(a, b) -> bool:
                ra, rb = find(a), find(b)
                if ra == rb:
                    return False
                parent[ra] = rb
                return True

            weight, used = 0, 0
            if force != -1:
                a, b, w = edges[force]
                union(a, b)
                weight, used = w, 1
            for i in order:
                if i == skip or i == force:
                    continue
                a, b, w = edges[i]
                if union(a, b):
                    weight += w
                    used += 1
            return weight if used == n - 1 else float("inf")

        base = mst(-1, -1)
        critical, pseudo = [], []
        for i in range(len(edges)):
            if mst(i, -1) > base:      # MST gets worse (or impossible) without it
                critical.append(i)
            elif mst(-1, i) == base:   # some MST can include it
                pseudo.append(i)
        return [critical, pseudo]
```

## Complexity

- **Time:** `O(E^2 · α(V))` — `O(E)` Kruskal runs, each `O(E · α(V))` (sorting is done once: `O(E log E)`).
- **Space:** `O(V + E)` — union-find parents and the sorted index list.

## Other Approaches

- **Tarjan bridges per weight group:** process edges grouped by weight on the contracted component graph; bridges are critical, other non-self-loop edges pseudo-critical — Time `O(E log E)`, Space `O(V + E)` (much harder to code).

## Key Takeaway

To classify MST edges, compare against the baseline MST weight: "excluding raises the cost" means critical, "forcing keeps the cost" means pseudo-critical — Kruskal with skip/force hooks is the reusable tool.
