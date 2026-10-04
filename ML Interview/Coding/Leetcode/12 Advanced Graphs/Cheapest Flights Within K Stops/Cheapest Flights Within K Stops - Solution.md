---
topic: "Advanced Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/cheapest-flights-within-k-stops/
neetcode: https://neetcode.io/problems/cheapest-flight-path
---
# Cheapest Flights Within K Stops - Solution

**Question:** [[Cheapest Flights Within K Stops - Question]] · **Difficulty:** Medium

## Intuition

The stop limit breaks plain Dijkstra (a cheaper path with more hops may block a slightly pricier one with fewer hops). **Bellman-Ford limited to `k + 1` rounds** fits exactly: after round `i`, `prices[v]` is the cheapest cost using at most `i` flights. Relaxing from a snapshot of the previous round prevents chaining several flights within one round.

## Approach

1. `prices = [inf] * n`, `prices[src] = 0`.
2. Repeat `k + 1` times: copy `prices` to `tmp`; for every flight `(u, v, w)` with finite `prices[u]`, set `tmp[v] = min(tmp[v], prices[u] + w)`; then `prices = tmp`.
3. Return `prices[dst]` or `-1` if it's still infinite.

## Code

```python
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        prices = [INF] * n
        prices[src] = 0

        for _ in range(k + 1):  # at most k stops == at most k + 1 flights
            tmp = prices[:]  # relax from last round's values only
            for u, v, w in flights:
                if prices[u] != INF and prices[u] + w < tmp[v]:
                    tmp[v] = prices[u] + w
            prices = tmp

        return -1 if prices[dst] == INF else prices[dst]
```

## Complexity

- **Time:** `O(k · E)` — `k + 1` rounds over all flights.
- **Space:** `O(n)` — two price arrays.

## Other Approaches

- **BFS by levels with pruning:** expand level by level (one flight per level) up to `k + 1` levels, keeping best cost per city — Time `O(k · E)`, Space `O(n + E)`.
- **Dijkstra on state `(city, stops)`:** heap ordered by cost, track best stops per city to prune — Time `O(E · k · log(E · k))`, Space `O(n · k)`.

## Key Takeaway

When a shortest path has a hop limit, use Bellman-Ford with exactly `limit` rounds and a copy of the previous round's distances.
