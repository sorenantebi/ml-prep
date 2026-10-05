---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/minimum-height-trees/
neetcode: https://neetcode.io/problems/minimum-height-trees
---
# Minimum Height Trees

**Topic:** [[11 Graphs|Graphs]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/minimum-height-trees/) · [NeetCode](https://neetcode.io/problems/minimum-height-trees)

**Solve it in:** [[Minimum Height Trees]] · **Answer:** [[Minimum Height Trees - Solution]]

## Problem

A tree is an undirected, connected, acyclic graph. You are given a tree of `n` nodes labeled `0` to `n - 1` as a list of `n - 1` `edges`, where `edges[i] = [a, b]`.

You may pick any node as the root. The height of the rooted tree is the number of edges on the longest downward path from the root to a leaf. Among all possible roots, those that yield the minimum height produce **minimum height trees (MHTs)**.

Return the labels of all roots that produce MHTs, in any order.

## Examples

**Example 1**
```text
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: Rooting at node 1 gives height 1; any other root gives height 2.
```

**Example 2**
```text
Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
```

**Example 3**
```text
Input: n = 1, edges = []
Output: [0]
```

## Constraints

- `1 <= n <= 2 * 10^4`
- `edges.length == n - 1`, `0 <= a, b < n`, `a != b`
- All pairs are distinct and the input is guaranteed to be a tree

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert sorted(s.findMinHeightTrees(4, [[1,0],[1,2],[1,3]])) == [1]
	assert sorted(s.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])) == [3, 4]
	assert sorted(s.findMinHeightTrees(1, [])) == [0]
	assert sorted(s.findMinHeightTrees(2, [[0,1]])) == [0, 1]
	assert sorted(s.findMinHeightTrees(5, [[0,1],[1,2],[2,3],[3,4]])) == [2]  # path of odd length
	assert sorted(s.findMinHeightTrees(6, [[0,1],[1,2],[2,3],[3,4],[4,5]])) == [2, 3]  # even path
	assert sorted(s.findMinHeightTrees(7, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]])) == [1, 2]
	print("All tests passed!")
```
