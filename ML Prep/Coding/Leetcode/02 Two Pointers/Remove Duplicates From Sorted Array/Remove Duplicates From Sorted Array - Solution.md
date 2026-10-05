---
topic: "Two Pointers"
difficulty: Easy
leetcode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
neetcode: https://neetcode.io/problems/remove-duplicates-from-sorted-array
---
# Remove Duplicates From Sorted Array - Solution

**Question:** [[Remove Duplicates From Sorted Array - Question]] · **Difficulty:** Easy

## Intuition

Because the array is sorted, duplicates are adjacent. Keep a write pointer `k` marking the end of the deduplicated prefix; a read pointer scans forward and copies a value only when it differs from the previous one.

## Approach

1. Set `k = 1` (the first element is always kept).
2. For `i` from `1` to `n - 1`: if `nums[i] != nums[i - 1]`, write `nums[k] = nums[i]` and increment `k`.
3. Return `k`.

## Code

```python
from typing import List


class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		k = 1  # nums[:k] is the deduplicated prefix
		for i in range(1, len(nums)):
			if nums[i] != nums[i - 1]:
				nums[k] = nums[i]
				k += 1
		return k
```

## Complexity

- **Time:** `O(n)` — single pass.
- **Space:** `O(1)` — in place.

## Other Approaches

- **Set + sort copy:** `uniq = sorted(set(nums))` then copy back — Time `O(n log n)`, Space `O(n)`; violates the in-place spirit.

## Key Takeaway

The read/write (slow/fast) pointer pattern compacts an array in place; it generalizes to "keep at most k duplicates" by comparing with `nums[k - 2]`-style lookbacks.
