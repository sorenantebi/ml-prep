---
topic: "Linked List"
difficulty: Medium
leetcode: https://leetcode.com/problems/lru-cache/
neetcode: https://neetcode.io/problems/lru-cache
---
# LRU Cache

**Topic:** [[06 Linked List|Linked List]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/lru-cache/) · [NeetCode](https://neetcode.io/problems/lru-cache)

**Solve it in:** [[LRU Cache]] · **Answer:** [[LRU Cache - Solution]]

## Problem

Design a Least-Recently-Used (LRU) cache with a fixed capacity. Implement `LRUCache`:

- `LRUCache(capacity)` — initialize with a positive capacity.
- `get(key)` — return the value stored for `key`, or `-1` if absent. A successful lookup counts as a "use".
- `put(key, value)` — insert or update `key`. This also counts as a use. If inserting a new key makes the cache exceed its capacity, first evict the key that was used least recently.

Both `get` and `put` must run in `O(1)` average time.

## Examples

**Example 1**
```text
Input:  ["LRUCache","put","put","get","put","get","put","get","get","get"]
        [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
Output: [null,null,null,1,null,-1,null,-1,3,4]
Explanation: put(3,3) evicts key 2 (least recent); put(4,4) evicts key 1.
```

**Example 2**
```text
Input:  ["LRUCache","put","put","put","get","get"]
        [[1],[1,10],[1,20],[2,5],[1],[2]]
Output: [null,null,null,null,-1,5]
```

## Constraints

- `1 <= capacity <= 3000`
- `0 <= key <= 10^4`
- `0 <= value <= 10^5`
- At most `2 * 10^5` calls to `get` and `put`

## Starter Code & Test Cases

```python
class LRUCache:
    def __init__(self, capacity: int):
        pass  # your code here

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


if __name__ == "__main__":
    def run(ops, args):
        obj = None
        out = []
        for op, a in zip(ops, args):
            if op == "LRUCache":
                obj = LRUCache(*a)
                out.append(None)
            else:
                out.append(getattr(obj, op)(*a))
        return out

    assert run(
        ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
    ) == [None, None, None, 1, None, -1, None, -1, 3, 4]

    assert run(
        ["LRUCache", "put", "put", "put", "get", "get"],
        [[1], [1, 10], [1, 20], [2, 5], [1], [2]],
    ) == [None, None, None, None, -1, 5]

    # updating an existing key refreshes recency and does not evict
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    c.put(1, 100)        # 1 is now most recent
    c.put(3, 3)          # evicts 2
    assert c.get(2) == -1
    assert c.get(1) == 100
    assert c.get(3) == 3

    # get on a missing key in an empty cache
    assert LRUCache(3).get(42) == -1

    # randomized check against a simple reference model
    import random
    from collections import OrderedDict
    random.seed(0)
    cap = 5
    c, ref = LRUCache(cap), OrderedDict()
    for _ in range(5000):
        k = random.randint(0, 12)
        if random.random() < 0.5:
            exp = -1
            if k in ref:
                ref.move_to_end(k)
                exp = ref[k]
            assert c.get(k) == exp
        else:
            v = random.randint(0, 100)
            c.put(k, v)
            ref[k] = v
            ref.move_to_end(k)
            if len(ref) > cap:
                ref.popitem(last=False)
    print("All tests passed!")
```
