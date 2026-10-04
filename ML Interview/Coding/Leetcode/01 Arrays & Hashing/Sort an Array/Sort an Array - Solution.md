---
topic: "Arrays & Hashing"
difficulty: Medium
leetcode: https://leetcode.com/problems/sort-an-array/
neetcode: https://neetcode.io/problems/sort-an-array
---
# Sort an Array - Solution

**Question:** [[Sort an Array - Question]] · **Difficulty:** Medium

## Intuition

Merge sort guarantees `O(n log n)` in every case (unlike quicksort, which degrades on adversarial or many-duplicate inputs). Split the array in half, sort each half recursively, then merge the two sorted halves with two pointers.

## Approach

1. If the array has at most one element, it is already sorted.
2. Split at `mid = len // 2` and recursively sort the left and right halves.
3. Merge: repeatedly take the smaller head of the two halves (use `<=` to keep the sort stable), then append the leftovers.
4. Return the merged list.

## Code

```python
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr: List[int]) -> List[int]:
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
            merged, i, j = [], 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:  # <= keeps equal elements in original order
                    merged.append(left[i]); i += 1
                else:
                    merged.append(right[j]); j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        return merge_sort(nums)
```

## Complexity

- **Time:** `O(n log n)` — `log n` levels of recursion, each doing `O(n)` merging work.
- **Space:** `O(n)` — temporary lists for merging, plus `O(log n)` recursion stack.

## Other Approaches

- **Heap sort:** build a max-heap in place and repeatedly swap the max to the end — Time `O(n log n)`, Space `O(1)`.
- **Randomized quicksort (3-way partition):** fast in practice and in place — Time `O(n log n)` expected / `O(n^2)` worst, Space `O(log n)`.
- **Counting sort:** values lie in a bounded range of ~10^5 — Time `O(n + R)`, Space `O(R)`.

## Key Takeaway

Know at least one guaranteed `O(n log n)` sort (merge or heap sort) by heart, and when a bounded value range makes counting sort even faster.
