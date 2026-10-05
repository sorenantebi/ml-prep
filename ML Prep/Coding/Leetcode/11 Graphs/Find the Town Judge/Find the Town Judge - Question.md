---
topic: "Graphs"
difficulty: Easy
leetcode: https://leetcode.com/problems/find-the-town-judge/
neetcode: https://neetcode.io/problems/find-the-town-judge
---
# Find the Town Judge

**Topic:** [[11 Graphs|Graphs]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/find-the-town-judge/) · [NeetCode](https://neetcode.io/problems/find-the-town-judge)

**Solve it in:** [[Find the Town Judge]] · **Answer:** [[Find the Town Judge - Solution]]

## Problem

A town has `n` people labeled `1` to `n`. There is a rumor that one of them is the secret town judge. If the judge exists, then:

1. The judge trusts nobody.
2. Everybody else (all other `n - 1` people) trusts the judge.
3. Exactly one person satisfies both properties 1 and 2.

You are given `trust`, where `trust[i] = [a, b]` means person `a` trusts person `b`. If a trust relationship is not listed, it does not exist.

Return the label of the town judge if one can be identified, otherwise return `-1`.

## Examples

**Example 1**
```text
Input: n = 2, trust = [[1,2]]
Output: 2
```

**Example 2**
```text
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
```

**Example 3**
```text
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Explanation: Person 3 trusts person 1, so they cannot be the judge.
```

## Constraints

- `1 <= n <= 1000`
- `0 <= trust.length <= 10^4`
- `trust[i].length == 2`, all pairs are unique
- `a != b`, `1 <= a, b <= n`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def findJudge(self, n: int, trust: List[List[int]]) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.findJudge(2, [[1,2]]) == 2
	assert s.findJudge(3, [[1,3],[2,3]]) == 3
	assert s.findJudge(3, [[1,3],[2,3],[3,1]]) == -1
	assert s.findJudge(1, []) == 1
	assert s.findJudge(2, []) == -1
	assert s.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]) == 3
	assert s.findJudge(3, [[1,2],[2,3]]) == -1
	print("All tests passed!")
```
