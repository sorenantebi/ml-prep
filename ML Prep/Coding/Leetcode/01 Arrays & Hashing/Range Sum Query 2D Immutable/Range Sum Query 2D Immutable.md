# Range Sum Query 2D Immutable

You are given a 2D integer matrix `matrix`. Build a class `NumMatrix` that answers many queries of the form: what is the sum of all elements inside the rectangle whose upper-left corner is `(row1, col1)` and lower-right corner is `(row2, col2)` (both corners inclusive)?

- `NumMatrix(matrix)` preprocesses the matrix.
- `sumRegion(row1, col1, row2, col2)` returns the rectangle sum.

Each `sumRegion` call must run in `O(1)` time.

## Example

```text
Input:  ["NumMatrix","sumRegion","sumRegion","sumRegion"]
        [[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],
         [2,1,4,3],[1,1,2,2],[1,2,2,4]]
Output: [null,8,11,12]
Explanation: e.g. rows 1..2, cols 1..2 contain 6+3+2+0 = 11.
```

```python

```
