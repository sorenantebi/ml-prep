---
topic: "Greedy"
difficulty: Easy
leetcode: https://leetcode.com/problems/lemonade-change/
neetcode: https://neetcode.io/problems/lemonade-change
---
# Lemonade Change - Solution

**Question:** [[Lemonade Change - Question]] · **Difficulty:** Easy

## Intuition

Only the counts of `$5` and `$10` bills matter (`$20`s are never usable as change). `$5` bills are the most flexible, so when giving `$15` change prefer `$10 + $5` over three `$5`s.

## Approach

1. Keep counters `five` and `ten`.
2. For each bill:
   - `$5`: `five += 1`.
   - `$10`: need one `$5`; `five -= 1`, `ten += 1`.
   - `$20`: if `ten > 0 and five > 0` use one of each; else if `five >= 3` use three `$5`s; else return `False`.
   - If `five` goes negative, return `False`.
3. Return `True`.

## Code

```python
from typing import List


class Solution:
	def lemonadeChange(self, bills: List[int]) -> bool:
		five = ten = 0
		for b in bills:
			if b == 5:
				five += 1
			elif b == 10:
				five -= 1
				ten += 1
			elif ten > 0:  # $20: greedily spend the less useful $10 first
				ten -= 1
				five -= 1
			else:
				five -= 3
			if five < 0:
				return False
		return True
```

## Complexity

- **Time:** `O(n)` — single pass.
- **Space:** `O(1)` — two counters.

## Other Approaches

- **Simulate a cash drawer with a sorted multiset:** pick largest bills first for change — Time `O(n log n)`, Space `O(n)`; unnecessary given only three denominations.

## Key Takeaway

Greedy change-making: preserve the most versatile resource (`$5`) by spending larger, less flexible denominations first.
