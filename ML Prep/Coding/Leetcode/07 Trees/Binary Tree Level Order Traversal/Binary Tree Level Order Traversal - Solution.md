---
topic: "Trees"
difficulty: Medium
leetcode: https://leetcode.com/problems/binary-tree-level-order-traversal/
neetcode: https://neetcode.io/problems/level-order-traversal-of-binary-tree
---
# Binary Tree Level Order Traversal - Solution

**Question:** [[Binary Tree Level Order Traversal - Question]] · **Difficulty:** Medium

## Intuition

Breadth-first search naturally visits nodes level by level. If, at the start of each round, we record the queue's current length, exactly that many pops belong to the current level — the children they enqueue form the next level.

## Approach

1. If `root` is null, return `[]`; otherwise start a queue with `root`.
2. While the queue is non-empty, let `size = len(queue)`.
3. Pop `size` nodes, collecting their values into `level` and enqueueing their non-null children.
4. Append `level` to the result.
5. Return the result.

## Code

```python
from collections import deque
from typing import List, Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
		if not root:
			return []
		res, q = [], deque([root])
		while q:
			level = []
			for _ in range(len(q)):     # snapshot of this level's size
				node = q.popleft()
				level.append(node.val)
				if node.left:
					q.append(node.left)
				if node.right:
					q.append(node.right)
			res.append(level)
		return res
```

## Complexity

- **Time:** `O(n)` — each node is enqueued and dequeued once.
- **Space:** `O(w)` — the queue holds at most one level (up to `n/2` nodes); output not counted.

## Other Approaches

- **DFS with depth index:** preorder DFS passing `depth`; append `node.val` to `res[depth]` (creating it when `depth == len(res)`) — Time `O(n)`, Space `O(h)`.

## Key Takeaway

The "`for _ in range(len(q))`" BFS loop is the standard way to process a tree (or grid/graph) one level at a time — reused in right side view, zigzag order, minimum depth, and shortest-path problems.
