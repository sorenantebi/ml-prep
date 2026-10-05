---
topic: "2-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/minimum-path-sum/
neetcode: https://neetcode.io/problems/minimum-path-sum
---
# Minimum Path Sum

**Topic:** [[14 2-D Dynamic Programming|2-D Dynamic Programming]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/minimum-path-sum/) · [NeetCode](https://neetcode.io/problems/minimum-path-sum)

**Solve it in:** [[Minimum Path Sum]] · **Answer:** [[Minimum Path Sum - Solution]]

## Problem

Given an `m x n` grid of non-negative integers, find a path from the top-left cell to the bottom-right cell that minimizes the sum of all numbers along the path (including both endpoints). You may only move **right** or **down** at each step. Return that minimum sum.

## Examples

**Example 1**
```text
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: The path 1 -> 3 -> 1 -> 1 -> 1 has sum 7.
```

**Example 2**
```text
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
```

## Constraints

- `m == grid.length`, `n == grid[i].length`
- `1 <= m, n <= 200`
- `0 <= grid[i][j] <= 200`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def minPathSum(self, grid: List[List[int]]) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
	assert s.minPathSum([[1, 2, 3], [4, 5, 6]]) == 12
	assert s.minPathSum([[5]]) == 5
	assert s.minPathSum([[1, 2, 3, 4]]) == 10
	assert s.minPathSum([[1], [2], [3]]) == 6
	assert s.minPathSum([[0, 0], [0, 0]]) == 0
	assert s.minPathSum([[1, 9, 9], [1, 9, 9], [1, 1, 1]]) == 5
	print("All tests passed!")
```
