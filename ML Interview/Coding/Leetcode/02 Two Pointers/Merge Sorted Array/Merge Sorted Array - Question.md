---
topic: "Two Pointers"
difficulty: Easy
leetcode: https://leetcode.com/problems/merge-sorted-array/
neetcode: https://neetcode.io/problems/merge-sorted-array
---
# Merge Sorted Array

**Topic:** [[02 Two Pointers|Two Pointers]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/merge-sorted-array/) · [NeetCode](https://neetcode.io/problems/merge-sorted-array)

**Solve it in:** [[Merge Sorted Array]] · **Answer:** [[Merge Sorted Array - Solution]]

## Problem

You have two integer arrays `nums1` and `nums2`, each sorted in non-decreasing order, and integers `m` and `n` giving the number of real elements in each. `nums1` has length `m + n`: its first `m` entries are the real values and the last `n` entries are `0` placeholders. Merge `nums2` into `nums1` **in place** so that `nums1` becomes one sorted array of length `m + n`. The function returns nothing.

## Examples

**Example 1**
```text
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
```

**Example 2**
```text
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
```

**Example 3**
```text
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
```

## Constraints

- `nums1.length == m + n`, `nums2.length == n`
- `0 <= m, n <= 200`, `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pass  # your code here


if __name__ == "__main__":
    sol = Solution()

    a = [1, 2, 3, 0, 0, 0]
    sol.merge(a, 3, [2, 5, 6], 3)
    assert a == [1, 2, 2, 3, 5, 6]

    a = [1]
    sol.merge(a, 1, [], 0)
    assert a == [1]

    a = [0]
    sol.merge(a, 0, [1], 1)
    assert a == [1]

    a = [4, 5, 6, 0, 0, 0]
    sol.merge(a, 3, [1, 2, 3], 3)
    assert a == [1, 2, 3, 4, 5, 6]

    a = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
    sol.merge(a, 6, [1, 2, 2], 3)
    assert a == [-1, 0, 0, 1, 2, 2, 3, 3, 3]

    a = [2, 0]
    sol.merge(a, 1, [1], 1)
    assert a == [1, 2]

    print("All tests passed!")
```
