---
topic: "Two Pointers"
difficulty: Easy
leetcode: https://leetcode.com/problems/valid-palindrome-ii/
neetcode: https://neetcode.io/problems/valid-palindrome-ii
---
# Valid Palindrome II - Solution

**Question:** [[Valid Palindrome II - Question]] · **Difficulty:** Easy

## Intuition

Compare characters from both ends. As long as they match, the deletion is not needed. At the first mismatch the single allowed deletion must remove one of those two characters, so check whether either remaining inner substring (skip left or skip right) is a plain palindrome.

## Approach

1. Move `l` and `r` inward while `s[l] == s[r]`.
2. On the first mismatch, return `isPal(l + 1, r) or isPal(l, r - 1)`.
3. If the pointers meet without a mismatch, return `True`.

## Code

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # use the one deletion on either side
                return is_pal(l + 1, r) or is_pal(l, r - 1)
            l += 1
            r -= 1
        return True
```

## Complexity

- **Time:** `O(n)` — one outer scan plus at most two inner scans.
- **Space:** `O(1)` — only indices.

## Other Approaches

- **Brute force:** try deleting each index and check palindrome — Time `O(n^2)`, Space `O(n)`.

## Key Takeaway

When a problem allows "at most one" mistake, scan greedily until the first conflict, then branch only on the few possible fixes at that point.
