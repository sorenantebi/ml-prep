---
topic: "Sliding Window"
difficulty: Medium
leetcode: https://leetcode.com/problems/permutation-in-string/
neetcode: https://neetcode.io/problems/permutation-string
---
# Permutation In String - Solution

**Question:** [[Permutation In String - Question]] · **Difficulty:** Medium

## Intuition

A permutation of `s1` is any string with identical letter counts, so slide a window of fixed length `len(s1)` over `s2` and compare letter-count arrays. Instead of comparing all 26 counts each step, maintain `matches`: how many of the 26 letters currently have equal counts; the answer is found when `matches == 26`.

## Approach

1. If `len(s1) > len(s2)`, return `False`.
2. Build count arrays `c1` (for `s1`) and `c2` (for the first window of `s2`) and compute `matches`.
3. Slide the window one step at a time: add the new right char and remove the old left char, updating `matches` whenever a count becomes equal or stops being equal.
4. Return `True` as soon as `matches == 26`, otherwise `False`.

## Code

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        c1, c2 = [0] * 26, [0] * 26
        for i in range(n1):
            c1[ord(s1[i]) - 97] += 1
            c2[ord(s2[i]) - 97] += 1
        matches = sum(c1[i] == c2[i] for i in range(26))

        for r in range(n1, n2):
            if matches == 26:
                return True
            # add the incoming character
            i = ord(s2[r]) - 97
            c2[i] += 1
            if c2[i] == c1[i]:
                matches += 1
            elif c2[i] == c1[i] + 1:
                matches -= 1  # was equal before this increment
            # remove the outgoing character
            j = ord(s2[r - n1]) - 97
            c2[j] -= 1
            if c2[j] == c1[j]:
                matches += 1
            elif c2[j] == c1[j] - 1:
                matches -= 1  # was equal before this decrement
        return matches == 26
```

## Complexity

- **Time:** `O(n1 + n2)` — constant work per slide (plus a one-time 26-letter comparison).
- **Space:** `O(1)` — two fixed-size arrays of 26.

## Other Approaches

- **Compare count arrays each step:** slide the window and test `c1 == c2` directly — Time `O(26 * n2)`, Space `O(1)`; simpler and still linear.
- **Sort every window:** compare `sorted(window)` with `sorted(s1)` — Time `O(n2 * n1 log n1)`, Space `O(n1)`.

## Key Takeaway

"Anagram/permutation inside a string" = fixed-size sliding window with frequency counts; tracking the number of matching buckets makes each slide `O(1)`.
