---
topic: "Arrays & Hashing"
difficulty: Medium
leetcode: https://leetcode.com/problems/top-k-frequent-elements/
neetcode: https://neetcode.io/problems/top-k-elements-in-list
---
# Top K Frequent Elements

**Topic:** [[01 Arrays & Hashing|Arrays & Hashing]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/top-k-frequent-elements/) · [NeetCode](https://neetcode.io/problems/top-k-elements-in-list)

**Solve it in:** [[Top K Frequent Elements]] · **Answer:** [[Top K Frequent Elements - Solution]]

## Problem

Given an integer array `nums` and an integer `k`, return the `k` values that occur most often in `nums`. The answer may be returned in any order. The input guarantees that the answer is unique (there is no tie at the boundary of the top `k`).

## Examples

**Example 1**
```text
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2**
```text
Input: nums = [1], k = 1
Output: [1]
```

**Example 3**
```text
Input: nums = [4,4,-1,-1,-1,7], k = 1
Output: [-1]
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is between `1` and the number of distinct values in `nums`.
- The answer is guaranteed to be unique.
- Follow-up: your algorithm should be better than `O(n log n)`.

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert sorted(s.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
	assert sorted(s.topKFrequent([1], 1)) == [1]
	assert sorted(s.topKFrequent([4, 4, -1, -1, -1, 7], 1)) == [-1]
	assert sorted(s.topKFrequent([5, 6, 7], 3)) == [5, 6, 7]
	assert sorted(s.topKFrequent([3, 0, 1, 0], 1)) == [0]
	assert sorted(s.topKFrequent([2, 2, 3, 3, 3, 4, 4, 4, 4], 2)) == [3, 4]
	big = [i for i in range(1, 101) for _ in range(i)]  # value i appears i times
	assert sorted(s.topKFrequent(big, 5)) == [96, 97, 98, 99, 100]
	print("All tests passed!")
```
