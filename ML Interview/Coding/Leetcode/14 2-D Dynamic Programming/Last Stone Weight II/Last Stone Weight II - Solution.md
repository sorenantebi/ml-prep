---
topic: "2-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/last-stone-weight-ii/
neetcode: https://neetcode.io/problems/last-stone-weight-ii
---
# Last Stone Weight II - Solution

**Question:** [[Last Stone Weight II - Question]] · **Difficulty:** Medium

## Intuition

Every sequence of smashes ends up assigning each stone a `+` or `-` sign, and the final weight is `|sum(+group) - sum(-group)|`; conversely any split into two groups is achievable. So we want to split the stones into two piles whose sums are as close as possible — a 0/1 knapsack: find the largest achievable subset sum `s1 <= total // 2`, then the answer is `total - 2 * s1`.

## Approach

1. Compute `total = sum(stones)` and `half = total // 2`.
2. Track the set of achievable subset sums up to `half` (a boolean array or a bitmask).
3. For each stone, add it to every previously achievable sum (iterate downward in the boolean version so each stone is used once).
4. Let `best` be the largest achievable sum `<= half`; return `total - 2 * best`.

## Code

```python
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        half = total // 2
        reachable = [False] * (half + 1)
        reachable[0] = True
        for w in stones:
            # iterate downward so each stone is used at most once (0/1 knapsack)
            for t in range(half, w - 1, -1):
                if reachable[t - w]:
                    reachable[t] = True
        best = max(t for t in range(half + 1) if reachable[t])
        return total - 2 * best
```

## Complexity

- **Time:** `O(n * S)` — `n` stones times `S = sum(stones) / 2` targets.
- **Space:** `O(S)` — one boolean array.

## Other Approaches

- **Set of reachable differences:** keep a set of all `+/-` sums after each stone and take the minimum absolute value — Time `O(n * S)`, Space `O(S)`.
- **Brute force over sign assignments:** try all `2^n` partitions — Time `O(2^n)`, Space `O(n)`.

## Key Takeaway

When a process of pairwise subtraction can be reduced to "assign each item `+` or `-`", the problem becomes a partition / subset-sum knapsack.
