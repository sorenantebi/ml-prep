---
topic: "1-D Dynamic Programming"
difficulty: Easy
leetcode: https://leetcode.com/problems/min-cost-climbing-stairs/
neetcode: https://neetcode.io/problems/min-cost-climbing-stairs
---
# Min Cost Climbing Stairs

**Topic:** [[13 1-D Dynamic Programming|1-D Dynamic Programming]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/min-cost-climbing-stairs/) · [NeetCode](https://neetcode.io/problems/min-cost-climbing-stairs)

**Solve it in:** [[Min Cost Climbing Stairs]] · **Answer:** [[Min Cost Climbing Stairs - Solution]]

## Problem

You are given an integer array `cost`, where `cost[i]` is what you pay when you step on stair `i`. After paying for a stair you may climb one or two stairs. You may start on stair `0` or stair `1` (without paying anything to get there).

Return the minimum total cost to reach the top, which is the position just past the last stair (index `len(cost)`).

## Examples

**Example 1**
```text
Input: cost = [10,15,20]
Output: 15
Explanation: Start at index 1, pay 15, jump two steps to the top.
```

**Example 2**
```text
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
```

## Constraints

- `2 <= cost.length <= 1000`
- `0 <= cost[i] <= 999`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.minCostClimbingStairs([10,15,20]) == 15
    assert s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]) == 6
    assert s.minCostClimbingStairs([0,0]) == 0
    assert s.minCostClimbingStairs([5,3]) == 3
    assert s.minCostClimbingStairs([1,2,3]) == 2
    assert s.minCostClimbingStairs([0,1,2,2]) == 2
    print("All tests passed!")
```
