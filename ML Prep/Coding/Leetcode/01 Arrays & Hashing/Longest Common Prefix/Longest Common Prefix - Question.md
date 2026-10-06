---
topic: "Arrays & Hashing"
difficulty: Easy
leetcode: https://leetcode.com/problems/longest-common-prefix/
neetcode: https://neetcode.io/problems/longest-common-prefix
---
# Longest Common Prefix

**Topic:** [[01 Arrays & Hashing|Arrays & Hashing]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/longest-common-prefix/) · [NeetCode](https://neetcode.io/problems/longest-common-prefix)

**Solve it in:** [[Longest Common Prefix]] · **Answer:** [[Longest Common Prefix - Solution]]

## Problem

Given an array of strings `strs`, return the longest string that is a prefix of every string in the array. If the strings share no common starting characters, return the empty string `""`.

## Examples

**Example 1**
```text
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

**Example 2**
```text
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: the first characters already differ.
```

**Example 3**
```text
Input: strs = ["interview","internet","interval"]
Output: "inter"
```

## Constraints

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of lowercase English letters only.

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		ref = strs[0]
		for i in range(len(ref)):
			for word in strs:
				if i >= len(word) or word[i] != ref[i]:
					return ref[:i]
		return ref


if __name__ == "__main__":
	s = Solution()
	assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
	assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""
	assert s.longestCommonPrefix(["interview", "internet", "interval"]) == "inter"
	assert s.longestCommonPrefix(["alone"]) == "alone"
	assert s.longestCommonPrefix(["", "abc"]) == ""
	assert s.longestCommonPrefix(["same", "same", "same"]) == "same"
	assert s.longestCommonPrefix(["ab", "a"]) == "a"
	assert s.longestCommonPrefix(["abc", "abcd", "ab"]) == "ab"
	print("All tests passed!")
```
