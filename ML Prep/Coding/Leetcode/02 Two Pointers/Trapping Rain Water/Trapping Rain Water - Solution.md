---
topic: "Two Pointers"
difficulty: Hard
leetcode: https://leetcode.com/problems/trapping-rain-water/
neetcode: https://neetcode.io/problems/trapping-rain-water
---
# Trapping Rain Water - Solution

**Question:** [[Trapping Rain Water - Question]] · **Difficulty:** Hard

## Intuition

Water above a bar depends on the smaller of the tallest bars to its left and right. With two pointers, track `leftMax` and `rightMax`. Whichever side has the smaller max is the bottleneck: the opposite side is already known to have something at least as tall, so the water at the smaller side's pointer is fully determined and can be added immediately.

## Approach

1. Set `l = 0`, `r = n - 1`, `leftMax = height[l]`, `rightMax = height[r]`, `water = 0`.
2. While `l < r`:
   - If `leftMax < rightMax`: move `l` right, update `leftMax = max(leftMax, height[l])`, add `leftMax - height[l]`.
   - Else: move `r` left, update `rightMax`, add `rightMax - height[r]`.
3. Return `water`.

## Code

```python
from typing import List


class Solution:
	def trap(self, height: List[int]) -> int:
		l, r = 0, len(height) - 1
		left_max, right_max = height[l], height[r]
		water = 0
		while l < r:
			if left_max < right_max:
				# left side is the bottleneck, so water at l is decided
				l += 1
				left_max = max(left_max, height[l])
				water += left_max - height[l]
			else:
				r -= 1
				right_max = max(right_max, height[r])
				water += right_max - height[r]
		return water
```

## Complexity

- **Time:** `O(n)` — each index is visited once.
- **Space:** `O(1)` — only a few running values.

## Other Approaches

- **Prefix/suffix max arrays:** precompute `maxLeft[i]` and `maxRight[i]`, sum `min(...) - height[i]` — Time `O(n)`, Space `O(n)`.
- **Monotonic stack:** pop shorter bars and fill horizontal layers between boundaries — Time `O(n)`, Space `O(n)`.

## Key Takeaway

When an answer depends on `min(leftMax, rightMax)`, process from the side with the smaller max: that side's value is final, which turns an `O(n)`-space solution into `O(1)`.
