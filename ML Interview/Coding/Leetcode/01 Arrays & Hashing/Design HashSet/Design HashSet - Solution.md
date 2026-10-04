---
topic: "Arrays & Hashing"
difficulty: Easy
leetcode: https://leetcode.com/problems/design-hashset/
neetcode: https://neetcode.io/problems/design-hashset
---
# Design HashSet - Solution

**Question:** [[Design HashSet - Question]] · **Difficulty:** Easy

## Intuition

A hash set is an array of buckets plus a hash function that maps each key to a bucket. Collisions are handled by separate chaining: every bucket is a small list of keys, so operations only scan the one bucket a key hashes to. With a prime number of buckets and ~10^4 operations, each chain stays short.

## Approach

1. Allocate `size = 1009` (a prime) empty buckets.
2. Hash a key with `key % size` to choose its bucket.
3. `add`: append the key to its bucket if it is not already there.
4. `remove`: delete the key from its bucket if present.
5. `contains`: check membership in the key's bucket.

## Code

```python
class MyHashSet:

    def __init__(self):
        self.size = 1009  # prime bucket count spreads keys evenly
        self.buckets = [[] for _ in range(self.size)]

    def _bucket(self, key: int) -> list:
        return self.buckets[key % self.size]

    def add(self, key: int) -> None:
        bucket = self._bucket(key)
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self._bucket(key)
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        return key in self._bucket(key)
```

## Complexity

- **Time:** `O(n / b)` average per operation — `n` stored keys spread across `b` buckets (effectively `O(1)` for these limits); worst case `O(n)` if all keys collide.
- **Space:** `O(b + n)` — the bucket array plus stored keys.

## Other Approaches

- **Direct-address boolean array:** a `[False] * (10^6 + 1)` array indexed by key — Time `O(1)`, Space `O(U)` for key universe `U`.
- **Buckets of linked lists / BSTs:** same idea with a different chain structure (BST chains give `O(log n)` worst case per bucket).

## Key Takeaway

Know the anatomy of a hash table: hash function to bucket index, collision handling via chaining (or open addressing), and a prime table size to reduce clustering.
