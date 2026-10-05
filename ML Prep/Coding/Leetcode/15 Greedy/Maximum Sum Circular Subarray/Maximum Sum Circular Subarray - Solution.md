---
topic: "Greedy"
difficulty: Medium
leetcode: https://leetcode.com/problems/maximum-sum-circular-subarray/
neetcode: https://neetcode.io/problems/maximum-sum-circular-subarray
---
# Maximum Sum Circular Subarray - Solution

**Question:** [[Maximum Sum Circular Subarray - Question]] · **Difficulty:** Medium

## Intuition

A maximum circular subarray is either a normal (non-wrapping) subarray — found by Kadane's — or it wraps around, in which case its complement is a contiguous middle subarray with **minimum** sum, so the wrapping sum is `total - min_subarray`. Edge case: if every number is negative, the "wrap" would be empty (`total - total = 0`), so return the plain max instead.

## Approach

1. In one pass, run Kadane for both the max subarray (`cur_max`, `best_max`) and the min subarray (`cur_min`, `best_min`), and accumulate `total`.
2. If `best_max < 0`, all elements are negative: return `best_max`.
3. Otherwise return `max(best_max, total - best_min)`.

## Code

```python
from typing import List


class Solution:
	def maxSubarraySumCircular(self, nums: List[int]) -> int:
		total = 0
		cur_max = cur_min = 0
		best_max, best_min = nums[0], nums[0]
		for x in nums:
			cur_max = max(x, cur_max + x)
			best_max = max(best_max, cur_max)
			cur_min = min(x, cur_min + x)
			best_min = min(best_min, cur_min)
			total += x
		if best_max < 0:  # all negative: wrapping would mean an empty subarray
			return best_max
		return max(best_max, total - best_min)  # wrap = total minus the min middle part
```

## Complexity

- **Time:** `O(n)` — one pass.
- **Space:** `O(1)` — a few running values.

## Other Approaches

- **Prefix sums + monotonic deque over the doubled array:** max of `P[j] - P[i]` with `j - i <= n` — Time `O(n)`, Space `O(n)`.
- **Brute force:** Kadane from every starting rotation — Time `O(n^2)`, Space `O(1)`.

## Key Takeaway

Circular max subarray = max(normal Kadane, total - min Kadane), with the all-negative guard.
