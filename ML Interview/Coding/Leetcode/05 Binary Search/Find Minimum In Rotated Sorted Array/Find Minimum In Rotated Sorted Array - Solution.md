---
topic: "Binary Search"
difficulty: Medium
leetcode: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
neetcode: https://neetcode.io/problems/find-minimum-in-rotated-sorted-array
---
# Find Minimum In Rotated Sorted Array - Solution

**Question:** [[Find Minimum In Rotated Sorted Array - Question]] · **Difficulty:** Medium

## Intuition

The rotated array consists of two sorted runs, and the minimum is the first element of the second run. Comparing `nums[mid]` with the last element `nums[hi]` tells us which run `mid` is in: if `nums[mid] > nums[hi]`, the drop (and minimum) is strictly to the right of `mid`; otherwise the minimum is at `mid` or to its left.

## Approach

1. Set `lo = 0`, `hi = n - 1`.
2. While `lo < hi`: `mid = (lo + hi) // 2`.
3. If `nums[mid] > nums[hi]`, set `lo = mid + 1`; else set `hi = mid`.
4. Return `nums[lo]`.

## Code

```python
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1   # mid is in the left (larger) run
            else:
                hi = mid       # mid is in the right run; could be the min
        return nums[lo]
```

## Complexity

- **Time:** `O(log n)` — the range halves each iteration.
- **Space:** `O(1)`.

## Other Approaches

- **Linear scan / `min(nums)`:** Time `O(n)`, Space `O(1)`.
- **Compare with `nums[0]`:** if the range is already sorted return its left end, else narrow toward the half containing the drop — Time `O(log n)`, Space `O(1)`; slightly more cases to handle.

## Key Takeaway

In rotated-array searches, compare `mid` against the right end `hi` to decide which sorted run you are in; that comparison avoids the fully-sorted special case.
