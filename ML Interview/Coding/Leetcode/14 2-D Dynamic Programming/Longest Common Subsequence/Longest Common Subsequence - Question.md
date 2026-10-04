---
topic: "2-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/longest-common-subsequence/
neetcode: https://neetcode.io/problems/longest-common-subsequence
---
# Longest Common Subsequence

**Topic:** [[14 2-D Dynamic Programming|2-D Dynamic Programming]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/longest-common-subsequence/) · [NeetCode](https://neetcode.io/problems/longest-common-subsequence)

**Solve it in:** [[Longest Common Subsequence]] · **Answer:** [[Longest Common Subsequence - Solution]]

## Problem

Given two strings `text1` and `text2`, return the length of their longest common subsequence, or `0` if they share no characters.

A subsequence is obtained from a string by deleting zero or more characters without changing the order of the remaining characters (e.g. `"ace"` is a subsequence of `"abcde"`). A common subsequence is one that is a subsequence of both strings.

## Examples

**Example 1**
```text
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: "ace" is the longest common subsequence.
```

**Example 2**
```text
Input: text1 = "abc", text2 = "abc"
Output: 3
```

**Example 3**
```text
Input: text1 = "abc", text2 = "def"
Output: 0
```

## Constraints

- `1 <= text1.length, text2.length <= 1000`
- Both strings consist only of lowercase English letters.

## Starter Code & Test Cases

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.longestCommonSubsequence("abcde", "ace") == 3
    assert s.longestCommonSubsequence("abc", "abc") == 3
    assert s.longestCommonSubsequence("abc", "def") == 0
    assert s.longestCommonSubsequence("a", "a") == 1
    assert s.longestCommonSubsequence("a", "b") == 0
    assert s.longestCommonSubsequence("bsbininm", "jmjkbkjkv") == 1
    assert s.longestCommonSubsequence("abcba", "abcbcba") == 5
    assert s.longestCommonSubsequence("ezupkr", "ubmrapg") == 2
    print("All tests passed!")
```
