---
topic: "Intervals"
difficulty: Hard
leetcode: https://leetcode.com/problems/minimum-interval-to-include-each-query/
neetcode: https://neetcode.io/problems/minimum-interval-including-query
---
# Minimum Interval to Include Each Query

**Topic:** [[16 Intervals|Intervals]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/minimum-interval-to-include-each-query/) · [NeetCode](https://neetcode.io/problems/minimum-interval-including-query)

**Solve it in:** [[Minimum Interval to Include Each Query]] · **Answer:** [[Minimum Interval to Include Each Query - Solution]]

## Problem

You are given a 2D array `intervals` where `intervals[i] = [left_i, right_i]` describes the inclusive integer interval from `left_i` to `right_i`; its size is `right_i - left_i + 1`. You are also given an array `queries`. For each `queries[j]`, find the size of the **smallest** interval `i` with `left_i <= queries[j] <= right_i`, or `-1` if no interval contains it. Return an array of answers in the same order as `queries`.

## Examples

**Example 1**
```text
Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
Explanation: 2 → [2,4] (size 3); 3 → [2,4] (size 3); 4 → [4,4] (size 1); 5 → [3,6] (size 4).
```

**Example 2**
```text
Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2,-1,4,6]
```

## Constraints

- `1 <= intervals.length <= 10^5`
- `1 <= queries.length <= 10^5`
- `intervals[i].length == 2`, `1 <= left_i <= right_i <= 10^7`
- `1 <= queries[j] <= 10^7`

## Starter Code & Test Cases

```python
from typing import List
import heapq


class Solution:
	def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]) == [3, 3, 1, 4]
	assert s.minInterval([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]) == [2, -1, 4, 6]
	assert s.minInterval([[1, 1]], [1, 2]) == [1, -1]
	assert s.minInterval([[5, 10]], [4, 5, 10, 11]) == [-1, 6, 6, -1]
	assert s.minInterval([[1, 10], [3, 3]], [3, 3, 2]) == [1, 1, 10]   # duplicate queries

	# randomized check against brute force
	import random
	random.seed(11)
	for _ in range(200):
		iv = []
		for _ in range(random.randint(1, 12)):
			a = random.randint(1, 40)
			iv.append([a, a + random.randint(0, 15)])
		qs = [random.randint(1, 60) for _ in range(random.randint(1, 12))]
		brute = [min((r - l + 1 for l, r in iv if l <= q <= r), default=-1) for q in qs]
		assert s.minInterval([x[:] for x in iv], qs[:]) == brute
	print("All tests passed!")
```
