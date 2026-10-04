---
topic: "Heap / Priority Queue"
difficulty: Medium
leetcode: https://leetcode.com/problems/kth-largest-element-in-an-array/
neetcode: https://neetcode.io/problems/kth-largest-element-in-an-array
---
# Kth Largest Element In An Array

**Topic:** [[08 Heap - Priority Queue|Heap / Priority Queue]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/) · [NeetCode](https://neetcode.io/problems/kth-largest-element-in-an-array)

**Solve it in:** [[Kth Largest Element In An Array]] · **Answer:** [[Kth Largest Element In An Array - Solution]]

## Problem

Given an integer array `nums` and an integer `k`, return the `k`-th largest element of the array, i.e. the element that would sit at position `k` (1-indexed) if the array were sorted in descending order. Duplicates count separately, so this is not the `k`-th largest distinct value.

Try to solve it without fully sorting the array.

## Examples

**Example 1**
```text
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

**Example 2**
```text
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
Explanation: descending order is [6,5,5,4,...], 4th is 4
```

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Starter Code & Test Cases

```python
from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert s.findKthLargest([1], 1) == 1
    assert s.findKthLargest([2, 2, 2, 2], 3) == 2
    assert s.findKthLargest([-1, -5, -3], 1) == -1
    assert s.findKthLargest([-1, -5, -3], 3) == -5
    assert s.findKthLargest([7, 10, 4, 3, 20, 15], 6) == 3
    big = list(range(100000, 0, -1))
    assert s.findKthLargest(big, 50000) == 50001
    print("All tests passed!")
```
