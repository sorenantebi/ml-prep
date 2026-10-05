# Cheapest Flights Within K Stops

There are `n` cities numbered `0` to `n - 1`, connected by directed flights. `flights[i] = [from_i, to_i, price_i]` is a flight from `from_i` to `to_i` costing `price_i`.

Given `src`, `dst`, and an integer `k`, return the cheapest total price to fly from `src` to `dst` using **at most `k` stops** (i.e. at most `k + 1` flights; intermediate cities count as stops). If no such route exists, return `-1`.

## Example

```text
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation: 0 -> 1 -> 3 costs 700. 0 -> 1 -> 2 -> 3 is cheaper (400) but uses 2 stops.
```

```python

```
