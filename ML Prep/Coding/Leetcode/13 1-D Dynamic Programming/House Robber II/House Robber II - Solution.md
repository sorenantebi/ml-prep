---
topic: "1-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/house-robber-ii/
neetcode: https://neetcode.io/problems/house-robber-ii
---
# House Robber II - Solution

**Question:** [[House Robber II - Question]] · **Difficulty:** Medium

## Intuition

The circle only adds one constraint: you can't take both the first and the last house. So at least one of them is excluded — solve the linear House Robber on `nums[1:]` and on `nums[:-1]` and take the better result. A single house is a special case (both slices would be empty).

## Approach

1. If there is one house, return its value.
2. Define the linear helper `rob_line(arr)` with the rolling `max(skip, take)` DP.
3. Return `max(rob_line(nums[:-1]), rob_line(nums[1:]))`.

## Code

```python
from typing import List


class Solution:
	def rob(self, nums: List[int]) -> int:
		if len(nums) == 1:
			return nums[0]

		def rob_line(arr: List[int]) -> int:
			prev2, prev1 = 0, 0
			for x in arr:
				prev2, prev1 = prev1, max(prev1, prev2 + x)
			return prev1

		# either the last house is excluded, or the first one is
		return max(rob_line(nums[:-1]), rob_line(nums[1:]))
```

## Complexity

- **Time:** `O(n)` — two linear passes.
- **Space:** `O(n)` for the slices (`O(1)` if you pass index ranges instead).

## Other Approaches

- **Memoised recursion with a "took first house" flag:** state `(i, took_first)` — Time `O(n)`, Space `O(n)`.

## Key Takeaway

Break a circular constraint by splitting into a few linear cases (exclude the first element / exclude the last) and reuse the linear solution.
