---
topic: "Stack"
difficulty: Medium
leetcode: https://leetcode.com/problems/asteroid-collision/
neetcode: https://neetcode.io/problems/asteroid-collision
---
# Asteroid Collision

**Topic:** [[04 Stack|Stack]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/asteroid-collision/) · [NeetCode](https://neetcode.io/problems/asteroid-collision)

**Solve it in:** [[Asteroid Collision]] · **Answer:** [[Asteroid Collision - Solution]]

## Problem

You are given an integer array `asteroids` describing asteroids in a row. The absolute value is the asteroid's size; the sign is its direction (positive = moving right, negative = moving left). All asteroids move at the same speed.

When a right-moving asteroid meets a left-moving one, they collide: the smaller one explodes; if they are the same size, both explode. Asteroids moving in the same direction never meet (and a left-mover on the left with a right-mover on the right move apart).

Return the state of the asteroids after all collisions, in their original left-to-right order.

## Examples

**Example 1**
```text
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: 10 and -5 collide, 10 survives
```

**Example 2**
```text
Input: asteroids = [8,-8]
Output: []
```

**Example 3**
```text
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: -5 destroys 2, then 10 destroys -5
```

## Constraints

- `2 <= asteroids.length <= 10^4`
- `-1000 <= asteroids[i] <= 1000`
- `asteroids[i] != 0`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def asteroidCollision(self, asteroids: List[int]) -> List[int]:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.asteroidCollision([5, 10, -5]) == [5, 10]
	assert s.asteroidCollision([8, -8]) == []
	assert s.asteroidCollision([10, 2, -5]) == [10]
	assert s.asteroidCollision([-2, -1, 1, 2]) == [-2, -1, 1, 2]  # moving apart
	assert s.asteroidCollision([1, -2, -2, -2]) == [-2, -2, -2]
	assert s.asteroidCollision([1, 2, 3, -10]) == [-10]
	assert s.asteroidCollision([3, 5, -5, 4]) == [3, 4]
	assert s.asteroidCollision([-5, 5]) == [-5, 5]
	print("All tests passed!")
```
