---
topic: "Intervals"
difficulty: Medium
leetcode: https://leetcode.com/problems/merge-intervals/
neetcode: https://neetcode.io/problems/merge-intervals
---
# Merge Intervals

**Topic:** [[16 Intervals|Intervals]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/merge-intervals/) · [NeetCode](https://neetcode.io/problems/merge-intervals)

**Solve it in:** [[Merge Intervals]] · **Answer:** [[Merge Intervals - Solution]]

## Problem

Given an array `intervals` where `intervals[i] = [start_i, end_i]`, merge every group of overlapping intervals into a single interval and return the resulting array of non-overlapping intervals that together cover exactly the same points. Intervals that touch at an endpoint (e.g. `[1,4]` and `[4,5]`) are considered overlapping. The answer may be returned in any order.

## Examples

**Example 1**
```text
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
```

**Example 2**
```text
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
```

**Example 3**
```text
Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
```

## Constraints

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()

    def run(iv):
        return sorted(s.merge([x[:] for x in iv]))

    assert run([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert run([[1, 4], [4, 5]]) == [[1, 5]]
    assert run([[4, 7], [1, 4]]) == [[1, 7]]
    assert run([[1, 1]]) == [[1, 1]]
    assert run([[1, 10], [2, 3], [4, 5]]) == [[1, 10]]
    assert run([[5, 6], [1, 2], [3, 4]]) == [[1, 2], [3, 4], [5, 6]]
    assert run([[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]]) == [[1, 3], [4, 7]]
    print("All tests passed!")
```
