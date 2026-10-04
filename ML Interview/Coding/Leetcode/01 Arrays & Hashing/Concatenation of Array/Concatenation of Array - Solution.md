---
topic: "Arrays & Hashing"
difficulty: Easy
leetcode: https://leetcode.com/problems/concatenation-of-array/
neetcode: https://neetcode.io/problems/concatenation-of-array
---
# Concatenation of Array - Solution

**Question:** [[Concatenation of Array - Question]] · **Difficulty:** Easy

## Intuition

The answer is just the input written out twice. We can build the result by appending each element at position `i` and again at position `i + n`, or simply let Python concatenate the list with itself.

## Approach

1. Let `n = len(nums)` and allocate a result of size `2n`.
2. For each index `i`, write `nums[i]` to `ans[i]` and to `ans[i + n]`.
3. Return `ans`.

## Code

```python
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i, x in enumerate(nums):
            ans[i] = x
            ans[i + n] = x  # second copy, shifted by n
        return ans
```

## Complexity

- **Time:** `O(n)` — each element is written twice.
- **Space:** `O(n)` — the output array of size `2n` (no extra space beyond the output).

## Other Approaches

- **Built-in concatenation:** `return nums + nums` (or `nums * 2`) — Time `O(n)`, Space `O(n)`.

## Key Takeaway

Warm-up array indexing: when an output is a fixed transformation of positions, compute the target index directly (`i` and `i + n`) instead of building it incrementally.
