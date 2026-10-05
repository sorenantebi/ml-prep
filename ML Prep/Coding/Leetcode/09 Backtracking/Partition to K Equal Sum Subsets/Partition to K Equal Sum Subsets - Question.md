---
topic: "Backtracking"
difficulty: Medium
leetcode: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
neetcode: https://neetcode.io/problems/partition-to-k-equal-sum-subsets
---
# Partition to K Equal Sum Subsets

**Topic:** [[09 Backtracking|Backtracking]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) · [NeetCode](https://neetcode.io/problems/partition-to-k-equal-sum-subsets)

**Solve it in:** [[Partition to K Equal Sum Subsets]] · **Answer:** [[Partition to K Equal Sum Subsets - Solution]]

## Problem

Given an integer array `nums` and an integer `k`, determine whether `nums` can be divided into `k` **non-empty** groups (each element used in exactly one group) such that every group has the same sum.

Return `true` if such a division exists, otherwise `false`.

## Examples

**Example 1**
```text
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: (5), (1,4), (2,3), (2,3) each sum to 5
```

**Example 2**
```text
Input: nums = [1,2,3,4], k = 3
Output: false
```

## Constraints

- `1 <= k <= nums.length <= 16`
- `1 <= nums[i] <= 10^4`
- Each value appears at most 4 times

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4) is True
	assert s.canPartitionKSubsets([1, 2, 3, 4], 3) is False
	assert s.canPartitionKSubsets([7], 1) is True
	assert s.canPartitionKSubsets([2, 2, 2, 2, 3, 4, 5], 4) is False
	assert s.canPartitionKSubsets([1, 1, 1, 1, 2, 2, 2, 2], 4) is True
	assert s.canPartitionKSubsets([10, 10, 10, 7, 7, 7, 7, 7, 7, 6, 6, 6], 3) is True
	assert s.canPartitionKSubsets([5, 5, 5, 5], 4) is True
	assert s.canPartitionKSubsets([3, 3, 10, 2, 2], 2) is True
	assert s.canPartitionKSubsets([1] * 16, 16) is True
	assert s.canPartitionKSubsets([10000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 2) is False
	print("All tests passed!")
```
