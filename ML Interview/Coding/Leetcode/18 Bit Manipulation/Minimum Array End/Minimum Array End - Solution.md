---
topic: "Bit Manipulation"
difficulty: Medium
leetcode: https://leetcode.com/problems/minimum-array-end/
neetcode: https://neetcode.io/problems/minimum-array-end
---
# Minimum Array End - Solution

**Question:** [[Minimum Array End - Question]] · **Difficulty:** Medium

## Intuition

For the AND to equal `x`, every element must have all of `x`'s set bits. The valid numbers in increasing order are therefore `x` with its **zero bits** filled by the counting sequence 0, 1, 2, ... The smallest is `x` itself, which uses fill value 0, and the `n`-th smallest uses fill value `n - 1`. Spread the bits of `n - 1`, lowest first, into the zero-bit positions of `x`.

## Approach

1. Set `res = x`, `k = n - 1`, and `bit = 1`, a mask that scans the bit positions of `res`.
2. While `k > 0`:
   - if `res & bit == 0`, this is a free position: if `k & 1`, set it with `res |= bit`; then `k >>= 1`;
   - move to the next position with `bit <<= 1`.
3. Return `res`.

## Code

```python
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res, k, bit = x, n - 1, 1
        while k:
            if not (x & bit):  # free (zero) bit of x
                if k & 1:
                    res |= bit  # place next bit of n-1 here
                k >>= 1
            bit <<= 1
        return res
```

## Complexity

- **Time:** `O(log x + log n)`: each loop step moves `bit` one position, and the loop stops once all bits of `n - 1` are placed.
- **Space:** `O(1)`.

## Other Approaches

- **Iterate `n - 1` times with `cur = (cur + 1) | x`:** each step jumps to the next number that contains every bit of `x`. Time `O(n)`, Space `O(1)`. Fine for many inputs but slow at `n = 10^8` in Python.

## Key Takeaway

The numbers that contain a fixed mask `x`, in increasing order, correspond to counting in binary inside the free bits of `x`. To find the k-th one, deposit the bits of `k` into the zero positions of `x` (the operation known as "PDEP").
