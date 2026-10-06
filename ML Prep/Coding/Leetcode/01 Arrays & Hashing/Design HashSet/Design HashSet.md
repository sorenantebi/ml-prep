# Design HashSet

Implement a hash set of integers from scratch, without using any built-in hash table libraries. The class `MyHashSet` must support:

- `MyHashSet()` creates an empty set.
- `add(key)` inserts `key` into the set (no effect if it is already present).
- `contains(key)` returns `true` if `key` is in the set, otherwise `false`.
- `remove(key)` deletes `key` from the set; if `key` is not present, nothing happens.

## Example

```text
Input:  ["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]
        [[],[1],[2],[1],[3],[2],[2],[2],[2]]
Output: [null,null,null,true,false,null,true,null,false]
```

```python
# create buckets to store the key numbers in using % self.size, and then first index the correct bucket based on the key, and then find the key 
# set, not map
bucket_ = [[] for _ in range(self.size)]

bucket = bucket_[key % 1009]
if key not in bucket:
	bucket_[key % 1009].append(key)
```
