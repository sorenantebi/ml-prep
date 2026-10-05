# Task Scheduler

You are given a list of CPU tasks `tasks`, each labeled by an uppercase letter `'A'`–`'Z'`, and a non-negative integer `n`. Each time unit the CPU can either run exactly one task or stay idle. Tasks can be executed in any order, but two runs of the **same** label must be separated by at least `n` time units (i.e. at least `n` other units — tasks or idles — in between).

Return the minimum number of time units needed to finish all tasks.

## Example

```text
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B
```

```python

```
