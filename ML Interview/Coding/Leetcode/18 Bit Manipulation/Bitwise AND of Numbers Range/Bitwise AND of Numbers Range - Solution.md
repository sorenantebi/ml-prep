---
topic: "Bit Manipulation"
difficulty: Medium
leetcode: https://leetcode.com/problems/bitwise-and-of-numbers-range/
neetcode: https://neetcode.io/problems/bitwise-and-of-numbers-range
---
# Bitwise AND of Numbers Range - Solution

**Question:** [[Bitwise AND of Numbers Range - Question]] · **Difficulty:** Medium

## Intuition

Any bit position where `left` and `right` differ goes through both a 0 and a 1 somewhere in the range. So once they first differ at some bit, that bit and every bit below it come out as 0 in the AND. The answer is therefore the **common binary prefix** of `left` and `right`, followed by zeros. Shift both numbers right until they are equal, then shift the result back left.

## Approach

1. Set `shift = 0`.
2. While `left != right`: `left >>= 1`, `right >>= 1`, `shift += 1`.
3. Return `left << shift`.

## Code

```python
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        # strip differing low bits until only the common prefix remains
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
```

## Complexity

- **Time:** `O(log right)`: at most 31 shifts.
- **Space:** `O(1)`.

## Other Approaches

- **Kernighan on `right`:** while `right > left`, set `right &= right - 1` to clear its lowest set bit, then return `right`. Time `O(log right)`, Space `O(1)`.
- **AND every number:** loop over the whole range. Time `O(right - left)`, which is too slow for ranges up to `2^31`.

## Key Takeaway

ANDing a contiguous range leaves exactly the common high-bit prefix of its endpoints. Bits below the first difference always pass through a 0.
