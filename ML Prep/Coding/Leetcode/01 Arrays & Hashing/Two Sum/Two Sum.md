# Two Sum

You are given an integer array `nums` and an integer `target`. Find the two distinct indices `i` and `j` such that `nums[i] + nums[j] == target`, and return them as a list `[i, j]`. You may not use the same element twice. It is guaranteed that exactly one valid pair exists, and the two indices may be returned in either order.

## Example

```text
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] == 2 + 7 == 9
```

```python
# you will definitely only have one solution where two indices add up to target
# so what you can do is store the values of previous indices, and see if the target - current_value is in the hashmap

hashmap = {}
for i, num in enumerate(nums):
	if target - num in hashmap:
		return [hashmap[target - num], i]
	hashmap[num] = i

```
