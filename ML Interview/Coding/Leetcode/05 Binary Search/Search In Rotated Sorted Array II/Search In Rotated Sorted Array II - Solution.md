---
topic: "Binary Search"
difficulty: Medium
leetcode: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
neetcode: https://neetcode.io/problems/search-in-rotated-sorted-array-ii
---
# Search In Rotated Sorted Array II - Solution

**Question:** [[Search In Rotated Sorted Array II - Question]] · **Difficulty:** Medium

## Intuition

Use the same idea as the distinct version — one side of `mid` is sorted, so check whether `target` falls in it. Duplicates break this only when `nums[lo] == nums[mid] == nums[hi]`, because then we cannot tell which side is sorted; in that case we can safely shrink both ends by one, since neither equals the target.

## Approach

1. `lo = 0`, `hi = n - 1`; loop while `lo <= hi`.
2. If `nums[mid] == target`, return `True`.
3. If `nums[lo] == nums[mid] == nums[hi]`, do `lo += 1`, `hi -= 1` and continue.
4. If `nums[lo] <= nums[mid]` (left sorted): go left if `nums[lo] <= target < nums[mid]`, else right.
5. Else (right sorted): go right if `nums[mid] < target <= nums[hi]`, else left.
6. Return `False` when the range empties.

## Code

```python
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True
            if nums[lo] == nums[mid] == nums[hi]:
                # ambiguous: can't tell which side is sorted, shrink both ends
                lo += 1
                hi -= 1
            elif nums[lo] <= nums[mid]:             # left half sorted
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:                                   # right half sorted
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False
```

## Complexity

- **Time:** `O(log n)` on average, `O(n)` worst case — with many duplicates (e.g. `[1,1,1,…,13,…,1]`) we may only shrink by one element per step. This answers the follow-up.
- **Space:** `O(1)`.

## Other Approaches

- **Linear scan / `target in nums`:** Time `O(n)`, Space `O(1)` — same worst case, but no logarithmic average.

## Key Takeaway

Duplicates in rotated arrays create an ambiguous case (`lo == mid == hi` values); handle it by trimming the ends, accepting an `O(n)` worst case.
