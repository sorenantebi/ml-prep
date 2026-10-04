---
topic: "1-D Dynamic Programming"
difficulty: Easy
leetcode: https://leetcode.com/problems/n-th-tribonacci-number/
neetcode: https://neetcode.io/problems/n-th-tribonacci-number
---
# N-th Tribonacci Number - Solution

**Question:** [[N-th Tribonacci Number - Question]] · **Difficulty:** Easy

## Intuition

Each term depends only on the three before it, so iterate forward keeping a sliding window of three values instead of an array or recursion.

## Approach

1. Handle the base case `n == 0` (return 0); `T1 = T2 = 1` fall out of the loop running zero times.
2. Keep `(a, b, c) = (T0, T1, T2)` and shift `n - 2` times with `c = a + b + c`.
3. Return `c`.

## Code

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        a, b, c = 0, 1, 1  # T0, T1, T2
        for _ in range(n - 2):
            a, b, c = b, c, a + b + c
        return c
```

## Complexity

- **Time:** `O(n)` — one loop iteration per term.
- **Space:** `O(1)` — three variables.

## Other Approaches

- **Memoised recursion:** cache `T(n)` — Time `O(n)`, Space `O(n)`.
- **Matrix exponentiation:** 3x3 matrix power — Time `O(log n)`, Space `O(1)`.

## Key Takeaway

A linear recurrence of order `k` needs only a rolling window of `k` values — the same trick as Fibonacci/Climbing Stairs.
