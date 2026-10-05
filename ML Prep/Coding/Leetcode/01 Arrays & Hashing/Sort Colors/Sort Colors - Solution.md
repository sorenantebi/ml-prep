---
topic: "Arrays & Hashing"
difficulty: Medium
leetcode: https://leetcode.com/problems/sort-colors/
neetcode: https://neetcode.io/problems/sort-colors
---
# Sort Colors - Solution

**Question:** [[Sort Colors - Question]] · **Difficulty:** Medium

## Intuition

Dutch National Flag partitioning: maintain three regions with pointers `low` (end of the 0s), `mid` (current element), and `high` (start of the 2s). Each element under `mid` is either sent to the front, left in place, or sent to the back, so one pass sorts everything.

## Approach

1. Set `low = mid = 0` and `high = n - 1`.
2. While `mid <= high`:
   - If `nums[mid] == 0`: swap with `nums[low]`, increment both `low` and `mid`.
   - If `nums[mid] == 1`: just increment `mid`.
   - If `nums[mid] == 2`: swap with `nums[high]` and decrement `high` (do not advance `mid`, the swapped-in value is unexamined).
3. Invariant: `[0, low)` are 0s, `[low, mid)` are 1s, `(high, n-1]` are 2s.

## Code

```python
from typing import List


class Solution:
	def sortColors(self, nums: List[int]) -> None:
		low, mid, high = 0, 0, len(nums) - 1
		while mid <= high:
			if nums[mid] == 0:
				nums[low], nums[mid] = nums[mid], nums[low]
				low += 1
				mid += 1
			elif nums[mid] == 1:
				mid += 1
			else:
				nums[mid], nums[high] = nums[high], nums[mid]
				high -= 1  # don't move mid: the new nums[mid] still needs checking
```

## Complexity

- **Time:** `O(n)` — each step either advances `mid` or shrinks `high`.
- **Space:** `O(1)` — three pointers, sorting in place.

## Other Approaches

- **Counting sort (two passes):** count 0s, 1s, 2s, then overwrite the array — Time `O(n)`, Space `O(1)`.

## Key Takeaway

Three-way partitioning (Dutch National Flag) sorts a 3-valued array in one pass; it is also the core of 3-way quicksort for inputs with many duplicates.
