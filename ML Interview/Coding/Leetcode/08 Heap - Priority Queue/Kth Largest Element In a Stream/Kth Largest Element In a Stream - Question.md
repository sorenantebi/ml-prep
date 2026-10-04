---
topic: "Heap / Priority Queue"
difficulty: Easy
leetcode: https://leetcode.com/problems/kth-largest-element-in-a-stream/
neetcode: https://neetcode.io/problems/kth-largest-integer-in-a-stream
---
# Kth Largest Element In a Stream

**Topic:** [[08 Heap - Priority Queue|Heap / Priority Queue]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/kth-largest-element-in-a-stream/) · [NeetCode](https://neetcode.io/problems/kth-largest-integer-in-a-stream)

**Solve it in:** [[Kth Largest Element In a Stream]] · **Answer:** [[Kth Largest Element In a Stream - Solution]]

## Problem

Design a class that tracks the `k`-th largest value in a stream of integers that keeps growing over time. Note that this is the `k`-th largest in sorted order (duplicates count separately), not the `k`-th largest distinct value.

Implement `KthLargest`:

- `KthLargest(int k, int[] nums)` sets up the object with the integer `k` and an initial list of values `nums` (which may contain fewer than `k` elements).
- `int add(int val)` inserts `val` into the stream and returns the element that is currently the `k`-th largest among everything seen so far.

It is guaranteed that whenever `add` is called, the stream contains at least `k` elements after the insertion.

## Examples

**Example 1**
```text
Input:  ["KthLargest", "add", "add", "add", "add", "add"]
        [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output: [null, 4, 5, 5, 8, 8]
Explanation: after adding 3 the stream is [2,3,4,5,8] -> 3rd largest is 4
```

**Example 2**
```text
Input:  ["KthLargest", "add", "add", "add"]
        [[1, []], [-3], [-2], [-4]]
Output: [null, -3, -2, -2]
```

## Constraints

- `0 <= nums.length <= 10^4`
- `1 <= k <= nums.length + 1`
- `-10^4 <= nums[i], val <= 10^4`
- At most `10^4` calls to `add`

## Starter Code & Test Cases

```python
from typing import List
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        pass  # your code here

    def add(self, val: int) -> int:
        pass  # your code here


if __name__ == "__main__":
    obj = KthLargest(3, [4, 5, 8, 2])
    assert [obj.add(v) for v in [3, 5, 10, 9, 4]] == [4, 5, 5, 8, 8]

    obj = KthLargest(1, [])
    assert [obj.add(v) for v in [-3, -2, -4, 0, 4]] == [-3, -2, -2, 0, 4]

    obj = KthLargest(2, [0])
    assert [obj.add(v) for v in [-1, 1, -2, -4, 3]] == [-1, 0, 0, 0, 1]

    obj = KthLargest(4, [7, 7, 7, 7, 8, 3])
    assert [obj.add(v) for v in [2, 10, 9, 9]] == [7, 7, 7, 8]

    obj = KthLargest(1, [5])
    assert [obj.add(v) for v in [5, 1, 6]] == [5, 5, 6]

    obj = KthLargest(3, [1, 2])
    assert obj.add(3) == 1
    assert obj.add(0) == 1
    print("All tests passed!")
```
