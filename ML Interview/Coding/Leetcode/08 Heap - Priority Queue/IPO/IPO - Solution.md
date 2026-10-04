---
topic: "Heap / Priority Queue"
difficulty: Hard
leetcode: https://leetcode.com/problems/ipo/
neetcode: https://neetcode.io/problems/ipo
---
# IPO - Solution

**Question:** [[IPO - Question]] · **Difficulty:** Hard

## Intuition

Capital never decreases, so once a project becomes affordable it stays affordable. Greedily, at each of the `k` steps we should take the **most profitable project we can currently afford** — taking it only increases capital and unlocks a superset of options. Sort projects by required capital to unlock them incrementally, and keep unlocked profits in a **max-heap**.

## Approach

1. Pair `(capital[i], profits[i])` and sort by capital.
2. Repeat `k` times:
   - Push the profits of all projects with `capital <= w` onto a max-heap (advance a pointer).
   - If the heap is empty, stop — nothing more can be afforded.
   - Pop the largest profit and add it to `w`.
3. Return `w`.

## Code

```python
from typing import List
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        available = []  # max-heap (negated) of profits we can afford
        i = 0
        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(available, -projects[i][1])
                i += 1
            if not available:
                break  # no affordable project left
            w -= heapq.heappop(available)  # add the best profit
        return w
```

## Complexity

- **Time:** `O(n log n + k log n)` — sorting, each project pushed once, at most `k` pops.
- **Space:** `O(n)` — sorted projects and the heap.

## Other Approaches

- **Linear scan each round:** for each of the `k` rounds, scan all unused projects for the best affordable one — Time `O(k * n)`, Space `O(n)` for used flags.

## Key Takeaway

Two-stage greedy with "unlockable" items: sort by unlock threshold (or use a min-heap), move unlocked items into a max-heap by value, and repeatedly take the best.
