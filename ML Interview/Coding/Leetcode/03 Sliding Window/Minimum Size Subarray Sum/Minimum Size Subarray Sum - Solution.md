---
topic: "Sliding Window"
difficulty: Medium
leetcode: https://leetcode.com/problems/minimum-size-subarray-sum/
neetcode: https://neetcode.io/problems/minimum-size-subarray-sum
---
# Minimum Size Subarray Sum - Solution

**Question:** [[Minimum Size Subarray Sum - Question]] · **Difficulty:** Medium

## Intuition

All values are positive, so extending a window always increases its sum and shrinking always decreases it. Expand the right edge until the sum reaches `target`, then shrink from the left as long as it stays valid, recording the smallest valid width.

## Approach

1. Set `l = 0`, `total = 0`, `best = inf`.
2. For each `r`: add `nums[r]` to `total`.
   - While `total >= target`: update `best = min(best, r - l + 1)`, subtract `nums[l]`, move `l` right.
3. Return `0` if `best` is still `inf`, else `best`.

## Code

```python
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = total = 0
        best = float("inf")
        for r, x in enumerate(nums):
            total += x
            # shrink while the window still meets the target
            while total >= target:
                best = min(best, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if best == float("inf") else best
```

## Complexity

- **Time:** `O(n)` — each element is added once and removed at most once.
- **Space:** `O(1)` — a few variables.

## Other Approaches

- **Prefix sums + binary search:** for each start `i`, binary search the first prefix `>= prefix[i] + target` — Time `O(n log n)`, Space `O(n)`.
- **Brute force:** check every subarray — Time `O(n^2)`, Space `O(1)`.

## Key Takeaway

Positive numbers make window sums monotonic, which is what makes the shrinkable sliding window correct; with negatives you need prefix sums + a deque or hash map instead.
