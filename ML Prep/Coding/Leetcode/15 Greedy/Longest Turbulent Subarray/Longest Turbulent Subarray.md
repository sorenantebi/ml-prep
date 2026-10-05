# Longest Turbulent Subarray

Given an integer array `arr`, return the length of the longest **turbulent** subarray. A subarray `arr[i..j]` is turbulent if the comparison sign between each pair of adjacent elements flips at every step — e.g. `arr[k] > arr[k+1] < arr[k+2] > ...` or `arr[k] < arr[k+1] > arr[k+2] < ...`. Equal adjacent elements break turbulence. A single element is a turbulent subarray of length 1.

## Example

```text
Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: [4,2,10,7,8] has 4 > 2 < 10 > 7 < 8.
```

```python

```
