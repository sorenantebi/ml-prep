---
topic: "1-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/decode-ways/
neetcode: https://neetcode.io/problems/decode-ways
---
# Decode Ways - Solution

**Question:** [[Decode Ways - Question]] · **Difficulty:** Medium

## Intuition

Let `dp[i]` be the number of ways to decode the prefix `s[:i]`. The last piece is either one digit (valid if it isn't `'0'`) or two digits (valid if between `10` and `26`), so `dp[i] = dp[i-1]·[one-digit ok] + dp[i-2]·[two-digit ok]`. Only two previous values are needed.

## Approach

1. `prev2 = dp[i-2]`, `prev1 = dp[i-1]`; start with `dp[0] = 1` (empty prefix) so `prev1 = 1`, `prev2 = 0`.
2. For each position `i` (1-based), `cur = 0`; if `s[i-1] != '0'` add `prev1`; if `i >= 2` and `10 <= int(s[i-2:i]) <= 26` add `prev2`.
3. Shift and continue; return `prev1`.

## Code

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        prev2, prev1 = 0, 1  # dp[i-2], dp[i-1]; dp[0] = 1 for the empty prefix
        for i in range(1, len(s) + 1):
            cur = 0
            if s[i - 1] != "0":
                cur += prev1  # last piece is a single digit 1-9
            if i >= 2 and 10 <= int(s[i - 2:i]) <= 26:
                cur += prev2  # last piece is a two-digit code 10-26
            prev2, prev1 = prev1, cur
        return prev1
```

## Complexity

- **Time:** `O(n)` — one pass with constant work per character.
- **Space:** `O(1)` — two rolling values.

## Other Approaches

- **Memoised recursion:** `f(i)` = ways to decode `s[i:]`, branching on one or two digits — Time `O(n)`, Space `O(n)`.

## Key Takeaway

Decode Ways is Climbing Stairs with validity checks on each step; zeros are the trap — a `'0'` can only be the second digit of `10` or `20`.
