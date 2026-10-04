---
topic: "Bit Manipulation"
difficulty: Easy
leetcode: https://leetcode.com/problems/counting-bits/
neetcode: https://neetcode.io/problems/counting-bits
---
# Counting Bits - Solution

**Question:** [[Counting Bits - Question]] · **Difficulty:** Easy

## Intuition

`i >> 1` is `i` with its last bit removed, and it is smaller than `i`, so its answer has already been computed. The bit count of `i` is therefore the count for `i >> 1` plus the bit that was dropped, `i & 1`. That gives a one-line DP recurrence.

## Approach

1. Create `ans = [0] * (n + 1)`.
2. For `i` from `1` to `n`: `ans[i] = ans[i >> 1] + (i & 1)`.
3. Return `ans`.

## Code

```python
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)  # bits of i/2 plus the dropped low bit
        return ans
```

## Complexity

- **Time:** `O(n)`: constant work per index.
- **Space:** `O(1)` extra, not counting the output array of size `n + 1`.

## Other Approaches

- **Lowest-set-bit DP:** `ans[i] = ans[i & (i - 1)] + 1`. Time `O(n)`, Space `O(1)` extra.
- **Popcount each number:** run Brian Kernighan's loop on every `i`. Time `O(n log n)`, Space `O(1)` extra.

## Key Takeaway

Bit DP: a number's answer often follows from a smaller number obtained by a shift (`i >> 1`) or by clearing a bit (`i & (i - 1)`). Look for such a recurrence before computing each value from scratch.
