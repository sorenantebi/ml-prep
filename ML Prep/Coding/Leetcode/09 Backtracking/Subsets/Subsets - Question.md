---
topic: "Backtracking"
difficulty: Medium
leetcode: https://leetcode.com/problems/subsets/
neetcode: https://neetcode.io/problems/subsets
---
# Subsets

**Topic:** [[09 Backtracking|Backtracking]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/subsets/) · [NeetCode](https://neetcode.io/problems/subsets)

**Solve it in:** [[Subsets]] · **Answer:** [[Subsets - Solution]]

## Problem

Given an integer array `nums` whose elements are all **distinct**, return every possible subset (the power set), including the empty subset and the full array.

The result must not contain duplicate subsets. The subsets, and the elements inside each subset, may be returned in any order.

## Examples

**Example 1**
```text
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**Example 2**
```text
Input: nums = [0]
Output: [[],[0]]
```

## Constraints

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All values in `nums` are unique

## Starter Code & Test Cases

```python
from typing import List
from itertools import combinations


class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		pass  # your code here


def norm(res):
	return sorted(sorted(x) for x in res)


def brute(nums):
	return [list(c) for r in range(len(nums) + 1) for c in combinations(nums, r)]


if __name__ == "__main__":
	s = Solution()
	assert norm(s.subsets([1, 2, 3])) == norm([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
	assert norm(s.subsets([0])) == norm([[], [0]])
	assert norm(s.subsets([-1, 5])) == norm([[], [-1], [5], [-1, 5]])
	assert norm(s.subsets([4, -3, 0, 9])) == norm(brute([4, -3, 0, 9]))
	big = list(range(-5, 5))
	res = s.subsets(big)
	assert len(res) == 1024
	assert norm(res) == norm(brute(big))
	print("All tests passed!")
```
