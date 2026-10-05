---
topic: "1-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/maximum-product-subarray/
neetcode: https://neetcode.io/problems/maximum-product-subarray
---
# Maximum Product Subarray

**Topic:** [[13 1-D Dynamic Programming|1-D Dynamic Programming]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/maximum-product-subarray/) · [NeetCode](https://neetcode.io/problems/maximum-product-subarray)

**Solve it in:** [[Maximum Product Subarray]] · **Answer:** [[Maximum Product Subarray - Solution]]

## Problem

Given an integer array `nums`, find the non-empty contiguous subarray whose elements have the largest product, and return that product. The answer is guaranteed to fit in a 32-bit integer.

## Examples

**Example 1**
```text
Input: nums = [2,3,-2,4]
Output: 6
Explanation: The subarray [2,3] has product 6.
```

**Example 2**
```text
Input: nums = [-2,0,-1]
Output: 0
Explanation: [-2,-1] is not contiguous, so the best is 0.
```

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `-10 <= nums[i] <= 10`
- The product of any subarray fits in a 32-bit integer.

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def maxProduct(self, nums: List[int]) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.maxProduct([2,3,-2,4]) == 6
	assert s.maxProduct([-2,0,-1]) == 0
	assert s.maxProduct([-2]) == -2
	assert s.maxProduct([-2,3,-4]) == 24
	assert s.maxProduct([0,2]) == 2
	assert s.maxProduct([-1,-1]) == 1
	assert s.maxProduct([2,-5,-2,-4,3]) == 24
	print("All tests passed!")
```
