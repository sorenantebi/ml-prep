---
topic: "2-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/stone-game-ii/
neetcode: https://neetcode.io/problems/stone-game-ii
---
# Stone Game II - Solution

**Question:** [[Stone Game II - Question]] · **Difficulty:** Medium

## Intuition

The game state is fully described by `(i, M)`: the index of the first remaining pile and the current `M`. Because the game is zero-sum, the stones the current player gets equal `suffix_sum[i] - (what the opponent gets from the next state)`. So the player picks the `X` that minimizes the opponent's best result.

## Approach

1. Precompute `suffix[i] = sum(piles[i:])`.
2. Define `best(i, M)` = max stones the player to move can collect from piles `i..n-1`.
   - If `i + 2M >= n`, take everything: return `suffix[i]`.
   - Otherwise return `max(suffix[i] - best(i + X, max(M, X)))` over `X` in `1..2M`.
3. Memoize and return `best(0, 1)`.

## Code

```python
from typing import List
from functools import lru_cache


class Solution:
	def stoneGameII(self, piles: List[int]) -> int:
		n = len(piles)
		suffix = [0] * (n + 1)
		for i in range(n - 1, -1, -1):
			suffix[i] = suffix[i + 1] + piles[i]

		@lru_cache(maxsize=None)
		def best(i: int, m: int) -> int:
			if i + 2 * m >= n:  # can grab all remaining piles
				return suffix[i]
			# my stones = everything left minus what the opponent will get
			return max(suffix[i] - best(i + x, max(m, x)) for x in range(1, 2 * m + 1))

		return best(0, 1)
```

## Complexity

- **Time:** `O(n^3)` — `O(n^2)` states `(i, M)`, each trying up to `2M = O(n)` moves.
- **Space:** `O(n^2)` — memo table plus `O(n)` recursion depth.

## Other Approaches

- **Bottom-up DP table `dp[i][M]`:** fill `i` from `n-1` down to 0 with the same recurrence — Time `O(n^3)`, Space `O(n^2)`.
- **Explicit minimax with a turn flag:** track `(i, M, isAlice)` and add/skip piles accordingly — Time `O(n^3)`, Space `O(n^2)`, but twice the states.

## Key Takeaway

In zero-sum games with a fixed total, "my score = remaining total - opponent's optimal score from the next state" removes the need to track whose turn it is.
