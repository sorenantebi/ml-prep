# Find Critical and Pseudo Critical Edges in Minimum Spanning Tree

You are given a connected, undirected, weighted graph with `n` vertices (`0` to `n - 1`) and an array `edges` where `edges[i] = [a_i, b_i, weight_i]`. The index `i` identifies each edge.

A minimum spanning tree (MST) connects all vertices without cycles using the minimum total weight. Classify edges:

- **Critical:** removing the edge from the graph increases the MST weight (or disconnects the graph) — it is in every MST.
- **Pseudo-critical:** the edge appears in some MST but not in all of them.

Return `[critical_indices, pseudo_critical_indices]`. Indices within each list may be in any order.

## Example

```text
Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]
```

```python

```
