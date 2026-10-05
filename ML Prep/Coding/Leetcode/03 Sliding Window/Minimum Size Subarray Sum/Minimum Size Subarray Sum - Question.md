---
topic: "Sliding Window"
difficulty: Medium
leetcode: https://leetcode.com/problems/minimum-size-subarray-sum/
neetcode: https://neetcode.io/problems/minimum-size-subarray-sum
---
# Minimum Size Subarray Sum

**Topic:** [[03 Sliding Window|Sliding Window]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/) · [NeetCode](https://neetcode.io/problems/minimum-size-subarray-sum)

**Solve it in:** [[Minimum Size Subarray Sum]] · **Answer:** [[Minimum Size Subarray Sum - Solution]]

## Problem

Given an array of **positive** integers `nums` and a positive integer `target`, return the minimal length of a contiguous subarray whose sum is **greater than or equal to** `target`. If no such subarray exists, return `0`.

## Examples

**Example 1**
```text
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: [4,3]
```

**Example 2**
```text
Input: target = 4, nums = [1,4,4]
Output: 1
```

**Example 3**
```text
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

## Constraints

- `1 <= target <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def minSubArrayLen(self, target: int, nums: List[int]) -> int:
		pass  # your code here


if __name__ == "__main__":
	sol = Solution()
	assert sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
	assert sol.minSubArrayLen(4, [1, 4, 4]) == 1
	assert sol.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
	assert sol.minSubArrayLen(5, [5]) == 1
	assert sol.minSubArrayLen(6, [5]) == 0
	assert sol.minSubArrayLen(15, [1, 2, 3, 4, 5]) == 5
	assert sol.minSubArrayLen(11, [1, 2, 3, 4, 5]) == 3
	print("All tests passed!")
```
