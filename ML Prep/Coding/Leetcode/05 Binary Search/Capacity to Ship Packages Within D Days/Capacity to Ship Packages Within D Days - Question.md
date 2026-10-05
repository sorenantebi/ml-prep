---
topic: "Binary Search"
difficulty: Medium
leetcode: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
neetcode: https://neetcode.io/problems/capacity-to-ship-packages-within-d-days
---
# Capacity to Ship Packages Within D Days

**Topic:** [[05 Binary Search|Binary Search]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) · [NeetCode](https://neetcode.io/problems/capacity-to-ship-packages-within-d-days)

**Solve it in:** [[Capacity to Ship Packages Within D Days]] · **Answer:** [[Capacity to Ship Packages Within D Days - Solution]]

## Problem

A conveyor belt carries packages that must be shipped from one port to another within `days` days. Package `i` weighs `weights[i]`. Each day, the ship is loaded with packages in the given order (no reordering) and may not carry more total weight than its capacity.

Return the minimum ship capacity that allows all packages to be shipped within `days` days.

## Examples

**Example 1**
```text
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: [1,2,3,4,5], [6,7], [8], [9], [10]
```

**Example 2**
```text
Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: [3,2], [2,4], [1,4]
```

**Example 3**
```text
Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation: [1], [2], [3], [1,1]
```

## Constraints

- `1 <= days <= weights.length <= 5 * 10^4`
- `1 <= weights[i] <= 500`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def shipWithinDays(self, weights: List[int], days: int) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15
	assert s.shipWithinDays([3, 2, 2, 4, 1, 4], 3) == 6
	assert s.shipWithinDays([1, 2, 3, 1, 1], 4) == 3
	assert s.shipWithinDays([7], 1) == 7
	assert s.shipWithinDays([5, 5, 5, 5], 1) == 20     # everything in one day
	assert s.shipWithinDays([5, 5, 5, 5], 4) == 5      # one package per day
	assert s.shipWithinDays([1, 1, 1, 10], 2) == 10    # capacity at least max weight
	print("All tests passed!")
```
