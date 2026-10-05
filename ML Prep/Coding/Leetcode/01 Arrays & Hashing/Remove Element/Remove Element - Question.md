---
topic: "Arrays & Hashing"
difficulty: Easy
leetcode: https://leetcode.com/problems/remove-element/
neetcode: https://neetcode.io/problems/remove-element
---
# Remove Element

**Topic:** [[01 Arrays & Hashing|Arrays & Hashing]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/remove-element/) · [NeetCode](https://neetcode.io/problems/remove-element)

**Solve it in:** [[Remove Element]] · **Answer:** [[Remove Element - Solution]]

## Problem

You are given an integer array `nums` and an integer `val`. Remove every occurrence of `val` from `nums` **in place** and return `k`, the number of elements that are not equal to `val`. After the call, the first `k` positions of `nums` must hold exactly the elements not equal to `val` (in any order); whatever is stored beyond index `k - 1` does not matter. You must not allocate a second array.

## Examples

**Example 1**
```text
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
```

**Example 2**
```text
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,3,0,4,_,_,_]
Explanation: the first five slots may hold 0,1,3,0,4 in any order.
```

## Constraints

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def removeElement(self, nums: List[int], val: int) -> int:
		pass  # your code here


def check(nums, val):
	expected = sorted(x for x in nums if x != val)
	arr = list(nums)
	k = Solution().removeElement(arr, val)
	return k == len(expected) and sorted(arr[:k]) == expected


if __name__ == "__main__":
	assert check([3, 2, 2, 3], 3)
	assert check([0, 1, 2, 2, 3, 0, 4, 2], 2)
	assert check([], 1)
	assert check([1], 1)
	assert check([1], 2)
	assert check([4, 4, 4, 4], 4)
	assert check([1, 2, 3, 4], 5)
	assert check([2, 1, 2, 1, 2], 1)
	print("All tests passed!")
```
