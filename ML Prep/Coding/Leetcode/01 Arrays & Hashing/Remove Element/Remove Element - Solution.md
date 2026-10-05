---
topic: "Arrays & Hashing"
difficulty: Easy
leetcode: https://leetcode.com/problems/remove-element/
neetcode: https://neetcode.io/problems/remove-element
---
# Remove Element - Solution

**Question:** [[Remove Element - Question]] · **Difficulty:** Easy

## Intuition

Use two pointers: a read pointer scans every element, and a write pointer `k` marks where the next kept element goes. Copying each non-`val` element forward compacts the survivors into the prefix `nums[:k]` without extra memory.

## Approach

1. Set `k = 0`.
2. For each element `x` in `nums`: if `x != val`, write it to `nums[k]` and increment `k`.
3. Return `k`.

## Code

```python
from typing import List


class Solution:
	def removeElement(self, nums: List[int], val: int) -> int:
		k = 0  # next write position
		for x in nums:
			if x != val:
				nums[k] = x
				k += 1
		return k
```

## Complexity

- **Time:** `O(n)` — one pass over the array.
- **Space:** `O(1)` — in-place with two indices.

## Other Approaches

- **Swap with the end:** when `nums[i] == val`, overwrite it with the last element and shrink the length; fewer writes when `val` is rare (order not preserved) — Time `O(n)`, Space `O(1)`.

## Key Takeaway

Read/write two-pointer compaction is the standard pattern for in-place filtering of arrays (also used in Remove Duplicates, Move Zeroes).
