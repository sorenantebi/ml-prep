---
topic: "1-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/combination-sum-iv/
neetcode: https://neetcode.io/problems/combination-sum-iv
---
# Combination Sum IV

**Topic:** [[13 1-D Dynamic Programming|1-D Dynamic Programming]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/combination-sum-iv/) · [NeetCode](https://neetcode.io/problems/combination-sum-iv)

**Solve it in:** [[Combination Sum IV]] · **Answer:** [[Combination Sum IV - Solution]]

## Problem

Given an array of **distinct** positive integers `nums` and a positive integer `target`, return the number of ordered sequences of numbers from `nums` (each may be used any number of times) that add up to `target`. Different orderings count as different sequences. The answer fits in a 32-bit integer.

## Examples

**Example 1**
```text
Input: nums = [1,2,3], target = 4
Output: 7
Explanation: (1,1,1,1), (1,1,2), (1,2,1), (2,1,1), (2,2), (1,3), (3,1).
```

**Example 2**
```text
Input: nums = [9], target = 3
Output: 0
```

## Constraints

- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 1000`, all distinct
- `1 <= target <= 1000`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def combinationSum4(self, nums: List[int], target: int) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.combinationSum4([1,2,3], 4) == 7
	assert s.combinationSum4([9], 3) == 0
	assert s.combinationSum4([1], 1) == 1
	assert s.combinationSum4([2], 4) == 1
	assert s.combinationSum4([1,2], 3) == 3
	assert s.combinationSum4([4,2,1], 32) == 39882198
	assert s.combinationSum4([3,5], 7) == 0
	print("All tests passed!")
```
