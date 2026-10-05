---
topic: "1-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/decode-ways/
neetcode: https://neetcode.io/problems/decode-ways
---
# Decode Ways

**Topic:** [[13 1-D Dynamic Programming|1-D Dynamic Programming]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/decode-ways/) · [NeetCode](https://neetcode.io/problems/decode-ways)

**Solve it in:** [[Decode Ways]] · **Answer:** [[Decode Ways - Solution]]

## Problem

Letters are encoded as numbers: `'A' -> "1"`, `'B' -> "2"`, ..., `'Z' -> "26"`. Given a string `s` of digits, return the number of ways to split it back into letters.

Each piece must be a valid code from `"1"` to `"26"`; a piece cannot have a leading zero (`"06"` is not valid, and a lone `"0"` decodes to nothing). If the string can't be decoded at all, return `0`. The answer fits in a 32-bit integer.

## Examples

**Example 1**
```text
Input: s = "12"
Output: 2
Explanation: "AB" (1 2) or "L" (12).
```

**Example 2**
```text
Input: s = "226"
Output: 3
Explanation: (2 26), (22 6), (2 2 6).
```

**Example 3**
```text
Input: s = "06"
Output: 0
```

## Constraints

- `1 <= s.length <= 100`
- `s` contains only digits and may contain leading zeros.

## Starter Code & Test Cases

```python
class Solution:
	def numDecodings(self, s: str) -> int:
		pass  # your code here


if __name__ == "__main__":
	sol = Solution()
	assert sol.numDecodings("12") == 2
	assert sol.numDecodings("226") == 3
	assert sol.numDecodings("06") == 0
	assert sol.numDecodings("0") == 0
	assert sol.numDecodings("10") == 1
	assert sol.numDecodings("11106") == 2
	assert sol.numDecodings("2101") == 1
	assert sol.numDecodings("27") == 1
	assert sol.numDecodings("100") == 0
	print("All tests passed!")
```
