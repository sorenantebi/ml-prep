---
topic: "2-D Dynamic Programming"
difficulty: Hard
leetcode: https://leetcode.com/problems/burst-balloons/
neetcode: https://neetcode.io/problems/burst-balloons
---
# Burst Balloons - Solution

**Question:** [[Burst Balloons - Question]] · **Difficulty:** Hard

## Intuition

Choosing which balloon to burst *first* splits nothing cleanly, because neighbours change. Instead think about which balloon in an interval is burst **last**: if `k` is the last one in the open interval `(l, r)`, its neighbours at that moment are exactly `l` and `r`, and the left part `(l, k)` and right part `(k, r)` are independent subproblems. Pad the array with `1`s on both ends.

## Approach

1. `vals = [1] + nums + [1]`, `N = len(vals)`.
2. `dp[l][r]` = max coins from bursting every balloon strictly between `l` and `r`.
3. For gap sizes from 2 to `N - 1`, for each `l` with `r = l + gap`:
   `dp[l][r] = max(dp[l][k] + vals[l] * vals[k] * vals[r] + dp[k][r])` over `l < k < r`.
4. Return `dp[0][N-1]`.

## Code

```python
from typing import List


class Solution:
	def maxCoins(self, nums: List[int]) -> int:
		vals = [1] + nums + [1]
		N = len(vals)
		dp = [[0] * N for _ in range(N)]  # dp[l][r]: open interval (l, r)
		for gap in range(2, N):
			for l in range(N - gap):
				r = l + gap
				best = 0
				for k in range(l + 1, r):
					# k is burst last in (l, r): its neighbours are l and r
					best = max(best, dp[l][k] + vals[l] * vals[k] * vals[r] + dp[k][r])
				dp[l][r] = best
		return dp[0][N - 1]
```

## Complexity

- **Time:** `O(n^3)` — `O(n^2)` intervals, each trying `O(n)` split points.
- **Space:** `O(n^2)` — the interval DP table.

## Other Approaches

- **Memoized recursion on `(l, r)`:** same "last balloon" recurrence top-down — Time `O(n^3)`, Space `O(n^2)`.
- **Brute force over burst orders:** try all `n!` permutations — Time `O(n! * n)`, Space `O(n)`.

## Key Takeaway

For interval DPs where removing an element changes adjacency, reason about the element processed **last** in the interval — its boundaries are then fixed and the subproblems become independent.
