---
topic: "Backtracking"
difficulty: Medium
leetcode: https://leetcode.com/problems/permutations-ii/
neetcode: https://neetcode.io/problems/permutations-ii
---
# Permutations II - Solution

**Question:** [[Permutations II - Question]] · **Difficulty:** Medium

## Intuition

Count each distinct value and build permutations position by position, choosing from the **distinct values that still have copies left**. Because the choice at each position is among distinct values (not indices), identical permutations can never be generated twice — no dedupe set needed.

## Approach

1. Build `count = Counter(nums)`.
2. `dfs()`: if `len(path) == n`, record a copy.
3. Otherwise, for each distinct value `v` with `count[v] > 0`: decrement, append, recurse, pop, increment.

## Code

```python
from typing import List
from collections import Counter


class Solution:
	def permuteUnique(self, nums: List[int]) -> List[List[int]]:
		res, path = [], []
		count = Counter(nums)

		def dfs() -> None:
			if len(path) == len(nums):
				res.append(path[:])
				return
			for v in count:
				if count[v] == 0:
					continue
				count[v] -= 1        # use one copy of this distinct value
				path.append(v)
				dfs()
				path.pop()
				count[v] += 1        # restore

		dfs()
		return res
```

## Complexity

- **Time:** `O(n * n!)` worst case (all distinct); with duplicates it is proportional to `n` times the number of unique permutations.
- **Space:** `O(n)` — recursion depth, path, and counter (output excluded).

## Other Approaches

- **Sort + `used[]` with skip rule:** skip `nums[i]` if `nums[i] == nums[i-1]` and `nums[i-1]` is not currently used — Time `O(n * n!)`, Space `O(n)`.
- **Generate all permutations and dedupe with a set:** Time `O(n * n!)`, Space `O(n * n!)` — wasteful when many duplicates.

## Key Takeaway

With duplicate inputs, branch on distinct values (via a Counter) rather than on indices — duplicates are avoided by construction.
