---
topic: "Two Pointers"
difficulty: Medium
leetcode: https://leetcode.com/problems/container-with-most-water/
neetcode: https://neetcode.io/problems/max-water-container
---
# Container With Most Water

**Topic:** [[02 Two Pointers|Two Pointers]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/container-with-most-water/) · [NeetCode](https://neetcode.io/problems/max-water-container)

**Solve it in:** [[Container With Most Water]] · **Answer:** [[Container With Most Water - Solution]]

## Problem

You are given an integer array `height` of length `n`. Picture `n` vertical lines where line `i` goes from `(i, 0)` up to `(i, height[i])`. Choose two lines that, together with the x-axis, form a container; the water it holds is `min(height[i], height[j]) * (j - i)`. Return the maximum amount of water any such container can hold. The container may not be tilted.

## Examples

**Example 1**
```text
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: lines at index 1 (8) and 8 (7): min(8,7) * 7 = 49
```

**Example 2**
```text
Input: height = [1,1]
Output: 1
```

## Constraints

- `2 <= height.length <= 10^5`
- `0 <= height[i] <= 10^4`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def maxArea(self, height: List[int]) -> int:
		pass  # your code here


if __name__ == "__main__":
	sol = Solution()
	assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
	assert sol.maxArea([1, 1]) == 1
	assert sol.maxArea([0, 0]) == 0
	assert sol.maxArea([4, 3, 2, 1, 4]) == 16
	assert sol.maxArea([1, 2, 1]) == 2
	assert sol.maxArea([1, 2, 4, 3]) == 4
	assert sol.maxArea([2, 3, 10, 5, 7, 8, 9]) == 36
	print("All tests passed!")
```
