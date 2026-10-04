---
topic: "Bit Manipulation"
difficulty: Easy
leetcode: https://leetcode.com/problems/number-of-1-bits/
neetcode: https://neetcode.io/problems/number-of-one-bits
---
# Number of 1 Bits

**Topic:** [[18 Bit Manipulation|Bit Manipulation]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/number-of-1-bits/) · [NeetCode](https://neetcode.io/problems/number-of-one-bits)

**Solve it in:** [[Number of 1 Bits]] · **Answer:** [[Number of 1 Bits - Solution]]

## Problem

Given a positive integer `n`, return the number of `1` bits in its binary representation. This count is also called the **Hamming weight** or population count.

(Older versions of this problem passed `n` as a 32-bit unsigned integer, so values up to `2^32 - 1` should also work.)

## Examples

**Example 1**
```text
Input: n = 11
Output: 3
Explanation: 11 = 0b1011 has three set bits.
```

**Example 2**
```text
Input: n = 128
Output: 1
Explanation: 128 = 0b10000000
```

**Example 3**
```text
Input: n = 2147483645
Output: 30
Explanation: 0b1111111111111111111111111111101 has thirty set bits.
```

## Constraints

- `1 <= n <= 2^31 - 1`

## Starter Code & Test Cases

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.hammingWeight(11) == 3
    assert s.hammingWeight(128) == 1
    assert s.hammingWeight(2147483645) == 30
    assert s.hammingWeight(1) == 1
    assert s.hammingWeight(2147483647) == 31
    assert s.hammingWeight(0) == 0
    assert s.hammingWeight(4294967293) == 31  # 32-bit unsigned variant
    assert s.hammingWeight(0b1010101010) == 5
    print("All tests passed!")
```
