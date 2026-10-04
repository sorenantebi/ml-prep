---
topic: "Arrays & Hashing"
difficulty: Hard
leetcode: https://leetcode.com/problems/first-missing-positive/
neetcode: https://neetcode.io/problems/first-missing-positive
---
# First Missing Positive - Solution

**Question:** [[First Missing Positive - Question]] · **Difficulty:** Hard

## Intuition

For an array of length `n`, the answer is always in `1..n+1`, so only values in that range matter. Use the array itself as a hash table: place each value `v` in `1..n` at index `v - 1` by swapping (cyclic sort). Afterwards, the first index `i` where `nums[i] != i + 1` reveals the missing number; if none, the answer is `n + 1`.

## Approach

1. For each index `i`, while `nums[i]` is in `1..n` and the target slot `nums[i] - 1` does not already hold the same value, swap `nums[i]` into its slot.
2. Scan again: return `i + 1` for the first `i` with `nums[i] != i + 1`.
3. If every slot is correct, return `n + 1`.

## Code

```python
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            # keep swapping the value at i into its home slot (value v -> index v-1);
            # the second check stops infinite loops on duplicates
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
```

## Complexity

- **Time:** `O(n)` — every swap places one value in its final slot, so there are at most `n` swaps in total.
- **Space:** `O(1)` — the input array is reused as the lookup table.

## Other Approaches

- **Hash set:** insert all values and probe `1, 2, ...` — Time `O(n)`, Space `O(n)`.
- **Sign marking:** replace non-positive / out-of-range values with `n + 1`, then mark presence of `v` by negating `nums[v - 1]`; the first positive index gives the answer — Time `O(n)`, Space `O(1)`.

## Key Takeaway

When values are bounded by the array length, the array can serve as its own hash table (cyclic sort or sign marking), giving `O(1)` extra space.
