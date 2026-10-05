---
topic: "Backtracking"
difficulty: Medium
leetcode: https://leetcode.com/problems/matchsticks-to-square/
neetcode: https://neetcode.io/problems/matchsticks-to-square
---
# Matchsticks to Square - Solution

**Question:** [[Matchsticks to Square - Question]] · **Difficulty:** Medium

## Intuition

The square's side must be `total / 4`, so we're placing each stick into one of four buckets so every bucket reaches exactly `side`. Backtracking assigns sticks one by one; sorting **longest first** makes overfull buckets fail early, and skipping buckets with the same current length avoids exploring symmetric (equivalent) assignments.

## Approach

1. If `total % 4 != 0` or the longest stick exceeds `side = total // 4`, return `false`.
2. Sort sticks in descending order; keep `sides = [0, 0, 0, 0]`.
3. `dfs(i)`: if `i == n`, return `true` (sums must all equal `side` since each is capped and totals match).
4. For each bucket `j`: if `sides[j] + sticks[i] <= side` and no earlier bucket had the same current length, add the stick, recurse, and remove it.
5. Return `false` if no bucket works.

## Code

```python
from typing import List


class Solution:
	def makesquare(self, matchsticks: List[int]) -> bool:
		total = sum(matchsticks)
		if total % 4:
			return False
		side = total // 4
		sticks = sorted(matchsticks, reverse=True)  # big sticks first -> fail fast
		if sticks[0] > side:
			return False
		sides = [0] * 4

		def dfs(i: int) -> bool:
			if i == len(sticks):
				return True  # every bucket is <= side and the total is 4*side
			tried = set()
			for j in range(4):
				if sides[j] in tried or sides[j] + sticks[i] > side:
					continue  # equal-length buckets are interchangeable
				tried.add(sides[j])
				sides[j] += sticks[i]
				if dfs(i + 1):
					return True
				sides[j] -= sticks[i]
			return False

		return dfs(0)
```

## Complexity

- **Time:** `O(4^n)` worst case — each stick tries up to 4 buckets; pruning (sorting, symmetry skip) cuts this drastically in practice.
- **Space:** `O(n)` — recursion depth.

## Other Approaches

- **Bitmask DP:** `dp[mask]` = current partial side length after using sticks in `mask` (or -1 if unreachable); extend with any unused stick that fits — Time `O(n * 2^n)`, Space `O(2^n)`.

## Key Takeaway

"Split into k equal-sum groups" is bucket backtracking: sort descending, cap each bucket at the target, and skip buckets with identical current sums to kill symmetric branches.
