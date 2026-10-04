---
topic: "Two Pointers"
difficulty: Easy
leetcode: https://leetcode.com/problems/merge-sorted-array/
neetcode: https://neetcode.io/problems/merge-sorted-array
---
# Merge Sorted Array - Solution

**Question:** [[Merge Sorted Array - Question]] · **Difficulty:** Easy

## Intuition

Merging from the front would overwrite unread values of `nums1`. The free space is at the back, so fill `nums1` from the end: repeatedly place the larger of the two current tails at the last free position. Writes never overtake unread elements.

## Approach

1. Set `i = m - 1`, `j = n - 1`, `k = m + n - 1`.
2. While `j >= 0`:
   - If `i >= 0` and `nums1[i] > nums2[j]`, write `nums1[i]` to `nums1[k]` and decrement `i`.
   - Otherwise write `nums2[j]` to `nums1[k]` and decrement `j`.
   - Decrement `k`.
3. Any remaining `nums1` elements are already in place.

## Code

```python
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1
        # only need to loop until nums2 is exhausted
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
```

## Complexity

- **Time:** `O(m + n)` — each element is written once.
- **Space:** `O(1)` — merged in place.

## Other Approaches

- **Copy and sort:** `nums1[m:] = nums2; nums1.sort()` — Time `O((m+n) log(m+n))`, Space `O(1)` to `O(m+n)` depending on sort.
- **Forward merge with a copy of nums1:** copy the first `m` items, then standard merge — Time `O(m + n)`, Space `O(m)`.

## Key Takeaway

When the buffer space is at the end of an array, merge backwards from the largest elements to avoid overwriting data.
