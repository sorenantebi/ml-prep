---
topic: "Trees"
difficulty: Easy
leetcode: https://leetcode.com/problems/same-tree/
neetcode: https://neetcode.io/problems/same-binary-tree
---
# Same Tree

**Topic:** [[07 Trees|Trees]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/same-tree/) · [NeetCode](https://neetcode.io/problems/same-binary-tree)

**Solve it in:** [[Same Tree]] · **Answer:** [[Same Tree - Solution]]

## Problem

Given the roots `p` and `q` of two binary trees, return `true` if the trees are identical — same shape and equal values at every corresponding node — and `false` otherwise. Two empty trees are identical.

## Examples

**Example 1**
```text
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

**Example 2**
```text
Input: p = [1,2], q = [1,null,2]
Output: false
```

**Example 3**
```text
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

## Constraints

- The number of nodes in each tree is in the range `[0, 100]`
- `-10^4 <= Node.val <= 10^4`

## Starter Code & Test Cases

```python
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a tree from a LeetCode-style level-order list (None = missing child)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Serialize a tree to a LeetCode-style level-order list (trailing Nones trimmed)."""
    if not root:
        return []
    out, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    return out


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.isSameTree(build_tree([1, 2, 3]), build_tree([1, 2, 3])) is True
    assert s.isSameTree(build_tree([1, 2]), build_tree([1, None, 2])) is False
    assert s.isSameTree(build_tree([1, 2, 1]), build_tree([1, 1, 2])) is False
    assert s.isSameTree(build_tree([]), build_tree([])) is True
    assert s.isSameTree(build_tree([1]), build_tree([])) is False
    assert s.isSameTree(build_tree([5, 3, 8, 1, None, None, 9]), build_tree([5, 3, 8, 1, None, None, 9])) is True
    assert s.isSameTree(build_tree([5, 3, 8, 1]), build_tree([5, 3, 8, None, 1])) is False
    print("All tests passed!")
```
