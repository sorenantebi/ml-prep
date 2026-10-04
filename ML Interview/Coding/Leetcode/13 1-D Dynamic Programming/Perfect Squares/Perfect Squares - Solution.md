---
topic: "1-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/perfect-squares/
neetcode: https://neetcode.io/problems/perfect-squares
---
# Perfect Squares - Solution

**Question:** [[Perfect Squares - Question]] · **Difficulty:** Medium

## Intuition

This is Coin Change where the "coins" are the perfect squares `<= n`: `dp[i] = 1 + min(dp[i - s])` over squares `s <= i`. Every `i` is reachable (using 1s), so no `-1` case exists.

## Approach

1. Precompute `squares = [1, 4, 9, ...]` up to `n`.
2. `dp[0] = 0`; for `i` from 1 to `n`, `dp[i] = 1 + min(dp[i - s] for s in squares if s <= i)`.
3. Return `dp[n]`.

## Code

```python
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [k * k for k in range(1, int(n ** 0.5) + 1)]
        dp = [0] + [n] * n  # n ones is always a valid upper bound
        for i in range(1, n + 1):
            for sq in squares:
                if sq > i:
                    break  # squares are sorted ascending
                if dp[i - sq] + 1 < dp[i]:
                    dp[i] = dp[i - sq] + 1
        return dp[n]
```

## Complexity

- **Time:** `O(n · sqrt(n))` — each `i` tries up to `sqrt(n)` squares.
- **Space:** `O(n)` — the DP array.

## Other Approaches

- **BFS by levels:** each level subtracts one square; the first level that reaches 0 is the answer — Time `O(n · sqrt(n))`, Space `O(n)`.
- **Math (Lagrange's four-square theorem + Legendre's three-square):** answer is 1 if `n` is a square, 4 if `n = 4^a(8b + 7)`, 2 if `n` is a sum of two squares, else 3 — Time `O(sqrt(n))`, Space `O(1)`.

## Key Takeaway

Recognise "min number of items summing to `n`" as unbounded knapsack/Coin Change; the items here are generated (perfect squares) rather than given.
