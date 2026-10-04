---
topic: "Bit Manipulation"
difficulty: Easy
leetcode: https://leetcode.com/problems/counting-bits/
neetcode: https://neetcode.io/problems/counting-bits
---
# Counting Bits

**Topic:** [[18 Bit Manipulation|Bit Manipulation]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/counting-bits/) · [NeetCode](https://neetcode.io/problems/counting-bits)

**Solve it in:** [[Counting Bits]] · **Answer:** [[Counting Bits - Solution]]

## Problem

Given a non-negative integer `n`, return an array `ans` of length `n + 1` where `ans[i]` is the number of `1` bits in the binary representation of `i`, for every `0 <= i <= n`.

Follow-up: can you do it in `O(n)` total time, without a built-in popcount?

## Examples

**Example 1**
```text
Input: n = 2
Output: [0,1,1]
Explanation: 0 -> 0, 1 -> 1, 2 -> 10
```

**Example 2**
```text
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation: 3 -> 11, 4 -> 100, 5 -> 101
```

## Constraints

- `0 <= n <= 10^5`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.countBits(2) == [0, 1, 1]
    assert s.countBits(5) == [0, 1, 1, 2, 1, 2]
    assert s.countBits(0) == [0]
    assert s.countBits(1) == [0, 1]
    assert s.countBits(8) == [0, 1, 1, 2, 1, 2, 2, 3, 1]
    assert s.countBits(16)[15] == 4 and s.countBits(16)[16] == 1
    assert s.countBits(100000) == [bin(i).count("1") for i in range(100001)]
    print("All tests passed!")
```
