---
topic: "Two Pointers"
difficulty: Medium
leetcode: https://leetcode.com/problems/rotate-array/
neetcode: https://neetcode.io/problems/rotate-array
---
# Rotate Array - Solution

**Question:** [[Rotate Array - Question]] · **Difficulty:** Medium

## Intuition

After rotating right by `k`, the last `k` elements come first, followed by the first `n - k`. Reversing the whole array puts those two blocks in the right order but each block backwards; reversing each block individually fixes them. Reduce `k` modulo `n` first.

## Approach

1. `k %= n`.
2. Reverse the entire array.
3. Reverse the first `k` elements.
4. Reverse the remaining `n - k` elements.

## Code

```python
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # rotations by n are no-ops

        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
```

## Complexity

- **Time:** `O(n)` — each element is swapped a constant number of times.
- **Space:** `O(1)` — in-place swaps.

## Other Approaches

- **Extra array:** place `nums[i]` at `(i + k) % n` in a copy, then copy back — Time `O(n)`, Space `O(n)`.
- **Cyclic replacements:** follow each cycle of `i -> (i + k) % n` moving elements one at a time — Time `O(n)`, Space `O(1)`, but trickier to get right.

## Key Takeaway

The triple-reverse trick rotates (or swaps two blocks of) an array in place; always normalize `k` with `k % n`.
