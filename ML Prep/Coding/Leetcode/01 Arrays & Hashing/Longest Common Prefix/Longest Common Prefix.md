# Longest Common Prefix

Given an array of strings `strs`, return the longest string that is a prefix of every string in the array. If the strings share no common starting characters, return the empty string `""`.

## Example

```text
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

```python
# use the first word as a reference, and look through the rest of the words, if you reach an i that is out of bounds or a char that isnt equal exit

ref = strs[0]
for i in range(len(ref)):
	for word in strs[1:]:
		if i >= len(word) or word[i] != ref[i]:
			return ref[:i]
return ref
		
```
