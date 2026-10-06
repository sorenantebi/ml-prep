# Sort Colors

You are given an array `nums` of `n` objects colored red, white, or blue, encoded as the integers `0`, `1`, and `2` respectively. Rearrange the array **in place** so that all `0`s come first, then all `1`s, then all `2`s. Do not use the library sort function; the method returns nothing.

## Example

```text
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

```python

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
