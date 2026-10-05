---
topic: "Backtracking"
difficulty: Medium
leetcode: https://leetcode.com/problems/combination-sum/
neetcode: https://neetcode.io/problems/combination-target-sum
---
# Combination Sum - Solution

**Question:** [[Combination Sum - Question]] · **Difficulty:** Medium

## Intuition

Build combinations in **non-decreasing index order** so each multiset is generated exactly once: at each step we may reuse the current candidate or move on to later ones, but never go back. Sorting the candidates lets us stop exploring as soon as a candidate exceeds the remaining target.

## Approach

1. Sort `candidates`.
2. `dfs(start, remaining)`: if `remaining == 0`, record a copy of `path`.
3. Otherwise for each index `i` from `start`: if `candidates[i] > remaining`, break (all later ones are larger).
4. Append `candidates[i]`, recurse with `dfs(i, remaining - candidates[i])` (same `i` allows reuse), then pop.

## Code

```python
from typing import List


class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		candidates.sort()
		res, path = [], []

		def dfs(start: int, remaining: int) -> None:
			if remaining == 0:
				res.append(path[:])
				return
			for i in range(start, len(candidates)):
				c = candidates[i]
				if c > remaining:
					break  # sorted: nothing further can fit
				path.append(c)
				dfs(i, remaining - c)  # i, not i + 1: c may be reused
				path.pop()

		dfs(0, target)
		return res
```

## Complexity

- **Time:** `O(N^(T/m + 1))` in the worst case, where `N` = number of candidates, `T` = target, `m` = smallest candidate (depth of the tree is at most `T/m`); pruning makes it much faster in practice.
- **Space:** `O(T/m)` — recursion depth and path length (output excluded).

## Other Approaches

- **Include/exclude binary tree:** at each index either take `candidates[i]` again (stay at `i`) or skip to `i + 1` — same complexity, slightly different tree shape.
- **DP over targets:** `dp[t]` = list of combinations summing to `t`, built candidate by candidate to avoid permutations — Time/Space proportional to the output size times `T`.

## Key Takeaway

To avoid duplicate combinations, only pick candidates at index `>= start`; pass `i` (not `i + 1`) when reuse is allowed, and sort to enable early `break` pruning.
