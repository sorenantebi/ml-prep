---
topic: "Binary Search"
difficulty: Easy
leetcode: https://leetcode.com/problems/binary-search/
neetcode: https://neetcode.io/problems/binary-search
---
# Binary Search

**Topic:** [[05 Binary Search|Binary Search]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/binary-search/) · [NeetCode](https://neetcode.io/problems/binary-search)

**Solve it in:** [[Binary Search]] · **Answer:** [[Binary Search - Solution]]

## Problem

Given an array of integers `nums` sorted in ascending order with all elements distinct, and an integer `target`, return the index of `target` in `nums`, or `-1` if it is not present. The algorithm must run in `O(log n)` time.

## Examples

**Example 1**
```text
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
```

**Example 2**
```text
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
```

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 < nums[i], target < 10^4`
- All values in `nums` are unique
- `nums` is sorted in ascending order

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def search(self, nums: List[int], target: int) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.search([-1, 0, 3, 5, 9, 12], 9) == 4
	assert s.search([-1, 0, 3, 5, 9, 12], 2) == -1
	assert s.search([5], 5) == 0
	assert s.search([5], -5) == -1
	assert s.search([1, 3, 5, 7], 1) == 0
	assert s.search([1, 3, 5, 7], 7) == 3
	assert s.search([1, 3, 5, 7], 8) == -1
	nums = list(range(-5000, 5000, 3))
	assert all(s.search(nums, v) == i for i, v in enumerate(nums))
	print("All tests passed!")
```
