---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/clone-graph/
neetcode: https://neetcode.io/problems/clone-graph
---
# Clone Graph

**Topic:** [[11 Graphs|Graphs]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/clone-graph/) · [NeetCode](https://neetcode.io/problems/clone-graph)

**Solve it in:** [[Clone Graph]] · **Answer:** [[Clone Graph - Solution]]

## Problem

You are given a reference to one node of a connected, undirected graph. Return a **deep copy** (clone) of the whole graph.

Each node has an integer `val` and a list `neighbors` of its adjacent nodes:

```text
class Node:
    val: int
    neighbors: List[Node]
```

For testing, node values are `1..n` and equal to their 1-based index; the graph is described as an adjacency list where entry `i` lists the neighbors of node `i + 1`. The given node is always the node with `val = 1` (or `None` for an empty graph). The returned clone must contain completely new node objects with the same structure — no node of the original graph may appear in the copy.

## Examples

**Example 1**
```text
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: 4 nodes in a cycle 1-2-3-4-1.
```

**Example 2**
```text
Input: adjList = [[]]
Output: [[]]
Explanation: A single node with no neighbors.
```

**Example 3**
```text
Input: adjList = []
Output: []
Explanation: Empty graph.
```

## Constraints

- Number of nodes is in the range `[0, 100]`
- `1 <= Node.val <= 100`, all values are unique
- No repeated edges and no self-loops
- The graph is connected and all nodes are reachable from the given node

## Starter Code & Test Cases

```python
from typing import List, Optional


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def build_graph(adj: List[List[int]]) -> Optional[Node]:
    """Build a graph from a 1-indexed adjacency list; return node 1 (or None)."""
    if not adj:
        return None
    nodes = [Node(i + 1) for i in range(len(adj))]
    for i, nbrs in enumerate(adj):
        nodes[i].neighbors = [nodes[j - 1] for j in nbrs]
    return nodes[0]


def graph_to_adj(node: Optional[Node]) -> List[List[int]]:
    """Serialize a graph back to an adjacency list (collects all reachable nodes)."""
    if node is None:
        return []
    seen = {node.val: node}
    stack = [node]
    while stack:
        cur = stack.pop()
        for nb in cur.neighbors:
            if nb.val not in seen:
                seen[nb.val] = nb
                stack.append(nb)
    return [[nb.val for nb in seen[v].neighbors] for v in sorted(seen)]


def all_nodes(node: Optional[Node]) -> set:
    """Return the set of ids of all node objects reachable from node."""
    if node is None:
        return set()
    ids, stack, seen = set(), [node], {id(node)}
    while stack:
        cur = stack.pop()
        ids.add(id(cur))
        for nb in cur.neighbors:
            if id(nb) not in seen:
                seen.add(id(nb))
                stack.append(nb)
    return ids


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    cases = [
        [[2, 4], [1, 3], [2, 4], [1, 3]],
        [[]],
        [],
        [[2], [1]],
        [[2, 3, 4], [1, 3, 4], [1, 2, 4], [1, 2, 3]],
        [[2], [1, 3], [2, 4], [3, 5], [4]],
    ]
    for adj in cases:
        original = build_graph(adj)
        clone = s.cloneGraph(original)
        assert graph_to_adj(clone) == adj
        # deep copy: no shared node objects
        assert all_nodes(original).isdisjoint(all_nodes(clone))
        # original graph is untouched
        assert graph_to_adj(original) == adj
    print("All tests passed!")
```
