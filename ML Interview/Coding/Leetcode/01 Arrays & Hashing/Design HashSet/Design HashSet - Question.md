---
topic: "Arrays & Hashing"
difficulty: Easy
leetcode: https://leetcode.com/problems/design-hashset/
neetcode: https://neetcode.io/problems/design-hashset
---
# Design HashSet

**Topic:** [[01 Arrays & Hashing|Arrays & Hashing]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/design-hashset/) · [NeetCode](https://neetcode.io/problems/design-hashset)

**Solve it in:** [[Design HashSet]] · **Answer:** [[Design HashSet - Solution]]

## Problem

Implement a hash set of integers from scratch, without using any built-in hash table libraries. The class `MyHashSet` must support:

- `MyHashSet()` creates an empty set.
- `add(key)` inserts `key` into the set (no effect if it is already present).
- `contains(key)` returns `true` if `key` is in the set, otherwise `false`.
- `remove(key)` deletes `key` from the set; if `key` is not present, nothing happens.

## Examples

**Example 1**
```text
Input:  ["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]
        [[],[1],[2],[1],[3],[2],[2],[2],[2]]
Output: [null,null,null,true,false,null,true,null,false]
```

**Example 2**
```text
Input:  ["MyHashSet","remove","add","contains"]
        [[],[5],[5],[5]]
Output: [null,null,null,true]
Explanation: removing a missing key is a no-op.
```

## Constraints

- `0 <= key <= 10^6`
- At most `10^4` calls in total to `add`, `remove`, and `contains`.

## Starter Code & Test Cases

```python
class MyHashSet:

    def __init__(self):
        pass  # your code here

    def add(self, key: int) -> None:
        pass  # your code here

    def remove(self, key: int) -> None:
        pass  # your code here

    def contains(self, key: int) -> bool:
        pass  # your code here


if __name__ == "__main__":
    hs = MyHashSet()
    hs.add(1)
    hs.add(2)
    assert hs.contains(1) is True
    assert hs.contains(3) is False
    hs.add(2)
    assert hs.contains(2) is True
    hs.remove(2)
    assert hs.contains(2) is False

    hs2 = MyHashSet()
    hs2.remove(5)  # removing a missing key is a no-op
    hs2.add(5)
    assert hs2.contains(5) is True
    hs2.add(0)
    hs2.add(10**6)
    assert hs2.contains(0) is True and hs2.contains(10**6) is True
    hs2.remove(10**6)
    assert hs2.contains(10**6) is False

    # many keys that collide in a small table, cross-checked against a built-in set
    hs3, ref = MyHashSet(), set()
    for k in range(0, 20000, 7):
        hs3.add(k); ref.add(k)
    for k in range(0, 20000, 14):
        hs3.remove(k); ref.discard(k)
    assert all(hs3.contains(k) == (k in ref) for k in range(20000))
    print("All tests passed!")
```
