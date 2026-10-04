---
topic: "Trees"
difficulty: Medium
leetcode: https://leetcode.com/problems/construct-quad-tree/
neetcode: https://neetcode.io/problems/construct-quad-tree
---
# Construct Quad Tree

**Topic:** [[07 Trees|Trees]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/construct-quad-tree/) · [NeetCode](https://neetcode.io/problems/construct-quad-tree)

**Solve it in:** [[Construct Quad Tree]] · **Answer:** [[Construct Quad Tree - Solution]]

## Problem

You are given an `n x n` matrix `grid` of `0`s and `1`s, where `n` is a power of two. Build a **Quad-Tree** that represents it and return its root.

Each quad-tree node has six attributes: `val` (a boolean), `isLeaf` (a boolean) and four children `topLeft`, `topRight`, `bottomLeft`, `bottomRight`. Construction rules for a (sub)grid:

- If every cell in the region has the same value, the node is a leaf: `isLeaf = True`, `val` = that value, and all four children are `null`.
- Otherwise `isLeaf = False`, `val` may be anything, and the region is split into four equal quadrants, each built recursively into the corresponding child.

LeetCode serializes the output in level order where each node is `[isLeaf, val]` (as `0/1`) and `null` marks a missing child.

## Examples

**Example 1**
```text
Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: the root is internal; its four children are leaves with values 0, 1, 1, 0.
```

**Example 2**
```text
Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],
               [1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: only the top-right quadrant is mixed and gets split further.
```

## Constraints

- `n == grid.length == grid[i].length`
- `n == 2^x` where `0 <= x <= 6`
- `grid[i][j]` is `0` or `1`

## Starter Code & Test Cases

```python
from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def to_nested(node: 'Node'):
    """Test helper: a leaf becomes its value (0/1); an internal node becomes a
    tuple of its four children (TL, TR, BL, BR). Ignores internal nodes' val."""
    if node.isLeaf:
        assert not (node.topLeft or node.topRight or node.bottomLeft or node.bottomRight)
        return int(node.val)
    return tuple(to_nested(c) for c in (node.topLeft, node.topRight, node.bottomLeft, node.bottomRight))


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert to_nested(s.construct([[0, 1], [1, 0]])) == (0, 1, 1, 0)
    g = [[1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 0]]
    assert to_nested(s.construct(g)) == (1, (0, 0, 1, 1), 1, 0)
    assert to_nested(s.construct([[1]])) == 1
    assert to_nested(s.construct([[0]])) == 0
    assert to_nested(s.construct([[1, 1], [1, 1]])) == 1          # uniform -> single leaf
    g4 = [[0] * 4 for _ in range(4)]
    g4[3][3] = 1
    assert to_nested(s.construct(g4)) == (0, 0, 0, (0, 0, 0, 1))
    assert to_nested(s.construct([[0] * 64 for _ in range(64)])) == 0
    print("All tests passed!")
```
