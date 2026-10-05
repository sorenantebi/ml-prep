---
topic: "Binary Search"
difficulty: Medium
leetcode: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
neetcode: https://neetcode.io/problems/find-minimum-in-rotated-sorted-array
---
# Find Minimum In Rotated Sorted Array

**Topic:** [[05 Binary Search|Binary Search]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) · [NeetCode](https://neetcode.io/problems/find-minimum-in-rotated-sorted-array)

**Solve it in:** [[Find Minimum In Rotated Sorted Array]] · **Answer:** [[Find Minimum In Rotated Sorted Array - Solution]]

## Problem

An array of `n` distinct integers, originally sorted in ascending order, has been rotated between `1` and `n` times. (Rotating once moves the last element to the front, so `[0,1,2,4,5,6,7]` rotated 4 times becomes `[4,5,6,7,0,1,2]`; rotating `n` times gives back the sorted array.)

Given the rotated array `nums`, return its minimum element. The algorithm must run in `O(log n)` time.

## Examples

**Example 1**
```text
Input: nums = [3,4,5,1,2]
Output: 1
```

**Example 2**
```text
Input: nums = [4,5,6,7,0,1,2]
Output: 0
```

**Example 3**
```text
Input: nums = [11,13,15,17]
Output: 11
Explanation: rotated n times, i.e. fully sorted
```

## Constraints

- `n == nums.length`, `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All values are unique
- `nums` is a sorted array rotated between `1` and `n` times

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def findMin(self, nums: List[int]) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.findMin([3, 4, 5, 1, 2]) == 1
	assert s.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
	assert s.findMin([11, 13, 15, 17]) == 11
	assert s.findMin([1]) == 1
	assert s.findMin([2, 1]) == 1
	assert s.findMin([1, 2]) == 1
	base = list(range(-20, 20, 3))
	for r in range(len(base)):
		assert s.findMin(base[r:] + base[:r]) == -20
	print("All tests passed!")
```
