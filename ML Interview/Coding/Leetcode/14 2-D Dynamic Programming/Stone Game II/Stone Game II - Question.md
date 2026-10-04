---
topic: "2-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/stone-game-ii/
neetcode: https://neetcode.io/problems/stone-game-ii
---
# Stone Game II

**Topic:** [[14 2-D Dynamic Programming|2-D Dynamic Programming]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/stone-game-ii/) · [NeetCode](https://neetcode.io/problems/stone-game-ii)

**Solve it in:** [[Stone Game II]] · **Answer:** [[Stone Game II - Solution]]

## Problem

Piles of stones are arranged in a row, with `piles[i]` stones in pile `i`. Alice and Bob alternate turns, Alice first. A value `M` starts at `1`.

On each turn, the current player takes **all** stones from the first `X` remaining piles, where `1 <= X <= 2M`. Afterwards `M` becomes `max(M, X)`. The game ends when all piles are taken.

Both players play optimally to maximize their own stones. Return the maximum number of stones Alice can collect.

## Examples

**Example 1**
```text
Input: piles = [2,7,9,4,4]
Output: 10
Explanation: Alice takes 1 pile (2), Bob takes 2 (7+9), Alice takes the last 2 (4+4) -> 2+4+4 = 10.
```

**Example 2**
```text
Input: piles = [1,2,3,4,5,100]
Output: 104
```

## Constraints

- `1 <= piles.length <= 100`
- `1 <= piles[i] <= 10^4`

## Starter Code & Test Cases

```python
from typing import List
from functools import lru_cache


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.stoneGameII([2, 7, 9, 4, 4]) == 10
    assert s.stoneGameII([1, 2, 3, 4, 5, 100]) == 104
    assert s.stoneGameII([5]) == 5
    assert s.stoneGameII([3, 4]) == 7  # take both piles with X = 2
    assert s.stoneGameII([1, 1, 1]) == 2
    assert s.stoneGameII([10, 1, 1, 1]) == 11
    assert s.stoneGameII([1] * 100) > 0
    print("All tests passed!")
```
