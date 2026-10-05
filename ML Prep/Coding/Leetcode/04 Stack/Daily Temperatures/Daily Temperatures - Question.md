---
topic: "Stack"
difficulty: Medium
leetcode: https://leetcode.com/problems/daily-temperatures/
neetcode: https://neetcode.io/problems/daily-temperatures
---
# Daily Temperatures

**Topic:** [[04 Stack|Stack]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/daily-temperatures/) · [NeetCode](https://neetcode.io/problems/daily-temperatures)

**Solve it in:** [[Daily Temperatures]] · **Answer:** [[Daily Temperatures - Solution]]

## Problem

Given an integer array `temperatures` of daily temperatures, return an array `answer` where `answer[i]` is the number of days you must wait after day `i` to get a strictly warmer temperature. If no future day is warmer, `answer[i] = 0`.

## Examples

**Example 1**
```text
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

**Example 2**
```text
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

**Example 3**
```text
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

## Constraints

- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
	assert s.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
	assert s.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
	assert s.dailyTemperatures([50]) == [0]
	assert s.dailyTemperatures([90, 80, 70]) == [0, 0, 0]
	assert s.dailyTemperatures([70, 70, 70, 71]) == [3, 2, 1, 0]  # equal is not warmer
	assert s.dailyTemperatures([55, 38, 53, 81, 61, 93, 97, 32, 43, 78]) == [3, 1, 1, 2, 1, 1, 0, 1, 1, 0]
	print("All tests passed!")
```
