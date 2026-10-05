---
topic: "Heap / Priority Queue"
difficulty: Medium
leetcode: https://leetcode.com/problems/design-twitter/
neetcode: https://neetcode.io/problems/design-twitter-feed
---
# Design Twitter - Solution

**Question:** [[Design Twitter - Question]] · **Difficulty:** Medium

## Intuition

Each user's tweets are already in chronological order in their own list, so building a feed is a **merge of k sorted lists** where we only need the first 10 items. A max-heap seeded with the newest tweet from each relevant user lets us pull the global newest, then advance into that user's list — just like merging k sorted lists.

## Approach

1. Keep a global counter `time` that increases on every post, `tweets[user] = [(time, tweetId), ...]`, and `following[user] = set()`.
2. `postTweet`: append `(time, tweetId)` and increment `time`.
3. `follow` / `unfollow`: add to / discard from the follower's set (ignore self-follow).
4. `getNewsFeed`: for the user and each followee with tweets, push `(-time, tweetId, user, index)` of their latest tweet.
5. Pop up to 10 times; after each pop, push the same user's previous tweet (`index - 1`) if it exists.

## Code

```python
from typing import List
from collections import defaultdict
import heapq


class Twitter:
	def __init__(self):
		self.time = 0
		self.tweets = defaultdict(list)     # userId -> [(time, tweetId)] oldest -> newest
		self.following = defaultdict(set)   # userId -> set of followees

	def postTweet(self, userId: int, tweetId: int) -> None:
		self.tweets[userId].append((self.time, tweetId))
		self.time += 1

	def getNewsFeed(self, userId: int) -> List[int]:
		heap = []
		for uid in self.following[userId] | {userId}:
			if self.tweets[uid]:
				idx = len(self.tweets[uid]) - 1
				t, tid = self.tweets[uid][idx]
				heap.append((-t, tid, uid, idx))  # negate time -> newest first
		heapq.heapify(heap)

		feed = []
		while heap and len(feed) < 10:
			_, tid, uid, idx = heapq.heappop(heap)
			feed.append(tid)
			if idx > 0:  # advance to this user's next-older tweet
				t, ntid = self.tweets[uid][idx - 1]
				heapq.heappush(heap, (-t, ntid, uid, idx - 1))
		return feed

	def follow(self, followerId: int, followeeId: int) -> None:
		if followerId != followeeId:
			self.following[followerId].add(followeeId)

	def unfollow(self, followerId: int, followeeId: int) -> None:
		self.following[followerId].discard(followeeId)
```

## Complexity

- **Time:** `postTweet`, `follow`, `unfollow` are `O(1)`; `getNewsFeed` is `O(F + 10 log F)` where `F` is the number of followees (heapify plus at most 10 pops/pushes).
- **Space:** `O(U + T + E)` for users, tweets, and follow edges; the feed heap uses `O(F)`.

## Other Approaches

- **Collect and sort:** gather all tweets of the user and followees, sort by time, take 10 — Time `O(N log N)` per feed where `N` is the total relevant tweets, Space `O(N)`.
- **Cap stored tweets:** only keep each user's last 10 tweets (enough for any feed), bounding memory per user — same heap merge, Space `O(10 * U)` for tweets.

## Key Takeaway

A news feed is "merge k sorted lists, take the top 10": seed a heap with each source's newest item and lazily advance only the source you popped from.
