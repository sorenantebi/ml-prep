---
topic: "Math & Geometry"
difficulty: Medium
leetcode: https://leetcode.com/problems/spiral-matrix/
neetcode: https://neetcode.io/problems/spiral-matrix
---
# Spiral Matrix - Solution

**Question:** [[Spiral Matrix - Question]] · **Difficulty:** Medium

## Intuition

Keep four boundaries: `top`, `bottom`, `left`, `right`. Walk each side of the current outer ring and move the matching boundary inward once that side is done. The difficult cases are a single leftover row or column. After the top row and right column have been taken, re-check the boundaries before walking back left or up, so no element is visited twice.

## Approach

1. Set `top, bottom = 0, m - 1` and `left, right = 0, n - 1`.
2. While `top <= bottom` and `left <= right`:
   - read the top row from `left` to `right`, then `top += 1`;
   - read the right column from `top` to `bottom`, then `right -= 1`;
   - if `top <= bottom`, read the bottom row from `right` to `left`, then `bottom -= 1`;
   - if `left <= right`, read the left column from `bottom` to `top`, then `left += 1`.
3. Return the collected list.

## Code

```python
from typing import List


class Solution:
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		res = []
		top, bottom = 0, len(matrix) - 1
		left, right = 0, len(matrix[0]) - 1

		while top <= bottom and left <= right:
			for c in range(left, right + 1):
				res.append(matrix[top][c])
			top += 1
			for r in range(top, bottom + 1):
				res.append(matrix[r][right])
			right -= 1
			if top <= bottom:  # a bottom row still remains
				for c in range(right, left - 1, -1):
					res.append(matrix[bottom][c])
				bottom -= 1
			if left <= right:  # a left column still remains
				for r in range(bottom, top - 1, -1):
					res.append(matrix[r][left])
				left += 1
		return res
```

## Complexity

- **Time:** `O(m * n)`: each element is appended exactly once.
- **Space:** `O(1)` extra, not counting the output list.

## Other Approaches

- **Direction vector + visited marks:** step in direction `(dr, dc)` and turn right when the next cell is out of bounds or already visited. Time `O(m * n)`, Space `O(m * n)` for the visited grid (or `O(1)` if you overwrite the input with a sentinel).
- **Peel and rotate:** pop the first row, rotate the rest counter-clockwise (`list(zip(*matrix))[::-1]`), and repeat. Easy to write but `O(m * n * min(m, n))` time.

## Key Takeaway

Shrinking-boundary traversal handles spiral and layered matrix problems. After each pass, re-check `top <= bottom` and `left <= right` so a single row or column isn't read twice.
