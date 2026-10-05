---
topic: "Heap / Priority Queue"
difficulty: Medium
leetcode: https://leetcode.com/problems/design-twitter/
neetcode: https://neetcode.io/problems/design-twitter-feed
---
# Design Twitter

**Topic:** [[08 Heap - Priority Queue|Heap / Priority Queue]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/design-twitter/) · [NeetCode](https://neetcode.io/problems/design-twitter-feed)

**Solve it in:** [[Design Twitter]] · **Answer:** [[Design Twitter - Solution]]

## Problem

Design a tiny social feed service. Users can post tweets, follow and unfollow other users, and fetch a news feed containing the **10 most recent** tweet IDs posted by themselves or by anyone they follow, ordered from newest to oldest.

Implement `Twitter`:

- `Twitter()` creates an empty service.
- `void postTweet(int userId, int tweetId)` records a new tweet with a unique `tweetId` by `userId`. Each call is more recent than all previous calls.
- `List[int] getNewsFeed(int userId)` returns up to 10 tweet IDs from the user and their followees, most recent first.
- `void follow(int followerId, int followeeId)` makes `followerId` follow `followeeId`.
- `void unfollow(int followerId, int followeeId)` makes `followerId` stop following `followeeId` (no-op if not following).

A user always sees their own tweets; following or unfollowing oneself has no effect on that.

## Examples

**Example 1**
```text
Input:  ["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
        [[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]
Output: [null,null,[5],null,null,[6,5],null,[5]]
```

**Example 2**
```text
Input:  ["Twitter","postTweet","postTweet","getNewsFeed"]
        [[],[1,1],[1,2],[2]]
Output: [null,null,null,[]]
Explanation: user 2 follows nobody and has no tweets
```

## Constraints

- `1 <= userId, followerId, followeeId <= 500`
- `0 <= tweetId <= 10^4`, all tweet IDs are unique
- At most `3 * 10^4` total calls

## Starter Code & Test Cases

```python
from typing import List
from collections import defaultdict
import heapq


class Twitter:
	def __init__(self):
		pass  # your code here

	def postTweet(self, userId: int, tweetId: int) -> None:
		pass  # your code here

	def getNewsFeed(self, userId: int) -> List[int]:
		pass  # your code here

	def follow(self, followerId: int, followeeId: int) -> None:
		pass  # your code here

	def unfollow(self, followerId: int, followeeId: int) -> None:
		pass  # your code here


if __name__ == "__main__":
	t = Twitter()
	t.postTweet(1, 5)
	assert t.getNewsFeed(1) == [5]
	t.follow(1, 2)
	t.postTweet(2, 6)
	assert t.getNewsFeed(1) == [6, 5]
	t.unfollow(1, 2)
	assert t.getNewsFeed(1) == [5]

	t = Twitter()
	t.postTweet(1, 1)
	t.postTweet(1, 2)
	assert t.getNewsFeed(2) == []

	# more than 10 tweets: only the 10 most recent, interleaved across users
	t = Twitter()
	for i in range(1, 13):
		t.postTweet(1 if i % 2 else 2, i)
	t.follow(1, 2)
	assert t.getNewsFeed(1) == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3]
	assert t.getNewsFeed(2) == [12, 10, 8, 6, 4, 2]

	# self-follow / unfollow of self and of non-followed users are harmless
	t = Twitter()
	t.postTweet(3, 100)
	t.follow(3, 3)
	t.unfollow(3, 3)
	t.unfollow(3, 4)
	assert t.getNewsFeed(3) == [100]

	# following a user includes their older tweets too
	t = Twitter()
	t.postTweet(2, 20)
	t.postTweet(1, 10)
	t.follow(1, 2)
	t.follow(1, 2)
	assert t.getNewsFeed(1) == [10, 20]
	print("All tests passed!")
```
