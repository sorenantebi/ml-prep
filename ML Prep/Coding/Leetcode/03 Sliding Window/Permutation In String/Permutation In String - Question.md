---
topic: "Sliding Window"
difficulty: Medium
leetcode: https://leetcode.com/problems/permutation-in-string/
neetcode: https://neetcode.io/problems/permutation-string
---
# Permutation In String

**Topic:** [[03 Sliding Window|Sliding Window]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/permutation-in-string/) · [NeetCode](https://neetcode.io/problems/permutation-string)

**Solve it in:** [[Permutation In String]] · **Answer:** [[Permutation In String - Solution]]

## Problem

Given two strings `s1` and `s2`, return `true` if `s2` contains some permutation of `s1` as a contiguous substring, i.e. some window of `s2` with length `len(s1)` uses exactly the same characters with the same counts as `s1`. Otherwise return `false`.

## Examples

**Example 1**
```text
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains "ba"
```

**Example 2**
```text
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

## Constraints

- `1 <= s1.length, s2.length <= 10^4`
- Both strings consist of lowercase English letters

## Starter Code & Test Cases

```python
class Solution:
	def checkInclusion(self, s1: str, s2: str) -> bool:
		pass  # your code here


if __name__ == "__main__":
	sol = Solution()
	assert sol.checkInclusion("ab", "eidbaooo") is True
	assert sol.checkInclusion("ab", "eidboaoo") is False
	assert sol.checkInclusion("abc", "ab") is False
	assert sol.checkInclusion("a", "a") is True
	assert sol.checkInclusion("adc", "dcda") is True
	assert sol.checkInclusion("hello", "ooolleoooleh") is False
	assert sol.checkInclusion("aab", "xxbaa") is True
	assert sol.checkInclusion("abc", "cbaxyz") is True
	print("All tests passed!")
```
