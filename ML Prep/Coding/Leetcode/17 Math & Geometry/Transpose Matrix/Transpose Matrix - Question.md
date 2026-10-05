---
topic: "Math & Geometry"
difficulty: Easy
leetcode: https://leetcode.com/problems/transpose-matrix/
neetcode: https://neetcode.io/problems/transpose-matrix
---
# Transpose Matrix

**Topic:** [[17 Math & Geometry|Math & Geometry]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/transpose-matrix/) · [NeetCode](https://neetcode.io/problems/transpose-matrix)

**Solve it in:** [[Transpose Matrix]] · **Answer:** [[Transpose Matrix - Solution]]

## Problem

Given a 2D integer array `matrix`, return its **transpose**.

The transpose flips a matrix over its main diagonal, turning rows into columns: the element at `matrix[i][j]` ends up at position `[j][i]`. An `m x n` input therefore produces an `n x m` output. The matrix does not have to be square.

## Examples

**Example 1**
```text
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
```

**Example 2**
```text
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
```

## Constraints

- `m == matrix.length`, `n == matrix[i].length`
- `1 <= m, n <= 1000`
- `1 <= m * n <= 10^5`
- `-10^9 <= matrix[i][j] <= 10^9`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
	assert s.transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
	assert s.transpose([[5]]) == [[5]]
	assert s.transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]]
	assert s.transpose([[1], [2], [3]]) == [[1, 2, 3]]
	assert s.transpose([[-1, 0], [10**9, -10**9]]) == [[-1, 10**9], [0, -10**9]]
	print("All tests passed!")
```
