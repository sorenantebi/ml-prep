---
topic: "Math & Geometry"
difficulty: Medium
leetcode: https://leetcode.com/problems/detect-squares/
neetcode: https://neetcode.io/problems/count-squares
---
# Detect Squares

**Topic:** [[17 Math & Geometry|Math & Geometry]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/detect-squares/) · [NeetCode](https://neetcode.io/problems/count-squares)

**Solve it in:** [[Detect Squares]] · **Answer:** [[Detect Squares - Solution]]

## Problem

Design a data structure that accepts a stream of points on the 2D plane and answers queries about squares.

- `add(point)` adds the point `[x, y]` to the structure. Duplicate points are allowed and are counted separately.
- `count(point)` is given a query point `[qx, qy]`. Count the ways to pick **three points already stored** so that, together with the query point, they form an **axis-aligned square with positive area**. Points chosen from the same coordinates but added at different times count as different choices.

Implement the class `DetectSquares`:

- `DetectSquares()` initializes the structure with no points.
- `void add(int[] point)` adds a point.
- `int count(int[] point)` returns the number of such squares for the query point.

## Examples

**Example 1**
```text
Input:
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
Output:
[null, null, null, null, 1, 0, null, 2]
Explanation:
count([11,10]) -> 1, using [3,10], [11,2], [3,2].
count([14,8]) -> 0, no square possible.
After adding a second [11,2], count([11,10]) -> 2, since either copy of [11,2] can be chosen.
```

## Constraints

- `point.length == 2`
- `0 <= x, y <= 1000`
- At most `3000` calls in total to `add` and `count`.

## Starter Code & Test Cases

```python
from typing import List
from collections import Counter


class DetectSquares:
    def __init__(self):
        pass  # your code here

    def add(self, point: List[int]) -> None:
        pass  # your code here

    def count(self, point: List[int]) -> int:
        pass  # your code here


if __name__ == "__main__":
    ds = DetectSquares()
    ds.add([3, 10])
    ds.add([11, 2])
    ds.add([3, 2])
    assert ds.count([11, 10]) == 1
    assert ds.count([14, 8]) == 0
    ds.add([11, 2])
    assert ds.count([11, 10]) == 2

    # Zero-area "squares" are not counted, even if the query point exists
    ds2 = DetectSquares()
    ds2.add([5, 5])
    ds2.add([5, 5])
    assert ds2.count([5, 5]) == 0

    # Squares on both sides of the query point (a 3x3 grid of unit squares around (1,1))
    ds3 = DetectSquares()
    for x in range(3):
        for y in range(3):
            ds3.add([x, y])
    assert ds3.count([1, 1]) == 4  # four unit squares touch the centre
    assert ds3.count([0, 0]) == 2  # unit square + 2x2 square

    # Duplicates multiply
    ds4 = DetectSquares()
    for p in ([0, 0], [0, 0], [0, 2], [2, 0], [2, 0], [2, 0]):
        ds4.add(p)
    assert ds4.count([2, 2]) == 2 * 1 * 3
    assert ds4.count([1, 1]) == 0
    print("All tests passed!")
```
