---
topic: "Two Pointers"
difficulty: Medium
leetcode: https://leetcode.com/problems/4sum/
neetcode: https://neetcode.io/problems/4sum
---
# 4Sum - Solution

**Question:** [[4Sum - Question]] · **Difficulty:** Medium

## Intuition

4Sum is 3Sum with one more fixed element: sort, fix the first two values with nested loops, and find the last two with opposite-end two pointers. Sorting lets us skip equal neighbors at every level to avoid duplicate quadruplets.

## Approach

1. Sort `nums`.
2. For each `i` (skip if `nums[i] == nums[i - 1]`):
   - For each `j > i` (skip if `j > i + 1` and `nums[j] == nums[j - 1]`):
     - Run two pointers `l = j + 1`, `r = n - 1` searching for `target - nums[i] - nums[j]`.
     - On a hit, record it, move both pointers, and skip duplicates of `nums[l]`.
3. Return the collected quadruplets.

## Code

```python
from typing import List


class Solution:
	def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
		nums.sort()
		n = len(nums)
		res = []
		for i in range(n - 3):
			if i > 0 and nums[i] == nums[i - 1]:
				continue
			for j in range(i + 1, n - 2):
				if j > i + 1 and nums[j] == nums[j - 1]:
					continue
				l, r = j + 1, n - 1
				while l < r:
					s = nums[i] + nums[j] + nums[l] + nums[r]
					if s < target:
						l += 1
					elif s > target:
						r -= 1
					else:
						res.append([nums[i], nums[j], nums[l], nums[r]])
						l += 1
						r -= 1
						while l < r and nums[l] == nums[l - 1]:
							l += 1  # skip duplicate third values
		return res
```

## Complexity

- **Time:** `O(n^3)` — two nested loops plus a linear two-pointer scan.
- **Space:** `O(1)` extra (or `O(n)` for sorting), excluding the output.

## Other Approaches

- **Generic recursive k-Sum:** recursively fix one element until reaching a 2Sum base case solved with two pointers — Time `O(n^(k-1))`, Space `O(k)` recursion.
- **Brute force with a set:** all 4-index combinations deduplicated with sorted tuples — Time `O(n^4)`, Space `O(k)` results.

## Key Takeaway

Every extra element in k-Sum adds one outer loop on top of a two-pointer core; deduplicate at each level by skipping equal neighbors in the sorted array. (In Python big sums are safe; in fixed-width languages watch for overflow.)
