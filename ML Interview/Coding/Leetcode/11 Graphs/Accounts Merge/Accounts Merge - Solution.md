---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/accounts-merge/
neetcode: https://neetcode.io/problems/accounts-merge
---
# Accounts Merge - Solution

**Question:** [[Accounts Merge - Question]] · **Difficulty:** Medium

## Intuition

Each account says "all of these emails belong together". Treat accounts as nodes and union two accounts whenever they share an email — mapping each email to the first account that contained it makes this easy. After all unions, each Union-Find root represents one person; collect and sort the emails per root.

## Approach

1. Initialize Union-Find over account indices.
2. Iterate accounts; for every email, if it was seen before in account `j`, union the current account with `j`; otherwise record `owner[email] = i`.
3. Group emails by `find(owner[email])`.
4. For each group, output `[name of root account] + sorted(emails)`.

## Code

```python
from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = list(range(len(accounts)))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        owner = {}  # email -> index of first account containing it
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in owner:
                    parent[find(i)] = find(owner[email])  # union the two accounts
                else:
                    owner[email] = i

        groups = defaultdict(list)  # root account -> emails
        for email, i in owner.items():
            groups[find(i)].append(email)

        return [[accounts[root][0]] + sorted(emails) for root, emails in groups.items()]
```

## Complexity

- **Time:** `O(N K log(N K))` — `N K` total emails; Union-Find work is near-linear and sorting the emails dominates.
- **Space:** `O(N K)` — the owner map and the groups.

## Other Approaches

- **DFS on an email graph:** connect each account's first email to its other emails, then DFS from each unvisited email to collect a component — Time `O(N K log(N K))`, Space `O(N K)`.

## Key Takeaway

"Merge groups that share any element" is a classic Union-Find problem: map each element to its first group and union on collisions.
