---
topic: "2-D Dynamic Programming"
difficulty: Hard
leetcode: https://leetcode.com/problems/burst-balloons/
neetcode: https://neetcode.io/problems/burst-balloons
---
# Burst Balloons

**Topic:** [[14 2-D Dynamic Programming|2-D Dynamic Programming]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/burst-balloons/) · [NeetCode](https://neetcode.io/problems/burst-balloons)

**Solve it in:** [[Burst Balloons]] · **Answer:** [[Burst Balloons - Solution]]

## Problem

There are `n` balloons in a row, balloon `i` painted with the number `nums[i]`. When you burst balloon `i`, you earn `nums[left] * nums[i] * nums[right]` coins, where `left` and `right` are the balloons currently adjacent to `i` (after earlier bursts have closed the gaps). If a neighbour does not exist (past either end), treat it as a balloon with value `1`.

Burst all balloons in some order and return the maximum total coins you can collect.

## Examples

**Example 1**
```text
Input: nums = [3,1,5,8]
Output: 167
Explanation: burst 1, 5, 3, 8 -> 3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 15 + 120 + 24 + 8 = 167
```

**Example 2**
```text
Input: nums = [1,5]
Output: 10
```

## Constraints

- `1 <= nums.length <= 300`
- `0 <= nums[i] <= 100`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def maxCoins(self, nums: List[int]) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.maxCoins([3, 1, 5, 8]) == 167
	assert s.maxCoins([1, 5]) == 10
	assert s.maxCoins([7]) == 7
	assert s.maxCoins([0]) == 0
	assert s.maxCoins([2, 3]) == 9  # burst 2 (1*2*3=6), then 3 (1*3*1=3)
	assert s.maxCoins([1, 1, 1]) == 3
	assert s.maxCoins([0, 0, 5]) == 5
	print("All tests passed!")
```
