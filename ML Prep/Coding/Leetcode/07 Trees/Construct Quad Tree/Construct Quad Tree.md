# Construct Quad Tree

You are given an `n x n` matrix `grid` of `0`s and `1`s, where `n` is a power of two. Build a **Quad-Tree** that represents it and return its root.

Each quad-tree node has six attributes: `val` (a boolean), `isLeaf` (a boolean) and four children `topLeft`, `topRight`, `bottomLeft`, `bottomRight`. Construction rules for a (sub)grid:

- If every cell in the region has the same value, the node is a leaf: `isLeaf = True`, `val` = that value, and all four children are `null`.
- Otherwise `isLeaf = False`, `val` may be anything, and the region is split into four equal quadrants, each built recursively into the corresponding child.

LeetCode serializes the output in level order where each node is `[isLeaf, val]` (as `0/1`) and `null` marks a missing child.

## Example

```text
Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: the root is internal; its four children are leaves with values 0, 1, 1, 0.
```

```python

```
