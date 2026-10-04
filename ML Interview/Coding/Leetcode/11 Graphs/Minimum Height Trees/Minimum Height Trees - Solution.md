---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/minimum-height-trees/
neetcode: https://neetcode.io/problems/minimum-height-trees
---
# Minimum Height Trees - Solution

**Question:** [[Minimum Height Trees - Question]] · **Difficulty:** Medium

## Intuition

The best roots are the **centers** of the tree — the middle node(s) of its longest path (diameter). A tree has either one or two centers. We can find them by repeatedly peeling off all current leaves (like a topological sort from the outside in); the last 1 or 2 nodes remaining are the centers.

## Approach

1. Handle `n <= 2`: every node is a center.
2. Build adjacency sets and collect all leaves (degree 1).
3. While more than 2 nodes remain:
   - Remove all current leaves (`remaining -= len(leaves)`).
   - For each removed leaf, delete it from its neighbor's set; a neighbor whose degree becomes 1 is a leaf of the next layer.
4. Return the remaining leaves.

## Code

```python
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))
        adj = [set() for _ in range(n)]
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        leaves = [i for i in range(n) if len(adj[i]) == 1]
        remaining = n
        while remaining > 2:  # at most 2 centers can remain
            remaining -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                nb = adj[leaf].pop()  # a leaf has exactly one neighbor
                adj[nb].remove(leaf)
                if len(adj[nb]) == 1:
                    new_leaves.append(nb)
            leaves = new_leaves
        return leaves
```

## Complexity

- **Time:** `O(n)` — each node is removed once and each edge is deleted once.
- **Space:** `O(n)` — adjacency sets and leaf lists.

## Other Approaches

- **BFS from every node:** compute the height for each possible root and keep the minimum — Time `O(n^2)`, Space `O(n)`.
- **Two BFS passes for the diameter:** find the longest path (BFS from any node to the farthest node `u`, then from `u` to the farthest `v`, tracking parents) and return its middle 1 or 2 nodes — Time `O(n)`, Space `O(n)`.

## Key Takeaway

Minimum-height roots are the tree's centers; find them by trimming leaves layer by layer (Kahn-style topological peeling on an undirected tree).
