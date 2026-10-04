---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/course-schedule-iv/
neetcode: https://neetcode.io/problems/course-schedule-iv
---
# Course Schedule IV

**Topic:** [[11 Graphs|Graphs]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/course-schedule-iv/) · [NeetCode](https://neetcode.io/problems/course-schedule-iv)

**Solve it in:** [[Course Schedule IV]] · **Answer:** [[Course Schedule IV - Solution]]

## Problem

There are `numCourses` courses labeled `0` to `numCourses - 1`. `prerequisites[i] = [a, b]` means course `a` must be taken **before** course `b` (note: the opposite direction from Course Schedule I/II). Prerequisites are transitive: if `a` is a prerequisite of `b` and `b` of `c`, then `a` is a prerequisite of `c`.

You are also given `queries`, where `queries[j] = [u, v]` asks whether course `u` is a (direct or indirect) prerequisite of course `v`.

Return a list of booleans `answer` where `answer[j]` is the answer to the `j`-th query. The prerequisite graph has no cycles.

## Examples

**Example 1**
```text
Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
```

**Example 2**
```text
Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
```

**Example 3**
```text
Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]
```

## Constraints

- `2 <= numCourses <= 100`
- `0 <= prerequisites.length <= numCourses * (numCourses - 1) / 2`
- `prerequisites[i] = [a, b]`, `a != b`, all pairs unique, no cycles
- `1 <= queries.length <= 10^4`, `queries[j] = [u, v]`, `u != v`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]],
                            queries: List[List[int]]) -> List[bool]:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.checkIfPrerequisite(2, [[1,0]], [[0,1],[1,0]]) == [False, True]
    assert s.checkIfPrerequisite(2, [], [[1,0],[0,1]]) == [False, False]
    assert s.checkIfPrerequisite(3, [[1,2],[1,0],[2,0]], [[1,0],[1,2]]) == [True, True]
    assert s.checkIfPrerequisite(4, [[0,1],[1,2],[2,3]], [[0,3],[3,0],[1,3],[2,1]]) == [True, False, True, False]
    assert s.checkIfPrerequisite(5, [[0,1],[0,2],[3,4]], [[0,4],[3,4],[1,2],[0,2]]) == [False, True, False, True]
    assert s.checkIfPrerequisite(4, [[2,3],[2,1],[0,3],[0,1]], [[0,1],[0,3],[2,3],[3,0],[2,0],[0,2]]) == \
        [True, True, True, False, False, False]
    print("All tests passed!")
```
