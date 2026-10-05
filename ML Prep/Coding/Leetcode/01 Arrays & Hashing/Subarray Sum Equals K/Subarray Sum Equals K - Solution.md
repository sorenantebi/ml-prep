---
topic: "Arrays & Hashing"
difficulty: Medium
leetcode: https://leetcode.com/problems/subarray-sum-equals-k/
neetcode: https://neetcode.io/problems/subarray-sum-equals-k
---
# Subarray Sum Equals K - Solution

**Question:** [[Subarray Sum Equals K - Question]] · **Difficulty:** Medium

## Intuition

Let `prefix[j]` be the sum of the first `j` elements. The subarray `(i, j]` sums to `k` exactly when `prefix[j] - prefix[i] == k`, i.e. `prefix[i] == prefix[j] - k`. Scanning left to right while counting how often each prefix sum has occurred lets us add, at every position, the number of earlier prefixes equal to `current - k`. Sliding windows fail here because negatives break monotonicity.

## Approach

1. Initialize `counts = {0: 1}` (the empty prefix) and `prefix = 0`, `result = 0`.
2. For each `x` in `nums`: `prefix += x`.
3. Add `counts.get(prefix - k, 0)` to `result` (all subarrays ending here with sum `k`).
4. Increment `counts[prefix]`.
5. Return `result`.

## Code

```python
from collections import defaultdict
from typing import List


class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		counts = defaultdict(int)
		counts[0] = 1  # empty prefix: lets subarrays starting at index 0 be counted
		prefix = result = 0
		for x in nums:
			prefix += x
			result += counts[prefix - k]  # earlier prefixes that leave exactly k
			counts[prefix] += 1
		return result
```

## Complexity

- **Time:** `O(n)` — one pass with `O(1)` average hash operations.
- **Space:** `O(n)` — up to `n + 1` distinct prefix sums stored.

## Other Approaches

- **Brute force with running sum:** fix each start and extend the end while accumulating — Time `O(n^2)`, Space `O(1)`.

## Key Takeaway

"Count subarrays with sum k" = prefix sums + a hash map of prefix frequencies, seeded with `{0: 1}`; the same trick handles "sum divisible by k" (store `prefix % k`) and "equal 0s and 1s".
