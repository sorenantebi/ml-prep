---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
neetcode: https://neetcode.io/problems/count-connected-components
---
# Number of Connected Components In An Undirected Graph

**Topic:** [[11 Graphs|Graphs]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) · [NeetCode](https://neetcode.io/problems/count-connected-components)

**Solve it in:** [[Number of Connected Components In An Undirected Graph]] · **Answer:** [[Number of Connected Components In An Undirected Graph - Solution]]

## Problem

You are given `n` nodes labeled `0` to `n - 1` and a list of undirected `edges`, where `edges[i] = [a, b]` connects nodes `a` and `b`.

Return the number of connected components in the graph. An isolated node (no edges) counts as its own component.

## Examples

**Example 1**
```text
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Explanation: Components {0,1,2} and {3,4}.
```

**Example 2**
```text
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
```

## Constraints

- `1 <= n <= 2000`
- `1 <= edges.length <= 5000`
- `edges[i].length == 2`, `0 <= a, b < n`, `a != b`
- No repeated edges

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.countComponents(5, [[0,1],[1,2],[3,4]]) == 2
    assert s.countComponents(5, [[0,1],[1,2],[2,3],[3,4]]) == 1
    assert s.countComponents(1, []) == 1
    assert s.countComponents(4, []) == 4
    assert s.countComponents(4, [[0,1],[1,2],[2,0]]) == 2  # triangle + isolated node
    assert s.countComponents(6, [[0,1],[2,3],[4,5]]) == 3
    assert s.countComponents(2000, [[i, i + 1] for i in range(0, 1999, 2)]) == 1000
    print("All tests passed!")
```
