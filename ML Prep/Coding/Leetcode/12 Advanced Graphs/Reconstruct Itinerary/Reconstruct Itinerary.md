# Reconstruct Itinerary

You are given a list of airline `tickets`, where `tickets[i] = [from_i, to_i]` is a one-way flight between two airports (three-letter codes). Rebuild the full travel itinerary in order and return it as a list of airports.

The trip always starts at `"JFK"`. Every ticket must be used exactly once. If several itineraries are valid, return the one that is lexicographically smallest when read as a single sequence of airport codes (e.g. `["JFK","LGA"]` comes before `["JFK","LGB"]`). You may assume at least one valid itinerary exists.

## Example

```text
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
```

```python

```
