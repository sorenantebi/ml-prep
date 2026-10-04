---
topic: "Binary Search"
difficulty: Easy
leetcode: https://leetcode.com/problems/guess-number-higher-or-lower/
neetcode: https://neetcode.io/problems/guess-number-higher-or-lower
---
# Guess Number Higher Or Lower

**Topic:** [[05 Binary Search|Binary Search]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/guess-number-higher-or-lower/) · [NeetCode](https://neetcode.io/problems/guess-number-higher-or-lower)

**Solve it in:** [[Guess Number Higher Or Lower]] · **Answer:** [[Guess Number Higher Or Lower - Solution]]

## Problem

A number `pick` has been chosen from the range `1` to `n` (inclusive). Your job is to find it. You cannot see `pick` directly; instead you can call a predefined API `guess(num)` that returns:

- `-1` if your guess is higher than the picked number (`num > pick`),
- `1` if your guess is lower than the picked number (`num < pick`),
- `0` if your guess is correct (`num == pick`).

Return the picked number.

## Examples

**Example 1**
```text
Input: n = 10, pick = 6
Output: 6
```

**Example 2**
```text
Input: n = 1, pick = 1
Output: 1
```

**Example 3**
```text
Input: n = 2, pick = 1
Output: 1
```

## Constraints

- `1 <= n <= 2^31 - 1`
- `1 <= pick <= n`

## Starter Code & Test Cases

```python
# Mock of the hidden API: the judge keeps `pick` secret.
pick = 0
calls = 0


def set_pick(value: int) -> None:
    global pick, calls
    pick, calls = value, 0


def guess(num: int) -> int:
    global calls
    calls += 1
    if num > pick:
        return -1
    if num < pick:
        return 1
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    for n, p in [(10, 6), (1, 1), (2, 1), (2, 2), (100, 100), (100, 1), (2**31 - 1, 2**31 - 1), (2**31 - 1, 123456789)]:
        set_pick(p)
        assert s.guessNumber(n) == p
        assert calls <= 40, "should use O(log n) guesses"
    print("All tests passed!")
```
