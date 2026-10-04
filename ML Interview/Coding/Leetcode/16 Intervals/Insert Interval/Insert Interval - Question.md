---
topic: "Intervals"
difficulty: Medium
leetcode: https://leetcode.com/problems/insert-interval/
neetcode: https://neetcode.io/problems/insert-new-interval
---
# Insert Interval

**Topic:** [[16 Intervals|Intervals]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/insert-interval/) · [NeetCode](https://neetcode.io/problems/insert-new-interval)

**Solve it in:** [[Insert Interval]] · **Answer:** [[Insert Interval - Solution]]

## Problem

You are given a list of non-overlapping intervals `intervals`, where `intervals[i] = [start_i, end_i]`, sorted in ascending order by `start_i`, and one more interval `newInterval = [start, end]`. Insert `newInterval` so that the list is still sorted by start and contains no overlapping intervals, merging any intervals that overlap with it (intervals that touch at an endpoint, like `[1,2]` and `[2,3]`, count as overlapping). Return the resulting list; you may build a new list rather than editing in place.

## Examples

**Example 1**
```text
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

**Example 2**
```text
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: [4,8] overlaps [3,5], [6,7] and [8,10].
```

**Example 3**
```text
Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]
```

## Constraints

- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`, `0 <= start_i <= end_i <= 10^5`
- `intervals` is sorted by `start_i` and non-overlapping
- `newInterval.length == 2`, `0 <= start <= end <= 10^5`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
    assert s.insert([], [5, 7]) == [[5, 7]]
    assert s.insert([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]
    assert s.insert([[3, 5]], [0, 1]) == [[0, 1], [3, 5]]
    assert s.insert([[1, 5]], [2, 3]) == [[1, 5]]
    assert s.insert([[1, 2], [5, 6]], [2, 5]) == [[1, 6]]       # touching endpoints merge
    assert s.insert([[1, 2], [3, 4]], [0, 10]) == [[0, 10]]
    print("All tests passed!")
```
