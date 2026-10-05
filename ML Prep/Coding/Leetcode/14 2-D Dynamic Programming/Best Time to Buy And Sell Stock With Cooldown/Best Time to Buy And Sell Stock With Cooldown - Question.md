---
topic: "2-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
neetcode: https://neetcode.io/problems/buy-and-sell-crypto-with-cooldown
---
# Best Time to Buy And Sell Stock With Cooldown

**Topic:** [[14 2-D Dynamic Programming|2-D Dynamic Programming]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) · [NeetCode](https://neetcode.io/problems/buy-and-sell-crypto-with-cooldown)

**Solve it in:** [[Best Time to Buy And Sell Stock With Cooldown]] · **Answer:** [[Best Time to Buy And Sell Stock With Cooldown - Solution]]

## Problem

You are given an array `prices` where `prices[i]` is the price of a stock on day `i`. Find the maximum profit you can achieve. You may complete as many transactions as you like (buy one share and later sell it, repeatedly), subject to:

- You can hold at most one share at a time (you must sell before buying again).
- After selling, you must wait one day (**cooldown**) before buying again — you cannot buy on the day right after a sale.

Return the maximum profit (`0` if no profitable trade exists).

## Examples

**Example 1**
```text
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: buy, sell, cooldown, buy, sell -> (2-1) + (2-0) = 3
```

**Example 2**
```text
Input: prices = [1]
Output: 0
```

## Constraints

- `1 <= prices.length <= 5000`
- `0 <= prices[i] <= 1000`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.maxProfit([1, 2, 3, 0, 2]) == 3
	assert s.maxProfit([1]) == 0
	assert s.maxProfit([5, 4, 3, 2, 1]) == 0
	assert s.maxProfit([1, 2, 3, 4, 5]) == 4
	assert s.maxProfit([1, 2]) == 1
	assert s.maxProfit([2, 1, 4]) == 3
	assert s.maxProfit([1, 4, 2, 7]) == 6  # one long trade beats 3 + 5 with no cooldown room
	assert s.maxProfit([6, 1, 6, 4, 3, 0, 2]) == 7
	print("All tests passed!")
```
