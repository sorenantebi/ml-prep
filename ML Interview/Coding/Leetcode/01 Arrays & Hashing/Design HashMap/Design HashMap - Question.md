---
topic: "Arrays & Hashing"
difficulty: Easy
leetcode: https://leetcode.com/problems/design-hashmap/
neetcode: https://neetcode.io/problems/design-hashmap
---
# Design HashMap

**Topic:** [[01 Arrays & Hashing|Arrays & Hashing]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/design-hashmap/) · [NeetCode](https://neetcode.io/problems/design-hashmap)

**Solve it in:** [[Design HashMap]] · **Answer:** [[Design HashMap - Solution]]

## Problem

Implement a hash map from integer keys to integer values without using any built-in hash table libraries. The class `MyHashMap` must support:

- `MyHashMap()` creates an empty map.
- `put(key, value)` stores the pair; if `key` already exists, its value is overwritten.
- `get(key)` returns the value mapped to `key`, or `-1` if the key is absent.
- `remove(key)` deletes `key` and its value if present; otherwise nothing happens.

## Examples

**Example 1**
```text
Input:  ["MyHashMap","put","put","get","get","put","get","remove","get"]
        [[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]
Output: [null,null,null,1,-1,null,1,null,-1]
```

**Example 2**
```text
Input:  ["MyHashMap","put","put","get"]
        [[],[7,70],[7,700],[7]]
Output: [null,null,null,700]
Explanation: the second put overwrites the first value.
```

## Constraints

- `0 <= key, value <= 10^6`
- At most `10^4` calls in total to `put`, `get`, and `remove`.

## Starter Code & Test Cases

```python
class MyHashMap:

    def __init__(self):
        pass  # your code here

    def put(self, key: int, value: int) -> None:
        pass  # your code here

    def get(self, key: int) -> int:
        pass  # your code here

    def remove(self, key: int) -> None:
        pass  # your code here


if __name__ == "__main__":
    m = MyHashMap()
    m.put(1, 1)
    m.put(2, 2)
    assert m.get(1) == 1
    assert m.get(3) == -1
    m.put(2, 1)
    assert m.get(2) == 1
    m.remove(2)
    assert m.get(2) == -1

    m2 = MyHashMap()
    m2.put(7, 70)
    m2.put(7, 700)
    assert m2.get(7) == 700
    m2.remove(8)  # no-op
    m2.put(0, 0)
    assert m2.get(0) == 0  # value 0 must not be confused with "missing"
    m2.put(10**6, 5)
    assert m2.get(10**6) == 5

    # stress against a built-in dict with many colliding keys
    m3, ref = MyHashMap(), {}
    for k in range(0, 30000, 3):
        m3.put(k, k * 2); ref[k] = k * 2
    for k in range(0, 30000, 9):
        m3.remove(k); ref.pop(k, None)
    for k in range(0, 30000, 6):
        m3.put(k, k + 1); ref[k] = k + 1  # overwrite / re-insert
    assert all(m3.get(k) == ref.get(k, -1) for k in range(30000))
    print("All tests passed!")
```
