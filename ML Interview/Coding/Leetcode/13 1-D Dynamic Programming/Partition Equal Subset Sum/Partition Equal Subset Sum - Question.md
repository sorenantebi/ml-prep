---
topic: "1-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/partition-equal-subset-sum/
neetcode: https://neetcode.io/problems/partition-equal-subset-sum
---
# Partition Equal Subset Sum

**Topic:** [[13 1-D Dynamic Programming|1-D Dynamic Programming]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/partition-equal-subset-sum/) · [NeetCode](https://neetcode.io/problems/partition-equal-subset-sum)

**Solve it in:** [[Partition Equal Subset Sum]] · **Answer:** [[Partition Equal Subset Sum - Solution]]

## Problem

Given an array `nums` of positive integers, return `true` if the array can be split into two subsets (every element in exactly one) whose sums are equal, and `false` otherwise.

## Examples

**Example 1**
```text
Input: nums = [1,5,11,5]
Output: true
Explanation: [1,5,5] and [11] both sum to 11.
```

**Example 2**
```text
Input: nums = [1,2,3,5]
Output: false
```

## Constraints

- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 100`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.canPartition([1,5,11,5]) is True
    assert s.canPartition([1,2,3,5]) is False
    assert s.canPartition([1]) is False
    assert s.canPartition([2,2]) is True
    assert s.canPartition([1,2,5]) is False
    assert s.canPartition([3,3,3,4,5]) is True
    assert s.canPartition([100] * 200) is True
    print("All tests passed!")
```
