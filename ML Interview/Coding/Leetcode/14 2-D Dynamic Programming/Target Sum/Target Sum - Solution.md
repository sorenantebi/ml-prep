---
topic: "2-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/target-sum/
neetcode: https://neetcode.io/problems/target-sum
---
# Target Sum - Solution

**Question:** [[Target Sum - Question]] · **Difficulty:** Medium

## Intuition

Let `P` be the sum of elements with `+` and `N` the sum with `-`. Then `P - N = target` and `P + N = total`, so `P = (total + target) / 2`. The question becomes: how many subsets of `nums` sum to `P`? That is a 0/1 knapsack count. If `total + target` is odd or `|target| > total`, the answer is `0`.

## Approach

1. Compute `total = sum(nums)`. If `abs(target) > total` or `(total + target)` is odd, return `0`.
2. Let `goal = (total + target) // 2`; `dp = [0] * (goal + 1)`, `dp[0] = 1`.
3. For each `x` in `nums`, for `s` from `goal` down to `x`: `dp[s] += dp[s - x]` (descending -> each number used once). Zeros naturally double the count.
4. Return `dp[goal]`.

## Code

```python
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total or (total + target) % 2:
            return 0
        goal = (total + target) // 2  # required sum of the "+" group
        dp = [0] * (goal + 1)
        dp[0] = 1
        for x in nums:
            for s in range(goal, x - 1, -1):  # descending: 0/1 knapsack
                dp[s] += dp[s - x]
        return dp[goal]
```

## Complexity

- **Time:** `O(n * goal)` — `goal <= sum(nums)`.
- **Space:** `O(goal)` — one 1-D table.

## Other Approaches

- **Memoized DFS on `(i, running_sum)`:** branch on `+`/`-` with caching — Time `O(n * total)`, Space `O(n * total)`.
- **Dictionary DP of reachable sums:** map sum -> count, updated per element — Time `O(n * total)`, Space `O(total)`.

## Key Takeaway

"Assign +/- to every element" problems usually reduce algebraically to a subset-sum count; watch the parity and bound checks.
