# Minimum Height Trees

A tree is an undirected, connected, acyclic graph. You are given a tree of `n` nodes labeled `0` to `n - 1` as a list of `n - 1` `edges`, where `edges[i] = [a, b]`.

You may pick any node as the root. The height of the rooted tree is the number of edges on the longest downward path from the root to a leaf. Among all possible roots, those that yield the minimum height produce **minimum height trees (MHTs)**.

Return the labels of all roots that produce MHTs, in any order.

## Example

```text
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: Rooting at node 1 gives height 1; any other root gives height 2.
```

```python

```
