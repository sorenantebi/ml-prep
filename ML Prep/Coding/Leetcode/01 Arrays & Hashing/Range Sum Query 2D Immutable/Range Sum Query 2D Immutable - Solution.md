---
topic: "Arrays & Hashing"
difficulty: Medium
leetcode: https://leetcode.com/problems/range-sum-query-2d-immutable/
neetcode: https://neetcode.io/problems/range-sum-query-2d-immutable
---
# Range Sum Query 2D Immutable - Solution

**Question:** [[Range Sum Query 2D Immutable - Question]] · **Difficulty:** Medium

## Intuition

Precompute a 2D prefix sum `P[r][c]` = sum of the sub-matrix from `(0, 0)` to `(r - 1, c - 1)`. Any rectangle sum is then the big prefix minus the strip above and the strip to the left, plus the top-left corner that was subtracted twice (inclusion-exclusion), which takes `O(1)` per query.

## Approach

1. Allocate `P` of size `(m + 1) x (n + 1)` filled with zeros (the extra row/column removes boundary checks).
2. Fill `P[r + 1][c + 1] = matrix[r][c] + P[r][c + 1] + P[r + 1][c] - P[r][c]`.
3. For a query, return `P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]`.

## Code

```python
from typing import List


class NumMatrix:

	def __init__(self, matrix: List[List[int]]):
		m, n = len(matrix), len(matrix[0])
		# P[r][c] = sum of matrix[0..r-1][0..c-1]; padded with a zero row/col
		self.P = [[0] * (n + 1) for _ in range(m + 1)]
		for r in range(m):
			for c in range(n):
				self.P[r + 1][c + 1] = (matrix[r][c] + self.P[r][c + 1]
										+ self.P[r + 1][c] - self.P[r][c])

	def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
		P = self.P
		# inclusion-exclusion: whole - above - left + overlap counted twice
		return (P[row2 + 1][col2 + 1] - P[row1][col2 + 1]
				- P[row2 + 1][col1] + P[row1][col1])
```

## Complexity

- **Time:** `O(m · n)` preprocessing, `O(1)` per `sumRegion` query.
- **Space:** `O(m · n)` — the prefix-sum table.

## Other Approaches

- **Row-wise 1D prefix sums:** a prefix array per row, sum `row2 - row1 + 1` row ranges per query — Time `O(m)` per query, Space `O(m · n)`.
- **Brute force:** sum the rectangle on each query — Time `O(m · n)` per query, Space `O(1)`.

## Key Takeaway

2D prefix sums plus inclusion-exclusion give constant-time rectangle queries; pad with a zero row and column to avoid edge-case branches.
