---
topic: "Greedy"
difficulty: Easy
leetcode: https://leetcode.com/problems/lemonade-change/
neetcode: https://neetcode.io/problems/lemonade-change
---
# Lemonade Change

**Topic:** [[15 Greedy|Greedy]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/lemonade-change/) · [NeetCode](https://neetcode.io/problems/lemonade-change)

**Solve it in:** [[Lemonade Change]] · **Answer:** [[Lemonade Change - Solution]]

## Problem

At a lemonade stand each lemonade costs `$5`. Customers stand in a queue and buy one lemonade each, in the order given by `bills`. Each customer pays with a single `$5`, `$10`, or `$20` bill, and you must give back correct change so that each customer effectively pays `$5`.

You start with no money at all. Return `true` if you can give every customer correct change, otherwise `false`.

## Examples

**Example 1**
```text
Input: bills = [5,5,5,10,20]
Output: true
Explanation: Collect three $5s, give one back for the $10, then give $10 + $5 for the $20.
```

**Example 2**
```text
Input: bills = [5,5,10,10,20]
Output: false
Explanation: For the final $20 you hold two $10s but no $5, so you cannot make $15.
```

## Constraints

- `1 <= bills.length <= 10^5`
- `bills[i]` is `5`, `10`, or `20`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def lemonadeChange(self, bills: List[int]) -> bool:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.lemonadeChange([5, 5, 5, 10, 20]) is True
	assert s.lemonadeChange([5, 5, 10, 10, 20]) is False
	assert s.lemonadeChange([10]) is False
	assert s.lemonadeChange([5]) is True
	assert s.lemonadeChange([5, 20]) is False
	assert s.lemonadeChange([5, 5, 5, 20]) is True  # three $5s as change
	assert s.lemonadeChange([5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]) is True
	print("All tests passed!")
```
