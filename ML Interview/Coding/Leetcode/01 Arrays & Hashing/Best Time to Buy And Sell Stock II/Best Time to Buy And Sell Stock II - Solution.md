---
topic: "Arrays & Hashing"
difficulty: Medium
leetcode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
neetcode: https://neetcode.io/problems/best-time-to-buy-and-sell-stock-ii
---
# Best Time to Buy And Sell Stock II - Solution

**Question:** [[Best Time to Buy And Sell Stock II - Question]] · **Difficulty:** Medium

## Intuition

Any profitable multi-day hold `buy at i, sell at j` equals the sum of the daily changes between `i` and `j`. Since we can trade unlimited times, we can collect every positive day-to-day increase and skip every decrease, which is exactly the maximum (greedy).

## Approach

1. Initialize `profit = 0`.
2. For each day `i` from `1` to `n - 1`, if `prices[i] > prices[i - 1]`, add the difference to `profit`.
3. Return `profit`.

## Code

```python
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            # capture every upward move; a long climb is the sum of its daily gains
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
```

## Complexity

- **Time:** `O(n)` — one pass over the prices.
- **Space:** `O(1)` — a single accumulator.

## Other Approaches

- **State-machine DP:** track `hold` (max profit holding a share) and `cash` (max profit holding none) per day: `cash = max(cash, hold + p)`, `hold = max(hold, cash - p)` — Time `O(n)`, Space `O(1)`; generalizes to fees and cooldowns.
- **Peak-valley:** find each local minimum and the following local maximum and sum their differences — Time `O(n)`, Space `O(1)`.

## Key Takeaway

With unlimited transactions, total profit is the sum of all positive consecutive differences; remember the hold/cash DP for the variants with fees, cooldowns, or limited trades.
