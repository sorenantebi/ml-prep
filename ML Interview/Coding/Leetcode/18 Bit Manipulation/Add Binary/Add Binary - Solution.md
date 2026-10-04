---
topic: "Bit Manipulation"
difficulty: Easy
leetcode: https://leetcode.com/problems/add-binary/
neetcode: https://neetcode.io/problems/add-binary
---
# Add Binary - Solution

**Question:** [[Add Binary - Question]] · **Difficulty:** Easy

## Intuition

This is grade-school addition in base 2. Use two pointers starting at the right end of each string and a carry. At each position the digit sum is between 0 and 3: the output bit is `sum % 2` and the new carry is `sum // 2`. Keep going until both strings are used up and no carry remains.

## Approach

1. Set `i = len(a) - 1`, `j = len(b) - 1`, `carry = 0`, and `res = []`.
2. While `i >= 0` or `j >= 0` or `carry`:
   - `total = carry`, plus `a[i]` if `i >= 0`, plus `b[j]` if `j >= 0`;
   - append `str(total % 2)`, set `carry = total // 2`, and decrement `i` and `j`.
3. Return the reversed `res` joined into a string.

## Code

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, carry = len(a) - 1, len(b) - 1, 0
        res = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += ord(a[i]) - ord('0')
                i -= 1
            if j >= 0:
                total += ord(b[j]) - ord('0')
                j -= 1
            res.append(str(total % 2))
            carry = total // 2
        return "".join(reversed(res))
```

## Complexity

- **Time:** `O(max(m, n))`: one step per output bit.
- **Space:** `O(max(m, n))`: for the output, with `O(1)` extra beyond it.

## Other Approaches

- **Built-in conversion:** `bin(int(a, 2) + int(b, 2))[2:]`. Short, but it relies on big integers. Time `O(m + n)`, Space `O(m + n)`.
- **Bitwise add without `+`:** convert to integers, then loop `x, y = x ^ y, (x & y) << 1` until `y == 0`. Time `O((m + n) * max(m, n))` with big integers, Space `O(m + n)`.

## Key Takeaway

Adding two digit strings in any base uses the same template: right-aligned pointers, a carry, and a loop that runs while either pointer is valid or the carry is non-zero, followed by a reverse at the end.
