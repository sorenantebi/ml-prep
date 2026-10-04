---
topic: "Stack"
difficulty: Easy
leetcode: https://leetcode.com/problems/valid-parentheses/
neetcode: https://neetcode.io/problems/validate-parentheses
---
# Valid Parentheses

**Topic:** [[04 Stack|Stack]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/valid-parentheses/) · [NeetCode](https://neetcode.io/problems/validate-parentheses)

**Solve it in:** [[Valid Parentheses]] · **Answer:** [[Valid Parentheses - Solution]]

## Problem

Given a string `s` made up only of the bracket characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, decide whether it is valid. A string is valid when:

- every opening bracket is closed by a closing bracket of the same type,
- brackets are closed in the correct order (the most recently opened bracket must be closed first), and
- every closing bracket has a matching opening bracket before it.

Return `true` if the string is valid, otherwise `false`.

## Examples

**Example 1**
```text
Input: s = "()[]{}"
Output: true
```

**Example 2**
```text
Input: s = "([)]"
Output: false
Explanation: '[' is still open when ')' arrives
```

**Example 3**
```text
Input: s = "{[]}"
Output: true
```

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists only of `'()[]{}'`

## Starter Code & Test Cases

```python
class Solution:
    def isValid(self, s: str) -> bool:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.isValid("()") is True
    assert s.isValid("()[]{}") is True
    assert s.isValid("(]") is False
    assert s.isValid("([)]") is False
    assert s.isValid("{[]}") is True
    assert s.isValid("(") is False
    assert s.isValid("]") is False
    assert s.isValid("((()))[{}]") is True
    print("All tests passed!")
```
