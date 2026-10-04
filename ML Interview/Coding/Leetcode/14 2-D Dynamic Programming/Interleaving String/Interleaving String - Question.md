---
topic: "2-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/interleaving-string/
neetcode: https://neetcode.io/problems/interleaving-string
---
# Interleaving String

**Topic:** [[14 2-D Dynamic Programming|2-D Dynamic Programming]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/interleaving-string/) · [NeetCode](https://neetcode.io/problems/interleaving-string)

**Solve it in:** [[Interleaving String]] · **Answer:** [[Interleaving String - Solution]]

## Problem

Given strings `s1`, `s2`, and `s3`, determine whether `s3` can be formed by **interleaving** `s1` and `s2`: that is, by merging all characters of `s1` and all characters of `s2` into one string while preserving the relative order of characters from each source string. Return `true` if possible, otherwise `false`.

## Examples

**Example 1**
```text
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
```

**Example 2**
```text
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
```

**Example 3**
```text
Input: s1 = "", s2 = "", s3 = ""
Output: true
```

## Constraints

- `0 <= s1.length, s2.length <= 100`
- `0 <= s3.length <= 200`
- All strings consist of lowercase English letters.

## Starter Code & Test Cases

```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.isInterleave("aabcc", "dbbca", "aadbbcbcac") is True
    assert s.isInterleave("aabcc", "dbbca", "aadbbbaccc") is False
    assert s.isInterleave("", "", "") is True
    assert s.isInterleave("", "abc", "abc") is True
    assert s.isInterleave("abc", "", "abd") is False
    assert s.isInterleave("a", "b", "ab") is True
    assert s.isInterleave("a", "b", "abc") is False  # length mismatch
    assert s.isInterleave("ab", "ab", "abab") is True
    assert s.isInterleave("aa", "ab", "abaa") is True
    print("All tests passed!")
```
