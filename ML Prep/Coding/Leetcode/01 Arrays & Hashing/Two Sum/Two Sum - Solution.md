---
topic: "Arrays & Hashing"
difficulty: Easy
leetcode: https://leetcode.com/problems/two-sum/
neetcode: https://neetcode.io/problems/two-integer-sum
---
# Two Sum - Solution

**Question:** [[Two Sum - Question]] · **Difficulty:** Easy

## Intuition

For each number `x`, the partner we need is `target - x`. If we store every value we have already passed together with its index in a hash map, we can check in `O(1)` whether the partner appeared earlier, turning the quadratic pair search into one pass.

## Approach

1. Create an empty dict `index_of` mapping value to index.
2. Iterate over `nums` with index `i` and value `x`.
3. Compute `need = target - x`; if `need` is in `index_of`, return `[index_of[need], i]`.
4. Otherwise store `index_of[x] = i` and continue.

## Code

```python
from typing import List


class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		index_of = {}  # value -> index of an earlier occurrence
		for i, x in enumerate(nums):
			need = target - x
			if need in index_of:  # look up before inserting so we never reuse x itself
				return [index_of[need], i]
			index_of[x] = i
		return []  # unreachable: a solution is guaranteed
```

## Complexity

- **Time:** `O(n)` — single pass with `O(1)` average hash lookups.
- **Space:** `O(n)` — the dict can store up to `n` entries.

## Other Approaches

- **Brute force:** check every pair `(i, j)` — Time `O(n^2)`, Space `O(1)`.
- **Sort + two pointers:** sort `(value, index)` pairs and move pointers inward — Time `O(n log n)`, Space `O(n)`.

## Key Takeaway

"Find a complement" problems become one-pass with a hash map from value to index; check for the complement before inserting the current element.
