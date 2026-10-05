---
topic: "2-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/stone-game/
neetcode: https://neetcode.io/problems/stone-game
---
# Stone Game

**Topic:** [[14 2-D Dynamic Programming|2-D Dynamic Programming]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/stone-game/) · [NeetCode](https://neetcode.io/problems/stone-game)

**Solve it in:** [[Stone Game]] · **Answer:** [[Stone Game - Solution]]

## Problem

There is a row of an **even** number of piles of stones, `piles[i]` stones in pile `i`. The **total** number of stones is **odd**, so there are no ties. Alice and Bob alternate turns, Alice first. On each turn a player takes the whole pile from either the **left end** or the **right end** of the row. When no piles are left, the player with more stones wins.

Assuming both play optimally, return `true` if Alice wins and `false` if Bob wins.

## Examples

**Example 1**
```text
Input: piles = [5,3,4,5]
Output: true
Explanation: Alice takes 5 (left); whatever Bob does, Alice ends with 10 vs Bob's 7 or better.
```

**Example 2**
```text
Input: piles = [3,7,2,3]
Output: true
```

## Constraints

- `2 <= piles.length <= 500`
- `piles.length` is even
- `1 <= piles[i] <= 500`
- `sum(piles)` is odd

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def stoneGame(self, piles: List[int]) -> bool:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.stoneGame([5, 3, 4, 5]) is True
	assert s.stoneGame([3, 7, 2, 3]) is True
	assert s.stoneGame([1, 2]) is True
	assert s.stoneGame([2, 1]) is True
	assert s.stoneGame([1, 100, 2, 4]) is True
	assert s.stoneGame([7, 8, 8, 10]) is True
	assert s.stoneGame([3, 2, 10, 4]) is True
	print("All tests passed!")
```
