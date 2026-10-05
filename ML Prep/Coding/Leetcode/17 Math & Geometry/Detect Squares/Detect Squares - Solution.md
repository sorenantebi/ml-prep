---
topic: "Math & Geometry"
difficulty: Medium
leetcode: https://leetcode.com/problems/detect-squares/
neetcode: https://neetcode.io/problems/count-squares
---
# Detect Squares - Solution

**Question:** [[Detect Squares - Question]] · **Difficulty:** Medium

## Intuition

Fix the query point `(qx, qy)`. Any axis-aligned square through it has a diagonal corner `(x, y)` with `|x - qx| == |y - qy| != 0`, and the other two corners are then fixed at `(x, qy)` and `(qx, y)`. Store point counts in a hash map, try each stored point as the diagonal corner, and multiply the counts of the three corners.

## Approach

1. Keep `cnt`, a Counter of `(x, y) -> multiplicity`, and `pts`, a list of the distinct points added.
2. `add`: increment `cnt[(x, y)]`; if it is the first copy, also append to `pts`.
3. `count(qx, qy)`: for each distinct `(x, y)` in `pts`:
   - skip it unless `abs(x - qx) == abs(y - qy)` and `x != qx`, so that it is a diagonal corner of a square with positive area;
   - add `cnt[(x, y)] * cnt[(x, qy)] * cnt[(qx, y)]` to the result.
4. Return the sum.

## Code

```python
from typing import List
from collections import Counter


class DetectSquares:
	def __init__(self):
		self.cnt = Counter()
		self.pts = []  # distinct points, so each diagonal is visited once

	def add(self, point: List[int]) -> None:
		p = tuple(point)
		if self.cnt[p] == 0:
			self.pts.append(p)
		self.cnt[p] += 1

	def count(self, point: List[int]) -> int:
		qx, qy = point
		res = 0
		for x, y in self.pts:
			# (x, y) must be a diagonal corner of a square with positive area
			if abs(x - qx) != abs(y - qy) or x == qx:
				continue
			res += self.cnt[(x, y)] * self.cnt[(x, qy)] * self.cnt[(qx, y)]
		return res
```

## Complexity

- **Time:** `add` is `O(1)`. `count` is `O(P)`, where `P` is the number of distinct points added so far.
- **Space:** `O(P)`: for the counter and the list of distinct points.

## Other Approaches

- **Iterate over side length:** for each `d` in `1..1000` and both directions, look up the three corners via `cnt`. Time `O(C)` per query where `C = 1000` is the coordinate range, Space `O(P)`.
- **Group by x-coordinate:** for each stored point sharing `qx`, the side length is fixed, so check the two candidate squares (left and right). Time `O(points on the same column)` per query, Space `O(P)`.

## Key Takeaway

For geometry counting, fix one point and enumerate a single free parameter (here the diagonal corner); the other points are then determined. Multiply hash-map counts to account for duplicates.
