---
topic: "Binary Search"
difficulty: Hard
leetcode: https://leetcode.com/problems/find-in-mountain-array/
neetcode: https://neetcode.io/problems/find-in-mountain-array
---
# Find in Mountain Array

**Topic:** [[05 Binary Search|Binary Search]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/find-in-mountain-array/) · [NeetCode](https://neetcode.io/problems/find-in-mountain-array)

**Solve it in:** [[Find in Mountain Array]] · **Answer:** [[Find in Mountain Array - Solution]]

## Problem

An array `arr` is a **mountain array** if `arr.length >= 3` and there is an index `p` (`0 < p < arr.length - 1`) such that values strictly increase up to `arr[p]` and then strictly decrease after it.

This is an interactive problem: you cannot access the array directly, only through a `MountainArray` object with two methods:

- `MountainArray.get(k)` — returns the element at index `k` (0-indexed),
- `MountainArray.length()` — returns the array's length.

Given a mountain array `mountainArr` and an integer `target`, return the **minimum** index `i` such that `mountainArr.get(i) == target`, or `-1` if `target` does not occur. Solutions that call `get` more than `100` times are rejected.

## Examples

**Example 1**
```text
Input: mountainArr = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 occurs at indices 2 and 5; return the smaller one
```

**Example 2**
```text
Input: mountainArr = [0,1,2,4,2,1], target = 3
Output: -1
```

**Example 3**
```text
Input: mountainArr = [0,5,3,1], target = 1
Output: 3
```

## Constraints

- `3 <= mountainArr.length() <= 10^4`
- `0 <= target <= 10^9`
- `0 <= mountainArr.get(index) <= 10^9`

## Starter Code & Test Cases

```python
from typing import List


class MountainArray:
    """Mock of the interactive judge's API; counts calls to get()."""

    def __init__(self, arr: List[int]):
        self._arr = arr
        self.calls = 0

    def get(self, index: int) -> int:
        self.calls += 1
        return self._arr[index]

    def length(self) -> int:
        return len(self._arr)


class Solution:
    def findInMountainArray(self, target: int, mountainArr: "MountainArray") -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()

    def run(arr, target):
        m = MountainArray(arr)
        res = s.findInMountainArray(target, m)
        assert m.calls <= 100, "too many get() calls"
        return res

    assert run([1, 2, 3, 4, 5, 3, 1], 3) == 2
    assert run([0, 1, 2, 4, 2, 1], 3) == -1
    assert run([0, 5, 3, 1], 1) == 3
    assert run([1, 5, 2], 5) == 1          # target is the peak
    assert run([1, 5, 2], 2) == 2
    assert run([3, 5, 3, 2, 0], 0) == 4
    big = list(range(5000)) + list(range(4999, -1, -1))[1:]
    assert run(big, 4999) == 4999
    assert run(big, 0) == 0                # first occurrence on the ascending side
    assert run(big, 10**9) == -1
    print("All tests passed!")
```
