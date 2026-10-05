---
topic: "2-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/unique-paths/
neetcode: https://neetcode.io/problems/count-paths
---
# Unique Paths

**Topic:** [[14 2-D Dynamic Programming|2-D Dynamic Programming]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/unique-paths/) · [NeetCode](https://neetcode.io/problems/count-paths)

**Solve it in:** [[Unique Paths]] · **Answer:** [[Unique Paths - Solution]]

## Problem

A robot sits in the top-left cell of an `m x n` grid and wants to reach the bottom-right cell. At each step it may move only **one cell right** or **one cell down**. Return the number of distinct paths the robot can take from the start to the finish.

The answer is guaranteed to fit in a 32-bit signed integer (at most `2 * 10^9`).

## Examples

**Example 1**
```text
Input: m = 3, n = 7
Output: 28
```

**Example 2**
```text
Input: m = 3, n = 2
Output: 3
Explanation: Right->Down->Down, Down->Right->Down, Down->Down->Right
```

**Example 3**
```text
Input: m = 1, n = 1
Output: 1
Explanation: Start and finish are the same cell, so there is exactly one (empty) path.
```

## Constraints

- `1 <= m, n <= 100`
- The answer is `<= 2 * 10^9`

## Starter Code & Test Cases

```python
class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.uniquePaths(3, 7) == 28
	assert s.uniquePaths(3, 2) == 3
	assert s.uniquePaths(1, 1) == 1
	assert s.uniquePaths(1, 10) == 1
	assert s.uniquePaths(10, 1) == 1
	assert s.uniquePaths(2, 2) == 2
	assert s.uniquePaths(7, 3) == 28
	assert s.uniquePaths(10, 10) == 48620
	print("All tests passed!")
```
