---
topic: "1-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/integer-break/
neetcode: https://neetcode.io/problems/integer-break
---
# Integer Break

**Topic:** [[13 1-D Dynamic Programming|1-D Dynamic Programming]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/integer-break/) · [NeetCode](https://neetcode.io/problems/integer-break)

**Solve it in:** [[Integer Break]] · **Answer:** [[Integer Break - Solution]]

## Problem

Given an integer `n`, split it into a sum of **at least two** positive integers and maximise the product of those integers. Return the maximum product.

## Examples

**Example 1**
```text
Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, product 1.
```

**Example 2**
```text
Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, product 36.
```

## Constraints

- `2 <= n <= 58`

## Starter Code & Test Cases

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.integerBreak(2) == 1
    assert s.integerBreak(10) == 36
    assert s.integerBreak(3) == 2
    assert s.integerBreak(4) == 4
    assert s.integerBreak(8) == 18
    assert s.integerBreak(58) == 1549681956
    print("All tests passed!")
```
