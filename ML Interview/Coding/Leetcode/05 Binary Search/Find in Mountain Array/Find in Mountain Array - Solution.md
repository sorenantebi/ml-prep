---
topic: "Binary Search"
difficulty: Hard
leetcode: https://leetcode.com/problems/find-in-mountain-array/
neetcode: https://neetcode.io/problems/find-in-mountain-array
---
# Find in Mountain Array - Solution

**Question:** [[Find in Mountain Array - Question]] · **Difficulty:** Hard

## Intuition

A mountain array is two sorted runs glued at the peak: ascending on the left, descending on the right. Find the peak with binary search (compare `get(mid)` with `get(mid + 1)`), then binary search the ascending side first — that guarantees the minimum index — and only if not found, search the descending side with the comparison reversed. Three `O(log n)` searches stay well under the 100-call limit.

## Approach

1. **Peak:** `lo = 0`, `hi = n - 1`; while `lo < hi`, if `get(mid) < get(mid + 1)` the peak is to the right (`lo = mid + 1`), else `hi = mid`. Then `peak = lo`.
2. **Ascending side `[0, peak]`:** standard binary search for `target`; return the index if found.
3. **Descending side `[peak + 1, n - 1]`:** binary search with reversed ordering (go right when `get(mid) > target`).
4. Return `-1` if neither search finds `target`.

## Code

```python
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: "MountainArray") -> int:
        n = mountainArr.length()

        # 1) find the peak index
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                lo = mid + 1     # still climbing
            else:
                hi = mid         # at or past the peak
        peak = lo

        # 2) binary search on [lo, hi]; ascending=True for the left side
        def bsearch(lo: int, hi: int, ascending: bool) -> int:
            while lo <= hi:
                mid = (lo + hi) // 2
                val = mountainArr.get(mid)
                if val == target:
                    return mid
                if (val < target) == ascending:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return -1

        idx = bsearch(0, peak, True)     # left side first -> minimum index
        if idx != -1:
            return idx
        return bsearch(peak + 1, n - 1, False)
```

## Complexity

- **Time:** `O(log n)` — three binary searches (about `2·log n` calls for the peak plus `log n` per side, ~70 calls for `n = 10^4`).
- **Space:** `O(1)`.

## Other Approaches

- **Linear scan:** call `get(i)` for `i = 0..n-1` and return the first match — Time `O(n)`, Space `O(1)`; exceeds the 100-call limit.
- **Caching `get` results:** memoize calls in a dict to avoid repeated reads of the same index — same `O(log n)`, slightly fewer API calls.

## Key Takeaway

Decompose a bitonic (mountain) array into peak-finding plus two monotone binary searches; search the left side first when the smallest index is required.
