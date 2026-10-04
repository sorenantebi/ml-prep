---
topic: "Advanced Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/network-delay-time/
neetcode: https://neetcode.io/problems/network-delay-time
---
# Network Delay Time

**Topic:** [[12 Advanced Graphs|Advanced Graphs]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/network-delay-time/) · [NeetCode](https://neetcode.io/problems/network-delay-time)

**Solve it in:** [[Network Delay Time]] · **Answer:** [[Network Delay Time - Solution]]

## Problem

There is a network of `n` nodes labelled `1` to `n`. You are given a list `times` of directed edges, where `times[i] = [u, v, w]` means a signal sent from node `u` reaches node `v` after `w` time units.

A signal is sent from node `k`. Return the minimum time needed for **every** node to receive the signal. If at least one node can never receive it, return `-1`.

## Examples

**Example 1**
```text
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
```

**Example 2**
```text
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
```

**Example 3**
```text
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
Explanation: Node 1 is unreachable from node 2.
```

## Constraints

- `1 <= k <= n <= 100`
- `1 <= times.length <= 6000`
- `times[i].length == 3`, `1 <= u, v <= n`, `u != v`
- `0 <= w <= 100`
- All `(u, v)` pairs are unique (no duplicate edges).

## Starter Code & Test Cases

```python
from typing import List
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2
    assert s.networkDelayTime([[1,2,1]], 2, 1) == 1
    assert s.networkDelayTime([[1,2,1]], 2, 2) == -1
    assert s.networkDelayTime([], 1, 1) == 0
    assert s.networkDelayTime([[1,2,1],[2,3,2],[1,3,4]], 3, 1) == 3
    assert s.networkDelayTime([[1,2,1],[2,1,3]], 2, 2) == 3
    assert s.networkDelayTime([[1,2,0],[2,3,0]], 3, 1) == 0
    print("All tests passed!")
```
