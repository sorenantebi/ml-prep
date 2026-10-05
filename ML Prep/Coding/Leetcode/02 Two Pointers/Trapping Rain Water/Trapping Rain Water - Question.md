---
topic: "Two Pointers"
difficulty: Hard
leetcode: https://leetcode.com/problems/trapping-rain-water/
neetcode: https://neetcode.io/problems/trapping-rain-water
---
# Trapping Rain Water

**Topic:** [[02 Two Pointers|Two Pointers]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/trapping-rain-water/) · [NeetCode](https://neetcode.io/problems/trapping-rain-water)

**Solve it in:** [[Trapping Rain Water]] · **Answer:** [[Trapping Rain Water - Solution]]

## Problem

You are given `n` non-negative integers `height` describing an elevation map where every bar has width `1`. After rain, water collects in the dips between bars. Compute the total units of water trapped. The water above position `i` is `min(max height to its left, max height to its right) - height[i]`, if positive.

## Examples

**Example 1**
```text
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

**Example 2**
```text
Input: height = [4,2,0,3,2,5]
Output: 9
```

## Constraints

- `1 <= height.length <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def trap(self, height: List[int]) -> int:
		pass  # your code here


if __name__ == "__main__":
	sol = Solution()
	assert sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
	assert sol.trap([4, 2, 0, 3, 2, 5]) == 9
	assert sol.trap([5]) == 0
	assert sol.trap([1, 2, 3, 4]) == 0
	assert sol.trap([4, 3, 2, 1]) == 0
	assert sol.trap([3, 0, 3]) == 3
	assert sol.trap([5, 1, 1, 1, 5]) == 12
	assert sol.trap([2, 0, 2, 0, 1]) == 3
	print("All tests passed!")
```
