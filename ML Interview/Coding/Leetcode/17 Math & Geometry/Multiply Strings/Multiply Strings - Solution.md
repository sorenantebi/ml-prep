---
topic: "Math & Geometry"
difficulty: Medium
leetcode: https://leetcode.com/problems/multiply-strings/
neetcode: https://neetcode.io/problems/multiply-strings
---
# Multiply Strings - Solution

**Question:** [[Multiply Strings - Question]] · **Difficulty:** Medium

## Intuition

In grade-school multiplication, the digit at index `i` of `num1` times the digit at index `j` of `num2` lands in position `i + j + 1` of an array of length `m + n`, where `m + n` is the most digits the product can have. Add every pairwise product into its slot, push the carries left, and strip leading zeros.

## Approach

1. If either input is `"0"`, return `"0"`.
2. Create `res = [0] * (m + n)`.
3. For `i` from `m-1` down to `0` and `j` from `n-1` down to `0`:
   - `p = digit(num1[i]) * digit(num2[j]) + res[i + j + 1]`;
   - `res[i + j + 1] = p % 10`;
   - `res[i + j] += p // 10` (the carry goes one position left).
4. Skip leading zeros and join the digits into a string.

## Code

```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        res = [0] * (m + n)  # product has at most m + n digits

        for i in range(m - 1, -1, -1):
            d1 = ord(num1[i]) - ord('0')
            for j in range(n - 1, -1, -1):
                d2 = ord(num2[j]) - ord('0')
                p = d1 * d2 + res[i + j + 1]
                res[i + j + 1] = p % 10
                res[i + j] += p // 10  # carry; normalised by a later iteration

        # At most one leading zero (product of an m-digit and n-digit number has m+n-1 or m+n digits)
        start = 0
        while start < len(res) - 1 and res[start] == 0:
            start += 1
        return "".join(map(str, res[start:]))
```

## Complexity

- **Time:** `O(m * n)`: every pair of digits is multiplied once.
- **Space:** `O(m + n)`: for the result digit array, which is also the output.

## Other Approaches

- **Multiply by each digit, then add the strings:** compute `num1 * digit` for each digit of `num2`, pad with zeros, and sum using string addition. Time `O(n * (m + n))`, Space `O(m + n)`.
- **Karatsuba:** divide and conquer with 3 sub-multiplications instead of 4. Time `O(n^1.585)`. Overkill at these input sizes.

## Key Takeaway

Positional arithmetic on digit arrays uses the index rule: digit `i` times digit `j` contributes to position `i + j` (or `i + j + 1` when 0-indexed from the most significant digit). Accumulate into an array and carry as you go.
