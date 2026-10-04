---
topic: "Heap / Priority Queue"
difficulty: Hard
leetcode: https://leetcode.com/problems/find-median-from-data-stream/
neetcode: https://neetcode.io/problems/find-median-in-a-data-stream
---
# Find Median From Data Stream

**Topic:** [[08 Heap - Priority Queue|Heap / Priority Queue]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/find-median-from-data-stream/) · [NeetCode](https://neetcode.io/problems/find-median-in-a-data-stream)

**Solve it in:** [[Find Median From Data Stream]] · **Answer:** [[Find Median From Data Stream - Solution]]

## Problem

The median of a sorted list of integers is its middle element when the length is odd, and the average of the two middle elements when the length is even (e.g. median of `[2,3,4]` is `3`, median of `[2,3]` is `2.5`).

Design a `MedianFinder` that receives integers one at a time and can report the median of everything received so far:

- `MedianFinder()` creates an empty structure.
- `void addNum(int num)` adds `num` to the data.
- `double findMedian()` returns the current median. Answers within `10^-5` of the true value are accepted.

`findMedian` is only called when at least one number has been added.

## Examples

**Example 1**
```text
Input:  ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
        [[],[1],[2],[],[3],[]]
Output: [null,null,null,1.5,null,2.0]
```

**Example 2**
```text
Input:  ["MedianFinder","addNum","findMedian","addNum","findMedian"]
        [[],[-1],[],[-2],[]]
Output: [null,null,-1.0,null,-1.5]
```

## Constraints

- `-10^5 <= num <= 10^5`
- At most `5 * 10^4` total calls to `addNum` and `findMedian`
- Follow-up: what if all numbers are in `[0, 100]`? What if 99% of them are?

## Starter Code & Test Cases

```python
import heapq


class MedianFinder:
    def __init__(self):
        pass  # your code here

    def addNum(self, num: int) -> None:
        pass  # your code here

    def findMedian(self) -> float:
        pass  # your code here


if __name__ == "__main__":
    import random
    import statistics

    close = lambda x, y: abs(x - y) < 1e-5

    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert close(mf.findMedian(), 1.5)
    mf.addNum(3)
    assert close(mf.findMedian(), 2.0)

    mf = MedianFinder()
    mf.addNum(-1)
    assert close(mf.findMedian(), -1.0)
    mf.addNum(-2)
    assert close(mf.findMedian(), -1.5)
    mf.addNum(-3)
    assert close(mf.findMedian(), -2.0)

    mf = MedianFinder()
    for v in [5, 5, 5, 5]:
        mf.addNum(v)
    assert close(mf.findMedian(), 5.0)

    mf = MedianFinder()
    for v, exp in zip([6, 10, 2, 6, 5, 0], [6.0, 8.0, 6.0, 6.0, 6.0, 5.5]):
        mf.addNum(v)
        assert close(mf.findMedian(), exp)

    random.seed(0)
    mf, seen = MedianFinder(), []
    for _ in range(500):
        v = random.randint(-100000, 100000)
        mf.addNum(v)
        seen.append(v)
        assert close(mf.findMedian(), statistics.median(seen))
    print("All tests passed!")
```
