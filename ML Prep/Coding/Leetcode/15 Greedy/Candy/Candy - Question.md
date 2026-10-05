---
topic: "Greedy"
difficulty: Hard
leetcode: https://leetcode.com/problems/candy/
neetcode: https://neetcode.io/problems/candy
---
# Candy

**Topic:** [[15 Greedy|Greedy]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/candy/) · [NeetCode](https://neetcode.io/problems/candy)

**Solve it in:** [[Candy]] · **Answer:** [[Candy - Solution]]

## Problem

`n` children stand in a line, each with a rating given in the array `ratings`. You hand out candies such that:

- every child gets at least one candy, and
- a child with a strictly higher rating than an adjacent neighbour gets more candies than that neighbour.

Return the minimum total number of candies required. (Equal neighbours have no constraint between them.)

## Examples

**Example 1**
```text
Input: ratings = [1,0,2]
Output: 5
Explanation: Candies [2,1,2].
```

**Example 2**
```text
Input: ratings = [1,2,2]
Output: 4
Explanation: Candies [1,2,1]; the third child only needs 1 since equal ratings impose nothing.
```

## Constraints

- `n == ratings.length`
- `1 <= n <= 2 * 10^4`
- `0 <= ratings[i] <= 2 * 10^4`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def candy(self, ratings: List[int]) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.candy([1, 0, 2]) == 5
	assert s.candy([1, 2, 2]) == 4
	assert s.candy([5]) == 1
	assert s.candy([3, 3, 3]) == 3
	assert s.candy([1, 2, 3, 4]) == 10
	assert s.candy([4, 3, 2, 1]) == 10
	assert s.candy([1, 3, 2, 2, 1]) == 7
	assert s.candy([1, 2, 87, 87, 87, 2, 1]) == 13
	print("All tests passed!")
```
