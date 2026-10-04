---
topic: "2-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/coin-change-ii/
neetcode: https://neetcode.io/problems/coin-change-ii
---
# Coin Change II - Solution

**Question:** [[Coin Change II - Question]] · **Difficulty:** Medium

## Intuition

This is the unbounded knapsack counting problem. To count combinations (not permutations), process coins one at a time in the **outer** loop: `dp[a]` = number of ways to make `a` using only the coins seen so far. Adding coin `c` lets every amount `a` also be formed as `(a - c) + c`.

## Approach

1. `dp = [0] * (amount + 1)`, `dp[0] = 1`.
2. For each coin `c`, for `a` from `c` up to `amount` (ascending, so the coin can be reused): `dp[a] += dp[a - c]`.
3. Return `dp[amount]`.

## Code

```python
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1  # one way to make 0: take nothing
        for c in coins:  # coins outer -> each combination counted once
            for a in range(c, amount + 1):  # ascending -> unlimited copies of c
                dp[a] += dp[a - c]
        return dp[amount]
```

## Complexity

- **Time:** `O(n * amount)` — each coin sweeps all amounts once.
- **Space:** `O(amount)` — a single 1-D table.

## Other Approaches

- **2-D DP `dp[i][a]`:** ways to make `a` with the first `i` coins — Time `O(n * amount)`, Space `O(n * amount)`.
- **Memoized DFS on `(i, remaining)`:** take coin `i` again or move to `i + 1` — Time `O(n * amount)`, Space `O(n * amount)`.

## Key Takeaway

Loop order matters in counting knapsacks: coins outer counts combinations, amounts outer counts permutations; ascending inner loop = unbounded, descending = 0/1.
