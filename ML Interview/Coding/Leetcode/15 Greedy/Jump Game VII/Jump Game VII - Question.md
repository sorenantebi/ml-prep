---
topic: "Greedy"
difficulty: Medium
leetcode: https://leetcode.com/problems/jump-game-vii/
neetcode: https://neetcode.io/problems/jump-game-vii
---
# Jump Game VII

**Topic:** [[15 Greedy|Greedy]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/jump-game-vii/) · [NeetCode](https://neetcode.io/problems/jump-game-vii)

**Solve it in:** [[Jump Game VII]] · **Answer:** [[Jump Game VII - Solution]]

## Problem

You are given a binary string `s` (0-indexed) and integers `minJump` and `maxJump`. You start at index `0`, which is guaranteed to be `'0'`. From index `i` you may jump to index `j` if:

- `i + minJump <= j <= min(i + maxJump, s.length - 1)`, and
- `s[j] == '0'`.

Return `true` if you can reach index `s.length - 1`, otherwise `false`.

## Examples

**Example 1**
```text
Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation: 0 -> 3 -> 5
```

**Example 2**
```text
Input: s = "01101110", minJump = 2, maxJump = 3
Output: false
```

## Constraints

- `2 <= s.length <= 10^5`
- `s[i]` is `'0'` or `'1'`, and `s[0] == '0'`
- `1 <= minJump <= maxJump < s.length`

## Starter Code & Test Cases

```python
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        pass  # your code here


if __name__ == "__main__":
    sol = Solution()
    assert sol.canReach("011010", 2, 3) is True
    assert sol.canReach("01101110", 2, 3) is False
    assert sol.canReach("00", 1, 1) is True
    assert sol.canReach("01", 1, 1) is False  # last char is '1'
    assert sol.canReach("0000000", 2, 2) is True
    assert sol.canReach("000000", 2, 2) is False  # only even indices reachable
    assert sol.canReach("0" * 100000, 1, 99999) is True
    assert sol.canReach("00111010", 3, 5) is False
    print("All tests passed!")
```
