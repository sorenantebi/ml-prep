---
topic: "Greedy"
difficulty: Medium
leetcode: https://leetcode.com/problems/dota2-senate/
neetcode: https://neetcode.io/problems/dota2-senate
---
# Dota2 Senate - Solution

**Question:** [[Dota2 Senate - Question]] · **Difficulty:** Medium

## Intuition

The optimal move is always to ban the **next** opposing senator who would act — the one who threatens your party soonest. Simulate with two queues of indices, one per party. Compare the fronts: the smaller index acts first, bans the other front, and re-enters its queue at `index + n` (its position in the next round).

## Approach

1. Build queues `r` and `d` holding the indices of each party's senators.
2. While both are non-empty: pop `ri` and `di`. If `ri < di`, Radiant acts first: push `ri + n` back onto `r` (the Dire senator is banned). Otherwise push `di + n` onto `d`.
3. Return `"Radiant"` if `r` is non-empty, else `"Dire"`.

## Code

```python
from collections import deque


class Solution:
	def predictPartyVictory(self, senate: str) -> str:
		n = len(senate)
		r = deque(i for i, c in enumerate(senate) if c == "R")
		d = deque(i for i, c in enumerate(senate) if c == "D")
		while r and d:
			ri, di = r.popleft(), d.popleft()
			# the earlier senator bans the other and acts again next round
			if ri < di:
				r.append(ri + n)
			else:
				d.append(di + n)
		return "Radiant" if r else "Dire"
```

## Complexity

- **Time:** `O(n)` — every comparison permanently bans one senator.
- **Space:** `O(n)` — the two queues.

## Other Approaches

- **Single queue + ban counters:** cycle through senators, keeping a count of pending bans against each party — Time `O(n)`, Space `O(n)`.
- **Naive simulation with string scans:** for each active senator, search forward (circularly) for the next opponent to ban — Time `O(n^2)`, Space `O(n)`.

## Key Takeaway

Round-based elimination games are often modelled with queues where survivors re-enqueue with `index + n`; greedily eliminate the nearest upcoming opponent.
