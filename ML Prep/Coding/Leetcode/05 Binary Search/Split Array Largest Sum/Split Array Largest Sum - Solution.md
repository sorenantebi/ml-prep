---
topic: "Binary Search"
difficulty: Hard
leetcode: https://leetcode.com/problems/split-array-largest-sum/
neetcode: https://neetcode.io/problems/split-array-largest-sum
---
# Split Array Largest Sum - Solution

**Question:** [[Split Array Largest Sum - Question]] · **Difficulty:** Hard

## Intuition

Instead of choosing the split points directly, guess the answer `cap` and ask: can we split into at most `k` pieces with every piece sum `<= cap`? A greedy pass answers this, and the answer is monotone in `cap`, so binary search between `max(nums)` and `sum(nums)` finds the smallest feasible cap. (Using fewer than `k` pieces is fine because pieces can always be split further without increasing the max.)

## Approach

1. Search `lo = max(nums)`, `hi = sum(nums)`.
2. Feasibility for `cap`: walk through `nums`, extending the current piece while its sum stays `<= cap`, otherwise start a new piece. Count pieces.
3. If pieces `<= k`, `cap` works — try smaller (`hi = mid`); else `lo = mid + 1`.
4. Return `lo`.

## Code

```python
from typing import List


class Solution:
	def splitArray(self, nums: List[int], k: int) -> int:
		def pieces_needed(cap: int) -> int:
			count, cur = 1, 0
			for x in nums:
				if cur + x > cap:   # close the current piece
					count += 1
					cur = 0
				cur += x
			return count

		lo, hi = max(nums), sum(nums)
		while lo < hi:
			mid = (lo + hi) // 2
			if pieces_needed(mid) <= k:
				hi = mid
			else:
				lo = mid + 1
		return lo
```

## Complexity

- **Time:** `O(n log S)` where `S = sum(nums)` — `log S` greedy checks of `O(n)` each.
- **Space:** `O(1)`.

## Other Approaches

- **DP:** `dp[i][j]` = minimal largest sum splitting the first `i` elements into `j` parts, using prefix sums — Time `O(k · n^2)`, Space `O(k · n)`.

## Key Takeaway

"Minimize the maximum" over contiguous partitions → binary search on the answer with a greedy count; identical to Capacity to Ship Packages.
