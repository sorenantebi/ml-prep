---
topic: "Heap / Priority Queue"
difficulty: Medium
leetcode: https://leetcode.com/problems/car-pooling/
neetcode: https://neetcode.io/problems/car-pooling
---
# Car Pooling

**Topic:** [[08 Heap - Priority Queue|Heap / Priority Queue]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/car-pooling/) · [NeetCode](https://neetcode.io/problems/car-pooling)

**Solve it in:** [[Car Pooling]] · **Answer:** [[Car Pooling - Solution]]

## Problem

A car with `capacity` empty seats drives only in one direction (east), so it can never go back to an earlier location. You are given `trips`, where `trips[i] = [numPassengers_i, from_i, to_i]` means `numPassengers_i` people must be picked up at kilometer `from_i` and dropped off at kilometer `to_i`.

Return `true` if every trip can be completed without the number of passengers in the car ever exceeding `capacity`, otherwise `false`. Passengers dropped off at a location free their seats before new passengers are picked up at that same location.

## Examples

**Example 1**
```text
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Explanation: between km 3 and 5 there are 5 passengers
```

**Example 2**
```text
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
```

**Example 3**
```text
Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true
Explanation: the first group leaves at km 5 just as the second boards
```

## Constraints

- `1 <= trips.length <= 1000`
- `1 <= numPassengers_i <= 100`
- `0 <= from_i < to_i <= 1000`
- `1 <= capacity <= 10^5`

## Starter Code & Test Cases

```python
from typing import List
import heapq


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.carPooling([[2, 1, 5], [3, 3, 7]], 4) is False
    assert s.carPooling([[2, 1, 5], [3, 3, 7]], 5) is True
    assert s.carPooling([[2, 1, 5], [3, 5, 7]], 3) is True
    assert s.carPooling([[5, 0, 1]], 4) is False
    assert s.carPooling([[5, 0, 1]], 5) is True
    assert s.carPooling([[3, 2, 7], [3, 7, 9], [8, 3, 9]], 11) is True
    assert s.carPooling([[1, 0, 10], [1, 1, 9], [1, 2, 8], [1, 3, 7]], 3) is False
    assert s.carPooling([[9, 0, 1], [3, 3, 7]], 4) is False
    print("All tests passed!")
```
