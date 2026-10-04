---
topic: "Linked List"
difficulty: Medium
leetcode: https://leetcode.com/problems/lru-cache/
neetcode: https://neetcode.io/problems/lru-cache
---
# LRU Cache - Solution

**Question:** [[LRU Cache - Question]] · **Difficulty:** Medium

## Intuition

We need `O(1)` lookup by key (hash map) **and** `O(1)` reordering by recency (doubly linked list). The map stores `key → node`; the list keeps nodes ordered from least to most recently used. Sentinel `left` (LRU end) and `right` (MRU end) nodes eliminate null checks when inserting or removing.

## Approach

1. Keep `cache: dict[key, Node]` and a doubly linked list `left <-> ... <-> right`.
2. Helper `remove(node)` unlinks a node; helper `insert(node)` places it just before `right` (most recent).
3. `get(key)`: if present, move its node to the MRU end and return its value; else `-1`.
4. `put(key, value)`: if present, unlink the old node. Create/insert the new node at the MRU end and store it in the map. If `len(cache) > capacity`, evict `left.next` (the LRU node) from both list and map.

## Code

```python
class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}                         # key -> Node
        self.left, self.right = Node(), Node()  # sentinels: LRU side, MRU side
        self.left.next, self.right.prev = self.right, self.left

    def _remove(self, node: Node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev

    def _insert(self, node: Node) -> None:      # insert just before right (MRU)
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)
        if len(self.cache) > self.cap:
            lru = self.left.next                # least recently used
            self._remove(lru)
            del self.cache[lru.key]             # node stores key for this step
```

## Complexity

- **Time:** `O(1)` average per `get`/`put` — hash lookups plus constant pointer updates.
- **Space:** `O(capacity)` — one map entry and one list node per stored key.

## Other Approaches

- **`collections.OrderedDict`:** `move_to_end(key)` on access and `popitem(last=False)` to evict — Time `O(1)`, Space `O(capacity)`; concise, but interviewers usually want the manual version.
- **List/array of keys ordered by recency:** reordering is `O(capacity)` per op — Time `O(capacity)`, Space `O(capacity)`.

## Key Takeaway

Hash map + doubly linked list (with sentinels) is the standard recipe for `O(1)` ordered caches; store the key inside each node so eviction can delete it from the map.
