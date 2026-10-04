---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/graph-valid-tree/
neetcode: https://neetcode.io/problems/valid-tree
---
# Graph Valid Tree - Solution

**Question:** [[Graph Valid Tree - Question]] · **Difficulty:** Medium

## Intuition

A graph on `n` nodes is a tree iff it has exactly `n - 1` edges **and** no cycle (equivalently, `n - 1` edges and connected). Check the edge count first, then use **Union-Find**: if an edge joins two nodes that already share a root, it closes a cycle.

## Approach

1. If `len(edges) != n - 1`, return `false` (too few → disconnected, too many → cycle).
2. Initialize Union-Find with `n` singleton sets.
3. For each edge `(a, b)`, find both roots; if they are equal, a cycle exists → return `false`. Otherwise union them.
4. With `n - 1` edges and no cycle, the graph is connected → return `true`.

## Code

```python
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = list(range(n))
        rank = [0] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path halving
                x = parent[x]
            return x

        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False  # edge closes a cycle
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
        return True
```

## Complexity

- **Time:** `O(n + E * α(n))` — near-constant time per union/find.
- **Space:** `O(n)` — parent and rank arrays.

## Other Approaches

- **DFS/BFS:** after the `n - 1` edge check, traverse from node 0 and verify all `n` nodes are visited — Time `O(n + E)`, Space `O(n + E)` for the adjacency list.

## Key Takeaway

Tree ⇔ `n - 1` edges + connected ⇔ `n - 1` edges + acyclic; Union-Find is the go-to tool for cycle detection in undirected graphs.
