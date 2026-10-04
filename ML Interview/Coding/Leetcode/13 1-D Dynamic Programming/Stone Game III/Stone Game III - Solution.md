---
topic: "1-D Dynamic Programming"
difficulty: Hard
leetcode: https://leetcode.com/problems/stone-game-iii/
neetcode: https://neetcode.io/problems/stone-game-iii
---
# Stone Game III - Solution

**Question:** [[Stone Game III - Question]] · **Difficulty:** Hard

## Intuition

Model the game from the perspective of "the player about to move". Let `dp[i]` be the best **score difference** (my total minus opponent's total) the current player can achieve on the suffix starting at `i`. Taking `j` stones gains their sum, and then the opponent achieves `dp[i + j]` against us, so `dp[i] = max_j (sum(stones[i:i+j]) - dp[i + j])`. The sign of `dp[0]` decides the winner.

## Approach

1. `dp` has length `n + 1` with `dp[n] = 0` (no stones left -> difference 0).
2. Iterate `i` from `n - 1` down to 0; for each last-taken index `j` in `i .. min(i + 2, n - 1)`, accumulate `taken += stoneValue[j]` and keep the best `taken - dp[j + 1]`.
3. Return `"Alice"` if `dp[0] > 0`, `"Bob"` if `< 0`, else `"Tie"`.

## Code

```python
from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)  # dp[i]: best (my score - their score) from suffix i
        for i in range(n - 1, -1, -1):
            best, taken = float("-inf"), 0
            for j in range(i, min(i + 3, n)):
                taken += stoneValue[j]
                best = max(best, taken - dp[j + 1])  # opponent moves next on j+1
            dp[i] = best

        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"
```

## Complexity

- **Time:** `O(n)` — each index tries at most 3 moves.
- **Space:** `O(n)` — the DP array (can be reduced to `O(1)` with a rolling window of 4).

## Other Approaches

- **Memoised minimax on `(i, turn)`:** track each player's score explicitly — Time `O(n)`, Space `O(n)` but clumsier.
- **Suffix sums:** `dp[i]` = max stones value current player can collect = `suffix[i] - min(dp[i+1..i+3])` — Time `O(n)`, Space `O(n)`.

## Key Takeaway

For two-player zero-sum games, store the score **difference** for the player to move; the recurrence becomes `gain - dp[next]`, with no turn variable needed.
