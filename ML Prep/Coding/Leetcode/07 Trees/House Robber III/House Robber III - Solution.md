---
topic: "Trees"
difficulty: Medium
leetcode: https://leetcode.com/problems/house-robber-iii/
neetcode: https://neetcode.io/problems/house-robber-iii
---
# House Robber III - Solution

**Question:** [[House Robber III - Question]] · **Difficulty:** Medium

## Intuition

For each node there are only two states that matter to its parent: the best loot of its subtree **if this node is robbed** and **if it is not**. If we rob the node, its children must be skipped; if we skip it, each child independently contributes its better state. A post-order DFS returning that pair solves it in one pass (tree DP).

## Approach

1. `dfs(node)` returns `(with_node, without_node)`; null gives `(0, 0)`.
2. Get `(lw, lwo)` and `(rw, rwo)` from the children.
3. `with_node = node.val + lwo + rwo` (children must not be robbed).
4. `without_node = max(lw, lwo) + max(rw, rwo)` (children free to choose).
5. Answer is `max(dfs(root))`.

## Code

```python
from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	def rob(self, root: Optional[TreeNode]) -> int:
		def dfs(node):
			if not node:
				return 0, 0
			lw, lwo = dfs(node.left)
			rw, rwo = dfs(node.right)
			with_node = node.val + lwo + rwo            # children must be skipped
			without_node = max(lw, lwo) + max(rw, rwo)  # children choose freely
			return with_node, without_node

		return max(dfs(root))
```

## Complexity

- **Time:** `O(n)` — each node is processed once.
- **Space:** `O(h)` — recursion stack.

## Other Approaches

- **Memoized recursion on grandchildren:** `best(node) = max(node.val + sum(best(grandchildren)), best(left) + best(right))` with a node-keyed cache — Time `O(n)`, Space `O(n)`.
- **Plain recursion without memo:** same recurrence but recomputes subtrees — Time exponential.

## Key Takeaway

Tree DP: have the DFS return a small tuple of states (here "taken / not taken") so the parent can combine children in `O(1)` — the tree analogue of House Robber's `rob/skip` recurrence.
