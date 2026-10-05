---
topic: "Arrays & Hashing"
difficulty: Medium
leetcode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
neetcode: https://neetcode.io/problems/best-time-to-buy-and-sell-stock-ii
---
# Best Time to Buy And Sell Stock II

**Topic:** [[01 Arrays & Hashing|Arrays & Hashing]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) · [NeetCode](https://neetcode.io/problems/best-time-to-buy-and-sell-stock-ii)
Also --> [[13 1-D Dynamic Programming]]
**Solve it in:** [[Best Time to Buy And Sell Stock II]] · **Answer:** [[Best Time to Buy And Sell Stock II - Solution]]

## Problem

You are given an array `prices` where `prices[i]` is the price of a stock on day `i`. On each day you may buy and/or sell the stock, but you can hold at most one share at any time (you may sell and buy again on the same day). You may complete as many transactions as you like. Return the maximum total profit you can achieve; return `0` if no profit is possible.

## Examples

**Example 1**
```text
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: buy at 1, sell at 5 (+4); buy at 3, sell at 6 (+3).
```

**Example 2**
```text
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: buy on day 0 and sell on day 4 (or take every daily gain).
```

**Example 3**
```text
Input: prices = [7,6,4,3,1]
Output: 0
```

## Constraints

- `1 <= prices.length <= 3 * 10^4`
- `0 <= prices[i] <= 10^4`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		for price in prices:
			print(price)
		return 0


if __name__ == "__main__":
	s = Solution()
	assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 7
	assert s.maxProfit([1, 2, 3, 4, 5]) == 4
	assert s.maxProfit([7, 6, 4, 3, 1]) == 0
	assert s.maxProfit([5]) == 0
	assert s.maxProfit([2, 2, 2]) == 0
	assert s.maxProfit([1, 5, 1, 5, 1, 5]) == 12
	assert s.maxProfit([3, 0, 10]) == 10
	assert s.maxProfit([0, 10000] * 15000) == 10000 * 15000
	print("All tests passed!")
```
