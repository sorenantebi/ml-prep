# LFU Cache

Design a Least-Frequently-Used (LFU) cache with a fixed capacity. Implement `LFUCache`:

- `LFUCache(capacity)` — initialize the cache.
- `get(key)` — return the value for `key` or `-1` if absent.
- `put(key, value)` — update `key` if present, otherwise insert it. If inserting a new key when the cache is already full, first evict the key with the **lowest use count**; if several keys share that lowest count, evict the **least recently used** among them.

Every key has a use counter: it starts at `1` when the key is inserted and increases by `1` on every successful `get` or `put` to that key. Both operations must run in `O(1)` average time.

## Example

```text
Input:  ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
        [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
Output: [null,null,null,1,null,-1,3,null,-1,3,4]
Explanation: put(3,3) evicts key 2 (count 1 vs key 1's count 2).
             put(4,4): keys 1 and 3 both have count 2; key 1 is less recent, so it is evicted.
```

```python

```
