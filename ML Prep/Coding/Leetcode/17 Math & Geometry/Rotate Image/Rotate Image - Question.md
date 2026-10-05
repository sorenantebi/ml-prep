---
topic: "Math & Geometry"
difficulty: Medium
leetcode: https://leetcode.com/problems/rotate-image/
neetcode: https://neetcode.io/problems/rotate-matrix
---
# Rotate Image

**Topic:** [[17 Math & Geometry|Math & Geometry]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/rotate-image/) · [NeetCode](https://neetcode.io/problems/rotate-matrix)

**Solve it in:** [[Rotate Image]] · **Answer:** [[Rotate Image - Solution]]

## Problem

You are given an `n x n` 2D `matrix` that represents an image. Rotate it by **90 degrees clockwise**.

The rotation must be done **in place**: change the input matrix directly and do not allocate a second 2D matrix. The function returns nothing.

## Examples

**Example 1**
```text
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

**Example 2**
```text
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

## Constraints

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def rotate(self, matrix: List[List[int]]) -> None:
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		pass  # your code here


if __name__ == "__main__":
	s = Solution()

	m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	s.rotate(m)
	assert m == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

	m = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
	s.rotate(m)
	assert m == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

	m = [[1]]
	s.rotate(m)
	assert m == [[1]]

	m = [[1, 2], [3, 4]]
	s.rotate(m)
	assert m == [[3, 1], [4, 2]]

	# Four rotations return the original matrix
	orig = [[r * 5 + c for c in range(5)] for r in range(5)]
	m = [row[:] for row in orig]
	for _ in range(4):
		s.rotate(m)
	assert m == orig

	# In-place: the same list object is modified
	m = [[-1, -2], [-3, -4]]
	ref = m
	s.rotate(m)
	assert ref is m and m == [[-3, -1], [-4, -2]]
	print("All tests passed!")
```
