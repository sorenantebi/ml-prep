# Remove Element

You are given an integer array `nums` and an integer `val`. Remove every occurrence of `val` from `nums` **in place** and return `k`, the number of elements that are not equal to `val`. After the call, the first `k` positions of `nums` must hold exactly the elements not equal to `val` (in any order); whatever is stored beyond index `k - 1` does not matter. You must not allocate a second array.

## Example

```text
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
```

```python
# loop through with two pointers, one to keep track of the insertion index and one to loop through
# if you come across a number that is not val, put it into the insertion index and increment
l = 0

for r in range(len(nums)):
	if nums[r] != val:
		nums[l] = val
		l += 1
return l

```
