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
		pass  # your code here


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
