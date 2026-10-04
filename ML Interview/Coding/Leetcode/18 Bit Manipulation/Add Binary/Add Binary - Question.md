---
topic: "Bit Manipulation"
difficulty: Easy
leetcode: https://leetcode.com/problems/add-binary/
neetcode: https://neetcode.io/problems/add-binary
---
# Add Binary

**Topic:** [[18 Bit Manipulation|Bit Manipulation]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/add-binary/) · [NeetCode](https://neetcode.io/problems/add-binary)

**Solve it in:** [[Add Binary]] · **Answer:** [[Add Binary - Solution]]

## Problem

You are given two binary strings `a` and `b`, made only of the characters `'0'` and `'1'`. Return their sum as a binary string.

The inputs have no leading zeros, except for the string `"0"` itself.

## Examples

**Example 1**
```text
Input: a = "11", b = "1"
Output: "100"
```

**Example 2**
```text
Input: a = "1010", b = "1011"
Output: "10101"
```

## Constraints

- `1 <= a.length, b.length <= 10^4`
- `a` and `b` contain only `'0'` and `'1'`.
- Neither string has leading zeros, except `"0"` itself.

## Starter Code & Test Cases

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.addBinary("11", "1") == "100"
    assert s.addBinary("1010", "1011") == "10101"
    assert s.addBinary("0", "0") == "0"
    assert s.addBinary("0", "1") == "1"
    assert s.addBinary("1", "111") == "1000"
    assert s.addBinary("1111", "1111") == "11110"
    assert s.addBinary("100", "110010") == "110110"
    a, b = "1" * 500, "1" + "0" * 300
    assert s.addBinary(a, b) == bin(int(a, 2) + int(b, 2))[2:]
    print("All tests passed!")
```
