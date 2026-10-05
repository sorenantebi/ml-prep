---
topic: "Backtracking"
difficulty: Easy
leetcode: https://leetcode.com/problems/sum-of-all-subset-xor-totals/
neetcode: https://neetcode.io/problems/sum-of-all-subset-xor-totals
---
# Sum of All Subsets XOR Total - Solution

**Question:** [[Sum of All Subsets XOR Total - Question]] · **Difficulty:** Easy

## Intuition

The backtracking view: every element is either included or excluded, giving a binary decision tree whose `2^n` leaves are the subsets — accumulate the running XOR along each path and sum the leaves. The math shortcut: for any bit that appears in at least one number, exactly **half** of the `2^n` subsets have that bit set in their XOR. So the answer is `(OR of all nums) * 2^(n-1)`.

## Approach

1. Compute `acc = nums[0] | nums[1] | ... | nums[n-1]` — the set of bits that can ever appear.
2. Each such bit is set in the XOR of exactly `2^(n-1)` subsets, contributing `bit * 2^(n-1)`.
3. Return `acc << (n - 1)`.

## Code

```python
from typing import List


class Solution:
	def subsetXORSum(self, nums: List[int]) -> int:
		acc = 0
		for x in nums:
			acc |= x
		# every bit present in some element is "on" in exactly half of all subsets
		return acc << (len(nums) - 1)

	def subsetXORSumBacktrack(self, nums: List[int]) -> int:
		# include/exclude DFS: the classic backtracking formulation
		def dfs(i: int, cur: int) -> int:
			if i == len(nums):
				return cur
			return dfs(i + 1, cur ^ nums[i]) + dfs(i + 1, cur)
		return dfs(0, 0)
```

## Complexity

- **Time:** `O(n)` — one pass to OR the numbers (the DFS version is `O(2^n)`).
- **Space:** `O(1)` (the DFS version uses `O(n)` recursion stack).

## Other Approaches

- **Backtracking (include/exclude DFS):** shown above as `subsetXORSumBacktrack` — Time `O(2^n)`, Space `O(n)` recursion.
- **Enumerate bitmasks:** loop `mask` over `0..2^n - 1` and XOR the selected elements — Time `O(n * 2^n)`, Space `O(1)`.

## Key Takeaway

Subset enumeration is the include/exclude decision tree; for aggregate questions over all subsets, think per-bit — a bit present anywhere is set in exactly half the subsets' XORs.
