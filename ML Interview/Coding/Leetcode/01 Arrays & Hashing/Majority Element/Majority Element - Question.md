---
topic: "Arrays & Hashing"
difficulty: Easy
leetcode: https://leetcode.com/problems/majority-element/
neetcode: https://neetcode.io/problems/majority-element
---
# Majority Element

**Topic:** [[01 Arrays & Hashing|Arrays & Hashing]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/majority-element/) · [NeetCode](https://neetcode.io/problems/majority-element)

**Solve it in:** [[Majority Element]] · **Answer:** [[Majority Element - Solution]]

## Problem

Given an array `nums` of size `n`, return its majority element: the value that occurs strictly more than `⌊n / 2⌋` times. You may assume a majority element always exists in the input.

## Examples

**Example 1**
```text
Input: nums = [3,2,3]
Output: 3
```

**Example 2**
```text
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`
- A majority element is guaranteed to exist.
- Follow-up: solve it in linear time with `O(1)` extra space.

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.majorityElement([3, 2, 3]) == 3
    assert s.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert s.majorityElement([7]) == 7
    assert s.majorityElement([-1, -1, 5]) == -1
    assert s.majorityElement([1, 2, 1, 2, 1]) == 1
    assert s.majorityElement([4, 4, 4, 4]) == 4
    assert s.majorityElement([9] * 25001 + [0] * 24999) == 9
    print("All tests passed!")
```
