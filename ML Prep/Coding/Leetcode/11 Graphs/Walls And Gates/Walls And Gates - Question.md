---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/walls-and-gates/
neetcode: https://neetcode.io/problems/islands-and-treasure
---
# Walls And Gates

**Topic:** [[11 Graphs|Graphs]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/walls-and-gates/) · [NeetCode](https://neetcode.io/problems/islands-and-treasure)

**Solve it in:** [[Walls And Gates]] · **Answer:** [[Walls And Gates - Solution]]

## Problem

You are given an `m x n` grid `rooms` with three possible values:

- `-1`: a wall or obstacle
- `0`: a gate
- `INF = 2^31 - 1 = 2147483647`: an empty room

Fill each empty room **in place** with the distance (number of 4-directional steps) to its nearest gate. If an empty room cannot reach any gate, leave it as `INF`. Walls and gates stay unchanged. Moves go up, down, left, or right and cannot pass through walls.

The function returns nothing; the grid is modified in place.

## Examples

**Example 1**
```text
Input: rooms = [[INF,-1,0,INF],[INF,INF,INF,-1],[INF,-1,INF,-1],[0,-1,INF,INF]]
Output:        [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
```

**Example 2**
```text
Input: rooms = [[-1]]
Output: [[-1]]
```

**Example 3**
```text
Input: rooms = [[INF,-1],[-1,0]]
Output: [[INF,-1],[-1,0]]
Explanation: The top-left room is walled off from the gate.
```

## Constraints

- `1 <= m, n <= 250`
- `rooms[i][j]` is `-1`, `0`, or `2^31 - 1`

## Starter Code & Test Cases

```python
from typing import List

INF = 2**31 - 1


class Solution:
	def wallsAndGates(self, rooms: List[List[int]]) -> None:
		"""Do not return anything, modify rooms in-place instead."""
		pass  # your code here


if __name__ == "__main__":
	s = Solution()

	rooms = [[INF, -1, 0, INF], [INF, INF, INF, -1], [INF, -1, INF, -1], [0, -1, INF, INF]]
	s.wallsAndGates(rooms)
	assert rooms == [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]

	rooms = [[-1]]
	s.wallsAndGates(rooms)
	assert rooms == [[-1]]

	rooms = [[INF, -1], [-1, 0]]
	s.wallsAndGates(rooms)
	assert rooms == [[INF, -1], [-1, 0]]

	rooms = [[INF, INF, INF]]
	s.wallsAndGates(rooms)
	assert rooms == [[INF, INF, INF]]  # no gate at all

	rooms = [[0, INF, INF, INF, 0]]
	s.wallsAndGates(rooms)
	assert rooms == [[0, 1, 2, 1, 0]]

	rooms = [[0]]
	s.wallsAndGates(rooms)
	assert rooms == [[0]]

	rooms = [[INF, INF], [INF, 0]]
	s.wallsAndGates(rooms)
	assert rooms == [[2, 1], [1, 0]]
	print("All tests passed!")
```
