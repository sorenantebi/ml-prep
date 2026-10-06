# Majority Element

Given an array `nums` of size `n`, return its majority element: the value that occurs strictly more than `⌊n / 2⌋` times. You may assume a majority element always exists in the input.

## Example

```text
Input: nums = [3,2,3]
Output: 3
```

```python

# Boyer moore voting algorithm
# for O(1) space
# basically you have candidates and add if you see the same and subtract if you see different, basiclly cancel out
# 1 1 2 2 1
# +1 +1 -1 -1 --> count == 0 --> new candidate == 1 --> count += 1

candidate = -1
count = 0

for num in nums:
	if count == 0:
		candidate = num
	if num == candidate:
		count += 1
	else:
		count -= 1
return candidate

```
