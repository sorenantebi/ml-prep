---
topic: "Sliding Window"
difficulty: Medium
leetcode: https://leetcode.com/problems/find-k-closest-elements/
neetcode: https://neetcode.io/problems/find-k-closest-elements
---
# Find K Closest Elements - Solution

**Question:** [[Find K Closest Elements - Question]] · **Difficulty:** Medium

## Intuition

The answer is a contiguous window `arr[i : i + k]`, so we only need its left index `i` in `[0, n - k]`. Binary search on `i`: compare the element just leaving (`arr[mid]`) with the one just entering (`arr[mid + k]`). If `x - arr[mid] > arr[mid + k] - x`, the right candidate is strictly closer, so the window must start after `mid`; otherwise it starts at or before `mid`.

## Approach

1. Set `lo = 0`, `hi = n - k`.
2. While `lo < hi`:
   - `mid = (lo + hi) // 2`.
   - If `x - arr[mid] > arr[mid + k] - x`, set `lo = mid + 1`; else `hi = mid`.
3. Return `arr[lo : lo + k]`.

## Code

```python
from typing import List


class Solution:
	def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
		lo, hi = 0, len(arr) - k
		while lo < hi:
			mid = (lo + hi) // 2
			# arr[mid + k] beats arr[mid] -> shift window right
			if x - arr[mid] > arr[mid + k] - x:
				lo = mid + 1
			else:
				hi = mid
		return arr[lo:lo + k]
```

## Complexity

- **Time:** `O(log(n - k) + k)` — binary search plus slicing the output.
- **Space:** `O(1)` extra, excluding the `k`-element output.

## Other Approaches

- **Shrinking two pointers:** start with `l = 0`, `r = n - 1` and drop whichever end is farther (drop the right on ties) until `r - l + 1 == k` — Time `O(n - k)`, Space `O(1)`.
- **Sort by distance / heap:** sort by `(|a - x|, a)`, take `k`, re-sort — Time `O(n log n)`, Space `O(n)`.

## Key Takeaway

When the answer is a fixed-size window in a sorted array, binary search the window's start by comparing the two boundary candidates. Use the signed comparison `x - arr[mid] > arr[mid + k] - x` (not `abs`) to handle duplicates correctly.
