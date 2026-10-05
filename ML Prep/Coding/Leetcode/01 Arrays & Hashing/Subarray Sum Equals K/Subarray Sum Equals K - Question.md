---
topic: "Arrays & Hashing"
difficulty: Medium
leetcode: https://leetcode.com/problems/subarray-sum-equals-k/
neetcode: https://neetcode.io/problems/subarray-sum-equals-k
---
# Subarray Sum Equals K

**Topic:** [[01 Arrays & Hashing|Arrays & Hashing]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/) · [NeetCode](https://neetcode.io/problems/subarray-sum-equals-k)

**Solve it in:** [[Subarray Sum Equals K]] · **Answer:** [[Subarray Sum Equals K - Solution]]

## Problem

Given an integer array `nums` (which may contain negative numbers and zeros) and an integer `k`, return how many contiguous, non-empty subarrays of `nums` have elements summing to exactly `k`.

## Examples

**Example 1**
```text
Input: nums = [1,1,1], k = 2
Output: 2
Explanation: [1,1] starting at index 0 and [1,1] starting at index 1.
```

**Example 2**
```text
Input: nums = [1,2,3], k = 3
Output: 2
Explanation: [1,2] and [3].
```

**Example 3**
```text
Input: nums = [1,-1,0], k = 0
Output: 3
Explanation: [1,-1], [0], and [1,-1,0].
```

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`
- `-10^7 <= k <= 10^7`

## Starter Code & Test Cases

```python
import random
from typing import List


class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		pass  # your code here


def brute(nums, k):
	return sum(1 for i in range(len(nums)) for j in range(i, len(nums)) if sum(nums[i:j + 1]) == k)


if __name__ == "__main__":
	s = Solution()
	assert s.subarraySum([1, 1, 1], 2) == 2
	assert s.subarraySum([1, 2, 3], 3) == 2
	assert s.subarraySum([1, -1, 0], 0) == 3
	assert s.subarraySum([5], 5) == 1
	assert s.subarraySum([5], 0) == 0
	assert s.subarraySum([0, 0, 0], 0) == 6
	assert s.subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4
	rng = random.Random(3)
	for _ in range(50):
		arr = [rng.randint(-5, 5) for _ in range(rng.randint(1, 40))]
		target = rng.randint(-8, 8)
		assert s.subarraySum(arr, target) == brute(arr, target)
	print("All tests passed!")
```
