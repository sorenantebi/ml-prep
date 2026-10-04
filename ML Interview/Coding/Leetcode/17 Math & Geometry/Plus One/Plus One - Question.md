---
topic: "Math & Geometry"
difficulty: Easy
leetcode: https://leetcode.com/problems/plus-one/
neetcode: https://neetcode.io/problems/plus-one
---
# Plus One

**Topic:** [[17 Math & Geometry|Math & Geometry]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/plus-one/) · [NeetCode](https://neetcode.io/problems/plus-one)

**Solve it in:** [[Plus One]] · **Answer:** [[Plus One - Solution]]

## Problem

A large non-negative integer is stored as an array `digits`, where each element is one decimal digit and the most significant digit comes first. The number has no leading zeros (except for the number `0` itself).

Add one to the number and return the resulting array of digits.

## Examples

**Example 1**
```text
Input: digits = [1,2,3]
Output: [1,2,4]
```

**Example 2**
```text
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
```

**Example 3**
```text
Input: digits = [9]
Output: [1,0]
Explanation: 9 + 1 = 10
```

## Constraints

- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- `digits` has no leading zeros.

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.plusOne([1, 2, 3]) == [1, 2, 4]
    assert s.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert s.plusOne([9]) == [1, 0]
    assert s.plusOne([0]) == [1]
    assert s.plusOne([9, 9, 9]) == [1, 0, 0, 0]
    assert s.plusOne([1, 9, 9]) == [2, 0, 0]
    assert s.plusOne([8, 9]) == [9, 0]
    assert s.plusOne([9] * 100) == [1] + [0] * 100
    print("All tests passed!")
```
