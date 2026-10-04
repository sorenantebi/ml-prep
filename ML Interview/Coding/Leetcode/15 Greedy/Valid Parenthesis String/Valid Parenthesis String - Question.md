---
topic: "Greedy"
difficulty: Medium
leetcode: https://leetcode.com/problems/valid-parenthesis-string/
neetcode: https://neetcode.io/problems/valid-parenthesis-string
---
# Valid Parenthesis String

**Topic:** [[15 Greedy|Greedy]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/valid-parenthesis-string/) · [NeetCode](https://neetcode.io/problems/valid-parenthesis-string)

**Solve it in:** [[Valid Parenthesis String]] · **Answer:** [[Valid Parenthesis String - Solution]]

## Problem

Given a string `s` containing only `'('`, `')'`, and `'*'`, return `true` if `s` can be a valid parenthesis string. Each `'*'` may independently be treated as `'('`, as `')'`, or as an empty string. A valid string has every `'('` matched by a later `')'` and every `')'` matched by an earlier `'('`. The empty string is valid.

## Examples

**Example 1**
```text
Input: s = "()"
Output: true
```

**Example 2**
```text
Input: s = "(*)"
Output: true
```

**Example 3**
```text
Input: s = "(*))"
Output: true
Explanation: Treat '*' as '('.
```

## Constraints

- `1 <= s.length <= 100`
- `s[i]` is `'('`, `')'`, or `'*'`

## Starter Code & Test Cases

```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        pass  # your code here


if __name__ == "__main__":
    sol = Solution()
    assert sol.checkValidString("()") is True
    assert sol.checkValidString("(*)") is True
    assert sol.checkValidString("(*))") is True
    assert sol.checkValidString("*") is True
    assert sol.checkValidString(")") is False
    assert sol.checkValidString("(((**") is False
    assert sol.checkValidString("*(") is False  # '*' cannot close a later '('
    assert sol.checkValidString("(*()") is True
    assert sol.checkValidString("((*)(*))((*") is False
    print("All tests passed!")
```
