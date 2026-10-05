---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/graph-valid-tree/
neetcode: https://neetcode.io/problems/valid-tree
---
# Graph Valid Tree

**Topic:** [[11 Graphs|Graphs]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/graph-valid-tree/) · [NeetCode](https://neetcode.io/problems/valid-tree)

**Solve it in:** [[Graph Valid Tree]] · **Answer:** [[Graph Valid Tree - Solution]]

## Problem

You are given `n` nodes labeled `0` to `n - 1` and a list of undirected `edges`, where `edges[i] = [a, b]` connects nodes `a` and `b`.

Return `true` if these edges form a **valid tree**, otherwise `false`. A valid tree is connected (every node reachable from every other) and contains no cycles.

## Examples

**Example 1**
```text
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
```

**Example 2**
```text
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
Explanation: Nodes 1, 2, 3 form a cycle.
```

**Example 3**
```text
Input: n = 4, edges = [[0,1],[2,3]]
Output: false
Explanation: The graph is not connected.
```

## Constraints

- `1 <= n <= 2000`
- `0 <= edges.length <= 5000`
- `edges[i].length == 2`, `0 <= a, b < n`, `a != b`
- No duplicate edges

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def validTree(self, n: int, edges: List[List[int]]) -> bool:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.validTree(5, [[0,1],[0,2],[0,3],[1,4]]) is True
	assert s.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]) is False
	assert s.validTree(4, [[0,1],[2,3]]) is False
	assert s.validTree(1, []) is True
	assert s.validTree(2, []) is False
	assert s.validTree(3, [[0,1],[1,2],[2,0]]) is False
	assert s.validTree(4, [[0,1],[0,2],[0,3]]) is True
	assert s.validTree(4, [[0,1],[1,2],[0,2]]) is False  # cycle + isolated node, n-1 edges
	print("All tests passed!")
```
