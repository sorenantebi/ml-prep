---
topic: "Intervals"
difficulty: Medium
leetcode: https://leetcode.com/problems/meeting-rooms-ii/
neetcode: https://neetcode.io/problems/meeting-schedule-ii
---
# Meeting Rooms II

**Topic:** [[16 Intervals|Intervals]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/meeting-rooms-ii/) · [NeetCode](https://neetcode.io/problems/meeting-schedule-ii)

**Solve it in:** [[Meeting Rooms II]] · **Answer:** [[Meeting Rooms II - Solution]]

## Problem

Given an array of meeting time intervals `intervals[i] = [start_i, end_i]`, return the minimum number of conference rooms needed to hold all meetings so that no two meetings in the same room overlap. A meeting ending at time `t` frees its room for a meeting starting at time `t`.

## Examples

**Example 1**
```text
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
```

**Example 2**
```text
Input: intervals = [[7,10],[2,4]]
Output: 1
```

**Example 3**
```text
Input: intervals = [[1,5],[2,6],[3,7],[5,8]]
Output: 3
```

## Constraints

- `1 <= intervals.length <= 10^4`
- `0 <= start_i < end_i <= 10^6`

## Starter Code & Test Cases

```python
from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert s.minMeetingRooms([[7, 10], [2, 4]]) == 1
    assert s.minMeetingRooms([[1, 5], [2, 6], [3, 7], [5, 8]]) == 3
    assert s.minMeetingRooms([[1, 2]]) == 1
    assert s.minMeetingRooms([[1, 5], [5, 10], [10, 15]]) == 1     # back-to-back
    assert s.minMeetingRooms([[1, 10]] * 4) == 4

    # randomized check: max number of meetings in progress at any integer time
    import random
    random.seed(7)
    for _ in range(200):
        iv = []
        for _ in range(random.randint(1, 15)):
            a = random.randint(0, 30)
            iv.append([a, a + random.randint(1, 10)])
        brute = max(sum(1 for a, b in iv if a <= t < b) for t in range(0, 41))
        assert s.minMeetingRooms([x[:] for x in iv]) == brute
    print("All tests passed!")
```
