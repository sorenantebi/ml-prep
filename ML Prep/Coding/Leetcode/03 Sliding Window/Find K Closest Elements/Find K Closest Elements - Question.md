---
topic: "Sliding Window"
difficulty: Medium
leetcode: https://leetcode.com/problems/find-k-closest-elements/
neetcode: https://neetcode.io/problems/find-k-closest-elements
---
# Find K Closest Elements

**Topic:** [[03 Sliding Window|Sliding Window]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/find-k-closest-elements/) · [NeetCode](https://neetcode.io/problems/find-k-closest-elements)

**Solve it in:** [[Find K Closest Elements]] · **Answer:** [[Find K Closest Elements - Solution]]

## Problem

Given a **sorted** integer array `arr`, an integer `k`, and an integer `x`, return the `k` elements of `arr` closest to `x`, in ascending order. Element `a` is closer than `b` if `|a - x| < |b - x|`, or if the distances are equal and `a < b` (ties favor the smaller value).

## Examples

**Example 1**
```text
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
```

**Example 2**
```text
Input: arr = [1,1,2,3,4,5], k = 4, x = -1
Output: [1,1,2,3]
```

## Constraints

- `1 <= k <= arr.length <= 10^4`
- `arr` is sorted in ascending order
- `-10^4 <= arr[i], x <= 10^4`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
		pass  # your code here


if __name__ == "__main__":
	sol = Solution()
	assert sol.findClosestElements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]
	assert sol.findClosestElements([1, 1, 2, 3, 4, 5], 4, -1) == [1, 1, 2, 3]
	assert sol.findClosestElements([1, 2, 3, 4, 5], 4, 10) == [2, 3, 4, 5]
	assert sol.findClosestElements([5], 1, 0) == [5]
	assert sol.findClosestElements([1, 3], 1, 2) == [1]
	assert sol.findClosestElements([1, 1, 1, 10, 10, 10], 1, 9) == [10]
	assert sol.findClosestElements([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5) == [3, 3, 4]
	assert sol.findClosestElements([1, 2, 3, 4, 5], 5, 3) == [1, 2, 3, 4, 5]
	print("All tests passed!")
```
