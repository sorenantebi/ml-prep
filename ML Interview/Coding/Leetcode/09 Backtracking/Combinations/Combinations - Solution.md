---
topic: "Backtracking"
difficulty: Medium
leetcode: https://leetcode.com/problems/combinations/
neetcode: https://neetcode.io/problems/combinations
---
# Combinations - Solution

**Question:** [[Combinations - Question]] · **Difficulty:** Medium

## Intuition

Generate combinations in **increasing order** so each set is produced once: after choosing number `x`, only numbers greater than `x` may follow. Prune branches that cannot possibly reach length `k` because too few numbers remain.

## Approach

1. `dfs(start)` extends the current `path` with numbers from `start` to `n`.
2. If `len(path) == k`, record a copy and return.
3. Let `need = k - len(path)`; the next number can be at most `n - need + 1` (otherwise there aren't enough numbers left).
4. For each `x` in `start .. n - need + 1`: append `x`, recurse with `dfs(x + 1)`, pop.

## Code

```python
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, path = [], []

        def dfs(start: int) -> None:
            if len(path) == k:
                res.append(path[:])
                return
            need = k - len(path)
            for x in range(start, n - need + 2):  # leave room for the remaining picks
                path.append(x)
                dfs(x + 1)
                path.pop()

        dfs(1)
        return res
```

## Complexity

- **Time:** `O(k * C(n, k))` — each of the `C(n, k)` combinations is copied in `O(k)`; pruning keeps internal nodes proportional to that.
- **Space:** `O(k)` — recursion depth and path (output excluded).

## Other Approaches

- **Include/exclude per number:** decide for each `1..n` whether to take it, stopping when `k` are chosen — Time `O(k * C(n, k))` with pruning, Space `O(n)` recursion.
- **Library:** `itertools.combinations(range(1, n + 1), k)` — same complexity, useful to sanity-check.

## Key Takeaway

Combinations = backtracking with a `start` index that only moves forward; prune when the remaining range is shorter than the number of picks still needed.
