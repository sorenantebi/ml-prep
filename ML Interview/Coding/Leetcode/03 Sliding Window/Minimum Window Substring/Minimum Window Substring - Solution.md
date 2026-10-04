---
topic: "Sliding Window"
difficulty: Hard
leetcode: https://leetcode.com/problems/minimum-window-substring/
neetcode: https://neetcode.io/problems/minimum-window-with-characters
---
# Minimum Window Substring - Solution

**Question:** [[Minimum Window Substring - Question]] · **Difficulty:** Hard

## Intuition

Use a variable sliding window. Expand the right edge until the window contains all required characters, then shrink from the left as much as possible while it stays valid, recording the smallest valid window. A counter `have` of how many distinct characters currently meet their required count lets us test validity in `O(1)`.

## Approach

1. Build `need = Counter(t)`; `required = len(need)`; `have = 0`; `window = {}`.
2. For each `r`, add `s[r]` to `window`; if its count just reached `need[s[r]]`, increment `have`.
3. While `have == required`:
   - Record the window if it is the smallest so far.
   - Remove `s[l]` from `window`; if its count dropped below `need[s[l]]`, decrement `have`. Move `l` right.
4. Return the best window, or `""` if none was found.

## Code

```python
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        required = len(need)
        window = defaultdict(int)
        have = 0
        best_len, best_l = float("inf"), 0
        l = 0
        for r, c in enumerate(s):
            window[c] += 1
            if c in need and window[c] == need[c]:
                have += 1  # this character is now fully satisfied
            while have == required:
                if r - l + 1 < best_len:
                    best_len, best_l = r - l + 1, l
                lc = s[l]
                window[lc] -= 1
                if lc in need and window[lc] < need[lc]:
                    have -= 1  # window just became invalid
                l += 1
        return "" if best_len == float("inf") else s[best_l:best_l + best_len]
```

## Complexity

- **Time:** `O(m + n)` — building `need` is `O(n)`; each index of `s` enters and leaves the window once.
- **Space:** `O(k)` — `k` distinct characters in the maps (at most 52 letters here).

## Other Approaches

- **Brute force:** check every substring against `Counter(t)` — Time `O(m^2 * k)`, Space `O(k)`.
- **Filtered s:** run the same window only over positions of `s` whose characters occur in `t` — same worst case, faster when `t` is much smaller than the alphabet of `s`.

## Key Takeaway

Minimum-window problems = expand until valid, then shrink while valid. Track "number of satisfied distinct characters" instead of comparing full maps to keep each step `O(1)`.
