---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/accounts-merge/
neetcode: https://neetcode.io/problems/accounts-merge
---
# Accounts Merge

**Topic:** [[11 Graphs|Graphs]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/accounts-merge/) · [NeetCode](https://neetcode.io/problems/accounts-merge)

**Solve it in:** [[Accounts Merge]] · **Answer:** [[Accounts Merge - Solution]]

## Problem

You are given a list `accounts`. Each `accounts[i]` is a list of strings whose first element is a name and whose remaining elements are email addresses belonging to that account.

Two accounts belong to the same person if they share at least one email address (directly, or transitively through other accounts). Accounts with the same name do **not** necessarily belong to the same person, but all accounts of one person have the same name.

Merge the accounts and return them in the format `[name, email1, email2, ...]`, with each account's emails **sorted lexicographically**. The accounts themselves may be returned in any order.

## Examples

**Example 1**
```text
Input: accounts = [["Max","max@example.com","max.m@example.com"],
                   ["Max","max@example.com","mm@example.com"],
                   ["Erika","erika@example.com"],
                   ["Max","other.max@example.com"]]
Output: [["Max","max.m@example.com","max@example.com","mm@example.com"],
         ["Erika","erika@example.com"],
         ["Max","other.max@example.com"]]
Explanation: The first two accounts share "max@example.com"; the last "Max" is a different person.
```

**Example 2**
```text
Input: accounts = [["Anna","a1@example.com","a2@example.com"],["Ben","b1@example.com"]]
Output: [["Anna","a1@example.com","a2@example.com"],["Ben","b1@example.com"]]
```

## Constraints

- `1 <= accounts.length <= 1000`
- `2 <= accounts[i].length <= 10`
- `1 <= accounts[i][j].length <= 30`
- Names consist of English letters; emails are valid email strings

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
		pass  # your code here


def norm(res):
	"""Accounts may come back in any order; emails inside must be sorted."""
	return sorted(map(tuple, res))


if __name__ == "__main__":
	s = Solution()
	accounts = [["Max", "max@example.com", "max.m@example.com"],
				["Max", "max@example.com", "mm@example.com"],
				["Erika", "erika@example.com"],
				["Max", "other.max@example.com"]]
	assert norm(s.accountsMerge(accounts)) == norm([
		["Max", "max.m@example.com", "max@example.com", "mm@example.com"],
		["Erika", "erika@example.com"],
		["Max", "other.max@example.com"]])

	accounts = [["Anna", "a1@example.com", "a2@example.com"], ["Ben", "b1@example.com"]]
	assert norm(s.accountsMerge(accounts)) == norm(accounts)

	# transitive merge: A-B share x, B-C share y
	accounts = [["Max", "x@example.com", "a@example.com"],
				["Max", "c@example.com", "y@example.com"],
				["Max", "y@example.com", "x@example.com"]]
	assert norm(s.accountsMerge(accounts)) == norm([
		["Max", "a@example.com", "c@example.com", "x@example.com", "y@example.com"]])

	# duplicate email inside one account
	accounts = [["Ben", "b@example.com", "b@example.com"]]
	assert norm(s.accountsMerge(accounts)) == [("Ben", "b@example.com")]

	# same name, disjoint emails -> stay separate
	accounts = [["Anna", "z@example.com"], ["Anna", "y@example.com"]]
	assert norm(s.accountsMerge(accounts)) == [("Anna", "y@example.com"), ("Anna", "z@example.com")]
	print("All tests passed!")
```
