---
topic: "Advanced Graphs"
difficulty: Hard
leetcode: https://leetcode.com/problems/build-a-matrix-with-conditions/
neetcode: https://neetcode.io/problems/build-a-matrix-with-conditions
---
# Build a Matrix With Conditions - Solution

**Question:** [[Build a Matrix With Conditions - Question]] · **Difficulty:** Hard

## Intuition

Row and column constraints are independent. Each is a set of precedence edges over the numbers `1..k`, so a **topological sort** gives a valid row order and another gives a valid column order. Placing number `x` at `(row_rank[x], col_rank[x])` puts every number in its own row and column, satisfying everything. A cycle in either graph means no answer.

## Approach

1. `topo(conditions)`: build the graph on `1..k`, run Kahn's algorithm, return the order (or `None` if it contains fewer than `k` nodes, i.e. a cycle).
2. Compute `row_order` and `col_order`; if either is `None`, return `[]`.
3. Map each number to its index in `col_order`.
4. For each `r, x` in `row_order`, set `mat[r][col_index[x]] = x`.

## Code

```python
from typing import List
from collections import deque


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo(conditions):
            adj = [[] for _ in range(k + 1)]
            indeg = [0] * (k + 1)
            for a, b in conditions:
                adj[a].append(b)
                indeg[b] += 1
            queue = deque(x for x in range(1, k + 1) if indeg[x] == 0)
            order = []
            while queue:
                x = queue.popleft()
                order.append(x)
                for y in adj[x]:
                    indeg[y] -= 1
                    if indeg[y] == 0:
                        queue.append(y)
            return order if len(order) == k else None  # None -> cycle

        row_order = topo(rowConditions)
        col_order = topo(colConditions)
        if row_order is None or col_order is None:
            return []

        col_index = {x: c for c, x in enumerate(col_order)}
        mat = [[0] * k for _ in range(k)]
        for r, x in enumerate(row_order):
            mat[r][col_index[x]] = x  # each number gets its own row and column
        return mat
```

## Complexity

- **Time:** `O(k^2 + R + C)` — two topological sorts over `R` and `C` conditions plus filling a `k x k` matrix.
- **Space:** `O(k^2 + R + C)` — the output matrix and adjacency lists.

## Other Approaches

- **DFS topological sort:** post-order DFS with 3-colour cycle detection instead of Kahn's — same Time/Space.

## Key Takeaway

When constraints along two axes are independent, solve each axis separately (here: two topological sorts) and combine; duplicates in the edge list are harmless with Kahn's since in-degree counts each copy.
