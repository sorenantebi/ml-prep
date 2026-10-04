---
topic: "Two Pointers"
difficulty: Easy
leetcode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
neetcode: https://neetcode.io/problems/remove-duplicates-from-sorted-array
---
# Remove Duplicates From Sorted Array

**Topic:** [[02 Two Pointers|Two Pointers]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) · [NeetCode](https://neetcode.io/problems/remove-duplicates-from-sorted-array)

**Solve it in:** [[Remove Duplicates From Sorted Array]] · **Answer:** [[Remove Duplicates From Sorted Array - Solution]]

## Problem

Given an integer array `nums` sorted in non-decreasing order, remove duplicates **in place** so that each distinct value appears once and the relative order is kept. Return `k`, the number of distinct values. The first `k` positions of `nums` must hold the distinct values in order; what remains beyond index `k - 1` does not matter.

## Examples

**Example 1**
```text
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
```

**Example 2**
```text
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
```

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pass  # your code here


if __name__ == "__main__":
    sol = Solution()

    def check(nums, expected):
        k = sol.removeDuplicates(nums)
        assert k == len(expected), (k, expected)
        assert nums[:k] == expected

    check([1, 1, 2], [1, 2])
    check([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4])
    check([1], [1])
    check([1, 2, 3], [1, 2, 3])
    check([5, 5, 5, 5], [5])
    check([-3, -3, -1, 0, 0, 7], [-3, -1, 0, 7])
    print("All tests passed!")
```
