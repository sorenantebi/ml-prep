---
topic: "Intervals"
difficulty: Hard
leetcode: https://leetcode.com/problems/meeting-rooms-iii/
neetcode: https://neetcode.io/problems/meeting-rooms-iii
---
# Meeting Rooms III - Solution

**Question:** [[Meeting Rooms III - Question]] · **Difficulty:** Hard

## Intuition

Process meetings in order of original start time (this automatically gives priority to earlier meetings when a room frees). Two min-heaps capture the room-selection rules: `available` holds free room numbers (pop gives the lowest), and `busy` holds `(end_time, room)` so the root is the room that frees earliest (ties broken by lower room number).

## Approach

1. Sort meetings by start. Initialize `available = [0..n-1]`, `busy = []`, `count = [0] * n`.
2. For each meeting `[start, end]`: move every room whose end time `<= start` from `busy` back into `available`.
3. If a room is available, pop the lowest one and push `(end, room)` onto `busy`.
4. Otherwise pop the earliest-freeing `(t, room)` from `busy`; the meeting is delayed to start at `t`, so push `(t + (end - start), room)`.
5. Increment `count[room]`. Finally return the index of the maximum count (`list.index` returns the lowest on ties).

## Code

```python
from typing import List
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = list(range(n))       # free rooms, smallest number on top
        busy = []                        # (end_time, room) of occupied rooms
        count = [0] * n

        for start, end in meetings:
            while busy and busy[0][0] <= start:          # release finished rooms
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:                                        # wait for earliest room
                free_time, room = heapq.heappop(busy)
                heapq.heappush(busy, (free_time + end - start, room))
            count[room] += 1

        return count.index(max(count))
```

## Complexity

- **Time:** `O(m log m + m log n)` — sorting the `m` meetings plus heap operations on heaps of size `<= n`.
- **Space:** `O(n)` — the two heaps and the counts (plus sorting space).

## Other Approaches

- **Linear scan over rooms:** keep an array of room free times; for each meeting scan all rooms for the lowest free one or the earliest-freeing one — Time `O(m log m + m · n)`, Space `O(n)`; acceptable since `n <= 100`.

## Key Takeaway

Scheduling with "lowest free resource" and "earliest to finish" rules → two heaps: one of idle resource IDs, one of `(finish_time, id)` for busy resources. Note the delayed meeting's end is `free_time + duration`, which can exceed the original end (use Python ints, or 64-bit in other languages).
