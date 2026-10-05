---
topic: "Math & Geometry"
difficulty: Easy
leetcode: https://leetcode.com/problems/roman-to-integer/
neetcode: https://neetcode.io/problems/roman-to-integer
---
# Roman to Integer

**Topic:** [[17 Math & Geometry|Math & Geometry]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/roman-to-integer/) · [NeetCode](https://neetcode.io/problems/roman-to-integer)

**Solve it in:** [[Roman to Integer]] · **Answer:** [[Roman to Integer - Solution]]

## Problem

Roman numerals use seven symbols: `I = 1`, `V = 5`, `X = 10`, `L = 50`, `C = 100`, `D = 500`, `M = 1000`. Symbols are usually written from largest to smallest, left to right, and their values are added. There are six subtractive exceptions, where a smaller symbol placed before a larger one is subtracted: `IV = 4`, `IX = 9`, `XL = 40`, `XC = 90`, `CD = 400`, `CM = 900`.

Given a valid Roman numeral string `s`, return the integer it represents.

## Examples

**Example 1**
```text
Input: s = "III"
Output: 3
```

**Example 2**
```text
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V = 5, III = 3
```

**Example 3**
```text
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90, IV = 4
```

## Constraints

- `1 <= s.length <= 15`
- `s` contains only the characters `I, V, X, L, C, D, M`.
- `s` is guaranteed to be a valid Roman numeral in the range `[1, 3999]`.

## Starter Code & Test Cases

```python
class Solution:
	def romanToInt(self, s: str) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.romanToInt("III") == 3
	assert s.romanToInt("LVIII") == 58
	assert s.romanToInt("MCMXCIV") == 1994
	assert s.romanToInt("I") == 1
	assert s.romanToInt("IV") == 4
	assert s.romanToInt("IX") == 9
	assert s.romanToInt("XL") == 40
	assert s.romanToInt("CDXLIV") == 444
	assert s.romanToInt("MMMCMXCIX") == 3999
	print("All tests passed!")
```
