---
topic: "Backtracking"
difficulty: Medium
leetcode: https://leetcode.com/problems/permutations-ii/
neetcode: https://neetcode.io/problems/permutations-ii
---
# Permutations II

**Topic:** [[09 Backtracking|Backtracking]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/permutations-ii/) · [NeetCode](https://neetcode.io/problems/permutations-ii)

**Solve it in:** [[Permutations II]] · **Answer:** [[Permutations II - Solution]]

## Problem

Given an array `nums` that **may contain duplicate values**, return all distinct permutations of its elements. Permutations that look identical (same sequence of values) must appear only once. The result can be in any order.

## Examples

**Example 1**
```text
Input: nums = [1,1,2]
Output: [[1,1,2],[1,2,1],[2,1,1]]
```

**Example 2**
```text
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

## Constraints

- `1 <= nums.length <= 8`
- `-10 <= nums[i] <= 10`

## Starter Code & Test Cases

```python
from typing import List
from itertools import permutations


class Solution:
	def permuteUnique(self, nums: List[int]) -> List[List[int]]:
		pass  # your code here


def norm(res):
	return sorted(map(list, res))


if __name__ == "__main__":
	s = Solution()
	assert norm(s.permuteUnique([1, 1, 2])) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
	assert norm(s.permuteUnique([1, 2, 3])) == norm(permutations([1, 2, 3]))
	assert norm(s.permuteUnique([5])) == [[5]]
	assert norm(s.permuteUnique([2, 2, 2])) == [[2, 2, 2]]
	for case in ([3, 3, 0, 3], [1, -1, 1, -1], [1, 1, 2, 2, 3, 3, 4, 4]):
		res = s.permuteUnique(case)
		assert len(res) == len(set(map(tuple, res)))  # no duplicates returned
		assert norm(res) == sorted(map(list, set(permutations(case))))
	print("All tests passed!")
```
