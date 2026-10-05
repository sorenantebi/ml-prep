---
topic: "Two Pointers"
difficulty: Easy
leetcode: https://leetcode.com/problems/valid-palindrome/
neetcode: https://neetcode.io/problems/is-palindrome
---
# Valid Palindrome

**Topic:** [[02 Two Pointers|Two Pointers]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/valid-palindrome/) · [NeetCode](https://neetcode.io/problems/is-palindrome)

**Solve it in:** [[Valid Palindrome]] · **Answer:** [[Valid Palindrome - Solution]]

## Problem

A phrase counts as a palindrome if, after lowercasing all letters and discarding every character that is not a letter or digit, it reads the same forwards and backwards. Given a string `s`, return `true` if it is a palindrome under this definition and `false` otherwise. An empty string (after filtering) is a palindrome.

## Examples

**Example 1**
```text
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: filtered string is "amanaplanacanalpanama"
```

**Example 2**
```text
Input: s = "race a car"
Output: false
```

**Example 3**
```text
Input: s = " "
Output: true
Explanation: nothing remains after filtering, and "" is a palindrome
```

## Constraints

- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters

## Starter Code & Test Cases

```python
class Solution:
	def isPalindrome(self, s: str) -> bool:
		pass  # your code here


if __name__ == "__main__":
	sol = Solution()
	assert sol.isPalindrome("A man, a plan, a canal: Panama") is True
	assert sol.isPalindrome("race a car") is False
	assert sol.isPalindrome(" ") is True
	assert sol.isPalindrome("0P") is False
	assert sol.isPalindrome("a.") is True
	assert sol.isPalindrome("No 'x' in Nixon") is True
	assert sol.isPalindrome("12321") is True
	assert sol.isPalindrome("ab_a") is True
	print("All tests passed!")
```
