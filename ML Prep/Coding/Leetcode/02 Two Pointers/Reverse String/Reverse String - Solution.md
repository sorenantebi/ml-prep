---
topic: "Two Pointers"
difficulty: Easy
leetcode: https://leetcode.com/problems/reverse-string/
neetcode: https://neetcode.io/problems/reverse-string
---
# Reverse String - Solution

**Question:** [[Reverse String - Question]] · **Difficulty:** Easy

## Intuition

Reversing means the first character swaps with the last, the second with the second-to-last, and so on. Two pointers starting at both ends and moving inward perform exactly these swaps with no extra memory.

## Approach

1. Set `l = 0` and `r = len(s) - 1`.
2. While `l < r`, swap `s[l]` and `s[r]`.
3. Move `l` right and `r` left; stop when they meet or cross.

## Code

```python
from typing import List


class Solution:
	def reverseString(self, s: List[str]) -> None:
		l, r = 0, len(s) - 1
		while l < r:
			s[l], s[r] = s[r], s[l]
			l += 1
			r -= 1
```

## Complexity

- **Time:** `O(n)` — each character is touched once across `n/2` swaps.
- **Space:** `O(1)` — only two index variables.

## Other Approaches

- **Recursion:** swap the ends and recurse on the inner range — Time `O(n)`, Space `O(n)` for the call stack.
- **Built-in / slicing:** `s[:] = s[::-1]` — Time `O(n)`, Space `O(n)` for the temporary copy.

## Key Takeaway

Opposite-end two pointers are the standard tool for symmetric, in-place operations on arrays (reversal, palindrome checks, partitioning).
