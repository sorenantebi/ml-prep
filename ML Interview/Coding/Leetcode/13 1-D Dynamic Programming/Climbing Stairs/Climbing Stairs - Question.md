---
topic: "1-D Dynamic Programming"
difficulty: Easy
leetcode: https://leetcode.com/problems/climbing-stairs/
neetcode: https://neetcode.io/problems/climbing-stairs
---
# Climbing Stairs

**Topic:** [[13 1-D Dynamic Programming|1-D Dynamic Programming]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/climbing-stairs/) · [NeetCode](https://neetcode.io/problems/climbing-stairs)

**Solve it in:** [[Climbing Stairs]] · **Answer:** [[Climbing Stairs - Solution]]

## Problem

You are at the bottom of a staircase with `n` steps. Each move you climb either `1` or `2` steps. Return the number of distinct sequences of moves that take you exactly to the top (step `n`).

## Examples

**Example 1**
```text
Input: n = 2
Output: 2
Explanation: 1+1 or 2.
```

**Example 2**
```text
Input: n = 3
Output: 3
Explanation: 1+1+1, 1+2, 2+1.
```

## Constraints

- `1 <= n <= 45`

## Starter Code & Test Cases

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3
    assert s.climbStairs(1) == 1
    assert s.climbStairs(5) == 8
    assert s.climbStairs(10) == 89
    assert s.climbStairs(45) == 1836311903
    print("All tests passed!")
```
