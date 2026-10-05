---
topic: "Advanced Graphs"
difficulty: Hard
leetcode: https://leetcode.com/problems/reconstruct-itinerary/
neetcode: https://neetcode.io/problems/reconstruct-flight-path
---
# Reconstruct Itinerary - Solution

**Question:** [[Reconstruct Itinerary - Question]] · **Difficulty:** Hard

## Intuition

Using every ticket exactly once is an **Eulerian path** in a directed multigraph. Hierholzer's algorithm finds one: walk greedily along unused edges, and when you get stuck at a node, add it to the front of the route. Visiting neighbours in lexicographic order makes the result the smallest itinerary, because dead-end branches end up appended last in the final ordering.

## Approach

1. Build an adjacency list; sort each list in **reverse** so `pop()` returns the smallest destination in `O(1)`.
2. Iterative DFS with a stack starting at `"JFK"`.
3. While the top of the stack still has outgoing tickets, pop the smallest one and push the destination.
4. When the top has no tickets left, pop it into the `route`.
5. `route` is built in reverse; return `route[::-1]`.

## Code

```python
from typing import List
from collections import defaultdict


class Solution:
	def findItinerary(self, tickets: List[List[str]]) -> List[str]:
		graph = defaultdict(list)
		for src, dst in sorted(tickets, reverse=True):
			graph[src].append(dst)  # reverse-sorted so pop() yields the smallest

		stack, route = ["JFK"], []
		while stack:
			node = stack[-1]
			if graph[node]:
				stack.append(graph[node].pop())  # use the smallest remaining ticket
			else:
				route.append(stack.pop())  # stuck: node is finished (post-order)
		return route[::-1]
```

## Complexity

- **Time:** `O(E log E)` — dominated by sorting the tickets; the traversal itself is `O(E)`.
- **Space:** `O(E)` — adjacency lists, stack, and route.

## Other Approaches

- **Backtracking DFS:** try destinations in sorted order, undo when you get stuck before using all tickets — Time exponential in the worst case, Space `O(E)`.

## Key Takeaway

"Use every edge exactly once" means Eulerian path: Hierholzer's post-order DFS (append when stuck, reverse at the end) handles dead ends without backtracking.
