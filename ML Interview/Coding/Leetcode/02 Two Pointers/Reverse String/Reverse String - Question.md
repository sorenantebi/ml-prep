---
topic: "Two Pointers"
difficulty: Easy
leetcode: https://leetcode.com/problems/reverse-string/
neetcode: https://neetcode.io/problems/reverse-string
---
# Reverse String

**Topic:** [[02 Two Pointers|Two Pointers]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/reverse-string/) · [NeetCode](https://neetcode.io/problems/reverse-string)

**Solve it in:** [[Reverse String]] · **Answer:** [[Reverse String - Solution]]

## Problem

You are given a string represented as a list of single characters `s`. Reverse the order of the characters **in place**, modifying the input list directly. You must use only `O(1)` extra memory. The function returns nothing.

## Examples

**Example 1**
```text
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

**Example 2**
```text
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

## Constraints

- `1 <= s.length <= 10^5`
- `s[i]` is a printable ASCII character

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        pass  # your code here


if __name__ == "__main__":
    sol = Solution()

    s = ["h", "e", "l", "l", "o"]
    sol.reverseString(s)
    assert s == ["o", "l", "l", "e", "h"]

    s = ["H", "a", "n", "n", "a", "h"]
    sol.reverseString(s)
    assert s == ["h", "a", "n", "n", "a", "H"]

    s = ["a"]
    sol.reverseString(s)
    assert s == ["a"]

    s = ["a", "b"]
    sol.reverseString(s)
    assert s == ["b", "a"]

    s = list("abcdefg")
    sol.reverseString(s)
    assert s == list("gfedcba")

    s = list("x" * 1000 + "y")
    sol.reverseString(s)
    assert s == list("y" + "x" * 1000)

    print("All tests passed!")
```
