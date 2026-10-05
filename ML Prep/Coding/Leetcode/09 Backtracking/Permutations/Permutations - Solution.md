---
topic: "Backtracking"
difficulty: Medium
leetcode: https://leetcode.com/problems/permutations/
neetcode: https://neetcode.io/problems/permutations
---
# Permutations - Solution

**Question:** [[Permutations - Question]] · **Difficulty:** Medium

## Intuition

A permutation is built position by position: at each step choose any element not yet used. Backtracking explores this tree with a `used` marker per element — mark, recurse, unmark. The leaves (paths of length `n`) are exactly the `n!` permutations.

## Approach

1. Keep `path` and a boolean array `used`.
2. `dfs()`: if `len(path) == n`, record a copy.
3. Otherwise, for each index `i` not used: mark it, append `nums[i]`, recurse, then pop and unmark.

## Code

```python
from typing import List


class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		res, path = [], []
		used = [False] * len(nums)

		def dfs() -> None:
			if len(path) == len(nums):
				res.append(path[:])
				return
			for i, x in enumerate(nums):
				if used[i]:
					continue
				used[i] = True
				path.append(x)
				dfs()
				path.pop()       # backtrack
				used[i] = False

		dfs()
		return res
```

## Complexity

- **Time:** `O(n * n!)` — `n!` permutations, each copied in `O(n)` (each node also scans `n` indices).
- **Space:** `O(n)` — recursion depth, `path`, and `used` (output excluded).

## Other Approaches

- **In-place swapping:** at depth `d`, swap each `nums[i]` (`i >= d`) into position `d`, recurse, swap back — Time `O(n * n!)`, Space `O(n)` recursion, no `used` array.
- **Insertion build-up:** for each new number, insert it into every position of every permutation built so far — Time `O(n * n!)`, Space output-sized.

## Key Takeaway

Permutations = backtracking over positions with a `used` set (or swap-in-place); unlike combinations there is no `start` index because order matters.
