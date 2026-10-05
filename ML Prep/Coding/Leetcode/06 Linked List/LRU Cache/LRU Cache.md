# LRU Cache

Design a Least-Recently-Used (LRU) cache with a fixed capacity. Implement `LRUCache`:

- `LRUCache(capacity)` — initialize with a positive capacity.
- `get(key)` — return the value stored for `key`, or `-1` if absent. A successful lookup counts as a "use".
- `put(key, value)` — insert or update `key`. This also counts as a use. If inserting a new key makes the cache exceed its capacity, first evict the key that was used least recently.

Both `get` and `put` must run in `O(1)` average time.

## Example

```text
Input:  ["LRUCache","put","put","get","put","get","put","get","get","get"]
        [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
Output: [null,null,null,1,null,-1,null,-1,3,4]
Explanation: put(3,3) evicts key 2 (least recent); put(4,4) evicts key 1.
```

```python

```
