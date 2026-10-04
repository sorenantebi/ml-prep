---
topic: "Advanced Graphs"
difficulty: Hard
leetcode: https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/
neetcode: https://neetcode.io/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree
---
# Find Critical and Pseudo Critical Edges in Minimum Spanning Tree

**Topic:** [[12 Advanced Graphs|Advanced Graphs]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/) · [NeetCode](https://neetcode.io/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree)

**Solve it in:** [[Find Critical and Pseudo Critical Edges in Minimum Spanning Tree]] · **Answer:** [[Find Critical and Pseudo Critical Edges in Minimum Spanning Tree - Solution]]

## Problem

You are given a connected, undirected, weighted graph with `n` vertices (`0` to `n - 1`) and an array `edges` where `edges[i] = [a_i, b_i, weight_i]`. The index `i` identifies each edge.

A minimum spanning tree (MST) connects all vertices without cycles using the minimum total weight. Classify edges:

- **Critical:** removing the edge from the graph increases the MST weight (or disconnects the graph) — it is in every MST.
- **Pseudo-critical:** the edge appears in some MST but not in all of them.

Return `[critical_indices, pseudo_critical_indices]`. Indices within each list may be in any order.

## Examples

**Example 1**
```text
Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]
```

**Example 2**
```text
Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
Output: [[],[0,1,2,3]]
Explanation: Any 3 of the 4 equal-weight edges form an MST.
```

**Example 3**
```text
Input: n = 3, edges = [[0,1,1],[1,2,2],[0,2,2]]
Output: [[0],[1,2]]
```

## Constraints

- `2 <= n <= 100`
- `1 <= edges.length <= min(200, n * (n - 1) / 2)`
- `edges[i].length == 3`, `0 <= a_i < b_i < n`
- `1 <= weight_i <= 1000`
- All pairs `(a_i, b_i)` are distinct; the graph is connected.

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        pass  # your code here


def norm(res):
    return [sorted(res[0]), sorted(res[1])]


if __name__ == "__main__":
    s = Solution()
    assert norm(s.findCriticalAndPseudoCriticalEdges(5, [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]])) == [[0,1],[2,3,4,5]]
    assert norm(s.findCriticalAndPseudoCriticalEdges(4, [[0,1,1],[1,2,1],[2,3,1],[0,3,1]])) == [[],[0,1,2,3]]
    assert norm(s.findCriticalAndPseudoCriticalEdges(3, [[0,1,1],[1,2,2],[0,2,2]])) == [[0],[1,2]]
    assert norm(s.findCriticalAndPseudoCriticalEdges(2, [[0,1,1]])) == [[0],[]]
    assert norm(s.findCriticalAndPseudoCriticalEdges(3, [[0,1,1],[1,2,2]])) == [[0,1],[]]
    assert norm(s.findCriticalAndPseudoCriticalEdges(3, [[0,1,1],[1,2,2],[0,2,3]])) == [[0,1],[]]
    print("All tests passed!")
```
