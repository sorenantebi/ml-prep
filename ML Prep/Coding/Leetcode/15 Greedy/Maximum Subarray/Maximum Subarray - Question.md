---
topic: "Greedy"
difficulty: Medium
leetcode: https://leetcode.com/problems/maximum-subarray/
neetcode: https://neetcode.io/problems/maximum-subarray
---
# Maximum Subarray

**Topic:** [[15 Greedy|Greedy]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/maximum-subarray/) · [NeetCode](https://neetcode.io/problems/maximum-subarray)

**Solve it in:** [[Maximum Subarray]] · **Answer:** [[Maximum Subarray - Solution]]

## Problem

Given an integer array `nums`, find the contiguous, non-empty subarray with the largest sum and return that sum.

## Examples

**Example 1**
```text
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] sums to 6.
```

**Example 2**
```text
Input: nums = [1]
Output: 1
```

**Example 3**
```text
Input: nums = [5,4,-1,7,8]
Output: 23
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
	assert s.maxSubArray([1]) == 1
	assert s.maxSubArray([5, 4, -1, 7, 8]) == 23
	assert s.maxSubArray([-3, -1, -2]) == -1  # all negative: pick the max element
	assert s.maxSubArray([0, 0, 0]) == 0
	assert s.maxSubArray([-1, 2, -1, 2, -1]) == 3
	assert s.maxSubArray([2, -10, 3]) == 3
	print("All tests passed!")
```
