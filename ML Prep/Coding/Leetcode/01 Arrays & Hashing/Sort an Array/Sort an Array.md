# Sort an Array

Given an integer array `nums`, return it sorted in non-decreasing (ascending) order. You must implement the sort yourself without calling built-in sorting functions, achieving `O(n log n)` time and using as little extra space as possible.

## Example

```text
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
```

```python
# Mergesort

# keep splitting the array nums in half
# go from l -> m and m + 1 -> r
# this is inclusive

# if the size of l to m is 1, so if m - l == 0, return
# do left and right and then merge

# for merge u basically have a copy of nums on left and nums on right and it will be sorted from previous merges, so you just use two pointers to step through and add the minimum as the value on the l pointer
# r will start from len(nums) - 1
def merge(l, m, r):
	cp1, cp2 = nums[l:m+1], nums[m+1:r+1]
	i, j = 0, 0
	
	while i < len(cp1) and j < len(cp2):
		if cp1[i] < cp2[j]:
			nums[l] = cp1[i]
			i += 1
		else:
			nums[l] = cp2[j]
			j += 1
		l += 1
	
	# get rid of the rest
	while i < len(cp1):
		nums[l] = cp1[i]
		i += 1
		l += 1
	
	while j < len(cp2):
		nums[l] = cp2[j]
		j += 1
		l += 1
	
def mergeSort(l, r):
	if r - l == 0:
		return
	m = (r + l) // 2
	mergeSort(l, m)
	mergeSort(m + 1, r)
	merge(l, m, r)
	

mergeSort(0, len(nums) - 1)
return nums

```
