---
topic: "2-D Dynamic Programming"
difficulty: Hard
leetcode: https://leetcode.com/problems/regular-expression-matching/
neetcode: https://neetcode.io/problems/regular-expression-matching
---
# Regular Expression Matching

**Topic:** [[14 2-D Dynamic Programming|2-D Dynamic Programming]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/regular-expression-matching/) · [NeetCode](https://neetcode.io/problems/regular-expression-matching)

**Solve it in:** [[Regular Expression Matching]] · **Answer:** [[Regular Expression Matching - Solution]]

## Problem

Implement regular-expression matching for a string `s` against a pattern `p` that supports two special characters:

- `.` matches any single character.
- `*` matches zero or more copies of the element **immediately before it**.

The match must cover the **entire** input string (not just a part of it). Return `true` if `s` matches `p`.

It is guaranteed that every `*` in `p` is preceded by a valid character (a letter or `.`).

## Examples

**Example 1**
```text
Input: s = "aa", p = "a"
Output: false
Explanation: "a" only matches a single 'a'.
```

**Example 2**
```text
Input: s = "aa", p = "a*"
Output: true
```

**Example 3**
```text
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means zero or more of any character.
```

## Constraints

- `1 <= s.length <= 20`
- `1 <= p.length <= 20`
- `s` contains only lowercase letters; `p` contains lowercase letters, `.`, and `*`.
- Each `*` is preceded by a valid character.

## Starter Code & Test Cases

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pass  # your code here


if __name__ == "__main__":
    sol = Solution()
    assert sol.isMatch("aa", "a") is False
    assert sol.isMatch("aa", "a*") is True
    assert sol.isMatch("ab", ".*") is True
    assert sol.isMatch("aab", "c*a*b") is True
    assert sol.isMatch("mississippi", "mis*is*p*.") is False
    assert sol.isMatch("a", "ab*") is True
    assert sol.isMatch("ab", ".*c") is False
    assert sol.isMatch("aaa", "a*a") is True
    assert sol.isMatch("abcd", "d*") is False
    print("All tests passed!")
```
