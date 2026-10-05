---
topic: "Intervals"
difficulty: Easy
leetcode: https://leetcode.com/problems/meeting-rooms/
neetcode: https://neetcode.io/problems/meeting-schedule
---
# Meeting Rooms

**Topic:** [[16 Intervals|Intervals]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/meeting-rooms/) · [NeetCode](https://neetcode.io/problems/meeting-schedule)

**Solve it in:** [[Meeting Rooms]] · **Answer:** [[Meeting Rooms - Solution]]

## Problem

You are given an array of meeting time intervals `intervals[i] = [start_i, end_i]`. Determine whether a single person could attend every meeting, i.e. whether no two meetings overlap. A meeting that ends at time `t` does not conflict with one starting at time `t`. Return `True` if all meetings can be attended, otherwise `False`.

## Examples

**Example 1**
```text
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Explanation: [0,30] overlaps both other meetings.
```

**Example 2**
```text
Input: intervals = [[7,10],[2,4]]
Output: true
```

**Example 3**
```text
Input: intervals = [[5,8],[8,10]]
Output: true
Explanation: back-to-back meetings are allowed.
```

## Constraints

- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i < end_i <= 10^6`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.canAttendMeetings([[0, 30], [5, 10], [15, 20]]) is False
	assert s.canAttendMeetings([[7, 10], [2, 4]]) is True
	assert s.canAttendMeetings([[5, 8], [8, 10]]) is True
	assert s.canAttendMeetings([]) is True
	assert s.canAttendMeetings([[1, 5]]) is True
	assert s.canAttendMeetings([[1, 5], [4, 6]]) is False
	assert s.canAttendMeetings([[10, 20], [0, 5], [5, 10], [19, 25]]) is False
	assert s.canAttendMeetings([[i, i + 1] for i in range(1000, 0, -1)]) is True
	print("All tests passed!")
```
