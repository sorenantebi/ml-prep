---
topic: "Binary Search"
difficulty: Hard
leetcode: https://leetcode.com/problems/split-array-largest-sum/
neetcode: https://neetcode.io/problems/split-array-largest-sum
---
# Split Array Largest Sum

**Topic:** [[05 Binary Search|Binary Search]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/split-array-largest-sum/) · [NeetCode](https://neetcode.io/problems/split-array-largest-sum)

**Solve it in:** [[Split Array Largest Sum]] · **Answer:** [[Split Array Largest Sum - Solution]]

## Problem

Given an integer array `nums` and an integer `k`, split `nums` into exactly `k` non-empty contiguous subarrays so that the largest of the `k` subarray sums is as small as possible. Return that minimized largest sum.

## Examples

**Example 1**
```text
Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: [7,2,5] and [10,8] have sums 14 and 18
```

**Example 2**
```text
Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: [1,2,3] and [4,5]
```

**Example 3**
```text
Input: nums = [1,4,4], k = 3
Output: 4
```

## Constraints

- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 10^6`
- `1 <= k <= min(50, nums.length)`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.splitArray([7, 2, 5, 10, 8], 2) == 18
    assert s.splitArray([1, 2, 3, 4, 5], 2) == 9
    assert s.splitArray([1, 4, 4], 3) == 4
    assert s.splitArray([5], 1) == 5
    assert s.splitArray([0, 0, 0], 2) == 0
    assert s.splitArray([2, 3, 1, 2, 4, 3], 6) == 4     # each element alone
    assert s.splitArray([2, 3, 1, 2, 4, 3], 1) == 15    # whole array
    assert s.splitArray([10, 5, 13, 4, 8, 4, 5, 11, 14, 9, 16, 10, 20, 8], 8) == 25
    print("All tests passed!")
```
