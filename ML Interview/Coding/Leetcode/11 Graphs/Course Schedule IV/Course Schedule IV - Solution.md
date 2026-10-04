---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/course-schedule-iv/
neetcode: https://neetcode.io/problems/course-schedule-iv
---
# Course Schedule IV - Solution

**Question:** [[Course Schedule IV - Question]] · **Difficulty:** Medium

## Intuition

With up to `10^4` queries but only `100` courses, precompute the full reachability relation once and answer each query in `O(1)`. Process courses in **topological order**: when course `u` is finished, everything that is a prerequisite of `u` (plus `u` itself) is a prerequisite of each course `v` that directly depends on `u`.

## Approach

1. Build the adjacency list `a -> b` and in-degrees.
2. Keep `prereqs[v]`, the set of all courses that must come before `v`.
3. Run Kahn's algorithm: when popping `u`, for each neighbor `v` do `prereqs[v] |= prereqs[u] | {u}`; decrement `indeg[v]` and enqueue it at 0. Because `u` is popped only after all its own prerequisites, `prereqs[u]` is complete at that time.
4. Answer each query `[u, v]` with `u in prereqs[v]`.

## Code

```python
from collections import deque
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]],
                            queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for a, b in prerequisites:
            graph[a].append(b)
            indeg[b] += 1

        prereqs = [set() for _ in range(numCourses)]  # all ancestors of each course
        q = deque(i for i in range(numCourses) if indeg[i] == 0)
        while q:
            u = q.popleft()
            for v in graph[u]:
                prereqs[v].add(u)
                prereqs[v] |= prereqs[u]  # inherit u's (already complete) ancestors
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return [u in prereqs[v] for u, v in queries]
```

## Complexity

- **Time:** `O(V * E + Q)` — each edge merges a set of size up to `V`; each query is `O(1)`.
- **Space:** `O(V^2)` — the ancestor sets.

## Other Approaches

- **Floyd–Warshall transitive closure:** `reach[i][j] |= reach[i][k] and reach[k][j]` for all `k, i, j` — Time `O(V^3 + Q)`, Space `O(V^2)`.
- **DFS from each node:** compute the set reachable from every course with memoized DFS — Time `O(V * (V + E) + Q)`, Space `O(V^2)`.

## Key Takeaway

When there are many reachability queries on a small DAG, precompute the transitive closure (topological propagation, DFS per node, or Floyd–Warshall) and answer each query in constant time.
