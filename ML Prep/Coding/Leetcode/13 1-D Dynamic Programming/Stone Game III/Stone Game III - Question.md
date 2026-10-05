---
topic: "1-D Dynamic Programming"
difficulty: Hard
leetcode: https://leetcode.com/problems/stone-game-iii/
neetcode: https://neetcode.io/problems/stone-game-iii
---
# Stone Game III

**Topic:** [[13 1-D Dynamic Programming|1-D Dynamic Programming]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/stone-game-iii/) · [NeetCode](https://neetcode.io/problems/stone-game-iii)

**Solve it in:** [[Stone Game III]] · **Answer:** [[Stone Game III - Solution]]

## Problem

Alice and Bob play a game with a row of stones; `stoneValue[i]` is the (possibly negative) value of stone `i`. Alice moves first, and players alternate. On each turn, a player takes the first **1, 2, or 3** remaining stones from the left and adds their values to their score. Both scores start at 0, and the game ends when all stones are taken.

Assuming both players play optimally, return `"Alice"` if Alice ends with a higher score, `"Bob"` if Bob does, or `"Tie"` if the scores are equal.

## Examples

**Example 1**
```text
Input: stoneValue = [1,2,3,7]
Output: "Bob"
Explanation: Whatever Alice takes, Bob can grab the 7 and win.
```

**Example 2**
```text
Input: stoneValue = [1,2,3,-9]
Output: "Alice"
Explanation: Alice takes the first three stones (6); Bob is forced to take -9.
```

**Example 3**
```text
Input: stoneValue = [1,2,3,6]
Output: "Tie"
```

## Constraints

- `1 <= stoneValue.length <= 5 * 10^4`
- `-1000 <= stoneValue[i] <= 1000`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def stoneGameIII(self, stoneValue: List[int]) -> str:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.stoneGameIII([1,2,3,7]) == "Bob"
	assert s.stoneGameIII([1,2,3,-9]) == "Alice"
	assert s.stoneGameIII([1,2,3,6]) == "Tie"
	assert s.stoneGameIII([5]) == "Alice"
	assert s.stoneGameIII([-1]) == "Bob"
	assert s.stoneGameIII([0]) == "Tie"
	assert s.stoneGameIII([-1,-2,-3]) == "Tie"
	print("All tests passed!")
```
