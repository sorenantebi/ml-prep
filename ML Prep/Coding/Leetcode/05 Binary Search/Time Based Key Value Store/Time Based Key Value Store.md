# Time Based Key Value Store

Design a time-based key-value store that can keep several values for the same key at different timestamps and retrieve the value that was current at a given time. Implement the class `TimeMap`:

- `TimeMap()` — initializes the store.
- `set(key, value, timestamp)` — stores `value` for `key` at time `timestamp`.
- `get(key, timestamp)` — returns the value from the call `set(key, value, t)` with the largest `t <= timestamp`. If there is no such entry, return the empty string `""`.

All timestamps passed to `set` are strictly increasing across calls.

## Example

```text
Input:  ["TimeMap","set","get","get","set","get","get"]
        [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation: get("foo",3) has no entry at 3, so it returns the value at time 1
```

```python

```
