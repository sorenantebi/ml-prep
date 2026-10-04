---
topic: "Binary Search"
difficulty: Medium
leetcode: https://leetcode.com/problems/search-in-rotated-sorted-array/
neetcode: https://neetcode.io/problems/find-target-in-rotated-sorted-array
---
# Search In Rotated Sorted Array

**Topic:** [[05 Binary Search|Binary Search]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/) · [NeetCode](https://neetcode.io/problems/find-target-in-rotated-sorted-array)

**Solve it in:** [[Search In Rotated Sorted Array]] · **Answer:** [[Search In Rotated Sorted Array - Solution]]

## Problem

An integer array `nums`, sorted in ascending order with **distinct** values, may have been rotated at an unknown pivot index `k` (`0 <= k < n`), turning it into `[nums[k], ..., nums[n-1], nums[0], ..., nums[k-1]]`. For example `[0,1,2,4,5,6,7]` rotated at index 3 becomes `[4,5,6,7,0,1,2]`.

Given the rotated array `nums` and an integer `target`, return the index of `target` in `nums`, or `-1` if it is absent. The algorithm must run in `O(log n)` time.

## Examples

**Example 1**
```text
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

**Example 2**
```text
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

**Example 3**
```text
Input: nums = [1], target = 0
Output: -1
```

## Constraints

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i], target <= 10^4`
- All values in `nums` are unique
- `nums` is an ascending array that is possibly rotated

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert s.search([1], 0) == -1
    assert s.search([1], 1) == 0
    assert s.search([3, 1], 1) == 1
    assert s.search([5, 1, 3], 5) == 0
    base = list(range(0, 40, 4))
    for r in range(len(base)):
        arr = base[r:] + base[:r]
        for t in range(-2, 42):
            expected = arr.index(t) if t in arr else -1
            assert s.search(arr, t) == expected
    print("All tests passed!")
```
