---
topic: "Trees"
difficulty: Easy
leetcode: https://leetcode.com/problems/maximum-depth-of-binary-tree/
neetcode: https://neetcode.io/problems/depth-of-binary-tree
---
# Maximum Depth of Binary Tree - Solution

**Question:** [[Maximum Depth of Binary Tree - Question]] · **Difficulty:** Easy

## Intuition

The depth of a tree is `1 + max(depth(left), depth(right))`. Instead of recursing (which can hit Python's recursion limit on a 10^4-node chain), a level-order BFS counts how many levels exist — that count is the depth.

## Approach

1. If `root` is null, return `0`.
2. Put `root` in a queue and set `depth = 0`.
3. While the queue is non-empty: process exactly the nodes currently in it (one level), enqueue their children, and increment `depth`.
4. Return `depth`.

## Code

```python
from collections import deque
from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	def maxDepth(self, root: Optional[TreeNode]) -> int:
		if not root:
			return 0
		q = deque([root])
		depth = 0
		while q:
			for _ in range(len(q)):     # drain exactly one level
				node = q.popleft()
				if node.left:
					q.append(node.left)
				if node.right:
					q.append(node.right)
			depth += 1
		return depth
```

## Complexity

- **Time:** `O(n)` — each node is enqueued and dequeued once.
- **Space:** `O(w)` — the queue holds at most one level (`w` = max width, up to `n/2`).

## Other Approaches

- **Recursive DFS:** `return 1 + max(maxDepth(left), maxDepth(right))` — Time `O(n)`, Space `O(h)` (may overflow Python's default recursion limit on very deep trees).
- **Iterative DFS with `(node, depth)` stack:** track the max depth seen — Time `O(n)`, Space `O(h)`.

## Key Takeaway

"Height/depth" is the canonical post-order recursion; BFS level counting is the iterative alternative that avoids recursion-depth issues.
