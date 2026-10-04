---
topic: "Heap / Priority Queue"
difficulty: Medium
leetcode: https://leetcode.com/problems/longest-happy-string/
neetcode: https://neetcode.io/problems/longest-happy-string
---
# Longest Happy String

**Topic:** [[08 Heap - Priority Queue|Heap / Priority Queue]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/longest-happy-string/) · [NeetCode](https://neetcode.io/problems/longest-happy-string)

**Solve it in:** [[Longest Happy String]] · **Answer:** [[Longest Happy String - Solution]]

## Problem

A string is called *happy* if it uses only the letters `'a'`, `'b'`, `'c'`, never contains `"aaa"`, `"bbb"`, or `"ccc"` as a substring, and uses at most `a` copies of `'a'`, at most `b` copies of `'b'`, and at most `c` copies of `'c'`.

Given the integers `a`, `b`, `c`, return the **longest possible** happy string. If several longest strings exist, return any of them. If none can be formed, return `""`.

## Examples

**Example 1**
```text
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" is also a valid answer of length 8
```

**Example 2**
```text
Input: a = 7, b = 1, c = 0
Output: "aabaa"
```

**Example 3**
```text
Input: a = 0, b = 0, c = 0
Output: ""
```

## Constraints

- `0 <= a, b, c <= 100`
- `a + b + c > 0`

## Starter Code & Test Cases

```python
import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pass  # your code here


def check(a: int, b: int, c: int, out: str, expected_len: int) -> bool:
    return (
        len(out) == expected_len
        and set(out) <= set("abc")
        and out.count("a") <= a and out.count("b") <= b and out.count("c") <= c
        and "aaa" not in out and "bbb" not in out and "ccc" not in out
    )


if __name__ == "__main__":
    s = Solution()
    cases = [
        (1, 1, 7, 8),
        (7, 1, 0, 5),
        (0, 0, 0, 0),
        (0, 0, 5, 2),
        (2, 2, 1, 5),
        (4, 4, 4, 12),
        (1, 0, 0, 1),
        (0, 8, 11, 19),
        (100, 2, 3, 17),
    ]
    for a, b, c, exp in cases:
        out = s.longestDiverseString(a, b, c)
        assert check(a, b, c, out, exp), (a, b, c, out)
    print("All tests passed!")
```
