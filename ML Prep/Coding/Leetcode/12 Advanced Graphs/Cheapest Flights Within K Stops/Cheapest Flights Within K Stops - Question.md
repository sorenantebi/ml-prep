---
topic: "Advanced Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/cheapest-flights-within-k-stops/
neetcode: https://neetcode.io/problems/cheapest-flight-path
---
# Cheapest Flights Within K Stops

**Topic:** [[12 Advanced Graphs|Advanced Graphs]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/cheapest-flights-within-k-stops/) · [NeetCode](https://neetcode.io/problems/cheapest-flight-path)

**Solve it in:** [[Cheapest Flights Within K Stops]] · **Answer:** [[Cheapest Flights Within K Stops - Solution]]

## Problem

There are `n` cities numbered `0` to `n - 1`, connected by directed flights. `flights[i] = [from_i, to_i, price_i]` is a flight from `from_i` to `to_i` costing `price_i`.

Given `src`, `dst`, and an integer `k`, return the cheapest total price to fly from `src` to `dst` using **at most `k` stops** (i.e. at most `k + 1` flights; intermediate cities count as stops). If no such route exists, return `-1`.

## Examples

**Example 1**
```text
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation: 0 -> 1 -> 3 costs 700. 0 -> 1 -> 2 -> 3 is cheaper (400) but uses 2 stops.
```

**Example 2**
```text
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
```

**Example 3**
```text
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
```

## Constraints

- `1 <= n <= 100`
- `0 <= flights.length <= n * (n - 1) / 2`
- `flights[i].length == 3`, `0 <= from_i, to_i < n`, `from_i != to_i`
- `1 <= price_i <= 10^4`
- No duplicate flights between the same ordered pair.
- `0 <= src, dst, k < n`, `src != dst`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1) == 700
	assert s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1) == 200
	assert s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0) == 500
	assert s.findCheapestPrice(3, [[0,1,100]], 0, 2, 1) == -1
	assert s.findCheapestPrice(4, [[0,1,1],[1,2,1],[2,3,1],[0,3,10]], 0, 3, 2) == 3
	assert s.findCheapestPrice(4, [[0,1,1],[1,2,1],[2,3,1],[0,3,10]], 0, 3, 1) == 10
	assert s.findCheapestPrice(2, [], 0, 1, 0) == -1
	print("All tests passed!")
```
