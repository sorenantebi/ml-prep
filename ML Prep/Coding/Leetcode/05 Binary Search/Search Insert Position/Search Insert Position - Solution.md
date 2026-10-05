---
topic: "Binary Search"
difficulty: Easy
leetcode: https://leetcode.com/problems/search-insert-position/
neetcode: https://neetcode.io/problems/search-insert-position
---
# Search Insert Position - Solution

**Question:** [[Search Insert Position - Question]] · **Difficulty:** Easy

## Intuition

We want the first index whose value is `>= target` (the "lower bound"). That predicate is false then true across the sorted array, so binary search can find the boundary; it equals the index of `target` if present, or its insertion point otherwise.

## Approach

1. Search over the half-open range `lo = 0`, `hi = n` (the answer can be `n`).
2. While `lo < hi`: `mid = (lo + hi) // 2`.
3. If `nums[mid] < target`, the answer is to the right: `lo = mid + 1`; else `hi = mid`.
4. Return `lo`.

## Code

```python
from typing import List


class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		lo, hi = 0, len(nums)  # answer lies in [lo, hi]
		while lo < hi:
			mid = (lo + hi) // 2
			if nums[mid] < target:
				lo = mid + 1
			else:
				hi = mid       # mid could be the answer
		return lo
```

## Complexity

- **Time:** `O(log n)` — halving the range each step.
- **Space:** `O(1)`.

## Other Approaches

- **Linear scan:** return the first index with `nums[i] >= target`, else `n` — Time `O(n)`, Space `O(1)`.
- **Library:** `bisect.bisect_left(nums, target)` — Time `O(log n)`, Space `O(1)`.

## Key Takeaway

"Find the first position where a condition becomes true" is the lower-bound template: half-open `[lo, hi)`, `hi = mid` when true, `lo = mid + 1` when false.
