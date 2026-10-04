---
topic: "Sliding Window"
difficulty: Easy
leetcode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
neetcode: https://neetcode.io/problems/buy-and-sell-crypto
---
# Best Time to Buy And Sell Stock

**Topic:** [[03 Sliding Window|Sliding Window]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) · [NeetCode](https://neetcode.io/problems/buy-and-sell-crypto)

**Solve it in:** [[Best Time to Buy And Sell Stock]] · **Answer:** [[Best Time to Buy And Sell Stock - Solution]]

## Problem

You are given an array `prices` where `prices[i]` is a stock's price on day `i`. You may buy one share on some day and sell it on a **later** day. Return the maximum profit achievable from one such transaction, or `0` if no profitable trade exists.

## Examples

**Example 1**
```text
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: buy at 1 (day 1), sell at 6 (day 4)
```

**Example 2**
```text
Input: prices = [7,6,4,3,1]
Output: 0
```

## Constraints

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pass  # your code here


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
    assert sol.maxProfit([5]) == 0
    assert sol.maxProfit([1, 2]) == 1
    assert sol.maxProfit([2, 4, 1]) == 2
    assert sol.maxProfit([3, 3, 3]) == 0
    assert sol.maxProfit([2, 1, 2, 1, 0, 1, 2]) == 2
    print("All tests passed!")
```
