---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/open-the-lock/
neetcode: https://neetcode.io/problems/open-the-lock
---
# Open The Lock - Solution

**Question:** [[Open The Lock - Question]] · **Difficulty:** Medium

## Intuition

Each of the 10,000 combinations is a node; two nodes are connected if they differ by one wheel turn. All moves cost 1, so the shortest number of moves is found by **BFS** from `"0000"`, treating dead ends as removed nodes.

## Approach

1. If `"0000"` is a dead end, return `-1`; if it is the target, return `0`.
2. BFS from `"0000"` with a `visited` set pre-filled with the dead ends.
3. For each popped combination, generate its 8 neighbors (each of 4 wheels turned ±1 with wraparound).
4. Return the current distance + 1 when a neighbor equals `target`; otherwise mark unvisited neighbors and enqueue them.
5. If BFS exhausts, return `-1`.

## Code

```python
from collections import deque
from typing import List


class Solution:
	def openLock(self, deadends: List[str], target: str) -> int:
		visited = set(deadends)  # dead ends behave like already-visited (blocked) nodes
		if "0000" in visited:
			return -1
		if target == "0000":
			return 0
		visited.add("0000")
		q = deque([("0000", 0)])
		while q:
			combo, moves = q.popleft()
			for i in range(4):
				d = int(combo[i])
				for nd in ((d + 1) % 10, (d - 1) % 10):
					nxt = combo[:i] + str(nd) + combo[i + 1:]
					if nxt == target:
						return moves + 1
					if nxt not in visited:
						visited.add(nxt)
						q.append((nxt, moves + 1))
		return -1
```

## Complexity

- **Time:** `O(10^4 * 8 * 4)` = `O(N^A * A^2)` in general (`N` digits, `A` wheels) — every state is visited once, generating 8 neighbors of length 4; plus `O(D)` to build the dead-end set.
- **Space:** `O(10^4 + D)` — visited set and queue.

## Other Approaches

- **Bidirectional BFS:** expand alternately from start and target, always growing the smaller frontier, until they meet — same worst case, but typically explores far fewer states.

## Key Takeaway

When a puzzle has a small, enumerable state space and unit-cost moves, model states as graph nodes and BFS for the minimum number of moves; obstacles simply pre-populate the visited set.
