---
topic: "Arrays & Hashing"
difficulty: Medium
leetcode: https://leetcode.com/problems/sort-an-array/
neetcode: https://neetcode.io/problems/sort-an-array
---
# Sort an Array

**Topic:** [[01 Arrays & Hashing|Arrays & Hashing]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/sort-an-array/) · [NeetCode](https://neetcode.io/problems/sort-an-array)

**Solve it in:** [[Sort an Array]] · **Answer:** [[Sort an Array - Solution]]

## Problem

Given an integer array `nums`, return it sorted in non-decreasing (ascending) order. You must implement the sort yourself without calling built-in sorting functions, achieving `O(n log n)` time and using as little extra space as possible.

## Examples

**Example 1**
```text
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
```

**Example 2**
```text
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
```

**Example 3**
```text
Input: nums = [-4,10,-4,3]
Output: [-4,-4,3,10]
```

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `-5 * 10^4 <= nums[i] <= 5 * 10^4`
- Do not use built-in sort functions.

## Starter Code & Test Cases

```python
import random
from typing import List


class Solution:
	def sortArray(self, nums: List[int]) -> List[int]:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.sortArray([5, 2, 3, 1]) == [1, 2, 3, 5]
	assert s.sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
	assert s.sortArray([-4, 10, -4, 3]) == [-4, -4, 3, 10]
	assert s.sortArray([1]) == [1]
	assert s.sortArray([3, 3, 3]) == [3, 3, 3]
	assert s.sortArray(list(range(1000, 0, -1))) == list(range(1, 1001))
	rng = random.Random(0)
	data = [rng.randint(-50000, 50000) for _ in range(50000)]
	assert s.sortArray(list(data)) == sorted(data)
	print("All tests passed!")
```
