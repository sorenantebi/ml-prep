# Dota2 Senate

A senate has senators from two parties, Radiant (`'R'`) and Dire (`'D'`), given as a string `senate` in which character `i` is the party of senator `i`. Voting proceeds in rounds; within a round senators act in order of their index, and senators who have lost their rights are skipped. On their turn a senator may do one of two things:

- **Ban** one other senator, who loses all rights in this and all future rounds.
- **Announce victory**, if every senator who still has rights belongs to the same party.

Rounds repeat until one party announces victory. Assuming every senator plays optimally for their own party, return `"Radiant"` or `"Dire"` for the winning party.

## Example

```text
Input: senate = "RD"
Output: "Radiant"
Explanation: R bans D; R is then the only senator left.
```

```python

```
