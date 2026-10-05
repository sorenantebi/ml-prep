---
topic: "Bit Manipulation"
difficulty: Medium
leetcode: https://leetcode.com/problems/reverse-integer/
neetcode: https://neetcode.io/problems/reverse-integer
---
# Reverse Integer

**Topic:** [[18 Bit Manipulation|Bit Manipulation]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/reverse-integer/) · [NeetCode](https://neetcode.io/problems/reverse-integer)

**Solve it in:** [[Reverse Integer]] · **Answer:** [[Reverse Integer - Solution]]

## Problem

Given a signed 32-bit integer `x`, return `x` with its decimal digits reversed, keeping its sign. If the reversed value falls outside the signed 32-bit range `[-2^31, 2^31 - 1]`, return `0`.

Assume the environment cannot store 64-bit integers, so the overflow must be detected without computing the full out-of-range value.

## Examples

**Example 1**
```text
Input: x = 123
Output: 321
```

**Example 2**
```text
Input: x = -123
Output: -321
```

**Example 3**
```text
Input: x = 120
Output: 21
```

## Constraints

- `-2^31 <= x <= 2^31 - 1`

## Starter Code & Test Cases

```python
class Solution:
	def reverse(self, x: int) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.reverse(123) == 321
	assert s.reverse(-123) == -321
	assert s.reverse(120) == 21
	assert s.reverse(0) == 0
	assert s.reverse(-10) == -1
	assert s.reverse(1534236469) == 0      # 9646324351 overflows
	assert s.reverse(-2147483648) == 0     # -8463847412 overflows
	assert s.reverse(2147483647) == 0      # 7463847412 overflows
	assert s.reverse(1463847412) == 2147483641
	assert s.reverse(-1463847412) == -2147483641
	print("All tests passed!")
```
