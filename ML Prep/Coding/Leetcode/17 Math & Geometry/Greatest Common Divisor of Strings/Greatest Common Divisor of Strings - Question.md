---
topic: "Math & Geometry"
difficulty: Easy
leetcode: https://leetcode.com/problems/greatest-common-divisor-of-strings/
neetcode: https://neetcode.io/problems/greatest-common-divisor-of-strings
---
# Greatest Common Divisor of Strings

**Topic:** [[17 Math & Geometry|Math & Geometry]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/greatest-common-divisor-of-strings/) · [NeetCode](https://neetcode.io/problems/greatest-common-divisor-of-strings)

**Solve it in:** [[Greatest Common Divisor of Strings]] · **Answer:** [[Greatest Common Divisor of Strings - Solution]]

## Problem

A string `t` **divides** a string `s` if `s` is `t` repeated one or more times (i.e. `s = t + t + ... + t`).

Given two strings `str1` and `str2`, return the **longest** string `x` that divides both of them. If no such string exists, return the empty string `""`.

## Examples

**Example 1**
```text
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
```

**Example 2**
```text
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
```

**Example 3**
```text
Input: str1 = "LEET", str2 = "CODE"
Output: ""
```

## Constraints

- `1 <= str1.length, str2.length <= 1000`
- `str1` and `str2` consist of uppercase English letters.

## Starter Code & Test Cases

```python
class Solution:
	def gcdOfStrings(self, str1: str, str2: str) -> str:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.gcdOfStrings("ABCABC", "ABC") == "ABC"
	assert s.gcdOfStrings("ABABAB", "ABAB") == "AB"
	assert s.gcdOfStrings("LEET", "CODE") == ""
	assert s.gcdOfStrings("A", "A") == "A"
	assert s.gcdOfStrings("AAAAAA", "AAAA") == "AA"
	assert s.gcdOfStrings("ABAB", "BABA") == ""
	assert s.gcdOfStrings("ABCDEF", "ABC") == ""
	assert s.gcdOfStrings("XYXYXYXY", "XYXYXY") == "XY"
	print("All tests passed!")
```
