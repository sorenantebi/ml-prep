---
topic: "Stack"
difficulty: Hard
leetcode: https://leetcode.com/problems/largest-rectangle-in-histogram/
neetcode: https://neetcode.io/problems/largest-rectangle-in-histogram
---
# Largest Rectangle In Histogram

**Topic:** [[04 Stack|Stack]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/largest-rectangle-in-histogram/) · [NeetCode](https://neetcode.io/problems/largest-rectangle-in-histogram)

**Solve it in:** [[Largest Rectangle In Histogram]] · **Answer:** [[Largest Rectangle In Histogram - Solution]]

## Problem

You are given an array `heights` of non-negative integers representing a histogram where every bar has width `1`. Return the area of the largest axis-aligned rectangle that fits entirely inside the histogram.

## Examples

**Example 1**
```text
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: bars of height 5 and 6 form a 2-wide rectangle of height 5
```

**Example 2**
```text
Input: heights = [2,4]
Output: 4
```

**Example 3**
```text
Input: heights = [2,1,2]
Output: 3
Explanation: height 1 across all three bars
```

## Constraints

- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert s.largestRectangleArea([2, 4]) == 4
    assert s.largestRectangleArea([2, 1, 2]) == 3
    assert s.largestRectangleArea([0]) == 0
    assert s.largestRectangleArea([7]) == 7
    assert s.largestRectangleArea([1, 2, 3, 4, 5]) == 9
    assert s.largestRectangleArea([5, 4, 3, 2, 1]) == 9
    assert s.largestRectangleArea([3, 3, 3, 3]) == 12
    assert s.largestRectangleArea([6, 2, 5, 4, 5, 1, 6]) == 12
    print("All tests passed!")
```
