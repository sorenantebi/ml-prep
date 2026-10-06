---
topic: "Arrays & Hashing"
difficulty: Medium
leetcode: https://leetcode.com/problems/sort-colors/
neetcode: https://neetcode.io/problems/sort-colors
---
# Sort Colors

**Topic:** [[01 Arrays & Hashing|Arrays & Hashing]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/sort-colors/) · [NeetCode](https://neetcode.io/problems/sort-colors)

**Solve it in:** [[Sort Colors]] · **Answer:** [[Sort Colors - Solution]]

## Problem

You are given an array `nums` of `n` objects colored red, white, or blue, encoded as the integers `0`, `1`, and `2` respectively. Rearrange the array **in place** so that all `0`s come first, then all `1`s, then all `2`s. Do not use the library sort function; the method returns nothing.

## Examples

**Example 1**
```text
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

**Example 2**
```text
Input: nums = [2,0,1]
Output: [0,1,2]
```

## Constraints

- `1 <= nums.length <= 300`
- `nums[i]` is `0`, `1`, or `2`.
- Follow-up: can you do it in a single pass using only constant extra space?

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def sortColors(self, nums: List[int]) -> None:
		"""Do not return anything, modify nums in-place instead."""
	
		def merge(l, m, r):
			cp1, cp2 = nums[l:m+1], nums[m+1:r+1]
			i, j = 0, 0
			
			while i < len(cp1) and j < len(cp2):
				if cp1[i] < cp2[j]:
					nums[l] = cp1[i]
					i += 1
				else:
					nums[l] = cp2[j]
					j += 1
				l += 1
			
			# get rid of the rest
			while i < len(cp1):
				nums[l] = cp1[i]
				i += 1
				l += 1
			
			while j < len(cp2):
				nums[l] = cp2[j]
				j += 1
				l += 1
			
		def mergeSort(l, r):
			if r - l == 0:
				return
			m = (r + l) // 2
			mergeSort(l, m)
			mergeSort(m + 1, r)
			merge(l, m, r)
	

		mergeSort(0, len(nums) - 1)
		return nums



def run(nums):
	Solution().sortColors(nums)
	return nums


if __name__ == "__main__":
	assert run([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]
	assert run([2, 0, 1]) == [0, 1, 2]
	assert run([0]) == [0]
	assert run([1, 1, 1]) == [1, 1, 1]
	assert run([2, 2, 0, 0]) == [0, 0, 2, 2]
	assert run([1, 2, 0]) == [0, 1, 2]
	arr = [2, 1, 0] * 100
	assert run(arr) == [0] * 100 + [1] * 100 + [2] * 100
	print("All tests passed!")
```
