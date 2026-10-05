---
topic: "Stack"
difficulty: Medium
leetcode: https://leetcode.com/problems/decode-string/
neetcode: https://neetcode.io/problems/decode-string
---
# Decode String

**Topic:** [[04 Stack|Stack]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/decode-string/) · [NeetCode](https://neetcode.io/problems/decode-string)

**Solve it in:** [[Decode String]] · **Answer:** [[Decode String - Solution]]

## Problem

Given an encoded string `s`, return its decoded form. The encoding rule is `k[encoded_string]`: the `encoded_string` inside the brackets is repeated exactly `k` times, where `k` is a positive integer. Encodings may be nested.

You can assume the input is always valid: brackets are well-formed, there are no extra spaces, digits appear only as repeat counts (the original data contains no digits — e.g. there is no `3a` or `2[4]`), and the decoded output length never exceeds `10^5`.

## Examples

**Example 1**
```text
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
```

**Example 2**
```text
Input: s = "3[a2[c]]"
Output: "accaccacc"
```

**Example 3**
```text
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

## Constraints

- `1 <= s.length <= 30`
- `s` consists of lowercase English letters, digits and `'['`, `']'`
- `s` is a valid encoding; all integers are in `[1, 300]`

## Starter Code & Test Cases

```python
class Solution:
	def decodeString(self, s: str) -> str:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.decodeString("3[a]2[bc]") == "aaabcbc"
	assert s.decodeString("3[a2[c]]") == "accaccacc"
	assert s.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
	assert s.decodeString("abc") == "abc"
	assert s.decodeString("10[a]") == "a" * 10           # multi-digit count
	assert s.decodeString("2[a2[b3[c]]]") == "abcccbccc" * 2
	assert s.decodeString("x1[y]z") == "xyz"
	assert s.decodeString("100[ab]") == "ab" * 100
	print("All tests passed!")
```
