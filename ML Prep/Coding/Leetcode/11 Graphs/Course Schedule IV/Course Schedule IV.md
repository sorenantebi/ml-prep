# Course Schedule IV

There are `numCourses` courses labeled `0` to `numCourses - 1`. `prerequisites[i] = [a, b]` means course `a` must be taken **before** course `b` (note: the opposite direction from Course Schedule I/II). Prerequisites are transitive: if `a` is a prerequisite of `b` and `b` of `c`, then `a` is a prerequisite of `c`.

You are also given `queries`, where `queries[j] = [u, v]` asks whether course `u` is a (direct or indirect) prerequisite of course `v`.

Return a list of booleans `answer` where `answer[j]` is the answer to the `j`-th query. The prerequisite graph has no cycles.

## Example

```text
Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
```

```python

```
