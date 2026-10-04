---
topic: "Arrays & Hashing"
difficulty: Easy
leetcode: https://leetcode.com/problems/majority-element/
neetcode: https://neetcode.io/problems/majority-element
---
# Majority Element - Solution

**Question:** [[Majority Element - Question]] · **Difficulty:** Easy

## Intuition

Boyer-Moore voting: pair off each occurrence of the majority value with a different value and cancel them. Because the majority occurs more than half the time, it cannot be completely cancelled, so the candidate left standing at the end must be it.

## Approach

1. Keep a `candidate` and a `count`, starting at `count = 0`.
2. For each `x`: if `count == 0`, adopt `x` as the new candidate.
3. Increment `count` if `x == candidate`, otherwise decrement it.
4. Return `candidate` (no verification pass needed since a majority is guaranteed).

## Code

```python
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = None, 0
        for x in nums:
            if count == 0:  # previous candidate fully cancelled; start fresh
                candidate = x
            count += 1 if x == candidate else -1
        return candidate
```

## Complexity

- **Time:** `O(n)` — single pass.
- **Space:** `O(1)` — just two variables.

## Other Approaches

- **Hash map counting:** count occurrences and return the one above `n / 2` — Time `O(n)`, Space `O(n)`.
- **Sorting:** the element at index `n // 2` after sorting is the majority — Time `O(n log n)`, Space `O(1)` to `O(n)`.

## Key Takeaway

Boyer-Moore voting finds a strict majority in one pass and constant space by cancelling pairs of different values; remember it also generalizes to `> n/3` with two candidates.
