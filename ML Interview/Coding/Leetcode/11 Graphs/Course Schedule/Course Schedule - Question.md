---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/course-schedule/
neetcode: https://neetcode.io/problems/course-schedule
---
# Course Schedule

**Topic:** [[11 Graphs|Graphs]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/course-schedule/) · [NeetCode](https://neetcode.io/problems/course-schedule)

**Solve it in:** [[Course Schedule]] · **Answer:** [[Course Schedule - Solution]]

## Problem

There are `numCourses` courses labeled `0` to `numCourses - 1`. You are given `prerequisites`, where `prerequisites[i] = [a, b]` means course `b` must be completed before course `a`.

Return `true` if it is possible to finish all courses, otherwise return `false`. (This is impossible exactly when the prerequisites contain a cycle.)

## Examples

**Example 1**
```text
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: Take course 0, then course 1.
```

**Example 2**
```text
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: Each course requires the other.
```

## Constraints

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`, `0 <= a, b < numCourses`
- All pairs are unique

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.canFinish(2, [[1,0]]) is True
    assert s.canFinish(2, [[1,0],[0,1]]) is False
    assert s.canFinish(1, []) is True
    assert s.canFinish(3, [[1,0],[2,1]]) is True
    assert s.canFinish(3, [[1,0],[2,1],[0,2]]) is False
    assert s.canFinish(5, [[1,0],[2,0],[3,1],[3,2],[4,3]]) is True  # diamond, no cycle
    assert s.canFinish(4, [[1,0],[2,3],[3,2]]) is False  # cycle in a separate component
    assert s.canFinish(2000, [[i + 1, i] for i in range(1999)]) is True  # long chain
    print("All tests passed!")
```
