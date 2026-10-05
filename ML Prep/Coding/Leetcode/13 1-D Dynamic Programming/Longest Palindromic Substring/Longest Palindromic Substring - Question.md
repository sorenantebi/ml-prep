---
topic: "1-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/longest-palindromic-substring/
neetcode: https://neetcode.io/problems/longest-palindromic-substring
---
# Longest Palindromic Substring

**Topic:** [[13 1-D Dynamic Programming|1-D Dynamic Programming]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/longest-palindromic-substring/) · [NeetCode](https://neetcode.io/problems/longest-palindromic-substring)

**Solve it in:** [[Longest Palindromic Substring]] · **Answer:** [[Longest Palindromic Substring - Solution]]

## Problem

Given a string `s`, return the longest contiguous substring of `s` that reads the same forwards and backwards. If several substrings share the maximum length, any one of them is accepted.

## Examples

**Example 1**
```text
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also accepted.
```

**Example 2**
```text
Input: s = "cbbd"
Output: "bb"
```

## Constraints

- `1 <= s.length <= 1000`
- `s` consists only of digits and English letters.

## Starter Code & Test Cases

```python
class Solution:
	def longestPalindrome(self, s: str) -> str:
		pass  # your code here


if __name__ == "__main__":
	sol = Solution()
	assert sol.longestPalindrome("babad") in {"bab", "aba"}
	assert sol.longestPalindrome("cbbd") == "bb"
	assert sol.longestPalindrome("a") == "a"
	assert sol.longestPalindrome("ac") in {"a", "c"}
	assert sol.longestPalindrome("racecar") == "racecar"
	assert sol.longestPalindrome("forgeeksskeegfor") == "geeksskeeg"
	assert sol.longestPalindrome("aaaa") == "aaaa"
	print("All tests passed!")
```
