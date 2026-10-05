---
topic: "Two Pointers"
difficulty: Easy
leetcode: https://leetcode.com/problems/valid-palindrome-ii/
neetcode: https://neetcode.io/problems/valid-palindrome-ii
---
# Valid Palindrome II

**Topic:** [[02 Two Pointers|Two Pointers]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/valid-palindrome-ii/) · [NeetCode](https://neetcode.io/problems/valid-palindrome-ii)

**Solve it in:** [[Valid Palindrome II]] · **Answer:** [[Valid Palindrome II - Solution]]

## Problem

Given a string `s` of lowercase letters, decide whether it can become a palindrome after deleting **at most one** character. Return `true` if it can (including when it already is a palindrome), otherwise `false`.

## Examples

**Example 1**
```text
Input: s = "aba"
Output: true
```

**Example 2**
```text
Input: s = "abca"
Output: true
Explanation: delete 'b' or 'c'
```

**Example 3**
```text
Input: s = "abc"
Output: false
```

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters

## Starter Code & Test Cases

```python
class Solution:
	def validPalindrome(self, s: str) -> bool:
		pass  # your code here


if __name__ == "__main__":
	sol = Solution()
	assert sol.validPalindrome("aba") is True
	assert sol.validPalindrome("abca") is True
	assert sol.validPalindrome("abc") is False
	assert sol.validPalindrome("a") is True
	assert sol.validPalindrome("ab") is True
	assert sol.validPalindrome("deeee") is True
	assert sol.validPalindrome("eeccccbebaeeabebccceea") is False
	assert sol.validPalindrome("abccdba") is True
	assert sol.validPalindrome("abcdeba") is False
	print("All tests passed!")
```
