---
topic: "Bit Manipulation"
difficulty: Medium
leetcode: https://leetcode.com/problems/minimum-array-end/
neetcode: https://neetcode.io/problems/minimum-array-end
---
# Minimum Array End

**Topic:** [[18 Bit Manipulation|Bit Manipulation]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/minimum-array-end/) · [NeetCode](https://neetcode.io/problems/minimum-array-end)

**Solve it in:** [[Minimum Array End]] · **Answer:** [[Minimum Array End - Solution]]

## Problem

You are given two integers `n` and `x`. Build an array `nums` of `n` positive integers that is **strictly increasing** (`nums[i] < nums[i+1]`) and whose bitwise AND of all elements equals `x`.

Return the **smallest possible value** of the last element, `nums[n - 1]`.

## Examples

**Example 1**
```text
Input: n = 3, x = 4
Output: 6
Explanation: nums = [4,5,6]; 100 & 101 & 110 = 100
```

**Example 2**
```text
Input: n = 2, x = 7
Output: 15
Explanation: nums = [7,15]; 0111 & 1111 = 0111
```

## Constraints

- `1 <= n, x <= 10^8`

## Starter Code & Test Cases

```python
class Solution:
	def minEnd(self, n: int, x: int) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.minEnd(3, 4) == 6
	assert s.minEnd(2, 7) == 15
	assert s.minEnd(1, 5) == 5
	assert s.minEnd(5, 1) == 9       # 1, 3, 5, 7, 9
	assert s.minEnd(3, 2) == 6       # 2, 3, 6
	assert s.minEnd(6, 5) == 23      # 5, 7, 13, 15, 21, 23

	# Brute-force cross-check on small inputs
	def brute(n, x):
		cur, cnt = x, 1
		while cnt < n:
			cur += 1
			if cur & x == x:
				cnt += 1
		return cur

	for n in range(1, 12):
		for x in range(1, 20):
			assert s.minEnd(n, x) == brute(n, x)
	assert s.minEnd(1000, 12345) == brute(1000, 12345)
	print("All tests passed!")
```
