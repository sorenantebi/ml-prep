---
topic: "Two Pointers"
difficulty: Medium
leetcode: https://leetcode.com/problems/rotate-array/
neetcode: https://neetcode.io/problems/rotate-array
---
# Rotate Array

**Topic:** [[02 Two Pointers|Two Pointers]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/rotate-array/) · [NeetCode](https://neetcode.io/problems/rotate-array)

**Solve it in:** [[Rotate Array]] · **Answer:** [[Rotate Array - Solution]]

## Problem

Given an integer array `nums`, rotate it to the right by `k` steps **in place**, where `k` is non-negative. Rotating right by one step moves the last element to the front. `k` may be larger than the array length. The function returns nothing. Try to achieve `O(1)` extra space.

## Examples

**Example 1**
```text
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
```

**Example 2**
```text
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        pass  # your code here


if __name__ == "__main__":
    sol = Solution()

    def run(nums, k):
        sol.rotate(nums, k)
        return nums

    assert run([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
    assert run([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
    assert run([1], 5) == [1]
    assert run([1, 2], 0) == [1, 2]
    assert run([1, 2], 3) == [2, 1]
    assert run([1, 2, 3], 3) == [1, 2, 3]
    assert run([1, 2, 3, 4, 5, 6], 4) == [3, 4, 5, 6, 1, 2]
    print("All tests passed!")
```
