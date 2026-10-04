---
topic: "Intervals"
difficulty: Medium
leetcode: https://leetcode.com/problems/insert-interval/
neetcode: https://neetcode.io/problems/insert-new-interval
---
# Insert Interval - Solution

**Question:** [[Insert Interval - Question]] · **Difficulty:** Medium

## Intuition

Because the input is sorted and disjoint, it splits into three consecutive groups relative to `newInterval`: intervals that end before it starts (copy as-is), intervals that overlap it (absorb them by widening `newInterval`), and intervals that start after it ends (copy as-is). One linear scan handles all three.

## Approach

1. Copy every interval with `end < newInterval.start` to the result.
2. While the current interval has `start <= newInterval.end`, merge: `newInterval = [min(starts), max(ends)]`.
3. Append the merged `newInterval`.
4. Copy all remaining intervals.

## Code

```python
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i, n = 0, len(intervals)
        start, end = newInterval

        while i < n and intervals[i][1] < start:     # entirely before
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= end:      # overlapping: absorb
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        res.append([start, end])

        res.extend(intervals[i:])                    # entirely after
        return res
```

## Complexity

- **Time:** `O(n)` — single pass over the intervals.
- **Space:** `O(n)` for the output list; `O(1)` extra besides it.

## Other Approaches

- **Append then Merge Intervals:** add `newInterval`, sort, and run the standard merge — Time `O(n log n)`, Space `O(n)`.
- **Binary search for the insertion window:** find the first/last overlapping indices with `bisect` — still `O(n)` overall because the output must be built.

## Key Takeaway

With sorted, disjoint intervals, think "before / overlapping / after": the overlap condition is `a.start <= b.end and b.start <= a.end`.
