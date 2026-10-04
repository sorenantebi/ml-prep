---
topic: "2-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/stone-game/
neetcode: https://neetcode.io/problems/stone-game
---
# Stone Game - Solution

**Question:** [[Stone Game - Question]] · **Difficulty:** Medium

## Intuition

Interval DP on the score **difference**: let `dp[i][j]` be the best (current player's stones minus opponent's stones) achievable on `piles[i..j]`. Taking the left pile yields `piles[i] - dp[i+1][j]`, taking the right yields `piles[j] - dp[i][j-1]`. Alice wins iff `dp[0][n-1] > 0`. (There is also a math shortcut: with an even number of piles Alice can always take all even-indexed or all odd-indexed piles, whichever sum is larger, so she always wins.)

## Approach

1. `dp[i]` initially holds `piles[i]` (intervals of length 1).
2. For interval lengths 2..n, for each start `i` with end `j = i + len - 1`: `dp[i] = max(piles[i] - dp[i+1], piles[j] - dp[i])`, where before the update `dp[i]` refers to `[i..j-1]` and `dp[i+1]` to `[i+1..j]`.
3. Return `dp[0] > 0`.

## Code

```python
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = piles[:]  # dp[i] = best score difference on piles[i..i+len-1]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # dp[i+1] covers [i+1..j], old dp[i] covers [i..j-1]
                dp[i] = max(piles[i] - dp[i + 1], piles[j] - dp[i])
        return dp[0] > 0
```

## Complexity

- **Time:** `O(n^2)` — one update per interval.
- **Space:** `O(n)` — the interval table is compressed to one array.

## Other Approaches

- **Parity argument:** Alice can force taking all even-index or all odd-index piles, one of which sums to more — just `return True`; Time `O(1)`, Space `O(1)`.
- **Memoized minimax on `(i, j)`:** recurse with Alice maximizing and Bob minimizing her total — Time `O(n^2)`, Space `O(n^2)`.

## Key Takeaway

For two-player take-from-the-ends games, DP over intervals storing the score *difference* for the player to move turns minimax into a simple `max(take - dp(rest))`.
