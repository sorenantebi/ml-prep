---
topic: "Two Pointers"
difficulty: Medium
leetcode: https://leetcode.com/problems/boats-to-save-people/
neetcode: https://neetcode.io/problems/boats-to-save-people
---
# Boats to Save People - Solution

**Question:** [[Boats to Save People - Question]] · **Difficulty:** Medium

## Intuition

The heaviest person must ride in some boat; the best partner for them (if any) is the lightest person, because if even the lightest cannot fit, nobody can. Pairing heaviest with lightest when possible never hurts, so sort and use two pointers from both ends.

## Approach

1. Sort `people`.
2. Set `l = 0`, `r = n - 1`, `boats = 0`.
3. While `l <= r`:
   - If `people[l] + people[r] <= limit`, the lightest joins: `l += 1`.
   - The heaviest always leaves: `r -= 1`, `boats += 1`.
4. Return `boats`.

## Code

```python
from typing import List


class Solution:
	def numRescueBoats(self, people: List[int], limit: int) -> int:
		people.sort()
		l, r = 0, len(people) - 1
		boats = 0
		while l <= r:
			if people[l] + people[r] <= limit:
				l += 1  # lightest shares the boat with the heaviest
			r -= 1      # heaviest always departs
			boats += 1
		return boats
```

## Complexity

- **Time:** `O(n log n)` — dominated by sorting; the scan is `O(n)`.
- **Space:** `O(1)` extra (or `O(n)` for the sort, depending on implementation).

## Other Approaches

- **Counting sort:** since weights are bounded by `limit`, bucket-count then run the same two-pointer logic over buckets — Time `O(n + limit)`, Space `O(limit)`.

## Key Takeaway

Greedy pairing of extremes (heaviest with lightest) after sorting is a common exchange-argument pattern for "at most two per group" problems.
