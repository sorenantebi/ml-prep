---
topic: "Stack"
difficulty: Easy
leetcode: https://leetcode.com/problems/baseball-game/
neetcode: https://neetcode.io/problems/baseball-game
---
# Baseball Game

**Topic:** [[04 Stack|Stack]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/baseball-game/) · [NeetCode](https://neetcode.io/problems/baseball-game)

**Solve it in:** [[Baseball Game]] · **Answer:** [[Baseball Game - Solution]]

## Problem

You are keeping score for a baseball game with unusual rules. You receive a list of strings `operations`, processed left to right, starting from an empty record of scores. Each operation is one of:

- An integer `x` (as a string): record a new score of `x`.
- `"+"`: record a new score equal to the sum of the previous two scores.
- `"D"`: record a new score equal to double the previous score.
- `"C"`: invalidate (remove) the previous score from the record.

Return the sum of all scores remaining in the record after every operation has been applied. The input is guaranteed to be valid: `"+"` always has at least two prior scores, and `"D"`/`"C"` always have at least one.

## Examples

**Example 1**
```text
Input: operations = ["5","2","C","D","+"]
Output: 30
Explanation: record evolves [5] -> [5,2] -> [5] -> [5,10] -> [5,10,15]; sum = 30
```

**Example 2**
```text
Input: operations = ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation: final record [5,-2,-4,9,5,14]
```

**Example 3**
```text
Input: operations = ["1","C"]
Output: 0
```

## Constraints

- `1 <= operations.length <= 1000`
- `operations[i]` is `"C"`, `"D"`, `"+"`, or an integer string in `[-3 * 10^4, 3 * 10^4]`
- All intermediate values fit in a 32-bit integer
- Operations are always valid

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def calPoints(self, operations: List[str]) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.calPoints(["5", "2", "C", "D", "+"]) == 30
	assert s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27
	assert s.calPoints(["1", "C"]) == 0
	assert s.calPoints(["7"]) == 7
	assert s.calPoints(["-3", "D"]) == -9
	assert s.calPoints(["1", "2", "+", "+", "+"]) == 1 + 2 + 3 + 5 + 8
	assert s.calPoints(["10", "C", "4", "D", "C", "3"]) == 7
	print("All tests passed!")
```
