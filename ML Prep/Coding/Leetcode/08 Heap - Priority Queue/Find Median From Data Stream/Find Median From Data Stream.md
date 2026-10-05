# Find Median From Data Stream

The median of a sorted list of integers is its middle element when the length is odd, and the average of the two middle elements when the length is even (e.g. median of `[2,3,4]` is `3`, median of `[2,3]` is `2.5`).

Design a `MedianFinder` that receives integers one at a time and can report the median of everything received so far:

- `MedianFinder()` creates an empty structure.
- `void addNum(int num)` adds `num` to the data.
- `double findMedian()` returns the current median. Answers within `10^-5` of the true value are accepted.

`findMedian` is only called when at least one number has been added.

## Example

```text
Input:  ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
        [[],[1],[2],[],[3],[]]
Output: [null,null,null,1.5,null,2.0]
```

```python

```
