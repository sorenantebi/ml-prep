---
topic: "Arrays & Hashing"
difficulty: Hard
leetcode: https://leetcode.com/problems/first-missing-positive/
neetcode: https://neetcode.io/problems/first-missing-positive
---
# First Missing Positive

**Topic:** [[01 Arrays & Hashing|Arrays & Hashing]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/first-missing-positive/) · [NeetCode](https://neetcode.io/problems/first-missing-positive)

**Solve it in:** [[First Missing Positive]] · **Answer:** [[First Missing Positive - Solution]]

## Problem

Given an unsorted integer array `nums`, return the smallest positive integer (`1, 2, 3, ...`) that does not appear in `nums`. Your algorithm must run in `O(n)` time and use only `O(1)` auxiliary space (modifying the input array is allowed).

## Examples

**Example 1**
```text
Input: nums = [1,2,0]
Output: 3
```

**Example 2**
```text
Input: nums = [3,4,-1,1]
Output: 2
```

**Example 3**
```text
Input: nums = [7,8,9,11,12]
Output: 1
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- Required: `O(n)` time and `O(1)` extra space.

## Starter Code & Test Cases

```python
import random
from typing import List


class Solution:
	def firstMissingPositive(self, nums: List[int]) -> int:
		pass  # your code here


def brute(nums):
	present = set(nums)
	m = 1
	while m in present:
		m += 1
	return m


if __name__ == "__main__":
	s = Solution()
	assert s.firstMissingPositive([1, 2, 0]) == 3
	assert s.firstMissingPositive([3, 4, -1, 1]) == 2
	assert s.firstMissingPositive([7, 8, 9, 11, 12]) == 1
	assert s.firstMissingPositive([1]) == 2
	assert s.firstMissingPositive([2]) == 1
	assert s.firstMissingPositive([1, 1]) == 2
	assert s.firstMissingPositive([-2**31, 2**31 - 1]) == 1
	assert s.firstMissingPositive(list(range(100000, 0, -1))) == 100001
	rng = random.Random(4)
	for _ in range(200):
		arr = [rng.randint(-3, 12) for _ in range(rng.randint(1, 12))]
		assert s.firstMissingPositive(list(arr)) == brute(arr)
	print("All tests passed!")
```
