---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/open-the-lock/
neetcode: https://neetcode.io/problems/open-the-lock
---
# Open The Lock

**Topic:** [[11 Graphs|Graphs]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/open-the-lock/) · [NeetCode](https://neetcode.io/problems/open-the-lock)

**Solve it in:** [[Open The Lock]] · **Answer:** [[Open The Lock - Solution]]

## Problem

A lock has 4 circular wheels, each showing a digit `'0'`–`'9'`. A move turns exactly one wheel by one slot, either up or down; the wheels wrap around (`'9'` → `'0'` and `'0'` → `'9'`). The lock starts at `"0000"`.

You are given a list `deadends`: if the lock ever shows one of these combinations, it jams and can no longer be turned. You are also given a `target` combination.

Return the minimum number of moves needed to reach `target` from `"0000"` without ever passing through a dead end, or `-1` if it is impossible.

## Examples

**Example 1**
```text
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: e.g. "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
```

**Example 2**
```text
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: Turn the last wheel down once: "0000" -> "0009".
```

**Example 3**
```text
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: All neighbors of the target are dead ends.
```

## Constraints

- `1 <= deadends.length <= 500`
- `deadends[i].length == 4`, `target.length == 4`
- `target` is not in `deadends`
- All strings consist only of digits

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.openLock(["0201","0101","0102","1212","2002"], "0202") == 6
    assert s.openLock(["8888"], "0009") == 1
    assert s.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888") == -1
    assert s.openLock(["0000"], "8888") == -1  # start itself is dead
    assert s.openLock(["1111"], "0000") == 0
    assert s.openLock(["1234"], "5555") == 20
    assert s.openLock(["0001", "0009"], "0002") == 4  # must detour via another wheel
    print("All tests passed!")
```
