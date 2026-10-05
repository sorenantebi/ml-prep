---
topic: "Bit Manipulation"
difficulty: Medium
leetcode: https://leetcode.com/problems/sum-of-two-integers/
neetcode: https://neetcode.io/problems/sum-of-two-integers
---
# Sum of Two Integers

**Topic:** [[18 Bit Manipulation|Bit Manipulation]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/sum-of-two-integers/) · [NeetCode](https://neetcode.io/problems/sum-of-two-integers)

**Solve it in:** [[Sum of Two Integers]] · **Answer:** [[Sum of Two Integers - Solution]]

## Problem

Given two integers `a` and `b`, return their sum **without using the `+` or `-` operators**.

## Examples

**Example 1**
```text
Input: a = 1, b = 2
Output: 3
```

**Example 2**
```text
Input: a = 2, b = 3
Output: 5
```

**Example 3**
```text
Input: a = -5, b = -7
Output: -12
```

## Constraints

- `-1000 <= a, b <= 1000`

## Starter Code & Test Cases

```python
class Solution:
	def getSum(self, a: int, b: int) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.getSum(1, 2) == 3
	assert s.getSum(2, 3) == 5
	assert s.getSum(-5, -7) == -12
	assert s.getSum(-1, 1) == 0
	assert s.getSum(0, 0) == 0
	assert s.getSum(1000, -1000) == 0
	assert s.getSum(-1000, 999) == -1
	assert s.getSum(1000, 1000) == 2000
	assert s.getSum(-1000, -1000) == -2000
	for x in range(-20, 21, 7):
		for y in range(-20, 21, 3):
			assert s.getSum(x, y) == x + y
	print("All tests passed!")
```
