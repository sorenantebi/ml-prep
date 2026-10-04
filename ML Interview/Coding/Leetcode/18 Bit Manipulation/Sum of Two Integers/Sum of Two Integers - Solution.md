---
topic: "Bit Manipulation"
difficulty: Medium
leetcode: https://leetcode.com/problems/sum-of-two-integers/
neetcode: https://neetcode.io/problems/sum-of-two-integers
---
# Sum of Two Integers - Solution

**Question:** [[Sum of Two Integers - Question]] · **Difficulty:** Medium

## Intuition

Binary addition breaks into two parts. `a ^ b` gives the sum of each bit position ignoring carries, and `(a & b) << 1` gives the carries. Repeat with those two values until there are no carries left. Python integers have unlimited width, so a negative number's carries would never stop moving left. Emulating a 32-bit word with `& 0xFFFFFFFF`, then converting the final value back from two's complement, fixes this.

## Approach

1. Let `mask = 0xFFFFFFFF` (32 bits) and `max_int = 0x7FFFFFFF`.
2. While `b != 0`: `a, b = (a ^ b) & mask, ((a & b) << 1) & mask`.
3. If `a <= max_int` the result is non-negative, so return `a`. Otherwise it is a negative 32-bit value: return `~(a ^ mask)` to sign-extend it into a Python negative int.

## Code

```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b != 0:
            # partial sum without carry, and the carry shifted into place (kept to 32 bits)
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # interpret the 32-bit pattern as signed two's complement
        return a if a <= max_int else ~(a ^ mask)
```

## Complexity

- **Time:** `O(1)`: at most 32 iterations, because each round pushes the carry at least one bit to the left.
- **Space:** `O(1)`.

## Other Approaches

- **Built-in shortcut:** `sum([a, b])` meets the letter of the rules but defeats the point of the problem. Time `O(1)`, Space `O(1)`.
- **Recursive form:** `getSum(a ^ b, (a & b) << 1)` with the same masking. This is the same idea using `O(32)` recursion depth. Time `O(1)`, Space `O(1)`.

## Key Takeaway

Addition is XOR (sum without carry) plus AND-shift (carry), repeated until the carry is 0. In Python, mask to 32 bits and convert back with `~(a ^ mask)` to handle negatives.
