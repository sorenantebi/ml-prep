---
topic: "Advanced Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/network-delay-time/
neetcode: https://neetcode.io/problems/network-delay-time
---
# Network Delay Time - Solution

**Question:** [[Network Delay Time - Question]] · **Difficulty:** Medium

## Intuition

The time for the last node to hear the signal is the largest shortest-path distance from `k`. With non-negative edge weights, Dijkstra's algorithm computes all single-source shortest paths. If some node is never reached, the answer is `-1`.

## Approach

1. Build an adjacency list `u -> [(v, w)]`.
2. Run Dijkstra from `k` with a min-heap of `(time, node)`; record a node's distance the first time it is popped.
3. Skip nodes already finalised; otherwise push all neighbours with `time + w`.
4. If fewer than `n` nodes were finalised return `-1`, otherwise return the maximum distance.

## Code

```python
from typing import List
from collections import defaultdict
import heapq


class Solution:
	def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
		graph = defaultdict(list)
		for u, v, w in times:
			graph[u].append((v, w))

		dist = {}  # node -> finalised shortest time
		heap = [(0, k)]
		while heap:
			t, node = heapq.heappop(heap)
			if node in dist:
				continue  # already finalised with a smaller time
			dist[node] = t
			for nxt, w in graph[node]:
				if nxt not in dist:
					heapq.heappush(heap, (t + w, nxt))

		return max(dist.values()) if len(dist) == n else -1
```

## Complexity

- **Time:** `O(E log E)` — each edge can push one heap entry.
- **Space:** `O(V + E)` — adjacency list, heap and distance map.

## Other Approaches

- **Bellman-Ford:** relax all edges `n - 1` times — Time `O(V·E)`, Space `O(V)`.
- **Floyd-Warshall:** all-pairs shortest paths, then read row `k` — Time `O(V^3)`, Space `O(V^2)`.

## Key Takeaway

"How long until everything is reached" from one source = max of single-source shortest paths; use Dijkstra with a "finalise on first pop" visited set when weights are non-negative.
