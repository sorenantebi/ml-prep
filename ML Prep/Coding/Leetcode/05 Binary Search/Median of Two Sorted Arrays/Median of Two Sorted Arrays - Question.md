---
topic: "Binary Search"
difficulty: Hard
leetcode: https://leetcode.com/problems/median-of-two-sorted-arrays/
neetcode: https://neetcode.io/problems/median-of-two-sorted-arrays
---
# Median of Two Sorted Arrays

**Topic:** [[05 Binary Search|Binary Search]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/) · [NeetCode](https://neetcode.io/problems/median-of-two-sorted-arrays)

**Solve it in:** [[Median of Two Sorted Arrays]] · **Answer:** [[Median of Two Sorted Arrays - Solution]]

## Problem

Given two sorted arrays `nums1` (length `m`) and `nums2` (length `n`), return the median of the combined collection of all `m + n` numbers. If the total count is even, the median is the average of the two middle values. The overall run time should be `O(log(m + n))`.

## Examples

**Example 1**
```text
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged = [1,2,3]
```

**Example 2**
```text
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged = [1,2,3,4], (2 + 3) / 2 = 2.5
```

**Example 3**
```text
Input: nums1 = [], nums2 = [1]
Output: 1.00000
```

## Constraints

- `0 <= m, n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`
- Both arrays are sorted in non-decreasing order

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()

	def close(a, b):
		return abs(a - b) < 1e-5

	assert close(s.findMedianSortedArrays([1, 3], [2]), 2.0)
	assert close(s.findMedianSortedArrays([1, 2], [3, 4]), 2.5)
	assert close(s.findMedianSortedArrays([], [1]), 1.0)
	assert close(s.findMedianSortedArrays([2], []), 2.0)
	assert close(s.findMedianSortedArrays([1, 1, 1], [1, 1]), 1.0)
	assert close(s.findMedianSortedArrays([-5, 3, 6, 12, 15], [-12, -10, -6, -3, 4, 10]), 3.0)
	assert close(s.findMedianSortedArrays([1, 2, 3, 4, 5, 6], [100]), 4.0)

	import random
	rng = random.Random(0)
	for _ in range(300):
		a = sorted(rng.randint(-50, 50) for _ in range(rng.randint(0, 8)))
		b = sorted(rng.randint(-50, 50) for _ in range(rng.randint(0 if a else 1, 8)))
		merged = sorted(a + b)
		L = len(merged)
		exp = merged[L // 2] if L % 2 else (merged[L // 2 - 1] + merged[L // 2]) / 2
		assert close(s.findMedianSortedArrays(a, b), exp)
	print("All tests passed!")
```
