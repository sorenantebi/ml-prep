---
topic: "Greedy"
difficulty: Medium
leetcode: https://leetcode.com/problems/jump-game/
neetcode: https://neetcode.io/problems/jump-game
---
# Jump Game

**Topic:** [[15 Greedy|Greedy]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/jump-game/) · [NeetCode](https://neetcode.io/problems/jump-game)

**Solve it in:** [[Jump Game]] · **Answer:** [[Jump Game - Solution]]

## Problem

You are given an integer array `nums`. You start at index `0`, and `nums[i]` is the **maximum** jump length from index `i` (you may jump any distance from `0` up to `nums[i]`). Return `true` if you can reach the last index, otherwise `false`.

## Examples

**Example 1**
```text
Input: nums = [2,3,1,1,4]
Output: true
Explanation: 0 -> 1 -> 4
```

**Example 2**
```text
Input: nums = [3,2,1,0,4]
Output: false
Explanation: Every path lands on index 3, whose jump length is 0.
```

## Constraints

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def canJump(self, nums: List[int]) -> bool:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.canJump([2, 3, 1, 1, 4]) is True
	assert s.canJump([3, 2, 1, 0, 4]) is False
	assert s.canJump([0]) is True  # already at the last index
	assert s.canJump([0, 1]) is False
	assert s.canJump([1, 0]) is True
	assert s.canJump([2, 0, 0]) is True
	assert s.canJump([1, 1, 0, 1]) is False
	assert s.canJump([5, 0, 0, 0, 0, 0]) is True
	print("All tests passed!")
```
