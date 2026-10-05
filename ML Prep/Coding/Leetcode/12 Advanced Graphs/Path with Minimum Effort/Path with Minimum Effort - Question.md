---
topic: "Advanced Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/path-with-minimum-effort/
neetcode: https://neetcode.io/problems/path-with-minimum-effort
---
# Path with Minimum Effort

**Topic:** [[12 Advanced Graphs|Advanced Graphs]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/path-with-minimum-effort/) · [NeetCode](https://neetcode.io/problems/path-with-minimum-effort)

**Solve it in:** [[Path with Minimum Effort]] · **Answer:** [[Path with Minimum Effort - Solution]]

## Problem

You are a hiker on a 2D grid `heights` of size `rows x columns`, where `heights[r][c]` is the altitude of cell `(r, c)`. You start in the top-left cell `(0, 0)` and want to reach the bottom-right cell `(rows - 1, columns - 1)`. From any cell you may step up, down, left, or right (staying inside the grid).

The **effort** of a route is the largest absolute height difference between any two consecutive cells along that route. Return the minimum effort over all possible routes from the top-left to the bottom-right cell.

## Examples

**Example 1**
```text
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: Route 1 -> 3 -> 5 -> 3 -> 5 never has a jump bigger than 2.
```

**Example 2**
```text
Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: Route 1 -> 2 -> 3 -> 4 -> 5 has max jump 1.
```

**Example 3**
```text
Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
```

## Constraints

- `rows == heights.length`, `columns == heights[i].length`
- `1 <= rows, columns <= 100`
- `1 <= heights[i][j] <= 10^6`

## Starter Code & Test Cases

```python
from typing import List
import heapq


class Solution:
	def minimumEffortPath(self, heights: List[List[int]]) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]) == 2
	assert s.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]) == 1
	assert s.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]) == 0
	assert s.minimumEffortPath([[5]]) == 0
	assert s.minimumEffortPath([[1, 10]]) == 9
	assert s.minimumEffortPath([[1], [4], [2]]) == 3
	assert s.minimumEffortPath([[1, 100], [2, 3]]) == 1
	print("All tests passed!")
```
