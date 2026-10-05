# Meeting Rooms III

There are `n` rooms numbered `0` to `n - 1` and a list of meetings `meetings[i] = [start_i, end_i]` occupying the half-open time range `[start_i, end_i)`. All start times are distinct. Meetings are assigned to rooms by these rules:

1. A meeting takes the free room with the **lowest number**.
2. If no room is free, the meeting is postponed until a room becomes free; it keeps its original **duration**.
3. When a room frees up, waiting meetings with an **earlier original start time** get it first.

Return the number of the room that hosted the most meetings. If there is a tie, return the lowest room number.

## Example

```text
Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
Output: 0
Explanation: [0,10]→room 0, [1,5]→room 1, [2,7] waits and runs [5,10) in room 1,
             [3,4] waits and runs [10,11) in room 0. Both rooms host 2 meetings.
```

```python

```
