---
topic: "Binary Search"
difficulty: Medium
leetcode: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
neetcode: https://neetcode.io/problems/search-in-rotated-sorted-array-ii
---
# Search In Rotated Sorted Array II

**Topic:** [[05 Binary Search|Binary Search]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) · [NeetCode](https://neetcode.io/problems/search-in-rotated-sorted-array-ii)

**Solve it in:** [[Search In Rotated Sorted Array II]] · **Answer:** [[Search In Rotated Sorted Array II - Solution]]

## Problem

An integer array `nums`, sorted in non-decreasing order and possibly containing **duplicates**, has been rotated at an unknown pivot index `k` (`0 <= k < n`), giving `[nums[k], ..., nums[n-1], nums[0], ..., nums[k-1]]`. For example `[0,1,2,4,4,4,5,6,6,7]` rotated at index 5 becomes `[4,5,6,6,7,0,1,2,4,4]`.

Given the rotated array and an integer `target`, return `true` if `target` is in `nums`, otherwise `false`. Try to reduce the number of operations as much as possible.

**Follow-up:** how do duplicates affect the run-time complexity compared to the distinct-values version?

## Examples

**Example 1**
```text
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
```

**Example 2**
```text
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
```

**Example 3**
```text
Input: nums = [1,0,1,1,1], target = 0
Output: true
```

## Constraints

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i], target <= 10^4`
- `nums` is a non-decreasing array that is possibly rotated

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def search(self, nums: List[int], target: int) -> bool:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.search([2, 5, 6, 0, 0, 1, 2], 0) is True
	assert s.search([2, 5, 6, 0, 0, 1, 2], 3) is False
	assert s.search([1, 0, 1, 1, 1], 0) is True
	assert s.search([1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 13) is True
	assert s.search([1], 0) is False
	assert s.search([1, 3, 1, 1, 1], 3) is True
	assert s.search([3, 1], 1) is True
	base = [0, 1, 1, 2, 4, 4, 4, 5, 6, 6, 7]
	for r in range(len(base)):
		arr = base[r:] + base[:r]
		for t in range(-1, 9):
			assert s.search(arr, t) is (t in arr)
	print("All tests passed!")
```
