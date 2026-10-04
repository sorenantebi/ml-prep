---
topic: "Greedy"
difficulty: Medium
leetcode: https://leetcode.com/problems/longest-turbulent-subarray/
neetcode: https://neetcode.io/problems/longest-turbulent-subarray
---
# Longest Turbulent Subarray

**Topic:** [[15 Greedy|Greedy]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/longest-turbulent-subarray/) · [NeetCode](https://neetcode.io/problems/longest-turbulent-subarray)

**Solve it in:** [[Longest Turbulent Subarray]] · **Answer:** [[Longest Turbulent Subarray - Solution]]

## Problem

Given an integer array `arr`, return the length of the longest **turbulent** subarray. A subarray `arr[i..j]` is turbulent if the comparison sign between each pair of adjacent elements flips at every step — e.g. `arr[k] > arr[k+1] < arr[k+2] > ...` or `arr[k] < arr[k+1] > arr[k+2] < ...`. Equal adjacent elements break turbulence. A single element is a turbulent subarray of length 1.

## Examples

**Example 1**
```text
Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: [4,2,10,7,8] has 4 > 2 < 10 > 7 < 8.
```

**Example 2**
```text
Input: arr = [4,8,12,16]
Output: 2
```

**Example 3**
```text
Input: arr = [100]
Output: 1
```

## Constraints

- `1 <= arr.length <= 4 * 10^4`
- `0 <= arr[i] <= 10^9`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]) == 5
    assert s.maxTurbulenceSize([4, 8, 12, 16]) == 2
    assert s.maxTurbulenceSize([100]) == 1
    assert s.maxTurbulenceSize([5, 5, 5]) == 1
    assert s.maxTurbulenceSize([1, 2, 1, 2, 1]) == 5
    assert s.maxTurbulenceSize([2, 2, 3]) == 2
    assert s.maxTurbulenceSize([1, 3, 2, 2, 5, 4, 6]) == 4
    print("All tests passed!")
```
