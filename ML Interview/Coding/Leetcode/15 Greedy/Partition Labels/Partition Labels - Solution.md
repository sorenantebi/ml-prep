---
topic: "Greedy"
difficulty: Medium
leetcode: https://leetcode.com/problems/partition-labels/
neetcode: https://neetcode.io/problems/partition-labels
---
# Partition Labels - Solution

**Question:** [[Partition Labels - Question]] · **Difficulty:** Medium

## Intuition

A part that contains letter `c` must extend at least to the **last** occurrence of `c`. Scan left to right, stretching the current part's end to the last occurrence of each letter seen; when the scan index reaches that end, no letter inside the part appears later, so we can cut there.

## Approach

1. Record `last[c]` = last index of each character.
2. Keep `start = 0`, `end = 0`. For each index `i`: `end = max(end, last[s[i]])`.
3. If `i == end`, append `end - start + 1` to the result and set `start = i + 1`.
4. Return the result.

## Code

```python
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}  # last occurrence of each letter
        res = []
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, last[c])  # this part must reach c's last occurrence
            if i == end:  # every letter so far ends inside the part -> cut
                res.append(end - start + 1)
                start = i + 1
        return res
```

## Complexity

- **Time:** `O(n)` — two linear passes.
- **Space:** `O(1)` — at most 26 entries in `last` (output excluded).

## Other Approaches

- **Merge intervals:** build `[first, last]` for each letter and merge overlapping intervals; the merged lengths are the answer — Time `O(n)` (26 intervals to sort), Space `O(1)`.

## Key Takeaway

"Each item in one group" partitioning = extend the current window to the furthest last-occurrence; cut when the index catches up.
