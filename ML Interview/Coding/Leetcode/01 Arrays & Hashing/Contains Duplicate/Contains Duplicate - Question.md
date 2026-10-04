---
topic: "Arrays & Hashing"
difficulty: Easy
leetcode: https://leetcode.com/problems/contains-duplicate/
neetcode: https://neetcode.io/problems/duplicate-integer
---
# Contains Duplicate

**Topic:** [[01 Arrays & Hashing|Arrays & Hashing]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/contains-duplicate/) · [NeetCode](https://neetcode.io/problems/duplicate-integer)

**Solve it in:** [[Contains Duplicate]] · **Answer:** [[Contains Duplicate - Solution]]

## Problem

Given an integer array `nums`, determine whether any value occurs at least twice. Return `true` if some value appears two or more times, and `false` if all elements are pairwise distinct.

## Examples

**Example 1**
```text
Input: nums = [1,2,3,1]
Output: true
Explanation: the value 1 occurs at indices 0 and 3.
```

**Example 2**
```text
Input: nums = [1,2,3,4]
Output: false
```

**Example 3**
```text
Input: nums = [5,5,6,6,7,7]
Output: true
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.containsDuplicate([1, 2, 3, 1]) is True
    assert s.containsDuplicate([1, 2, 3, 4]) is False
    assert s.containsDuplicate([5, 5, 6, 6, 7, 7]) is True
    assert s.containsDuplicate([42]) is False
    assert s.containsDuplicate([-1, -1]) is True
    assert s.containsDuplicate([-10**9, 10**9, 0]) is False
    assert s.containsDuplicate(list(range(100000))) is False
    assert s.containsDuplicate(list(range(99999)) + [12345]) is True
    print("All tests passed!")
```
