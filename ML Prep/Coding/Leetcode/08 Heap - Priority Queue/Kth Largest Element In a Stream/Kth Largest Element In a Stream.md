# Kth Largest Element In a Stream

Design a class that tracks the `k`-th largest value in a stream of integers that keeps growing over time. Note that this is the `k`-th largest in sorted order (duplicates count separately), not the `k`-th largest distinct value.

Implement `KthLargest`:

- `KthLargest(int k, int[] nums)` sets up the object with the integer `k` and an initial list of values `nums` (which may contain fewer than `k` elements).
- `int add(int val)` inserts `val` into the stream and returns the element that is currently the `k`-th largest among everything seen so far.

It is guaranteed that whenever `add` is called, the stream contains at least `k` elements after the insertion.

## Example

```text
Input:  ["KthLargest", "add", "add", "add", "add", "add"]
        [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output: [null, 4, 5, 5, 8, 8]
Explanation: after adding 3 the stream is [2,3,4,5,8] -> 3rd largest is 4
```

```python

```
