---
topic: "Heap / Priority Queue"
difficulty: Medium
leetcode: https://leetcode.com/problems/reorganize-string/
neetcode: https://neetcode.io/problems/reorganize-string
---
# Reorganize String - Solution

**Question:** [[Reorganize String - Question]] · **Difficulty:** Medium

## Intuition

Greedily place the character with the **highest remaining count** at each step — that is the one most at risk of being forced next to itself later. To avoid placing the same character twice in a row, hold back the character just used for one step before returning it to the max-heap. If the heap empties while a character is still held back, no arrangement exists.

## Approach

1. Count characters; if any count exceeds `(n + 1) // 2`, return `""` early.
2. Push `(-count, char)` for every character into a max-heap.
3. Repeatedly pop the most frequent char, append it, then push back the previously held char (if it still has copies). Hold the current char (with decremented count) for the next round.
4. Return the built string (the early check guarantees the heap never runs dry prematurely).

## Code

```python
from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        if max(counts.values()) > (len(s) + 1) // 2:
            return ""  # most frequent char cannot be separated

        heap = [(-c, ch) for ch, c in counts.items()]
        heapq.heapify(heap)
        res = []
        prev = None  # (negCount, char) used last step, held out of the heap
        while heap:
            cnt, ch = heapq.heappop(heap)
            res.append(ch)
            if prev:
                heapq.heappush(heap, prev)
            prev = (cnt + 1, ch) if cnt + 1 < 0 else None
        return "".join(res)
```

## Complexity

- **Time:** `O(n log A)` — `n` heap operations on at most `A = 26` distinct letters, i.e. effectively `O(n)`.
- **Space:** `O(A)` for the heap plus `O(n)` for the output.

## Other Approaches

- **Even/odd index filling:** place the most frequent char at indices `0, 2, 4, ...`, then fill remaining chars into the remaining even then odd slots — Time `O(n)`, Space `O(n)`.

## Key Takeaway

"No two equal neighbors" = greedy max-heap by remaining count with a one-step cooldown; feasibility check is `maxCount <= (n + 1) // 2`.
