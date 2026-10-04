---
topic: "1-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/partition-equal-subset-sum/
neetcode: https://neetcode.io/problems/partition-equal-subset-sum
---
# Partition Equal Subset Sum - Solution

**Question:** [[Partition Equal Subset Sum - Question]] · **Difficulty:** Medium

## Intuition

Equal halves exist iff the total is even and some subset sums to `total / 2`. That is 0/1 knapsack feasibility: `dp[t]` = "some subset of the items seen so far sums to `t`". Iterating `t` **downward** for each item ensures each number is used at most once.

## Approach

1. If `sum(nums)` is odd, return `False`. Let `target = sum // 2`.
2. `dp = [True] + [False] * target`.
3. For each `x`, for `t` from `target` down to `x`: `dp[t] = dp[t] or dp[t - x]`.
4. Return `dp[target]` (you may early-exit as soon as it becomes true).

## Code

```python
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = [True] + [False] * target  # dp[t]: some subset sums to t
        for x in nums:
            for t in range(target, x - 1, -1):  # go down so x is used at most once
                if dp[t - x]:
                    dp[t] = True
            if dp[target]:
                return True
        return dp[target]
```

## Complexity

- **Time:** `O(n · target)` — `target <= sum/2 <= 10^4`, so about `2 · 10^6` steps.
- **Space:** `O(target)` — a 1-D DP array.

## Other Approaches

- **Set of reachable sums:** `sums |= {s + x for s in sums}` — Time `O(n · target)`, Space `O(target)`.
- **Bitset trick:** `bits |= bits << x` on a Python int, check bit `target` — same complexity but very fast in practice.

## Key Takeaway

"Split into two equal-sum halves" reduces to subset-sum for `total/2`; 0/1 knapsack iterates capacity backwards, unbounded knapsack forwards.
