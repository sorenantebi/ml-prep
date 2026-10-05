---
topic: "Greedy"
difficulty: Hard
leetcode: https://leetcode.com/problems/candy/
neetcode: https://neetcode.io/problems/candy
---
# Candy - Solution

**Question:** [[Candy - Question]] · **Difficulty:** Hard

## Intuition

Each child has two independent constraints: relative to the left neighbour and relative to the right neighbour. A left-to-right pass satisfies all "higher than left" rules; a right-to-left pass satisfies all "higher than right" rules. Taking the max of the two requirements at each position satisfies both with the minimum count.

## Approach

1. `candies = [1] * n`.
2. Left to right: if `ratings[i] > ratings[i-1]`, `candies[i] = candies[i-1] + 1`.
3. Right to left: if `ratings[i] > ratings[i+1]`, `candies[i] = max(candies[i], candies[i+1] + 1)`.
4. Return `sum(candies)`.

## Code

```python
from typing import List


class Solution:
	def candy(self, ratings: List[int]) -> int:
		n = len(ratings)
		candies = [1] * n
		for i in range(1, n):  # enforce the left-neighbour rule
			if ratings[i] > ratings[i - 1]:
				candies[i] = candies[i - 1] + 1
		for i in range(n - 2, -1, -1):  # enforce the right-neighbour rule, keep the left one
			if ratings[i] > ratings[i + 1]:
				candies[i] = max(candies[i], candies[i + 1] + 1)
		return sum(candies)
```

## Complexity

- **Time:** `O(n)` — two linear passes.
- **Space:** `O(n)` — the candies array.

## Other Approaches

- **Slope counting (one pass, O(1) space):** count lengths of increasing and decreasing runs and add arithmetic-series sums, adjusting the peak — Time `O(n)`, Space `O(1)`.
- **Process children by rating order:** sort indices by rating and assign `1 + max(lower neighbours)` — Time `O(n log n)`, Space `O(n)`.

## Key Takeaway

When a constraint involves both neighbours, solve each direction separately with a sweep and combine with `max`.
