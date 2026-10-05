---
topic: "1-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/palindromic-substrings/
neetcode: https://neetcode.io/problems/palindromic-substrings
---
# Palindromic Substrings

**Topic:** [[13 1-D Dynamic Programming|1-D Dynamic Programming]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/palindromic-substrings/) · [NeetCode](https://neetcode.io/problems/palindromic-substrings)

**Solve it in:** [[Palindromic Substrings]] · **Answer:** [[Palindromic Substrings - Solution]]

## Problem

Given a string `s`, return how many of its substrings are palindromes. Substrings at different positions count separately even if their contents are equal.

## Examples

**Example 1**
```text
Input: s = "abc"
Output: 3
Explanation: "a", "b", "c".
```

**Example 2**
```text
Input: s = "aaa"
Output: 6
Explanation: three "a", two "aa", one "aaa".
```

## Constraints

- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

## Starter Code & Test Cases

```python
class Solution:
	def countSubstrings(self, s: str) -> int:
		pass  # your code here


if __name__ == "__main__":
	sol = Solution()
	assert sol.countSubstrings("abc") == 3
	assert sol.countSubstrings("aaa") == 6
	assert sol.countSubstrings("a") == 1
	assert sol.countSubstrings("abba") == 6
	assert sol.countSubstrings("aba") == 4
	assert sol.countSubstrings("aaaa") == 10
	print("All tests passed!")
```
