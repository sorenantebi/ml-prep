---
topic: "Two Pointers"
difficulty: Easy
leetcode: https://leetcode.com/problems/merge-strings-alternately/
neetcode: https://neetcode.io/problems/merge-strings-alternately
---
# Merge Strings Alternately

**Topic:** [[02 Two Pointers|Two Pointers]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/merge-strings-alternately/) · [NeetCode](https://neetcode.io/problems/merge-strings-alternately)

**Solve it in:** [[Merge Strings Alternately]] · **Answer:** [[Merge Strings Alternately - Solution]]

## Problem

Given two strings `word1` and `word2`, build a new string by taking characters alternately, starting with `word1`: first char of `word1`, first char of `word2`, second char of `word1`, and so on. When one string runs out, append the remainder of the other string. Return the merged string.

## Examples

**Example 1**
```text
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
```

**Example 2**
```text
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
```

**Example 3**
```text
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
```

## Constraints

- `1 <= word1.length, word2.length <= 100`
- Both strings consist of lowercase English letters

## Starter Code & Test Cases

```python
class Solution:
	def mergeAlternately(self, word1: str, word2: str) -> str:
		pass  # your code here


if __name__ == "__main__":
	sol = Solution()
	assert sol.mergeAlternately("abc", "pqr") == "apbqcr"
	assert sol.mergeAlternately("ab", "pqrs") == "apbqrs"
	assert sol.mergeAlternately("abcd", "pq") == "apbqcd"
	assert sol.mergeAlternately("a", "b") == "ab"
	assert sol.mergeAlternately("a", "xyz") == "axyz"
	assert sol.mergeAlternately("xyz", "a") == "xayz"
	print("All tests passed!")
```
