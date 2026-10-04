---
topic: "Heap / Priority Queue"
difficulty: Medium
leetcode: https://leetcode.com/problems/single-threaded-cpu/
neetcode: https://neetcode.io/problems/single-threaded-cpu
---
# Single Threaded CPU - Solution

**Question:** [[Single Threaded CPU - Question]] · **Difficulty:** Medium

## Intuition

This is an event simulation: sort tasks by arrival, and as time advances move every newly arrived task into a **min-heap keyed by `(processingTime, index)`** — exactly the CPU's selection rule. When the heap is empty, jump the clock straight to the next arrival instead of ticking.

## Approach

1. Build `(enqueueTime, processingTime, index)` triples and sort by enqueue time.
2. Keep a pointer `i` into the sorted list, a clock `time`, and an empty min-heap.
3. Loop until all tasks are scheduled:
   - If the heap is empty and the next task hasn't arrived, set `time` to its enqueue time.
   - Push all tasks with `enqueueTime <= time` onto the heap as `(processingTime, index)`.
   - Pop the best task, append its index, and advance `time` by its processing time.

## Code

```python
from typing import List
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        order = sorted((e, p, i) for i, (e, p) in enumerate(tasks))
        heap, res = [], []
        time, i, n = 0, 0, len(tasks)
        while len(res) < n:
            if not heap and time < order[i][0]:
                time = order[i][0]  # CPU idle: fast-forward to next arrival
            while i < n and order[i][0] <= time:
                _, p, idx = order[i]
                heapq.heappush(heap, (p, idx))  # tie-break on index automatically
                i += 1
            p, idx = heapq.heappop(heap)
            res.append(idx)
            time += p
        return res
```

## Complexity

- **Time:** `O(n log n)` — sorting plus one push and one pop per task.
- **Space:** `O(n)` — the sorted list, heap, and output.

## Other Approaches

- **Naive scan:** at each decision point linearly scan all unscheduled, arrived tasks for the best one — Time `O(n^2)`, Space `O(n)`.

## Key Takeaway

For CPU / meeting / event simulations: sort by arrival, feed arrivals into a heap ordered by the selection rule, and fast-forward the clock when idle.
