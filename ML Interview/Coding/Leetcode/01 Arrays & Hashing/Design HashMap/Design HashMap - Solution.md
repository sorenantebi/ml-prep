---
topic: "Arrays & Hashing"
difficulty: Easy
leetcode: https://leetcode.com/problems/design-hashmap/
neetcode: https://neetcode.io/problems/design-hashmap
---
# Design HashMap - Solution

**Question:** [[Design HashMap - Question]] · **Difficulty:** Easy

## Intuition

Same structure as a hash set, but each bucket stores `[key, value]` pairs. The hash function picks a bucket, and within that bucket we search linearly for the key to update, read, or delete its pair. A prime number of buckets keeps chains short.

## Approach

1. Allocate `size = 1009` buckets, each an empty list of `[key, value]` pairs.
2. `put`: scan the key's bucket; if the key exists, overwrite its value, else append a new pair.
3. `get`: scan the bucket and return the value if found, else `-1`.
4. `remove`: scan the bucket and delete the matching pair if present.

## Code

```python
class MyHashMap:

    def __init__(self):
        self.size = 1009  # prime number of buckets
        self.buckets = [[] for _ in range(self.size)]

    def _bucket(self, key: int) -> list:
        return self.buckets[key % self.size]

    def put(self, key: int, value: int) -> None:
        bucket = self._bucket(key)
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value  # overwrite existing key
                return
        bucket.append([key, value])

    def get(self, key: int) -> int:
        for k, v in self._bucket(key):
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        bucket = self._bucket(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return
```

## Complexity

- **Time:** `O(n / b)` average per operation — chain length for `n` keys in `b` buckets (effectively `O(1)` here); `O(n)` worst case if everything collides.
- **Space:** `O(b + n)` — bucket array plus stored pairs.

## Other Approaches

- **Direct-address array:** `[-1] * (10^6 + 1)` indexed by key — Time `O(1)`, Space `O(U)` for key universe `U`.
- **Open addressing (linear probing):** store pairs directly in the array and probe forward on collision, using tombstones for deletes — Time `O(1)` average, Space `O(b)`.

## Key Takeaway

A hash map is a hash set whose buckets store key/value pairs; be ready to explain chaining vs. open addressing, load factor, and resizing.
