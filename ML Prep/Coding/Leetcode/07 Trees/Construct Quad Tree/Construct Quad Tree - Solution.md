---
topic: "Trees"
difficulty: Medium
leetcode: https://leetcode.com/problems/construct-quad-tree/
neetcode: https://neetcode.io/problems/construct-quad-tree
---
# Construct Quad Tree - Solution

**Question:** [[Construct Quad Tree - Question]] · **Difficulty:** Medium

## Intuition

The definition is recursive: a region is either uniform (a leaf) or four quadrants. Building bottom-up avoids rescanning cells: construct the four children first; if all four are leaves with the same value, collapse them into a single leaf, otherwise create an internal node pointing to them.

## Approach

1. Define `build(r, c, size)` for the square with top-left `(r, c)`.
2. If `size == 1`, return a leaf with `grid[r][c]`.
3. Otherwise recursively build the four quadrants of size `size // 2`.
4. If all four are leaves with equal `val`, return one leaf with that value.
5. Else return an internal node (`isLeaf=False`) with those four children.
6. Return `build(0, 0, n)`.

## Code

```python
from typing import List

# class Node:
#     def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
#         self.val = val
#         self.isLeaf = isLeaf
#         self.topLeft = topLeft
#         self.topRight = topRight
#         self.bottomLeft = bottomLeft
#         self.bottomRight = bottomRight

class Solution:
	def construct(self, grid: List[List[int]]) -> 'Node':
		def build(r, c, size):
			if size == 1:
				return Node(bool(grid[r][c]), True, None, None, None, None)
			h = size // 2
			kids = [build(r, c, h), build(r, c + h, h),
					build(r + h, c, h), build(r + h, c + h, h)]
			# merge four identical leaves into one leaf
			if all(k.isLeaf for k in kids) and len({k.val for k in kids}) == 1:
				return Node(kids[0].val, True, None, None, None, None)
			return Node(True, False, *kids)

		return build(0, 0, len(grid))
```

## Complexity

- **Time:** `O(n^2)` — every cell is a base case once, and there are `O(n^2)` internal recursive calls in total (geometric series over levels).
- **Space:** `O(log n)` recursion depth, plus the `O(n^2)` nodes allocated temporarily (the returned tree itself has up to `O(n^2)` nodes).

## Other Approaches

- **Top-down uniform check:** at each region scan all cells; if uniform make a leaf, else split — Time `O(n^2 log n)`, Space `O(log n)`.
- **Top-down with 2D prefix sums:** a region is uniform iff its sum is `0` or `size^2`, checked in `O(1)` — Time `O(n^2)`, Space `O(n^2)`.

## Key Takeaway

Divide-and-conquer on a grid: solve the four quadrants and merge. Building bottom-up (or using 2D prefix sums) avoids repeatedly scanning the same cells.
