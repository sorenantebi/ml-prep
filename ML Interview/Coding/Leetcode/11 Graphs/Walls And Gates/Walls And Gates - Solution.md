---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/walls-and-gates/
neetcode: https://neetcode.io/problems/islands-and-treasure
---
# Walls And Gates - Solution

**Question:** [[Walls And Gates - Question]] · **Difficulty:** Medium

## Intuition

We want, for every room, the shortest distance to *any* gate. Running a BFS from each room (or each gate separately) repeats work. Instead, do a **multi-source BFS**: start with all gates in the queue at distance 0. BFS expands in rings of increasing distance, so the first time a room is reached is via its nearest gate.

## Approach

1. Enqueue the coordinates of every gate (`0`).
2. Pop a cell `(r, c)`; for each 4-directional neighbor that is an empty room (`INF`), set it to `rooms[r][c] + 1` and enqueue it.
3. Walls (`-1`), gates, and already-filled rooms are never `INF`, so they are skipped automatically — the grid doubles as the visited set.
4. Rooms never reached remain `INF`.

## Code

```python
from collections import deque
from typing import List

INF = 2**31 - 1


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return
        rows, cols = len(rooms), len(rooms[0])
        q = deque((r, c) for r in range(rows) for c in range(cols) if rooms[r][c] == 0)
        while q:
            r, c = q.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                # only unvisited empty rooms are still INF
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))
```

## Complexity

- **Time:** `O(m * n)` — every cell is enqueued at most once.
- **Space:** `O(m * n)` — the BFS queue in the worst case.

## Other Approaches

- **BFS/DFS from each gate separately:** relax distances with `min` from every gate — Time `O(k * m * n)` for `k` gates, Space `O(m * n)`.
- **BFS from each empty room:** search outward until a gate is found — Time `O((m * n)^2)`, Space `O(m * n)`.

## Key Takeaway

"Distance to the nearest of many sources" → multi-source BFS: seed the queue with all sources at once.
