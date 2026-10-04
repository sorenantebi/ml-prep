---
topic: "Greedy"
difficulty: Medium
leetcode: https://leetcode.com/problems/maximum-sum-circular-subarray/
neetcode: https://neetcode.io/problems/maximum-sum-circular-subarray
---
# Maximum Sum Circular Subarray

**Topic:** [[15 Greedy|Greedy]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/maximum-sum-circular-subarray/) · [NeetCode](https://neetcode.io/problems/maximum-sum-circular-subarray)

**Solve it in:** [[Maximum Sum Circular Subarray]] · **Answer:** [[Maximum Sum Circular Subarray - Solution]]

## Problem

Given a **circular** integer array `nums` of length `n` (the element after `nums[n-1]` is `nums[0]`), return the maximum possible sum of a non-empty subarray. A subarray may wrap around the end, but it may include each element at most once (its length is at most `n`).

## Examples

**Example 1**
```text
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: [3]
```

**Example 2**
```text
Input: nums = [5,-3,5]
Output: 10
Explanation: Wrapping subarray [5,5].
```

**Example 3**
```text
Input: nums = [-3,-2,-3]
Output: -2
```

## Constraints

- `n == nums.length`
- `1 <= n <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.maxSubarraySumCircular([1, -2, 3, -2]) == 3
    assert s.maxSubarraySumCircular([5, -3, 5]) == 10
    assert s.maxSubarraySumCircular([-3, -2, -3]) == -2
    assert s.maxSubarraySumCircular([7]) == 7
    assert s.maxSubarraySumCircular([3, -1, 2, -1]) == 4
    assert s.maxSubarraySumCircular([3, -2, 2, -3]) == 3
    assert s.maxSubarraySumCircular([1, 2, 3]) == 6
    assert s.maxSubarraySumCircular([2, -5, -5, 3]) == 5  # wraps: 3 + 2
    print("All tests passed!")
```
