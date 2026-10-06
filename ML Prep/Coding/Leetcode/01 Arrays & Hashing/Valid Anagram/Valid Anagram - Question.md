---
topic: "Arrays & Hashing"
difficulty: Easy
leetcode: https://leetcode.com/problems/valid-anagram/
neetcode: https://neetcode.io/problems/is-anagram
---
# Valid Anagram

**Topic:** [[01 Arrays & Hashing|Arrays & Hashing]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/valid-anagram/) · [NeetCode](https://neetcode.io/problems/is-anagram)

**Solve it in:** [[Valid Anagram]] · **Answer:** [[Valid Anagram - Solution]]

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, otherwise return `false`. Two strings are anagrams when one can be produced by rearranging the characters of the other, using every character exactly as many times as it appears (so both strings must have identical character counts).

## Examples

**Example 1**
```text
Input: s = "listen", t = "silent"
Output: true
```

**Example 2**
```text
Input: s = "apple", t = "paple"
Output: true
```

**Example 3**
```text
Input: s = "car", t = "cat"
Output: false
```

## Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` contain only lowercase English letters.
- Follow-up: how would you adapt the solution if inputs could contain arbitrary Unicode characters?

## Starter Code & Test Cases

```python
class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		from collections import Counter
		return Counter(s) == Counter(t)


if __name__ == "__main__":
	sol = Solution()
	assert sol.isAnagram("listen", "silent") is True
	assert sol.isAnagram("apple", "paple") is True
	assert sol.isAnagram("car", "cat") is False
	assert sol.isAnagram("a", "a") is True
	assert sol.isAnagram("a", "ab") is False
	assert sol.isAnagram("aab", "abb") is False
	assert sol.isAnagram("abc" * 10000, "cba" * 10000) is True
	print("All tests passed!")
```
