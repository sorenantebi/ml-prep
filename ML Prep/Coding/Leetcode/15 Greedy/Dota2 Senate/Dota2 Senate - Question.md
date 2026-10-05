---
topic: "Greedy"
difficulty: Medium
leetcode: https://leetcode.com/problems/dota2-senate/
neetcode: https://neetcode.io/problems/dota2-senate
---
# Dota2 Senate

**Topic:** [[15 Greedy|Greedy]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/dota2-senate/) · [NeetCode](https://neetcode.io/problems/dota2-senate)

**Solve it in:** [[Dota2 Senate]] · **Answer:** [[Dota2 Senate - Solution]]

## Problem

A senate has senators from two parties, Radiant (`'R'`) and Dire (`'D'`), given as a string `senate` in which character `i` is the party of senator `i`. Voting proceeds in rounds; within a round senators act in order of their index, and senators who have lost their rights are skipped. On their turn a senator may do one of two things:

- **Ban** one other senator, who loses all rights in this and all future rounds.
- **Announce victory**, if every senator who still has rights belongs to the same party.

Rounds repeat until one party announces victory. Assuming every senator plays optimally for their own party, return `"Radiant"` or `"Dire"` for the winning party.

## Examples

**Example 1**
```text
Input: senate = "RD"
Output: "Radiant"
Explanation: R bans D; R is then the only senator left.
```

**Example 2**
```text
Input: senate = "RDD"
Output: "Dire"
Explanation: R bans the first D, the second D bans R, and Dire wins.
```

## Constraints

- `n == senate.length`
- `1 <= n <= 10^4`
- `senate[i]` is `'R'` or `'D'`

## Starter Code & Test Cases

```python
from collections import deque


class Solution:
	def predictPartyVictory(self, senate: str) -> str:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.predictPartyVictory("RD") == "Radiant"
	assert s.predictPartyVictory("RDD") == "Dire"
	assert s.predictPartyVictory("R") == "Radiant"
	assert s.predictPartyVictory("D") == "Dire"
	assert s.predictPartyVictory("DDRRR") == "Dire"
	assert s.predictPartyVictory("RRDDD") == "Radiant"
	assert s.predictPartyVictory("DRRDRDRDRDDRDRDR") == "Radiant"
	print("All tests passed!")
```
