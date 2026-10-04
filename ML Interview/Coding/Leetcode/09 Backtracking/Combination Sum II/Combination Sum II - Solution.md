---
topic: "Backtracking"
difficulty: Medium
leetcode: https://leetcode.com/problems/combination-sum-ii/
neetcode: https://neetcode.io/problems/combination-target-sum-ii
---
# Combination Sum II - Solution

**Question:** [[Combination Sum II - Question]] · **Difficulty:** Medium

## Intuition

Same backtracking as Combination Sum, but each index is used at most once (recurse with `i + 1`) and duplicates in the input must not produce duplicate combinations. After **sorting**, equal values are adjacent; at a given recursion level, picking the second copy of a value as the *next* element would rebuild exactly the subtrees already explored with the first copy, so skip it.

## Approach

1. Sort `candidates`.
2. `dfs(start, remaining)`: if `remaining == 0`, record a copy of `path`.
3. Loop `i` from `start`:
   - If `i > start` and `candidates[i] == candidates[i - 1]`, skip (same value already tried at this level).
   - If `candidates[i] > remaining`, break (sorted).
   - Append, recurse with `dfs(i + 1, remaining - candidates[i])`, pop.

## Code

```python
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, path = [], []

        def dfs(start: int, remaining: int) -> None:
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # same value at the same depth -> duplicate branch
                if candidates[i] > remaining:
                    break
                path.append(candidates[i])
                dfs(i + 1, remaining - candidates[i])  # each index used once
                path.pop()

        dfs(0, target)
        return res
```

## Complexity

- **Time:** `O(n * 2^n)` worst case — each index is in or out, plus `O(n)` to copy a result; sorting is `O(n log n)`.
- **Space:** `O(n)` — recursion depth and path (output excluded).

## Other Approaches

- **Generate all and dedupe with a set of tuples:** explore every subset of indices and store sorted tuples — Time `O(n * 2^n)` without pruning benefits, Space `O(2^n)` for the set.
- **Counter-based DFS:** iterate over distinct values with their counts and choose how many copies to take — same worst case, naturally duplicate-free.

## Key Takeaway

Sort + "skip `nums[i] == nums[i-1]` when `i > start`" is the universal trick to deduplicate combination/subset backtracking with repeated input values.
