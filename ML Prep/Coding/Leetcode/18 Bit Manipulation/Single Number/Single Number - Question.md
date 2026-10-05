---
topic: "Bit Manipulation"
difficulty: Easy
leetcode: https://leetcode.com/problems/single-number/
neetcode: https://neetcode.io/problems/single-number
---
# Single Number

**Topic:** [[18 Bit Manipulation|Bit Manipulation]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/single-number/) · [NeetCode](https://neetcode.io/problems/single-number)

**Solve it in:** [[Single Number]] · **Answer:** [[Single Number - Solution]]

## Problem

You are given a non-empty integer array `nums`. Every value appears **exactly twice** except for one value, which appears exactly once. Return that single value.

Your solution must run in linear time and use only constant extra space.

## Examples

**Example 1**
```text
Input: nums = [2,2,1]
Output: 1
```

**Example 2**
```text
Input: nums = [4,1,2,1,2]
Output: 4
```

**Example 3**
```text
Input: nums = [1]
Output: 1
```

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`
- Every element appears twice except for exactly one element, which appears once.

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def singleNumber(self, nums: List[int]) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.singleNumber([2, 2, 1]) == 1
	assert s.singleNumber([4, 1, 2, 1, 2]) == 4
	assert s.singleNumber([1]) == 1
	assert s.singleNumber([-3, 5, 5]) == -3
	assert s.singleNumber([0, 7, 7]) == 0
	assert s.singleNumber([-1, -1, -2]) == -2
	assert s.singleNumber([30000, -30000, 30000]) == -30000
	big = list(range(1, 10001)) * 2 + [12345]
	assert s.singleNumber(big) == 12345
	print("All tests passed!")
```
