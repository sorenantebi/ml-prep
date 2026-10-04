---
topic: "1-D Dynamic Programming"
difficulty: Easy
leetcode: https://leetcode.com/problems/n-th-tribonacci-number/
neetcode: https://neetcode.io/problems/n-th-tribonacci-number
---
# N-th Tribonacci Number

**Topic:** [[13 1-D Dynamic Programming|1-D Dynamic Programming]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/n-th-tribonacci-number/) · [NeetCode](https://neetcode.io/problems/n-th-tribonacci-number)

**Solve it in:** [[N-th Tribonacci Number]] · **Answer:** [[N-th Tribonacci Number - Solution]]

## Problem

The Tribonacci sequence is defined as `T0 = 0`, `T1 = 1`, `T2 = 1`, and `T(n + 3) = T(n) + T(n + 1) + T(n + 2)` for `n >= 0`. Given `n`, return `Tn`.

## Examples

**Example 1**
```text
Input: n = 4
Output: 4
Explanation: T3 = 0 + 1 + 1 = 2, T4 = 1 + 1 + 2 = 4.
```

**Example 2**
```text
Input: n = 25
Output: 1389537
```

## Constraints

- `0 <= n <= 37`
- The answer fits in a 32-bit signed integer.

## Starter Code & Test Cases

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.tribonacci(4) == 4
    assert s.tribonacci(25) == 1389537
    assert s.tribonacci(0) == 0
    assert s.tribonacci(1) == 1
    assert s.tribonacci(2) == 1
    assert s.tribonacci(3) == 2
    assert s.tribonacci(37) == 2082876103
    print("All tests passed!")
```
