---
topic: "Math & Geometry"
difficulty: Easy
leetcode: https://leetcode.com/problems/greatest-common-divisor-of-strings/
neetcode: https://neetcode.io/problems/greatest-common-divisor-of-strings
---
# Greatest Common Divisor of Strings - Solution

**Question:** [[Greatest Common Divisor of Strings - Question]] · **Difficulty:** Easy

## Intuition

If both strings are built from the same repeating block, then gluing them together in either order gives the same string: `str1 + str2 == str2 + str1`. When that holds, the longest common divisor has length `gcd(len(str1), len(str2))`, so its prefix of that length is the answer. When it doesn't hold, there is no common divisor.

## Approach

1. If `str1 + str2 != str2 + str1`, return `""`.
2. Otherwise compute `g = gcd(len(str1), len(str2))`.
3. Return `str1[:g]`.

## Code

```python
from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # A shared repeating unit exists iff concatenation commutes
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:gcd(len(str1), len(str2))]
```

## Complexity

- **Time:** `O(m + n)`: building and comparing the two concatenations is linear, and the gcd costs `O(log min(m, n))`.
- **Space:** `O(m + n)`: for the temporary concatenated strings.

## Other Approaches

- **Try every candidate length:** for each `L` from `min(m, n)` down to 1 that divides both lengths, check whether `str1[:L]` repeated builds both strings. Time `O(min(m, n) * (m + n))`, Space `O(m + n)`.

## Key Takeaway

`a + b == b + a` is the standard test for "these two strings share a common period". Once it passes, string gcd becomes integer gcd on the lengths.
