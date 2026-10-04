---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/evaluate-division/
neetcode: https://neetcode.io/problems/evaluate-division
---
# Evaluate Division

**Topic:** [[11 Graphs|Graphs]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/evaluate-division/) · [NeetCode](https://neetcode.io/problems/evaluate-division)

**Solve it in:** [[Evaluate Division]] · **Answer:** [[Evaluate Division - Solution]]

## Problem

You are given `equations`, where `equations[i] = [A, B]` are variable names, and `values[i]` is a real number such that `A / B = values[i]`.

You are also given `queries`, where `queries[j] = [C, D]` asks for the value of `C / D`.

Return a list with the answer to each query, derived from the given equations. If an answer cannot be determined — for example, a variable never appears in any equation, or `C` and `D` are not connected through the equations — return `-1.0` for that query. Note that `X / X` is `1.0` only if `X` appears in some equation; otherwise it is `-1.0`.

The input is guaranteed to be consistent (no contradictions, no division by zero).

## Examples

**Example 1**
```text
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0],
       queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.0,0.5,-1.0,1.0,-1.0]
Explanation: a/b = 2, b/c = 3 => a/c = 6, b/a = 0.5; "e" and "x" are unknown.
```

**Example 2**
```text
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"]]
Output: [0.5,2.0,-1.0]
```

## Constraints

- `1 <= equations.length <= 20`, `equations[i].length == 2`
- `1 <= A.length, B.length <= 5`, lowercase letters and digits
- `values.length == equations.length`, `0.0 < values[i] <= 20.0`
- `1 <= queries.length <= 20`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]) -> List[float]:
        pass  # your code here


def close(a: List[float], b: List[float]) -> bool:
    return len(a) == len(b) and all(abs(x - y) < 1e-5 for x, y in zip(a, b))


if __name__ == "__main__":
    s = Solution()
    assert close(s.calcEquation([["a","b"],["b","c"]], [2.0, 3.0],
                                [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]),
                 [6.0, 0.5, -1.0, 1.0, -1.0])
    assert close(s.calcEquation([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]),
                 [0.5, 2.0, -1.0, -1.0])
    assert close(s.calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5, 2.5, 5.0],
                                [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]),
                 [3.75, 0.4, 5.0, 0.2])
    # disconnected components
    assert close(s.calcEquation([["a","b"],["c","d"]], [2.0, 4.0], [["a","d"],["d","c"],["b","b"]]),
                 [-1.0, 0.25, 1.0])
    # longer chain
    assert close(s.calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], [3.0, 4.0, 5.0, 6.0],
                                [["x1","x5"],["x5","x2"],["x2","x4"]]),
                 [360.0, 1 / 120.0, 20.0])
    print("All tests passed!")
```
