---
topic: "2-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/coin-change-ii/
neetcode: https://neetcode.io/problems/coin-change-ii
---
# Coin Change II

**Topic:** [[14 2-D Dynamic Programming|2-D Dynamic Programming]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/coin-change-ii/) · [NeetCode](https://neetcode.io/problems/coin-change-ii)

**Solve it in:** [[Coin Change II]] · **Answer:** [[Coin Change II - Solution]]

## Problem

You are given an integer `amount` and an array `coins` of distinct coin denominations. Each denomination may be used an unlimited number of times. Return the number of **combinations** of coins that add up exactly to `amount` (order does not matter, so `1+2` and `2+1` count once). If the amount cannot be formed, return `0`. An `amount` of `0` has exactly one combination (use no coins).

The answer fits in a 32-bit signed integer.

## Examples

**Example 1**
```text
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: 5 = 5 = 2+2+1 = 2+1+1+1 = 1+1+1+1+1
```

**Example 2**
```text
Input: amount = 3, coins = [2]
Output: 0
```

**Example 3**
```text
Input: amount = 10, coins = [10]
Output: 1
```

## Constraints

- `1 <= coins.length <= 300`
- `1 <= coins[i] <= 5000`, all values distinct
- `0 <= amount <= 5000`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def change(self, amount: int, coins: List[int]) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.change(5, [1, 2, 5]) == 4
	assert s.change(3, [2]) == 0
	assert s.change(10, [10]) == 1
	assert s.change(0, [7]) == 1
	assert s.change(4, [1, 2, 3]) == 4
	assert s.change(100, [1, 2]) == 51
	assert s.change(7, [2, 4]) == 0
	assert s.change(12, [3, 5, 7]) == 2  # 3+3+3+3, 5+7
	print("All tests passed!")
```
