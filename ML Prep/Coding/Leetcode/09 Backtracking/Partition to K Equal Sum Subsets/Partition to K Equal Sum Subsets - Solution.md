---
topic: "Backtracking"
difficulty: Medium
leetcode: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
neetcode: https://neetcode.io/problems/partition-to-k-equal-sum-subsets
---
# Partition to K Equal Sum Subsets - Solution

**Question:** [[Partition to K Equal Sum Subsets - Question]] · **Difficulty:** Medium

## Intuition

The target sum per group is `total / k`. Treat the groups as `k` buckets and assign each number to a bucket by backtracking, never letting a bucket exceed the target. Sorting descending makes dead ends appear early, and skipping buckets whose current sum equals one already tried removes symmetric duplicates (buckets are interchangeable).

## Approach

1. If `total % k != 0` or the largest number exceeds `target = total // k`, return `false`.
2. Sort `nums` descending and set `buckets = [0] * k`.
3. `dfs(i)`: if `i == n`, return `true`.
4. For each bucket: skip if adding `nums[i]` would exceed `target` or a bucket with the same sum was already tried at this level. Otherwise add, recurse, and undo.
5. Return `false` if no placement works.

## Code

```python
from typing import List


class Solution:
	def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
		total = sum(nums)
		if total % k:
			return False
		target = total // k
		nums = sorted(nums, reverse=True)  # large numbers first prune faster
		if nums[0] > target:
			return False
		buckets = [0] * k

		def dfs(i: int) -> bool:
			if i == len(nums):
				return True  # all buckets <= target and total == k * target
			seen = set()
			for b in range(k):
				if buckets[b] in seen or buckets[b] + nums[i] > target:
					continue  # identical bucket states lead to identical subtrees
				seen.add(buckets[b])
				buckets[b] += nums[i]
				if dfs(i + 1):
					return True
				buckets[b] -= nums[i]
			return False

		return dfs(0)
```

## Complexity

- **Time:** `O(k^n)` worst case — each number may try every bucket; symmetry pruning and sorting make it fast for `n <= 16`.
- **Space:** `O(n + k)` — recursion depth and bucket sums.

## Other Approaches

- **Bitmask DP:** `dp[mask]` = sum of the current partially filled group (mod `target`) after using `mask`, valid if reachable — Time `O(n * 2^n)`, Space `O(2^n)`.
- **Fill one group at a time:** backtrack choosing elements (with a `used` mask and memo) until a group hits `target`, then start the next group — Time `O(n * 2^n)` with memoization.

## Key Takeaway

Equal-sum k-partition = bucket backtracking with descending sort + "skip duplicate bucket sums"; mention the `O(n * 2^n)` bitmask DP as the guaranteed-bound alternative.
