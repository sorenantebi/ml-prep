---
topic: "Sliding Window"
difficulty: Hard
leetcode: https://leetcode.com/problems/sliding-window-maximum/
neetcode: https://neetcode.io/problems/sliding-window-maximum
---
# Sliding Window Maximum

**Topic:** [[03 Sliding Window|Sliding Window]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/sliding-window-maximum/) · [NeetCode](https://neetcode.io/problems/sliding-window-maximum)

**Solve it in:** [[Sliding Window Maximum]] · **Answer:** [[Sliding Window Maximum - Solution]]

## Problem

You are given an integer array `nums` and a window size `k`. A window of length `k` starts at the left of the array and slides right one position at a time until it reaches the end. Return an array containing the maximum value of each window position, in order (there are `n - k + 1` windows).

## Examples

**Example 1**
```text
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
```

**Example 2**
```text
Input: nums = [1], k = 1
Output: [1]
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`

## Starter Code & Test Cases

```python
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pass  # your code here


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert sol.maxSlidingWindow([1], 1) == [1]
    assert sol.maxSlidingWindow([1, -1], 1) == [1, -1]
    assert sol.maxSlidingWindow([9, 11], 2) == [11]
    assert sol.maxSlidingWindow([4, -2], 2) == [4]
    assert sol.maxSlidingWindow([7, 2, 4], 2) == [7, 4]
    assert sol.maxSlidingWindow([1, 3, 1, 2, 0, 5], 3) == [3, 3, 2, 5]
    assert sol.maxSlidingWindow([5, 4, 3, 2, 1], 5) == [5]
    print("All tests passed!")
```
