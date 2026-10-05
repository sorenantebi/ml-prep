---
topic: "Intervals"
difficulty: Hard
leetcode: https://leetcode.com/problems/meeting-rooms-iii/
neetcode: https://neetcode.io/problems/meeting-rooms-iii
---
# Meeting Rooms III

**Topic:** [[16 Intervals|Intervals]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/meeting-rooms-iii/) · [NeetCode](https://neetcode.io/problems/meeting-rooms-iii)

**Solve it in:** [[Meeting Rooms III]] · **Answer:** [[Meeting Rooms III - Solution]]

## Problem

There are `n` rooms numbered `0` to `n - 1` and a list of meetings `meetings[i] = [start_i, end_i]` occupying the half-open time range `[start_i, end_i)`. All start times are distinct. Meetings are assigned to rooms by these rules:

1. A meeting takes the free room with the **lowest number**.
2. If no room is free, the meeting is postponed until a room becomes free; it keeps its original **duration**.
3. When a room frees up, waiting meetings with an **earlier original start time** get it first.

Return the number of the room that hosted the most meetings. If there is a tie, return the lowest room number.

## Examples

**Example 1**
```text
Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
Output: 0
Explanation: [0,10]→room 0, [1,5]→room 1, [2,7] waits and runs [5,10) in room 1,
             [3,4] waits and runs [10,11) in room 0. Both rooms host 2 meetings.
```

**Example 2**
```text
Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
Output: 1
Explanation: rooms 0,1,2 host [1,20], [2,10], [3,5]; [4,9] runs [5,10) in room 2;
             [6,8] runs [10,12) in room 1. Rooms 1 and 2 host 2 meetings each.
```

## Constraints

- `1 <= n <= 100`
- `1 <= meetings.length <= 10^5`
- `meetings[i].length == 2`, `0 <= start_i < end_i <= 5 * 10^5`
- All `start_i` are unique

## Starter Code & Test Cases

```python
from typing import List
import heapq


class Solution:
	def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]) == 0
	assert s.mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]) == 1
	assert s.mostBooked(1, [[0, 1], [1, 2], [5, 6]]) == 0
	assert s.mostBooked(4, [[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]) == 0
	assert s.mostBooked(3, [[0, 100], [1, 2], [3, 4], [5, 6]]) == 1
	assert s.mostBooked(2, [[0, 10], [1, 11], [2, 12], [3, 13], [4, 14]]) == 0

	# randomized check against a straightforward O(n * m) simulation
	def brute(n, meetings):
		free_at = [0] * n
		count = [0] * n
		for start, end in sorted(meetings):
			dur = end - start
			idle = [r for r in range(n) if free_at[r] <= start]
			if idle:
				room = idle[0]
				free_at[room] = end
			else:
				room = min(range(n), key=lambda r: (free_at[r], r))
				free_at[room] += dur
			count[room] += 1
		return count.index(max(count))

	import random
	random.seed(3)
	for _ in range(300):
		n = random.randint(1, 5)
		starts = random.sample(range(0, 60), random.randint(1, 25))
		meetings = [[st, st + random.randint(1, 15)] for st in starts]
		assert s.mostBooked(n, [m[:] for m in meetings]) == brute(n, meetings)
	print("All tests passed!")
```
