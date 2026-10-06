# Group Anagrams

Given an array of strings `strs`, partition the strings into groups such that two strings land in the same group exactly when they are anagrams of each other (same letters with the same multiplicities). Return the list of groups. Both the order of the groups and the order of strings inside each group may be arbitrary.

## Example

```text
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

```python
# create bin representation of the words using ord(char) - ord('a') and frequency. use a dict to store the tuple representation of the bins
hashmap = defaultdict(list)

for word in strs:
	bin_ = [0] * 26
	for c in word:
		bin_[ord(c) - ord('a')] += 1
	hashmap[tuple(bin_)].append(word)
return hashmap.values()


```
