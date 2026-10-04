---
topic: "Linked List"
difficulty: Hard
leetcode: https://leetcode.com/problems/lfu-cache/
neetcode: https://neetcode.io/problems/lfu-cache
---
# LFU Cache - Solution

**Question:** [[LFU Cache - Question]] · **Difficulty:** Hard

## Intuition

Group keys by use count: for each count keep an insertion-ordered collection of keys (an `OrderedDict` acts as a doubly linked list with `O(1)` removal), so the first key in a bucket is the least recently used among keys with that count. Also track `min_freq`, the smallest count currently present — it only changes in predictable ways: it resets to `1` on inserting a new key and increases by one when its bucket empties during a touch.

## Approach

1. Maintain `vals[key]`, `freq[key]`, `buckets[count] -> OrderedDict of keys` (LRU first) and `min_freq`.
2. `_touch(key)`: remove the key from `buckets[f]`, add it to the end of `buckets[f + 1]`, bump `freq[key]`; if `buckets[f]` became empty and `f == min_freq`, increment `min_freq`.
3. `get(key)`: if absent return `-1`; else `_touch` and return the value.
4. `put(key, value)`: if present, update the value and `_touch`. Otherwise, if full, pop the first (LRU) key from `buckets[min_freq]` and delete it everywhere; then insert the new key with count `1` and set `min_freq = 1`.

## Code

```python
from collections import defaultdict, OrderedDict


class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.vals = {}                              # key -> value
        self.freq = {}                              # key -> use count
        self.buckets = defaultdict(OrderedDict)     # count -> keys in LRU order
        self.min_freq = 0

    def _touch(self, key: int) -> None:
        f = self.freq[key]
        del self.buckets[f][key]
        if not self.buckets[f]:
            del self.buckets[f]
            if self.min_freq == f:                  # the min bucket just emptied
                self.min_freq += 1
        self.freq[key] = f + 1
        self.buckets[f + 1][key] = None             # most recent within its bucket

    def get(self, key: int) -> int:
        if key not in self.vals:
            return -1
        self._touch(key)
        return self.vals[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.vals:
            self.vals[key] = value
            self._touch(key)
            return
        if len(self.vals) == self.cap:
            victim, _ = self.buckets[self.min_freq].popitem(last=False)  # LRU among least frequent
            if not self.buckets[self.min_freq]:
                del self.buckets[self.min_freq]
            del self.vals[victim]
            del self.freq[victim]
        self.vals[key] = value
        self.freq[key] = 1
        self.buckets[1][key] = None
        self.min_freq = 1                           # a brand-new key always has count 1
```

## Complexity

- **Time:** `O(1)` average per `get`/`put` — dict and `OrderedDict` operations are constant time.
- **Space:** `O(capacity)` — each key appears in `vals`, `freq`, and exactly one bucket.

## Other Approaches

- **Min-heap keyed by `(count, last_used_time)` with lazy deletion:** Time `O(log n)` per operation, Space `O(n)` (plus stale heap entries).
- **Scan all keys on eviction:** find min `(count, time)` linearly — Time `O(capacity)` per eviction, Space `O(capacity)`.

## Key Takeaway

LFU = "LRU per frequency": a map from count to an ordered set of keys plus a running `min_freq`. `min_freq` never needs a search because it only resets to 1 or increments by 1.
