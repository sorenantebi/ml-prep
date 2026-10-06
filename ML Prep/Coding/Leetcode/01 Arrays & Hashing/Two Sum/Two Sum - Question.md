---
topic: "Arrays & Hashing"
difficulty: Easy
leetcode: https://leetcode.com/problems/two-sum/
neetcode: https://neetcode.io/problems/two-integer-sum
---
# Two Sum

**Topic:** [[01 Arrays & Hashing|Arrays & Hashing]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/two-sum/) · [NeetCode](https://neetcode.io/problems/two-integer-sum)

**Solve it in:** [[Two Sum]] · **Answer:** [[Two Sum - Solution]]

## Problem

You are given an integer array `nums` and an integer `target`. Find the two distinct indices `i` and `j` such that `nums[i] + nums[j] == target`, and return them as a list `[i, j]`. You may not use the same element twice. It is guaranteed that exactly one valid pair exists, and the two indices may be returned in either order.

## Examples

**Example 1**
```text
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] == 2 + 7 == 9
```

**Example 2**
```text
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3**
```text
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Exactly one valid answer exists.
- Follow-up: can you do better than `O(n^2)` time?

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		hashmap = {}
		for i, num in enumerate(nums):
			if target - num in hashmap:
				return [hashmap[target - num], i]
			hashmap[num] = i


if __name__ == "__main__":
	s = Solution()
	assert sorted(s.twoSum([2, 7, 11, 15], 9)) == [0, 1]
	assert sorted(s.twoSum([3, 2, 4], 6)) == [1, 2]
	assert sorted(s.twoSum([3, 3], 6)) == [0, 1]
	assert sorted(s.twoSum([-3, 4, 3, 90], 0)) == [0, 2]
	assert sorted(s.twoSum([0, 4, 3, 0], 0)) == [0, 3]
	assert sorted(s.twoSum([1, 5, 9, -2], 7)) == [2, 3]
	big = list(range(10000))
	assert sorted(s.twoSum(big, 19997)) == [9998, 9999]
	print("All tests passed!")
```
