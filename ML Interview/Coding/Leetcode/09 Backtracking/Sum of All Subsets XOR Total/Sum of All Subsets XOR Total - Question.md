---
topic: "Backtracking"
difficulty: Easy
leetcode: https://leetcode.com/problems/sum-of-all-subset-xor-totals/
neetcode: https://neetcode.io/problems/sum-of-all-subset-xor-totals
---
# Sum of All Subsets XOR Total

**Topic:** [[09 Backtracking|Backtracking]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/sum-of-all-subset-xor-totals/) · [NeetCode](https://neetcode.io/problems/sum-of-all-subset-xor-totals)

**Solve it in:** [[Sum of All Subsets XOR Total]] · **Answer:** [[Sum of All Subsets XOR Total - Solution]]

## Problem

The *XOR total* of an array is the bitwise XOR of all of its elements, and `0` for an empty array.

Given an integer array `nums`, return the sum of the XOR totals of **every subset** of `nums`. Subsets with the same elements taken from different positions are counted separately (there are exactly `2^n` subsets, including the empty one).

## Examples

**Example 1**
```text
Input: nums = [1,3]
Output: 6
Explanation: subsets [], [1], [3], [1,3] have XOR totals 0 + 1 + 3 + 2 = 6
```

**Example 2**
```text
Input: nums = [5,1,6]
Output: 28
```

**Example 3**
```text
Input: nums = [3,4,5,6,7,8]
Output: 480
```

## Constraints

- `1 <= nums.length <= 12`
- `1 <= nums[i] <= 20`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.subsetXORSum([1, 3]) == 6
    assert s.subsetXORSum([5, 1, 6]) == 28
    assert s.subsetXORSum([3, 4, 5, 6, 7, 8]) == 480
    assert s.subsetXORSum([7]) == 7
    assert s.subsetXORSum([2, 2]) == 4
    assert s.subsetXORSum([1, 2, 4]) == 28
    assert s.subsetXORSum([20] * 12) == 20 * 2 ** 11
    print("All tests passed!")
```
