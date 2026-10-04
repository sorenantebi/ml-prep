---
topic: "Greedy"
difficulty: Medium
leetcode: https://leetcode.com/problems/partition-labels/
neetcode: https://neetcode.io/problems/partition-labels
---
# Partition Labels

**Topic:** [[15 Greedy|Greedy]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/partition-labels/) · [NeetCode](https://neetcode.io/problems/partition-labels)

**Solve it in:** [[Partition Labels]] · **Answer:** [[Partition Labels - Solution]]

## Problem

Given a string `s`, split it into as many contiguous parts as possible such that each letter appears in **at most one** part. Concatenating the parts in order must give back `s`. Return a list of the sizes of the parts, in order.

## Examples

**Example 1**
```text
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation: "ababcbaca", "defegde", "hijhklij"
```

**Example 2**
```text
Input: s = "eccbbbbdec"
Output: [10]
```

**Example 3**
```text
Input: s = "abc"
Output: [1,1,1]
```

## Constraints

- `1 <= s.length <= 500`
- `s` consists of lowercase English letters.

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pass  # your code here


if __name__ == "__main__":
    sol = Solution()
    assert sol.partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert sol.partitionLabels("eccbbbbdec") == [10]
    assert sol.partitionLabels("abc") == [1, 1, 1]
    assert sol.partitionLabels("a") == [1]
    assert sol.partitionLabels("aaaa") == [4]
    assert sol.partitionLabels("abac") == [3, 1]
    assert sol.partitionLabels("caedbdedda") == [1, 9]
    print("All tests passed!")
```
