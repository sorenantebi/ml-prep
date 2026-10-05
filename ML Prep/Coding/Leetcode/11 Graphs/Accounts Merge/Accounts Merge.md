# Accounts Merge

You are given a list `accounts`. Each `accounts[i]` is a list of strings whose first element is a name and whose remaining elements are email addresses belonging to that account.

Two accounts belong to the same person if they share at least one email address (directly, or transitively through other accounts). Accounts with the same name do **not** necessarily belong to the same person, but all accounts of one person have the same name.

Merge the accounts and return them in the format `[name, email1, email2, ...]`, with each account's emails **sorted lexicographically**. The accounts themselves may be returned in any order.

## Example

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

```python

```
