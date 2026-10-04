---
topic: "Two Pointers"
difficulty: Medium
leetcode: https://leetcode.com/problems/3sum/
neetcode: https://neetcode.io/problems/three-integer-sum
---
# 3Sum

**Topic:** [[02 Two Pointers|Two Pointers]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/3sum/) · [NeetCode](https://neetcode.io/problems/three-integer-sum)

**Solve it in:** [[3Sum]] · **Answer:** [[3Sum - Solution]]

## Problem

Given an integer array `nums`, return every **unique** triplet `[nums[i], nums[j], nums[k]]` with `i`, `j`, `k` pairwise distinct indices such that the three values sum to `0`. The result must not contain duplicate triplets (as multisets of values). The triplets and the order inside them may be returned in any order.

## Examples

**Example 1**
```text
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

**Example 2**
```text
Input: nums = [0,1,1]
Output: []
```

**Example 3**
```text
Input: nums = [0,0,0]
Output: [[0,0,0]]
```

## Constraints

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass  # your code here


if __name__ == "__main__":
    sol = Solution()

    def norm(res):
        return sorted(tuple(sorted(t)) for t in res)

    assert norm(sol.threeSum([-1, 0, 1, 2, -1, -4])) == [(-1, -1, 2), (-1, 0, 1)]
    assert norm(sol.threeSum([0, 1, 1])) == []
    assert norm(sol.threeSum([0, 0, 0])) == [(0, 0, 0)]
    assert norm(sol.threeSum([0, 0, 0, 0, 0])) == [(0, 0, 0)]
    assert norm(sol.threeSum([-2, 0, 1, 1, 2])) == [(-2, 0, 2), (-2, 1, 1)]
    assert norm(sol.threeSum([1, 2, 3])) == []
    assert norm(sol.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6])) == [
        (-4, -2, 6), (-4, 0, 4), (-4, 1, 3), (-4, 2, 2),
        (-2, -2, 4), (-2, 0, 2),
    ]
    print("All tests passed!")
```
