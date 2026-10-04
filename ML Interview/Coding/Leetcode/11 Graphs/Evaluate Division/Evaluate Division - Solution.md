---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/evaluate-division/
neetcode: https://neetcode.io/problems/evaluate-division
---
# Evaluate Division - Solution

**Question:** [[Evaluate Division - Question]] · **Difficulty:** Medium

## Intuition

Build a weighted directed graph: `A / B = k` gives an edge `A -> B` with weight `k` and `B -> A` with weight `1/k`. Then `C / D` is the product of edge weights along any path from `C` to `D` (consistency guarantees every path gives the same result). Each query is answered by a BFS/DFS that multiplies weights along the way.

## Approach

1. Build an adjacency map `graph[u][v] = u / v` for both directions of each equation.
2. For each query `(C, D)`:
   - If either variable is missing from the graph, answer `-1.0`.
   - Otherwise BFS from `C`, carrying the running product `C / current`.
   - When `D` is reached, the running product is the answer; if BFS ends without reaching `D`, answer `-1.0`.

## Code

```python
from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a, b), k in zip(equations, values):
            graph[a][b] = k        # a / b = k
            graph[b][a] = 1.0 / k  # b / a = 1/k

        def query(src: str, dst: str) -> float:
            if src not in graph or dst not in graph:
                return -1.0
            q = deque([(src, 1.0)])  # (node, src / node)
            seen = {src}
            while q:
                node, ratio = q.popleft()
                if node == dst:
                    return ratio
                for nxt, w in graph[node].items():
                    if nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, ratio * w))  # src/nxt = src/node * node/nxt
            return -1.0

        return [query(c, d) for c, d in queries]
```

## Complexity

- **Time:** `O(Q * (V + E))` — one graph traversal per query.
- **Space:** `O(V + E)` — adjacency map plus BFS queue/visited set.

## Other Approaches

- **Weighted Union-Find:** store each variable's ratio to its root (`x = weight[x] * root`); a query is `weight[C] / weight[D]` when both share a root — Time `O((E + Q) * α(V))`, Space `O(V)`.
- **Floyd–Warshall:** precompute all pairwise ratios — Time `O(V^3 + Q)`, Space `O(V^2)`.

## Key Takeaway

Ratios/conversion rates form a weighted graph where path products give derived values; answer queries with BFS/DFS or weighted Union-Find.
