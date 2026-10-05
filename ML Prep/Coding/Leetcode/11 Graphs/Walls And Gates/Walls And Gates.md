# Walls And Gates

You are given an `m x n` grid `rooms` with three possible values:

- `-1`: a wall or obstacle
- `0`: a gate
- `INF = 2^31 - 1 = 2147483647`: an empty room

Fill each empty room **in place** with the distance (number of 4-directional steps) to its nearest gate. If an empty room cannot reach any gate, leave it as `INF`. Walls and gates stay unchanged. Moves go up, down, left, or right and cannot pass through walls.

The function returns nothing; the grid is modified in place.

## Example

```text
Input: rooms = [[INF,-1,0,INF],[INF,INF,INF,-1],[INF,-1,INF,-1],[0,-1,INF,INF]]
Output:        [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
```

```python

```
