---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/redundant-connection/
neetcode: https://neetcode.io/problems/redundant-connection
---
# Redundant Connection

**Topic:** [[11 Graphs|Graphs]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/redundant-connection/) · [NeetCode](https://neetcode.io/problems/redundant-connection)

**Solve it in:** [[Redundant Connection]] · **Answer:** [[Redundant Connection - Solution]]

## Problem

A tree with `n` nodes labeled `1` to `n` had **one extra edge** added, creating exactly one cycle. The resulting graph is given as `edges`, a list of `n` undirected edges `[a, b]`.

Return an edge that can be removed so that the remaining graph is a tree with all `n` nodes. If several edges qualify, return the one that appears **last** in `edges`.

## Examples

**Example 1**
```text
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
```

**Example 2**
```text
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
```

## Constraints

- `n == edges.length`, `3 <= n <= 1000`
- `edges[i].length == 2`, `1 <= a < b <= n`
- No repeated edges; the graph is connected

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.findRedundantConnection([[1,2],[1,3],[2,3]]) == [2,3]
	assert s.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]) == [1,4]
	assert s.findRedundantConnection([[1,4],[3,4],[1,3],[1,2],[4,5]]) == [1,3]
	assert s.findRedundantConnection([[2,3],[1,2],[1,3]]) == [1,3]
	assert s.findRedundantConnection([[1,2],[2,3],[3,4],[4,5],[1,5]]) == [1,5]
	assert s.findRedundantConnection([[3,4],[1,2],[2,4],[3,5],[2,5]]) == [2,5]
	print("All tests passed!")
```
