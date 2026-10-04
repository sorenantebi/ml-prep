---
topic: "Arrays & Hashing"
difficulty: Medium
leetcode: https://leetcode.com/problems/majority-element-ii/
neetcode: https://neetcode.io/problems/majority-element-ii
---
# Majority Element II

**Topic:** [[01 Arrays & Hashing|Arrays & Hashing]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/majority-element-ii/) · [NeetCode](https://neetcode.io/problems/majority-element-ii)

**Solve it in:** [[Majority Element II]] · **Answer:** [[Majority Element II - Solution]]

## Problem

Given an integer array `nums` of length `n`, return all values that occur strictly more than `⌊n / 3⌋` times. The result may be returned in any order (it contains at most two values, and may be empty).

## Examples

**Example 1**
```text
Input: nums = [3,2,3]
Output: [3]
```

**Example 2**
```text
Input: nums = [1]
Output: [1]
```

**Example 3**
```text
Input: nums = [1,2]
Output: [1,2]
Explanation: n/3 rounds down to 0, so both values (1 occurrence each) qualify.
```

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`
- Follow-up: solve it in linear time and `O(1)` space.

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.majorityElement([3, 2, 3])) == [3]
    assert sorted(s.majorityElement([1])) == [1]
    assert sorted(s.majorityElement([1, 2])) == [1, 2]
    assert sorted(s.majorityElement([1, 2, 3])) == []
    assert sorted(s.majorityElement([2, 2, 1, 1, 1, 2, 2])) == [1, 2]
    assert sorted(s.majorityElement([4, 4, 5, 5, 6])) == [4, 5]
    assert sorted(s.majorityElement([-1, -1, -1, 0])) == [-1]
    assert sorted(s.majorityElement([1, 2, 3, 4, 1, 2, 1, 2])) == [1, 2]
    assert sorted(s.majorityElement([0, 0, 0])) == [0]
    print("All tests passed!")
```
