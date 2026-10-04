---
topic: "Binary Search"
difficulty: Easy
leetcode: https://leetcode.com/problems/sqrtx/
neetcode: https://neetcode.io/problems/sqrtx
---
# Sqrt(x)

**Topic:** [[05 Binary Search|Binary Search]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/sqrtx/) · [NeetCode](https://neetcode.io/problems/sqrtx)

**Solve it in:** [[Sqrt(x)]] · **Answer:** [[Sqrt(x) - Solution]]

## Problem

Given a non-negative integer `x`, return the integer square root of `x`: the largest integer `r` such that `r * r <= x` (i.e. the square root rounded down). You may not use built-in exponent or square-root functions/operators such as `pow(x, 0.5)` or `x ** 0.5`.

## Examples

**Example 1**
```text
Input: x = 4
Output: 2
```

**Example 2**
```text
Input: x = 8
Output: 2
Explanation: sqrt(8) = 2.828..., rounded down to 2
```

**Example 3**
```text
Input: x = 0
Output: 0
```

## Constraints

- `0 <= x <= 2^31 - 1`

## Starter Code & Test Cases

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.mySqrt(4) == 2
    assert s.mySqrt(8) == 2
    assert s.mySqrt(0) == 0
    assert s.mySqrt(1) == 1
    assert s.mySqrt(2) == 1
    assert s.mySqrt(15) == 3
    assert s.mySqrt(16) == 4
    assert s.mySqrt(2**31 - 1) == 46340
    import math
    assert all(s.mySqrt(v) == math.isqrt(v) for v in range(0, 2000))
    print("All tests passed!")
```
