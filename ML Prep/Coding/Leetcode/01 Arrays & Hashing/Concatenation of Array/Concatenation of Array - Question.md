---
topic: "Arrays & Hashing"
difficulty: Easy
leetcode: https://leetcode.com/problems/concatenation-of-array/
neetcode: https://neetcode.io/problems/concatenation-of-array
---
# Concatenation of Array

**Topic:** [[01 Arrays & Hashing|Arrays & Hashing]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/concatenation-of-array/) · [NeetCode](https://neetcode.io/problems/concatenation-of-array)

**Solve it in:** [[Concatenation of Array]] · **Answer:** [[Concatenation of Array - Solution]]

## Problem

You are given an integer array `nums` of length `n`. Build and return a new array `ans` of length `2n` that consists of `nums` followed immediately by another copy of `nums`. In other words, for every index `0 <= i < n`, `ans[i] == nums[i]` and `ans[i + n] == nums[i]`.

## Examples

**Example 1**
```text
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
```

**Example 2**
```text
Input: nums = [4,9,3,7]
Output: [4,9,3,7,4,9,3,7]
```

## Constraints

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 1000`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def getConcatenation(self, nums: List[int]) -> List[int]:
		return nums + nums


if __name__ == "__main__":
	s = Solution()
	assert s.getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
	assert s.getConcatenation([4, 9, 3, 7]) == [4, 9, 3, 7, 4, 9, 3, 7]
	assert s.getConcatenation([5]) == [5, 5]
	assert s.getConcatenation([2, 2]) == [2, 2, 2, 2]
	assert s.getConcatenation([1000, 1]) == [1000, 1, 1000, 1]
	big = list(range(1, 1001))
	assert s.getConcatenation(big) == big + big
	print("All tests passed!")
```
