---
topic: "Stack"
difficulty: Hard
leetcode: https://leetcode.com/problems/maximum-frequency-stack/
neetcode: https://neetcode.io/problems/maximum-frequency-stack
---
# Maximum Frequency Stack - Solution

**Question:** [[Maximum Frequency Stack - Question]] · **Difficulty:** Hard

## Intuition

Think of the structure as a set of stacks, one per frequency level. When a value is pushed for the k-th time it goes onto stack `k`; it is still present on stacks `1..k-1` from its earlier pushes. The answer to `pop` is always the top of the highest non-empty frequency stack, which naturally breaks ties by recency.

## Approach

1. `freq[val]`: current count of `val`. `group[f]`: stack of values that reached frequency `f`, in push order. `max_freq`: highest current frequency.
2. `push(val)`: increment `freq[val]` to `f`, update `max_freq`, and append `val` to `group[f]`.
3. `pop()`: pop `val` from `group[max_freq]`, decrement `freq[val]`; if that group is now empty, decrement `max_freq`.
4. Return `val`.

## Code

```python
from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)       # val -> current frequency
        self.group = defaultdict(list)     # frequency -> stack of vals
        self.max_freq = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f
        self.max_freq = max(self.max_freq, f)
        self.group[f].append(val)

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        # frequencies are contiguous, so the next level down is non-empty
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val
```

## Complexity

- **Time:** `O(1)` for both `push` and `pop`.
- **Space:** `O(n)` — every pushed element appears exactly once across the group stacks.

## Other Approaches

- **Max-heap:** push `(-freq, -timestamp, val)` on every push and pop the heap top, decrementing the frequency — Time `O(log n)` per operation, Space `O(n)`.

## Key Takeaway

Bucket elements by frequency into per-level stacks; because frequencies change by exactly 1, `max_freq` can be maintained in O(1) without a heap.
