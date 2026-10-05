---
topic: "Advanced Graphs"
difficulty: Hard
leetcode: https://leetcode.com/problems/greatest-common-divisor-traversal/
neetcode: https://neetcode.io/problems/greatest-common-divisor-traversal
---
# Greatest Common Divisor Traversal

**Topic:** [[12 Advanced Graphs|Advanced Graphs]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/greatest-common-divisor-traversal/) · [NeetCode](https://neetcode.io/problems/greatest-common-divisor-traversal)

**Solve it in:** [[Greatest Common Divisor Traversal]] · **Answer:** [[Greatest Common Divisor Traversal - Solution]]

## Problem

You are given a 0-indexed integer array `nums`. You may move directly between indices `i` and `j` (`i != j`) if and only if `gcd(nums[i], nums[j]) > 1`.

Return `true` if, for **every** pair of indices `i < j`, there is some sequence of moves that gets from `i` to `j`; otherwise return `false`.

## Examples

**Example 1**
```text
Input: nums = [2,3,6]
Output: true
Explanation: 0 <-> 2 (gcd 2) and 1 <-> 2 (gcd 3), so all indices are connected.
```

**Example 2**
```text
Input: nums = [3,9,5]
Output: false
Explanation: 5 shares no factor with 3 or 9.
```

**Example 3**
```text
Input: nums = [4,3,12,8]
Output: true
```

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def canTraverseAllPairs(self, nums: List[int]) -> bool:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.canTraverseAllPairs([2,3,6]) is True
	assert s.canTraverseAllPairs([3,9,5]) is False
	assert s.canTraverseAllPairs([4,3,12,8]) is True
	assert s.canTraverseAllPairs([1]) is True
	assert s.canTraverseAllPairs([1,1]) is False
	assert s.canTraverseAllPairs([5,5]) is True
	assert s.canTraverseAllPairs([2,4,1]) is False
	assert s.canTraverseAllPairs([10,21,35,6]) is True
	assert s.canTraverseAllPairs([99991, 99989]) is False
	print("All tests passed!")
```
