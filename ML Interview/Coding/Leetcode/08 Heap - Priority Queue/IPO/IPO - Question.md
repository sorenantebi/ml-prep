---
topic: "Heap / Priority Queue"
difficulty: Hard
leetcode: https://leetcode.com/problems/ipo/
neetcode: https://neetcode.io/problems/ipo
---
# IPO

**Topic:** [[08 Heap - Priority Queue|Heap / Priority Queue]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/ipo/) · [NeetCode](https://neetcode.io/problems/ipo)

**Solve it in:** [[IPO]] · **Answer:** [[IPO - Solution]]

## Problem

A company wants to raise its capital before going public. It may complete **at most `k` distinct projects**. Project `i` yields a pure profit of `profits[i]` and can only be started if the current capital is at least `capital[i]`. Completing a project adds its profit to the capital (the required capital is not spent).

Starting with capital `w`, choose up to `k` projects (each at most once, one after another) to maximize the final capital, and return that maximum.

## Examples

**Example 1**
```text
Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: do project 0 (capital 0 -> 1), then project 2 (capital 1 -> 4)
```

**Example 2**
```text
Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6
Explanation: projects 0, 1, 2 in that order: 0 -> 1 -> 3 -> 6
```

## Constraints

- `1 <= k <= 10^5`
- `0 <= w <= 10^9`
- `n == profits.length == capital.length`, `1 <= n <= 10^5`
- `0 <= profits[i] <= 10^4`
- `0 <= capital[i] <= 10^9`

## Starter Code & Test Cases

```python
from typing import List
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]) == 4
    assert s.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]) == 6
    # nothing affordable
    assert s.findMaximizedCapital(1, 0, [1, 2, 3], [1, 1, 2]) == 0
    # k larger than the number of projects
    assert s.findMaximizedCapital(10, 0, [1, 2, 3], [0, 1, 2]) == 6
    # pick the most profitable affordable project, not the cheapest
    assert s.findMaximizedCapital(1, 5, [1, 9, 4], [0, 5, 2]) == 14
    # zero-profit projects don't help
    assert s.findMaximizedCapital(2, 1, [0, 0], [0, 1]) == 1
    assert s.findMaximizedCapital(2, 1, [5, 1, 10], [1, 0, 6]) == 16
    print("All tests passed!")
```
