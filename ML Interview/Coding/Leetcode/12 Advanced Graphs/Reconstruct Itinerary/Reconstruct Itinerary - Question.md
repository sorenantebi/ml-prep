---
topic: "Advanced Graphs"
difficulty: Hard
leetcode: https://leetcode.com/problems/reconstruct-itinerary/
neetcode: https://neetcode.io/problems/reconstruct-flight-path
---
# Reconstruct Itinerary

**Topic:** [[12 Advanced Graphs|Advanced Graphs]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/reconstruct-itinerary/) · [NeetCode](https://neetcode.io/problems/reconstruct-flight-path)

**Solve it in:** [[Reconstruct Itinerary]] · **Answer:** [[Reconstruct Itinerary - Solution]]

## Problem

You are given a list of airline `tickets`, where `tickets[i] = [from_i, to_i]` is a one-way flight between two airports (three-letter codes). Rebuild the full travel itinerary in order and return it as a list of airports.

The trip always starts at `"JFK"`. Every ticket must be used exactly once. If several itineraries are valid, return the one that is lexicographically smallest when read as a single sequence of airport codes (e.g. `["JFK","LGA"]` comes before `["JFK","LGB"]`). You may assume at least one valid itinerary exists.

## Examples

**Example 1**
```text
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
```

**Example 2**
```text
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: ["JFK","SFO","ATL","JFK","ATL","SFO"] is also valid but larger lexicographically.
```

**Example 3**
```text
Input: tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
Output: ["JFK","NRT","JFK","KUL"]
Explanation: Going to KUL first (smaller) would get stuck before using all tickets.
```

## Constraints

- `1 <= tickets.length <= 300`
- `tickets[i].length == 2`, each code has 3 uppercase English letters
- `from_i != to_i`
- At least one valid itinerary that uses all tickets exists.

## Starter Code & Test Cases

```python
from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]) == ["JFK","MUC","LHR","SFO","SJC"]
    assert s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]) == ["JFK","ATL","JFK","SFO","ATL","SFO"]
    assert s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]) == ["JFK","NRT","JFK","KUL"]
    assert s.findItinerary([["JFK","AAA"]]) == ["JFK","AAA"]
    assert s.findItinerary([["JFK","AAA"],["AAA","JFK"],["JFK","AAA"]]) == ["JFK","AAA","JFK","AAA"]
    assert s.findItinerary([["JFK","BBB"],["BBB","JFK"],["JFK","AAA"],["AAA","JFK"]]) == ["JFK","AAA","JFK","BBB","JFK"]
    print("All tests passed!")
```
