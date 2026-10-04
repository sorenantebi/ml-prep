---
topic: "Binary Search"
difficulty: Easy
leetcode: https://leetcode.com/problems/search-insert-position/
neetcode: https://neetcode.io/problems/search-insert-position
---
# Search Insert Position

**Topic:** [[05 Binary Search|Binary Search]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/search-insert-position/) · [NeetCode](https://neetcode.io/problems/search-insert-position)

**Solve it in:** [[Search Insert Position]] · **Answer:** [[Search Insert Position - Solution]]

## Problem

Given a sorted array `nums` of distinct integers and an integer `target`, return the index of `target` if it is present. If it is not, return the index at which it would have to be inserted to keep the array sorted. The solution must run in `O(log n)` time.

## Examples

**Example 1**
```text
Input: nums = [1,3,5,6], target = 5
Output: 2
```

**Example 2**
```text
Input: nums = [1,3,5,6], target = 2
Output: 1
```

**Example 3**
```text
Input: nums = [1,3,5,6], target = 7
Output: 4
```

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i], target <= 10^4`
- `nums` contains distinct values sorted in ascending order

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.searchInsert([1, 3, 5, 6], 5) == 2
    assert s.searchInsert([1, 3, 5, 6], 2) == 1
    assert s.searchInsert([1, 3, 5, 6], 7) == 4
    assert s.searchInsert([1, 3, 5, 6], 0) == 0
    assert s.searchInsert([1], 1) == 0
    assert s.searchInsert([1], 2) == 1
    assert s.searchInsert([-10, -3, 0, 4], -4) == 1
    import bisect
    nums = list(range(0, 300, 7))
    assert all(s.searchInsert(nums, t) == bisect.bisect_left(nums, t) for t in range(-5, 310))
    print("All tests passed!")
```
