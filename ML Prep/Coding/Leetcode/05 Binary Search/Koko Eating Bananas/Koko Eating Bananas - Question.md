---
topic: "Binary Search"
difficulty: Medium
leetcode: https://leetcode.com/problems/koko-eating-bananas/
neetcode: https://neetcode.io/problems/eating-bananas
---
# Koko Eating Bananas

**Topic:** [[05 Binary Search|Binary Search]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/koko-eating-bananas/) · [NeetCode](https://neetcode.io/problems/eating-bananas)

**Solve it in:** [[Koko Eating Bananas]] · **Answer:** [[Koko Eating Bananas - Solution]]

## Problem

Koko has `n` piles of bananas; pile `i` has `piles[i]` bananas. The guards return in `h` hours.

Koko picks an integer eating speed `k` (bananas per hour). Each hour she chooses one pile and eats `k` bananas from it; if the pile has fewer than `k` bananas, she finishes that pile and eats nothing more during that hour.

She wants to eat as slowly as possible while still finishing every banana within `h` hours. Return the minimum integer `k` that makes this possible.

## Examples

**Example 1**
```text
Input: piles = [3,6,7,11], h = 8
Output: 4
```

**Example 2**
```text
Input: piles = [30,11,23,4,20], h = 5
Output: 30
Explanation: one pile per hour requires eating the largest pile in one hour
```

**Example 3**
```text
Input: piles = [30,11,23,4,20], h = 6
Output: 23
```

## Constraints

- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def minEatingSpeed(self, piles: List[int], h: int) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.minEatingSpeed([3, 6, 7, 11], 8) == 4
	assert s.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
	assert s.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
	assert s.minEatingSpeed([1], 1) == 1
	assert s.minEatingSpeed([10], 3) == 4
	assert s.minEatingSpeed([1, 1, 1, 1], 10) == 1
	assert s.minEatingSpeed([10**9], 2) == 5 * 10**8
	assert s.minEatingSpeed([312884470], 312884469) == 2
	print("All tests passed!")
```
