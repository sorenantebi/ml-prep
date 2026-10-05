---
topic: "1-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/combination-sum-iv/
neetcode: https://neetcode.io/problems/combination-sum-iv
---
# Combination Sum IV - Solution

**Question:** [[Combination Sum IV - Question]] · **Difficulty:** Medium

## Intuition

Because order matters, think about the **last** number in the sequence: `ways(t) = sum(ways(t - x))` over all `x <= t`. Computing `dp` for every total from `0` to `target` (outer loop over totals, inner over numbers) counts permutations; swapping the loops would count combinations instead.

## Approach

1. `dp = [1] + [0] * target` (one way to make 0: the empty sequence).
2. For `t` from 1 to `target`, for each `x` in `nums` with `x <= t`: `dp[t] += dp[t - x]`.
3. Return `dp[target]`.

## Code

```python
from typing import List


class Solution:
	def combinationSum4(self, nums: List[int], target: int) -> int:
		dp = [1] + [0] * target  # dp[t] = number of ordered sequences summing to t
		for t in range(1, target + 1):
			for x in nums:
				if x <= t:
					dp[t] += dp[t - x]  # x is the last number of the sequence
		return dp[target]
```

## Complexity

- **Time:** `O(target · len(nums))` — every total tries every number.
- **Space:** `O(target)` — the DP array.

## Other Approaches

- **Memoised recursion:** `f(t) = sum f(t - x)` with a cache — Time `O(target · len(nums))`, Space `O(target)`.

## Key Takeaway

Loop order decides what you count: totals outside / items inside counts ordered sequences (permutations); items outside / totals inside counts unordered combinations (Coin Change II).
