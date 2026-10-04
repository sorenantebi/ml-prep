---
topic: "Math & Geometry"
difficulty: Medium
leetcode: https://leetcode.com/problems/multiply-strings/
neetcode: https://neetcode.io/problems/multiply-strings
---
# Multiply Strings

**Topic:** [[17 Math & Geometry|Math & Geometry]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/multiply-strings/) · [NeetCode](https://neetcode.io/problems/multiply-strings)

**Solve it in:** [[Multiply Strings]] · **Answer:** [[Multiply Strings - Solution]]

## Problem

You are given two non-negative integers `num1` and `num2` as decimal strings. Return their product, also as a string.

You may not use a built-in big-integer library, and you may not convert the inputs directly to integers. The digit arithmetic has to be done by hand.

## Examples

**Example 1**
```text
Input: num1 = "2", num2 = "3"
Output: "6"
```

**Example 2**
```text
Input: num1 = "123", num2 = "456"
Output: "56088"
```

**Example 3**
```text
Input: num1 = "0", num2 = "52"
Output: "0"
```

## Constraints

- `1 <= num1.length, num2.length <= 200`
- `num1` and `num2` contain only digits.
- Neither input has leading zeros, except the number `0` itself.

## Starter Code & Test Cases

```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.multiply("2", "3") == "6"
    assert s.multiply("123", "456") == "56088"
    assert s.multiply("0", "52") == "0"
    assert s.multiply("52", "0") == "0"
    assert s.multiply("9", "9") == "81"
    assert s.multiply("999", "999") == "998001"
    assert s.multiply("1", "123456789") == "123456789"
    assert s.multiply("100", "1000") == "100000"
    a, b = "98765432109876543210", "12345678901234567890"
    assert s.multiply(a, b) == str(int(a) * int(b))  # int() used only to check the answer
    print("All tests passed!")
```
