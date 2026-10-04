---
topic: "Binary Search"
difficulty: Easy
leetcode: https://leetcode.com/problems/sqrtx/
neetcode: https://neetcode.io/problems/sqrtx
---
# Sqrt(x) - Solution

**Question:** [[Sqrt(x) - Question]] · **Difficulty:** Easy

## Intuition

The predicate `r * r <= x` is true for all `r` up to the answer and false afterwards, so the answer is the last `r` for which it holds. Binary search over `[0, x]` finds that boundary in logarithmic time.

## Approach

1. Search `lo = 0`, `hi = x`, keeping `ans` as the best `r` found so far.
2. While `lo <= hi`: `mid = (lo + hi) // 2`.
3. If `mid * mid <= x`, record `ans = mid` and search right (`lo = mid + 1`); else search left (`hi = mid - 1`).
4. Return `ans`.

## Code

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi, ans = 0, x, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid <= x:
                ans = mid          # mid is a valid candidate; try larger
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
```

## Complexity

- **Time:** `O(log x)` — halving the search range.
- **Space:** `O(1)`.

## Other Approaches

- **Newton's method:** iterate `r = (r + x // r) // 2` from `r = x` while `r * r > x` — Time `O(log x)` (quadratic convergence in practice), Space `O(1)`.
- **Linear scan:** increase `r` while `(r + 1)^2 <= x` — Time `O(sqrt x)`, Space `O(1)`.

## Key Takeaway

"Largest value satisfying a monotone condition" → binary search on the answer, saving the last valid `mid`.
