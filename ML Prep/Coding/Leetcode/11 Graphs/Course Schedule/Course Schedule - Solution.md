---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/course-schedule/
neetcode: https://neetcode.io/problems/course-schedule
---
# Course Schedule - Solution

**Question:** [[Course Schedule - Question]] · **Difficulty:** Medium

## Intuition

Courses and prerequisites form a directed graph; all courses can be finished iff the graph has no cycle, i.e. a topological order exists. **Kahn's algorithm** builds that order by repeatedly taking courses with no remaining prerequisites (in-degree 0). If some courses are never freed, they sit on or behind a cycle.

## Approach

1. Build an adjacency list `b -> a` for each pair `[a, b]` and compute each course's in-degree.
2. Enqueue all courses with in-degree 0.
3. Pop a course, count it as taken, and decrement the in-degree of each dependent course; enqueue any that reach 0.
4. Return `taken == numCourses`.

## Code

```python
from collections import deque
from typing import List


class Solution:
	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		graph = [[] for _ in range(numCourses)]
		indeg = [0] * numCourses
		for course, pre in prerequisites:
			graph[pre].append(course)
			indeg[course] += 1

		q = deque(i for i in range(numCourses) if indeg[i] == 0)
		taken = 0
		while q:
			cur = q.popleft()
			taken += 1
			for nxt in graph[cur]:
				indeg[nxt] -= 1
				if indeg[nxt] == 0:  # all prerequisites of nxt are done
					q.append(nxt)
		return taken == numCourses  # leftover courses are stuck in a cycle
```

## Complexity

- **Time:** `O(V + E)` — each course and each prerequisite edge is processed once.
- **Space:** `O(V + E)` — adjacency list, in-degree array, and queue.

## Other Approaches

- **DFS with three colors (unvisited / visiting / done):** a back edge to a "visiting" node means a cycle — Time `O(V + E)`, Space `O(V + E)` (recursion stack up to `V`).

## Key Takeaway

"Can all tasks with dependencies be completed?" = cycle detection in a directed graph; Kahn's BFS topological sort answers it by checking whether every node gets processed.
