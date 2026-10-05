---
topic: "1-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/perfect-squares/
neetcode: https://neetcode.io/problems/perfect-squares
---
# Perfect Squares

**Topic:** [[13 1-D Dynamic Programming|1-D Dynamic Programming]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/perfect-squares/) · [NeetCode](https://neetcode.io/problems/perfect-squares)

**Solve it in:** [[Perfect Squares]] · **Answer:** [[Perfect Squares - Solution]]

## Problem

Given a positive integer `n`, return the minimum number of perfect squares (`1, 4, 9, 16, ...`) that sum to exactly `n`. Squares may be reused.

## Examples

**Example 1**
```text
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
```

**Example 2**
```text
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
```

## Constraints

- `1 <= n <= 10^4`

## Starter Code & Test Cases

```python
class Solution:
	def numSquares(self, n: int) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.numSquares(12) == 3
	assert s.numSquares(13) == 2
	assert s.numSquares(1) == 1
	assert s.numSquares(4) == 1
	assert s.numSquares(7) == 4
	assert s.numSquares(43) == 3
	assert s.numSquares(10000) == 1
	print("All tests passed!")
```
