---
topic: "Heap / Priority Queue"
difficulty: Medium
leetcode: https://leetcode.com/problems/longest-happy-string/
neetcode: https://neetcode.io/problems/longest-happy-string
---
# Longest Happy String - Solution

**Question:** [[Longest Happy String - Question]] · **Difficulty:** Medium

## Intuition

Greedy: always try to use the letter with the **most copies left**, since it is the hardest to place later. The only thing that can stop us is the "no three in a row" rule — if the top letter was used twice consecutively, take the second most plentiful letter for this step instead. A max-heap of `(count, letter)` makes both choices `O(1)`-ish.

## Approach

1. Push `(-count, letter)` for each letter with a positive count into a max-heap.
2. Pop the most frequent letter. If the result already ends with two of that letter:
   - If the heap is empty, stop — nothing else can be placed.
   - Otherwise pop the second letter, append it once, push it back if it still has copies, and push the first letter back unchanged.
3. Otherwise append the top letter once and push it back if it still has copies.
4. Repeat until the heap is empty; return the built string.

## Code

```python
import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [(-cnt, ch) for cnt, ch in ((a, "a"), (b, "b"), (c, "c")) if cnt > 0]
        heapq.heapify(heap)
        res = []
        while heap:
            cnt, ch = heapq.heappop(heap)
            if len(res) >= 2 and res[-1] == res[-2] == ch:
                if not heap:
                    break  # only this letter remains and it would make a triple
                cnt2, ch2 = heapq.heappop(heap)
                res.append(ch2)
                if cnt2 + 1 < 0:
                    heapq.heappush(heap, (cnt2 + 1, ch2))
                heapq.heappush(heap, (cnt, ch))  # top letter stays available
            else:
                res.append(ch)
                if cnt + 1 < 0:
                    heapq.heappush(heap, (cnt + 1, ch))
        return "".join(res)
```

## Complexity

- **Time:** `O(a + b + c)` — each iteration appends one character and does constant work on a heap of size `<= 3`.
- **Space:** `O(1)` extra (heap of 3) plus `O(a + b + c)` for the output.

## Other Approaches

- **Recursive greedy:** sort counts so `x >= y >= z`, emit up to two of the largest, then one of the next, recurse on updated counts — Time `O(a + b + c)`, Space `O(a + b + c)` recursion/output.

## Key Takeaway

Greedy "use the most plentiful item unless it breaks a local rule, else the runner-up" — the same max-heap pattern as Reorganize String and Task Scheduler.
