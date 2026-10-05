---
topic: "Arrays & Hashing"
difficulty: Medium
leetcode: https://leetcode.com/problems/longest-consecutive-sequence/
neetcode: https://neetcode.io/problems/longest-consecutive-sequence
---
# Longest Consecutive Sequence

**Topic:** [[01 Arrays & Hashing|Arrays & Hashing]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/) · [NeetCode](https://neetcode.io/problems/longest-consecutive-sequence)

**Solve it in:** [[Longest Consecutive Sequence]] · **Answer:** [[Longest Consecutive Sequence - Solution]]

## Problem

Given an unsorted integer array `nums`, return the length of the longest run of consecutive integers (values `x, x+1, x+2, ...`) whose members all appear in `nums`. The values do not need to be adjacent in the array, and duplicates count only once. Your algorithm should run in `O(n)` time.

## Examples

**Example 1**
```text
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: the run 1,2,3,4 has length 4.
```

**Example 2**
```text
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

**Example 3**
```text
Input: nums = [1,0,1,2]
Output: 3
```

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Starter Code & Test Cases

```python
import random
from typing import List


class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
	assert s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
	assert s.longestConsecutive([1, 0, 1, 2]) == 3
	assert s.longestConsecutive([]) == 0
	assert s.longestConsecutive([7]) == 1
	assert s.longestConsecutive([-3, -1, -2, 5, 6]) == 3
	assert s.longestConsecutive([10, 30, 20]) == 1
	big = list(range(100000))
	random.Random(2).shuffle(big)
	assert s.longestConsecutive(big) == 100000
	print("All tests passed!")
```
