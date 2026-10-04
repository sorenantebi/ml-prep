---
topic: "Bit Manipulation"
difficulty: Medium
leetcode: https://leetcode.com/problems/bitwise-and-of-numbers-range/
neetcode: https://neetcode.io/problems/bitwise-and-of-numbers-range
---
# Bitwise AND of Numbers Range

**Topic:** [[18 Bit Manipulation|Bit Manipulation]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/bitwise-and-of-numbers-range/) · [NeetCode](https://neetcode.io/problems/bitwise-and-of-numbers-range)

**Solve it in:** [[Bitwise AND of Numbers Range]] · **Answer:** [[Bitwise AND of Numbers Range - Solution]]

## Problem

Given two integers `left` and `right` with `left <= right`, return the bitwise AND of **every** integer in the inclusive range `[left, right]`.

## Examples

**Example 1**
```text
Input: left = 5, right = 7
Output: 4
Explanation: 101 & 110 & 111 = 100
```

**Example 2**
```text
Input: left = 0, right = 0
Output: 0
```

**Example 3**
```text
Input: left = 1, right = 2147483647
Output: 0
```

## Constraints

- `0 <= left <= right <= 2^31 - 1`

## Starter Code & Test Cases

```python
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.rangeBitwiseAnd(5, 7) == 4
    assert s.rangeBitwiseAnd(0, 0) == 0
    assert s.rangeBitwiseAnd(1, 2147483647) == 0
    assert s.rangeBitwiseAnd(6, 6) == 6
    assert s.rangeBitwiseAnd(12, 15) == 12
    assert s.rangeBitwiseAnd(7, 8) == 0
    assert s.rangeBitwiseAnd(8, 15) == 8
    assert s.rangeBitwiseAnd(2147483646, 2147483647) == 2147483646
    print("All tests passed!")
```
