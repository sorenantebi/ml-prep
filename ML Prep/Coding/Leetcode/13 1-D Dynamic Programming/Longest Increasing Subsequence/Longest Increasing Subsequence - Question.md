---
topic: "1-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/longest-increasing-subsequence/
neetcode: https://neetcode.io/problems/longest-increasing-subsequence
---
# Longest Increasing Subsequence

**Topic:** [[13 1-D Dynamic Programming|1-D Dynamic Programming]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/longest-increasing-subsequence/) · [NeetCode](https://neetcode.io/problems/longest-increasing-subsequence)

**Solve it in:** [[Longest Increasing Subsequence]] · **Answer:** [[Longest Increasing Subsequence - Solution]]

## Problem

Given an integer array `nums`, return the length of its longest **strictly increasing subsequence**. A subsequence keeps the original order but may skip elements.

## Examples

**Example 1**
```text
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: One example is [2,3,7,101].
```

**Example 2**
```text
Input: nums = [0,1,0,3,2,3]
Output: 4
```

**Example 3**
```text
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

## Constraints

- `1 <= nums.length <= 2500`
- `-10^4 <= nums[i] <= 10^4`

## Starter Code & Test Cases

```python
from typing import List
import bisect


class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
	assert s.lengthOfLIS([0,1,0,3,2,3]) == 4
	assert s.lengthOfLIS([7,7,7,7,7,7,7]) == 1
	assert s.lengthOfLIS([5]) == 1
	assert s.lengthOfLIS([1,2,3,4,5]) == 5
	assert s.lengthOfLIS([5,4,3,2,1]) == 1
	assert s.lengthOfLIS([4,10,4,3,8,9]) == 3
	assert s.lengthOfLIS([-3,-1,-2,0]) == 3
	print("All tests passed!")
```
