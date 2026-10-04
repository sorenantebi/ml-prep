---
topic: "Sliding Window"
difficulty: Easy
leetcode: https://leetcode.com/problems/contains-duplicate-ii/
neetcode: https://neetcode.io/problems/contains-duplicate-ii
---
# Contains Duplicate II

**Topic:** [[03 Sliding Window|Sliding Window]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/contains-duplicate-ii/) · [NeetCode](https://neetcode.io/problems/contains-duplicate-ii)

**Solve it in:** [[Contains Duplicate II]] · **Answer:** [[Contains Duplicate II - Solution]]

## Problem

Given an integer array `nums` and an integer `k`, return `true` if there exist two **different** indices `i` and `j` with `nums[i] == nums[j]` and `abs(i - j) <= k`. Otherwise return `false`.

## Examples

**Example 1**
```text
Input: nums = [1,2,3,1], k = 3
Output: true
```

**Example 2**
```text
Input: nums = [1,0,1,1], k = 1
Output: true
```

**Example 3**
```text
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= k <= 10^5`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pass  # your code here


if __name__ == "__main__":
    sol = Solution()
    assert sol.containsNearbyDuplicate([1, 2, 3, 1], 3) is True
    assert sol.containsNearbyDuplicate([1, 0, 1, 1], 1) is True
    assert sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) is False
    assert sol.containsNearbyDuplicate([1], 1) is False
    assert sol.containsNearbyDuplicate([1, 1], 0) is False
    assert sol.containsNearbyDuplicate([99, 99], 2) is True
    assert sol.containsNearbyDuplicate([1, 2, 3, 4, 5, 1], 4) is False
    assert sol.containsNearbyDuplicate([1, 2, 3, 4, 5, 1], 5) is True
    print("All tests passed!")
```
