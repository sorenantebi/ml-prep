# Single Threaded CPU

There are `n` tasks numbered `0` to `n - 1`, given as `tasks[i] = [enqueueTime_i, processingTime_i]`: task `i` becomes available at time `enqueueTime_i` and takes `processingTime_i` units to finish once started.

A single-threaded CPU processes at most one task at a time, without interruption, using this rule:

- If the CPU is idle and nothing is available, it stays idle until a task becomes available.
- If the CPU is idle and tasks are available, it picks the one with the **shortest processing time**; ties are broken by the **smallest index**.
- A task finishing and a new task starting can happen at the same instant.

Return the order (list of indices) in which the CPU processes the tasks.

## Example

```text
Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]
Explanation: t=1 run 0 (ends 3); t=3 pick 2 over 1 (shorter); t=5 pick 3; t=6 run 1
```

```python

```
