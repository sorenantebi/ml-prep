---
topic: "Linked List"
difficulty: Hard
leetcode: https://leetcode.com/problems/lfu-cache/
neetcode: https://neetcode.io/problems/lfu-cache
---
# LFU Cache

**Topic:** [[06 Linked List|Linked List]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/lfu-cache/) · [NeetCode](https://neetcode.io/problems/lfu-cache)

**Solve it in:** [[LFU Cache]] · **Answer:** [[LFU Cache - Solution]]

## Problem

Design a Least-Frequently-Used (LFU) cache with a fixed capacity. Implement `LFUCache`:

- `LFUCache(capacity)` — initialize the cache.
- `get(key)` — return the value for `key` or `-1` if absent.
- `put(key, value)` — update `key` if present, otherwise insert it. If inserting a new key when the cache is already full, first evict the key with the **lowest use count**; if several keys share that lowest count, evict the **least recently used** among them.

Every key has a use counter: it starts at `1` when the key is inserted and increases by `1` on every successful `get` or `put` to that key. Both operations must run in `O(1)` average time.

## Examples

**Example 1**
```text
Input:  ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
        [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
Output: [null,null,null,1,null,-1,3,null,-1,3,4]
Explanation: put(3,3) evicts key 2 (count 1 vs key 1's count 2).
             put(4,4): keys 1 and 3 both have count 2; key 1 is less recent, so it is evicted.
```

**Example 2**
```text
Input:  ["LFUCache","put","get","put","get","get"]
        [[1],[2,1],[2],[3,2],[2],[3]]
Output: [null,null,1,null,-1,2]
```

## Constraints

- `1 <= capacity <= 10^4`
- `0 <= key <= 10^5`
- `0 <= value <= 10^9`
- At most `2 * 10^5` calls to `get` and `put`

## Starter Code & Test Cases

```python
class LFUCache:
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
			if op == "LFUCache":
				obj = LFUCache(*a)
				out.append(None)
			else:
				out.append(getattr(obj, op)(*a))
		return out

	assert run(
		["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"],
		[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]],
	) == [None, None, None, 1, None, -1, 3, None, -1, 3, 4]

	assert run(
		["LFUCache", "put", "get", "put", "get", "get"],
		[[1], [2, 1], [2], [3, 2], [2], [3]],
	) == [None, None, 1, None, -1, 2]

	# updating a key with put increases its count
	c = LFUCache(2)
	c.put(1, 1)
	c.put(2, 2)
	c.put(1, 10)   # key 1 count 2
	c.put(3, 3)    # evicts key 2 (count 1)
	assert c.get(2) == -1 and c.get(1) == 10 and c.get(3) == 3

	# randomized check against a brute-force model
	import random
	random.seed(1)
	cap = 4
	c = LFUCache(cap)
	vals, cnt, last, t = {}, {}, {}, 0
	for _ in range(5000):
		t += 1
		k = random.randint(0, 9)
		if random.random() < 0.5:
			exp = -1
			if k in vals:
				exp = vals[k]
				cnt[k] += 1
				last[k] = t
			assert c.get(k) == exp
		else:
			v = random.randint(0, 50)
			c.put(k, v)
			if k in vals:
				cnt[k] += 1
			else:
				if len(vals) == cap:
					victim = min(vals, key=lambda x: (cnt[x], last[x]))
					for d in (vals, cnt, last):
						del d[victim]
				cnt[k] = 1
			vals[k] = v
			last[k] = t
	print("All tests passed!")
```
