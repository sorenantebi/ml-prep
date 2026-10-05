---
topic: "1-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/coin-change/
neetcode: https://neetcode.io/problems/coin-change
---
# Coin Change

**Topic:** [[13 1-D Dynamic Programming|1-D Dynamic Programming]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/coin-change/) · [NeetCode](https://neetcode.io/problems/coin-change)

**Solve it in:** [[Coin Change]] · **Answer:** [[Coin Change - Solution]]

## Problem

You have coins of the denominations in `coins` (an unlimited supply of each) and a target `amount`. Return the fewest coins whose values add up to exactly `amount`. If no combination works, return `-1`. An amount of `0` needs `0` coins.

## Examples

**Example 1**
```text
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1.
```

**Example 2**
```text
Input: coins = [2], amount = 3
Output: -1
```

**Example 3**
```text
Input: coins = [1], amount = 0
Output: 0
```

## Constraints

- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10^4`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.coinChange([1,2,5], 11) == 3
	assert s.coinChange([2], 3) == -1
	assert s.coinChange([1], 0) == 0
	assert s.coinChange([186,419,83,408], 6249) == 20
	assert s.coinChange([2,5,10,1], 27) == 4
	assert s.coinChange([3,7], 5) == -1
	assert s.coinChange([1,3,4], 6) == 2
	print("All tests passed!")
```
