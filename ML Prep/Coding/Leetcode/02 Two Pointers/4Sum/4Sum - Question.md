---
topic: "Two Pointers"
difficulty: Medium
leetcode: https://leetcode.com/problems/4sum/
neetcode: https://neetcode.io/problems/4sum
---
# 4Sum

**Topic:** [[02 Two Pointers|Two Pointers]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/4sum/) · [NeetCode](https://neetcode.io/problems/4sum)

**Solve it in:** [[4Sum]] · **Answer:** [[4Sum - Solution]]

## Problem

Given an integer array `nums` and an integer `target`, return all **unique** quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that `a`, `b`, `c`, `d` are pairwise distinct indices and the four values sum to `target`. No duplicate quadruplets (as multisets of values) may appear. The answer can be in any order.

## Examples

**Example 1**
```text
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

**Example 2**
```text
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
```

## Constraints

- `1 <= nums.length <= 200`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
		pass  # your code here


if __name__ == "__main__":
	sol = Solution()

	def norm(res):
		return sorted(tuple(sorted(q)) for q in res)

	assert norm(sol.fourSum([1, 0, -1, 0, -2, 2], 0)) == [(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)]
	assert norm(sol.fourSum([2, 2, 2, 2, 2], 8)) == [(2, 2, 2, 2)]
	assert norm(sol.fourSum([1], 1)) == []
	assert norm(sol.fourSum([1, 2, 3], 6)) == []
	assert norm(sol.fourSum([0, 0, 0, 0], 0)) == [(0, 0, 0, 0)]
	assert norm(sol.fourSum([1000000000, 1000000000, 1000000000, 1000000000], -294967296)) == []
	assert norm(sol.fourSum([-3, -1, 0, 2, 4, 5], 2)) == [(-3, -1, 2, 4)]
	print("All tests passed!")
```
