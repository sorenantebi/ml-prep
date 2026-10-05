---
topic: "Backtracking"
difficulty: Medium
leetcode: https://leetcode.com/problems/combination-sum-ii/
neetcode: https://neetcode.io/problems/combination-target-sum-ii
---
# Combination Sum II

**Topic:** [[09 Backtracking|Backtracking]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/combination-sum-ii/) · [NeetCode](https://neetcode.io/problems/combination-target-sum-ii)

**Solve it in:** [[Combination Sum II]] · **Answer:** [[Combination Sum II - Solution]]

## Problem

Given an array of positive integers `candidates` (which **may contain duplicates**) and a positive integer `target`, return all unique combinations whose elements sum to `target`. Each array position may be used **at most once** in a combination.

The result must not contain duplicate combinations (two combinations with the same multiset of values are the same). Return them in any order.

## Examples

**Example 1**
```text
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
```

**Example 2**
```text
Input: candidates = [2,5,2,1,2], target = 5
Output: [[1,2,2],[5]]
```

## Constraints

- `1 <= candidates.length <= 100`
- `1 <= candidates[i] <= 50`
- `1 <= target <= 30`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
		pass  # your code here


def norm(res):
	return sorted(sorted(x) for x in res)


if __name__ == "__main__":
	s = Solution()
	assert norm(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)) == norm([[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
	assert norm(s.combinationSum2([2, 5, 2, 1, 2], 5)) == norm([[1, 2, 2], [5]])
	assert s.combinationSum2([3], 2) == []
	assert norm(s.combinationSum2([1, 1, 1, 1], 2)) == [[1, 1]]
	assert norm(s.combinationSum2([1] * 30, 30)) == [[1] * 30]
	assert norm(s.combinationSum2([4, 4, 2, 1, 4, 2, 2, 1, 3], 6)) == norm([[1, 1, 4], [1, 2, 3], [1, 1, 2, 2], [2, 4], [2, 2, 2]])
	res = s.combinationSum2([2, 2, 2], 4)
	assert len(res) == 1 and sorted(res[0]) == [2, 2]
	print("All tests passed!")
```
