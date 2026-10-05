---
topic: "Heap / Priority Queue"
difficulty: Medium
leetcode: https://leetcode.com/problems/single-threaded-cpu/
neetcode: https://neetcode.io/problems/single-threaded-cpu
---
# Single Threaded CPU

**Topic:** [[08 Heap - Priority Queue|Heap / Priority Queue]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/single-threaded-cpu/) · [NeetCode](https://neetcode.io/problems/single-threaded-cpu)

**Solve it in:** [[Single Threaded CPU]] · **Answer:** [[Single Threaded CPU - Solution]]

## Problem

There are `n` tasks numbered `0` to `n - 1`, given as `tasks[i] = [enqueueTime_i, processingTime_i]`: task `i` becomes available at time `enqueueTime_i` and takes `processingTime_i` units to finish once started.

A single-threaded CPU processes at most one task at a time, without interruption, using this rule:

- If the CPU is idle and nothing is available, it stays idle until a task becomes available.
- If the CPU is idle and tasks are available, it picks the one with the **shortest processing time**; ties are broken by the **smallest index**.
- A task finishing and a new task starting can happen at the same instant.

Return the order (list of indices) in which the CPU processes the tasks.

## Examples

**Example 1**
```text
Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]
Explanation: t=1 run 0 (ends 3); t=3 pick 2 over 1 (shorter); t=5 pick 3; t=6 run 1
```

**Example 2**
```text
Input: tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
Output: [4,3,2,0,1]
Explanation: everything arrives at t=7, so tasks run in order of processing time
```

## Constraints

- `1 <= n <= 10^5`
- `1 <= enqueueTime_i, processingTime_i <= 10^9`

## Starter Code & Test Cases

```python
from typing import List
import heapq


class Solution:
	def getOrder(self, tasks: List[List[int]]) -> List[int]:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]) == [0, 2, 3, 1]
	assert s.getOrder([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]) == [4, 3, 2, 0, 1]
	assert s.getOrder([[5, 3]]) == [0]
	# tie on processing time -> lower index first
	assert s.getOrder([[1, 3], [1, 3], [1, 3]]) == [0, 1, 2]
	# idle gap: the CPU jumps ahead to the next enqueue time
	assert s.getOrder([[1, 1], [100, 2], [100, 1]]) == [0, 2, 1]
	# a long task arriving first still runs first because nothing else is available
	assert s.getOrder([[1, 10], [2, 1], [3, 1]]) == [0, 1, 2]
	assert s.getOrder([[19, 13], [16, 9], [21, 10], [32, 25], [37, 4], [49, 24], [2, 15], [38, 41], [37, 34], [33, 6], [45, 4], [18, 18], [46, 39], [12, 24]]) == [6, 1, 2, 9, 4, 10, 0, 11, 5, 13, 3, 8, 12, 7]
	print("All tests passed!")
```
