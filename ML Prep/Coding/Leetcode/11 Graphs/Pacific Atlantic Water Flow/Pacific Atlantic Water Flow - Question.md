---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/pacific-atlantic-water-flow/
neetcode: https://neetcode.io/problems/pacific-atlantic-water-flow
---
# Pacific Atlantic Water Flow

**Topic:** [[11 Graphs|Graphs]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/pacific-atlantic-water-flow/) · [NeetCode](https://neetcode.io/problems/pacific-atlantic-water-flow)

**Solve it in:** [[Pacific Atlantic Water Flow]] · **Answer:** [[Pacific Atlantic Water Flow - Solution]]

## Problem

An `m x n` island is described by a matrix `heights`, where `heights[r][c]` is the elevation of cell `(r, c)`. The **Pacific Ocean** touches the island's top and left edges, and the **Atlantic Ocean** touches its bottom and right edges.

When it rains, water can flow from a cell to a 4-directionally adjacent cell if the neighbor's height is **less than or equal to** the current cell's height. Water flows from any cell on an ocean-adjacent edge into that ocean.

Return a list of all coordinates `[r, c]` from which rain water can reach **both** the Pacific and the Atlantic. The result may be in any order.

## Examples

**Example 1**
```text
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

**Example 2**
```text
Input: heights = [[1]]
Output: [[0,0]]
```

## Constraints

- `1 <= m, n <= 200`
- `0 <= heights[r][c] <= 10^5`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
		pass  # your code here


def norm(cells):
	return sorted(map(tuple, cells))


if __name__ == "__main__":
	s = Solution()
	assert norm(s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])) == \
		norm([[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]])
	assert norm(s.pacificAtlantic([[1]])) == [(0, 0)]
	assert norm(s.pacificAtlantic([[1, 1], [1, 1]])) == [(0, 0), (0, 1), (1, 0), (1, 1)]
	assert norm(s.pacificAtlantic([[1, 2, 3]])) == [(0, 0), (0, 1), (0, 2)]
	# (0,0) is a pit that only touches the Pacific
	assert norm(s.pacificAtlantic([[1, 2], [4, 3]])) == [(0, 1), (1, 0), (1, 1)]
	assert norm(s.pacificAtlantic([[3,3,3],[3,1,3],[3,3,3]])) == \
		[(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
	print("All tests passed!")
```
