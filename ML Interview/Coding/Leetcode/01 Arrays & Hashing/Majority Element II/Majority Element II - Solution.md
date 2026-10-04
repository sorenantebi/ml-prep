---
topic: "Arrays & Hashing"
difficulty: Medium
leetcode: https://leetcode.com/problems/majority-element-ii/
neetcode: https://neetcode.io/problems/majority-element-ii
---
# Majority Element II - Solution

**Question:** [[Majority Element II - Question]] · **Difficulty:** Medium

## Intuition

At most two values can each exceed `n / 3` occurrences. Extended Boyer-Moore voting keeps two candidates with counters; a value matching neither candidate cancels one vote from both (removing a triple of distinct values). Any true answer survives this cancellation, but survivors are not guaranteed to qualify, so a second counting pass verifies them.

## Approach

1. Keep `cand1, cand2` with counts `c1 = c2 = 0`.
2. For each `x`:
   - If `x == cand1`: `c1 += 1`; elif `x == cand2`: `c2 += 1`.
   - Elif `c1 == 0`: `cand1, c1 = x, 1`; elif `c2 == 0`: `cand2, c2 = x, 1`.
   - Else decrement both `c1` and `c2`.
3. Count the real occurrences of each (distinct) candidate and keep those with count `> n // 3`.

## Code

```python
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2, c1, c2 = None, None, 0, 0
        for x in nums:
            if x == cand1:
                c1 += 1
            elif x == cand2:
                c2 += 1
            elif c1 == 0:
                cand1, c1 = x, 1
            elif c2 == 0:
                cand2, c2 = x, 1
            else:  # x differs from both: cancel a triple of distinct values
                c1 -= 1
                c2 -= 1
        # verification pass: candidates are only potential answers
        return [c for c in (cand1, cand2)
                if c is not None and nums.count(c) > len(nums) // 3]
```

## Complexity

- **Time:** `O(n)` — one voting pass plus two counting passes.
- **Space:** `O(1)` — two candidates and two counters (excluding the at-most-2-element output).

## Other Approaches

- **Hash map counting:** count every value and return those above `n // 3` — Time `O(n)`, Space `O(n)`.
- **Sorting:** after sorting, check runs of length `> n // 3` — Time `O(n log n)`, Space `O(1)` to `O(n)`.

## Key Takeaway

Boyer-Moore generalizes: to find elements occurring more than `n / k` times keep `k - 1` candidates, then always verify the survivors with a second pass.
