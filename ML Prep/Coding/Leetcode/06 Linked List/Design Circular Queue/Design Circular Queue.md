# Design Circular Queue

Design a fixed-capacity circular (ring-buffer) FIFO queue, where the slot after the last position wraps around to the first. Implement the class `MyCircularQueue`:

- `MyCircularQueue(k)` — create a queue that can hold at most `k` elements.
- `enQueue(value)` — add `value` to the rear; return `True` on success, `False` if full.
- `deQueue()` — remove the front element; return `True` on success, `False` if empty.
- `Front()` — return the front element, or `-1` if empty.
- `Rear()` — return the last element, or `-1` if empty.
- `isEmpty()` / `isFull()` — report whether the queue is empty / full.

Do not use a built-in queue type.

## Example

```text
Input:  ["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]
        [[3],[1],[2],[3],[4],[],[],[],[4],[]]
Output: [null,true,true,true,false,3,true,true,true,4]
```

```python

```
