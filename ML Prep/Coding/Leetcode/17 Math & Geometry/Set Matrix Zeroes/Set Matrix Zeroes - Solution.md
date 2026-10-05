---
topic: "Math & Geometry"
difficulty: Medium
leetcode: https://leetcode.com/problems/set-matrix-zeroes/
neetcode: https://neetcode.io/problems/set-zeroes-in-matrix
---
# Set Matrix Zeroes - Solution

**Question:** [[Set Matrix Zeroes - Question]] · **Difficulty:** Medium

## Intuition

The `O(m + n)` approach records which rows and columns contain a zero. To get `O(1)` extra space, store those markers in the matrix itself: `matrix[0][c]` marks column `c` and `matrix[r][0]` marks row `r`. The top-left cell `matrix[0][0]` would have to mark both row 0 and column 0, so keep one extra boolean, `first_row_zero`, for row 0. Apply the inner markers before clearing row 0 and column 0, because clearing them first would wipe out the markers.

## Approach

1. Scan every cell. When `matrix[r][c] == 0`, set `matrix[0][c] = 0`. Also set `matrix[r][0] = 0` if `r > 0`, or `first_row_zero = True` if `r == 0`.
2. For `r` in `1..m-1` and `c` in `1..n-1`, set `matrix[r][c] = 0` if `matrix[0][c] == 0` or `matrix[r][0] == 0`.
3. If `matrix[0][0] == 0`, column 0 must be zeroed: set `matrix[r][0] = 0` for all `r`.
4. If `first_row_zero`, set all of row 0 to zero.

## Code

```python
from typing import List


class Solution:
	def setZeroes(self, matrix: List[List[int]]) -> None:
		m, n = len(matrix), len(matrix[0])
		first_row_zero = False

		# 1) Use row 0 / column 0 as markers; row 0 gets its own flag
		for r in range(m):
			for c in range(n):
				if matrix[r][c] == 0:
					matrix[0][c] = 0
					if r > 0:
						matrix[r][0] = 0
					else:
						first_row_zero = True

		# 2) Zero the inner cells based on the markers
		for r in range(1, m):
			for c in range(1, n):
				if matrix[0][c] == 0 or matrix[r][0] == 0:
					matrix[r][c] = 0

		# 3) Column 0 (marker lives in matrix[0][0])
		if matrix[0][0] == 0:
			for r in range(m):
				matrix[r][0] = 0

		# 4) Row 0 last, since it held the column markers
		if first_row_zero:
			for c in range(n):
				matrix[0][c] = 0
```

## Complexity

- **Time:** `O(m * n)`: a constant number of passes over the grid.
- **Space:** `O(1)`: the markers are stored in the matrix itself, plus one boolean.

## Other Approaches

- **Row/column sets:** record the zero rows and zero columns in two sets, then make a second pass. Time `O(m * n)`, Space `O(m + n)`.
- **Copy the matrix:** read zeros from a copy and write into the original. Time `O(m * n * (m + n))` if done naively, Space `O(m * n)`.

## Key Takeaway

To meet an `O(1)` space requirement on a grid, reuse its first row and column as bookkeeping. Watch the shared corner cell, and process the marker row and column last.
