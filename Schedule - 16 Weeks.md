---
tags: [studyplan, schedule]
---
# Schedule: 16 weeks

**Tue 6 Oct 2026 to Mon 25 Jan 2027** · 16 weeks · Mon, Tue, Wed, Thu 19:30–21:30 · **Friday is the rest day** · Sat and Sun 11:00–13:00 and 14:00–16:00 · about 16 h/week

Part of [[STUDYPLAN]]. This is the slower, deeper plan: **system design, AI fundamentals and hands-on ML coding (NumPy, Pandas, PyTorch, a Claude agent) come first, LeetCode is one evening session a week plus your daytime problems.** Tick a session when it is done (the Tasks plugin stamps the date). Problems are ticked in their section notes (for example [[01 Arrays & Hashing]]) and each problem link opens the note where you read it and write your code.

## Weekly rhythm

| Day | Time | Block |
|---|---|---|
| Mon–Thu | before 19:00 | Daytime LeetCode: 2 problems a day, listed under each date |
| Mon | 19:30–21:30 | Review: redo 4 coding problems cold, then a rotating review hour |
| Tue | 19:30–21:30 | LeetCode |
| Wed | 19:30–21:30 | AI fundamentals |
| Thu | 19:30–21:30 | ML coding: NumPy, Pandas, PyTorch, then the Claude agent project |
| Fri | | Rest |
| Sat | 11:00–13:00 | System design concepts (databases, caching, queues, search and so on) |
| Sat | 14:00–16:00 | System design problem |
| Sun | 11:00–13:00 | AI fundamentals |
| Sun | 14:00–16:00 | System design problem |

## Rules

- **Coding pace:** every problem gets a fixed slot: **🟢 Easy 10 min, 🟡 Medium 30 min, 🔴 Hard 45 min**. If you have no approach after a third of the slot (3 / 10 / 15 min), read the Solution, close it, and rewrite it from memory in the time left. When the slot ends, move on, and put anything you did not solve alone on the Fumbled list in [[STUDYPLAN]].
- **System design:** read only the Question note, design out loud on a blank Excalidraw board, then compare. Never read the Solution first. Concept sessions use [[System Design Concepts]].
- **AI fundamentals:** answer out loud before opening the collapsed answers.
- **ML coding:** write the code yourself in the [[Numpy]], [[Pandas]] and [[Pytorch]] notes (run it with the code block). Do not paste solutions. The agent project is specified in [[Build an Agent with the Claude SDK]].
- **Daytime LeetCode:** the problems under each date's *Before 19:00* line are extras for free time before the evening, with the same slot lengths. Skip them on a heavy day rather than rushing.
- **Spaced review:** treat the review blocks as non-negotiable. If time is short, shorten new material, not review.
- **If you miss a session:** do not cram it in. Shift the rest of the day to the next free block, and drop the lowest-priority item first.

## Review map (spaced repetition)

| What | When it comes back |
|---|---|
| Coding problems | Mon of the same week, then 1, 2 and 4 weeks later (4 problems each Monday, exact names listed), plus the Fumbled list |
| AI fundamentals | 15-minute recall of the previous AI session at the start of every AI session, plus a rotating AI-75 quiz every Monday |
| System design | 10-minute recall of an earlier design (1 week earlier, every third session 3 weeks earlier) at the start of each design session, and two cold-redraw review hours on Mondays in weeks 12 and 13 |
| ML coding | Monday review hours re-implement earlier NumPy, Pandas and PyTorch code from memory, and the last Thursday has timed mocks |
| Final weeks | Timed coding rounds, four unseen design mocks, a timed agent build, and the cheat sheet |

- **Total:** 80 evening LeetCode problems (50 🟢 and 30 🟡, about 23 h) plus 128 (7 🟢, 121 🟡) daytime problems · 24 general design problems + 4 unseen mocks + 4 ML system design sessions + 16 concept sessions · all 12 AI fundamentals topics, 17 coding challenges and 5 AI case studies · 2 NumPy, 2 Pandas, 5 PyTorch, 6 agent-project sessions and a timed mock session.


---

## Week 1: Tue 6 Oct 2026 – Mon 12 Oct 2026

**Focus:** NumPy and ML foundations · LLM basics · Bitly, Rate Limiter · LeetCode: Arrays & Hashing

### Tue 6 Oct 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-10-06
	- 🟡 [[Sort an Array]] (Arrays & Hashing) (30 min)
	- 🟡 [[Sort Colors]] (Arrays & Hashing) (30 min)
- [ ] 19:30–21:30 · LeetCode: Arrays & Hashing (9 problems) 📅 2026-10-06
	- 19:30–19:40 🟢 [[Concatenation of Array]] (Arrays & Hashing) (10 min)
	- 19:40–19:50 🟢 [[Contains Duplicate]] (Arrays & Hashing) (10 min)
	- 19:50–20:00 🟢 [[Valid Anagram]] (Arrays & Hashing) (10 min)
	- 20:00–20:10 🟢 [[Two Sum]] (Arrays & Hashing) (10 min)
	- 20:10–20:20 🟢 [[Longest Common Prefix]] (Arrays & Hashing) (10 min)
	- 20:20–20:50 🟡 [[Group Anagrams]] (Arrays & Hashing) (30 min)
	- 20:50–21:00 🟢 [[Remove Element]] (Arrays & Hashing) (10 min)
	- 21:00–21:10 🟢 [[Majority Element]] (Arrays & Hashing) (10 min)
	- 21:10–21:20 🟢 [[Design HashSet]] (Arrays & Hashing) (10 min)
	- 21:20–21:30 Wrap-up and buffer: add anything you could not solve alone to the Fumbled list in [[STUDYPLAN]]; tick each problem in its section note

### Wed 7 Oct 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-10-07
	- 🟡 [[Top K Frequent Elements]] (Arrays & Hashing) (30 min)
	- 🟡 [[Encode and Decode Strings]] (Arrays & Hashing) (30 min)
- [ ] 19:30–21:30 · AI fundamentals 📅 2026-10-07
	- 19:30–20:10 Read the [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/01-ml-and-dl-foundations/README|ML & DL foundations crash course]]
	- 20:10–21:30 Answer out loud, before opening each answer: [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/01-ml-and-dl-foundations/questions|ML & DL foundations questions (Basic)]]

### Thu 8 Oct 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-10-08
	- 🟡 [[Range Sum Query 2D Immutable]] (Arrays & Hashing) (30 min)
	- 🟡 [[Product of Array Except Self]] (Arrays & Hashing) (30 min)
- [ ] 19:30–21:30 · ML coding: NumPy basics 📅 2026-10-08
	- 19:30–20:00 [[Numpy]]: shapes, dtypes, reshape, transpose, boolean masks and fancy indexing. Write 8 small exercises of your own in the note
	- 20:00–21:00 [[Numpy]]: broadcasting drills: normalise rows, pairwise Euclidean distance matrix with no loops, one-hot encoding with `np.eye`, moving average with `cumsum`
	- 21:00–21:30 [[Numpy]]: numerically stable softmax and logsumexp, then the top-k with `argpartition`

### Fri 9 Oct 2026
Rest day.

### Sat 10 Oct 2026
- [ ] 11:00–13:00 · System design concepts: Networking essentials 📅 2026-10-10
	- 11:00–11:50 Read: https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction  (find the sections on networking essentials; also search for any key technology named below). Cover: TCP vs UDP; HTTP/1.1 vs HTTP/2 vs HTTP/3; WebSocket vs SSE vs long polling; DNS; L4 vs L7 load balancers; CDN
	- 11:50–12:20 Write your one-page summary in [[System Design Concepts]] (section 1) in your own words
	- 12:20–12:45 See it applied: skim how [[WhatsApp - Solution|WhatsApp]], [[FB Live Comments - Solution|FB Live Comments]], [[YouTube - Solution|YouTube]] use it, and note the decision each one made
	- 12:45–13:00 Answer the self-check questions in the note out loud
- [ ] 14:00–16:00 · System design: Bitly 📅 2026-10-10
	- 14:00–14:25 Read the Hello Interview delivery framework and core concepts: https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction
	- 14:25–14:30 Read only [[Bitly - Question|Bitly]]; write requirements and scale numbers
	- 14:30–15:10 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 15:10–15:40 Compare with [[Bitly - Solution|Bitly solution]] and its Excalidraw diagrams; list what you missed
	- 15:40–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Sun 11 Oct 2026
- [ ] 11:00–13:00 · AI fundamentals 📅 2026-10-11
	- 11:00–11:15 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (ML & DL foundations), then check them against the answers
	- 11:15–12:00 Answer out loud, before opening each answer: [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/01-ml-and-dl-foundations/questions|ML & DL foundations questions (Intermediate + Advanced)]]
	- 12:00–13:00 Read the [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/02-llm-fundamentals/README|LLM fundamentals crash course]]
- [ ] 14:00–16:00 · System design: Rate Limiter 📅 2026-10-11
	- 14:00–14:10 Read only [[Rate Limiter - Question|Rate Limiter]]; write requirements and scale numbers
	- 14:10–14:55 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 14:55–15:30 Compare with [[Rate Limiter - Solution|Rate Limiter solution]] and its Excalidraw diagrams; list what you missed
	- 15:30–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Mon 12 Oct 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-10-12
	- 🟡 [[Valid Sudoku]] (Arrays & Hashing) (30 min)
	- 🟡 [[Longest Consecutive Sequence]] (Arrays & Hashing) (30 min)
- [ ] 19:30–21:30 · Weekly review (spaced repetition) 📅 2026-10-12
	- 19:30–20:30 Spaced coding review: redo cold, 15 min each, no notes. Do these (swap in anything from your Fumbled list): [[Group Anagrams]] (this week); [[Design HashSet]] (this week); [[Majority Element]] (this week); [[Remove Element]] (this week)
	- 20:30–21:30 AI-75 quiz: ML & DL Foundations, then re-implement 3 NumPy functions from week 1 from memory (softmax, pairwise distances, one-hot)


---

## Week 2: Tue 13 Oct 2026 – Mon 19 Oct 2026

**Focus:** NumPy from scratch, LLM internals · Distributed Cache, News Feed · LeetCode: Arrays & Hashing, Two Pointers, Sliding Window

### Tue 13 Oct 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-10-13
	- 🟡 [[Best Time to Buy And Sell Stock II]] (Arrays & Hashing) (30 min)
	- 🟡 [[Majority Element II]] (Arrays & Hashing) (30 min)
- [ ] 19:30–21:30 · LeetCode: Arrays & Hashing, Two Pointers, Sliding Window (9 problems) 📅 2026-10-13
	- 19:30–19:40 🟢 [[Design HashMap]] (Arrays & Hashing) (10 min)
	- 19:40–19:50 🟢 [[Reverse String]] (Two Pointers) (10 min)
	- 19:50–20:00 🟢 [[Valid Palindrome]] (Two Pointers) (10 min)
	- 20:00–20:10 🟢 [[Valid Palindrome II]] (Two Pointers) (10 min)
	- 20:10–20:20 🟢 [[Merge Strings Alternately]] (Two Pointers) (10 min)
	- 20:20–20:30 🟢 [[Merge Sorted Array]] (Two Pointers) (10 min)
	- 20:30–20:40 🟢 [[Remove Duplicates From Sorted Array]] (Two Pointers) (10 min)
	- 20:40–20:50 🟢 [[Contains Duplicate II]] (Sliding Window) (10 min)
	- 20:50–21:00 🟢 [[Best Time to Buy And Sell Stock]] (Sliding Window) (10 min)
	- 21:00–21:30 Wrap-up and buffer: add anything you could not solve alone to the Fumbled list in [[STUDYPLAN]]; tick each problem in its section note

### Wed 14 Oct 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-10-14
	- 🟡 [[Subarray Sum Equals K]] (Arrays & Hashing) (30 min)
	- 🟡 [[Two Sum II Input Array Is Sorted]] (Two Pointers) (30 min)
- [ ] 19:30–21:30 · AI fundamentals 📅 2026-10-14
	- 19:30–19:45 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (ML & DL intermediate and LLM intro), then check them against the answers
	- 19:45–20:50 Answer out loud, before opening each answer: [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/02-llm-fundamentals/questions|LLM fundamentals questions (Basic)]]
	- 20:50–21:30 Implement from scratch, no peeking: `02_bpe_tokenizer.py` (see [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/12-coding-challenges/README|coding challenges]])

### Thu 15 Oct 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-10-15
	- 🟡 [[3Sum]] (Two Pointers) (30 min)
	- 🟡 [[4Sum]] (Two Pointers) (30 min)
- [ ] 19:30–21:30 · ML coding: NumPy from scratch 📅 2026-10-15
	- 19:30–20:00 [[Numpy]]: linear regression with the normal equation and with gradient descent, using only NumPy
	- 20:00–20:30 [[Numpy]]: logistic regression with gradient descent and a cross-entropy loss
	- 20:30–21:00 [[Numpy]]: k-means (vectorised assignment and update steps)
	- 21:00–21:30 [[Numpy]]: PCA via SVD and a cosine-similarity matrix

### Fri 16 Oct 2026
Rest day.

### Sat 17 Oct 2026
- [ ] 11:00–13:00 · System design concepts: API design 📅 2026-10-17
	- 11:00–11:50 Read: https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction  (find the sections on api design; also search for any key technology named below). Cover: REST vs gRPC vs GraphQL; pagination (cursor vs offset); idempotency keys; versioning; rate limiting
	- 11:50–12:20 Write your one-page summary in [[System Design Concepts]] (section 2) in your own words
	- 12:20–12:45 See it applied: skim how [[Rate Limiter - Solution|Rate Limiter]], [[Payment System - Solution|Payment System]], [[FB News Feed - Solution|FB News Feed]] use it, and note the decision each one made
	- 12:45–13:00 Answer the self-check questions in the note out loud
- [ ] 14:00–16:00 · System design: Distributed Cache 📅 2026-10-17
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[Bitly - Solution|Bitly]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:20 Read only [[Distributed Cache - Question|Distributed Cache]]; write requirements and scale numbers
	- 14:20–15:05 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 15:05–15:35 Compare with [[Distributed Cache - Solution|Distributed Cache solution]] and its Excalidraw diagrams; list what you missed
	- 15:35–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Sun 18 Oct 2026
- [ ] 11:00–13:00 · AI fundamentals 📅 2026-10-18
	- 11:00–11:15 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (LLM basics and tokenization), then check them against the answers
	- 11:15–12:20 Answer out loud, before opening each answer: [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/02-llm-fundamentals/questions|LLM fundamentals questions (Intermediate)]]
	- 12:20–13:00 Implement from scratch, no peeking: `04_positional_encodings.py` (see [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/12-coding-challenges/README|coding challenges]])
- [ ] 14:00–16:00 · System design: FB News Feed 📅 2026-10-18
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[Rate Limiter - Solution|Rate Limiter]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:20 Read only [[FB News Feed - Question|FB News Feed]]; write requirements and scale numbers
	- 14:20–15:05 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 15:05–15:35 Compare with [[FB News Feed - Solution|FB News Feed solution]] and its Excalidraw diagrams; list what you missed
	- 15:35–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Mon 19 Oct 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-10-19
	- 🟡 [[Rotate Array]] (Two Pointers) (30 min)
	- 🟡 [[Container With Most Water]] (Two Pointers) (30 min)
- [ ] 19:30–21:30 · Weekly review (spaced repetition) 📅 2026-10-19
	- 19:30–20:30 Spaced coding review: redo cold, 15 min each, no notes. Do these (swap in anything from your Fumbled list): [[Best Time to Buy And Sell Stock]] (this week); [[Group Anagrams]] (last week); [[Merge Strings Alternately]] (this week); [[Contains Duplicate II]] (this week)
	- 20:30–21:30 AI-75 quiz: LLM & Transformer Fundamentals, then 15 min of tokenization and attention questions out loud


---

## Week 3: Tue 20 Oct 2026 – Mon 26 Oct 2026

**Focus:** Pandas, LLM advanced · Tinder, Ticketmaster · LeetCode: Sliding Window, Stack, Binary Search

### Tue 20 Oct 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-10-20
	- 🟡 [[Boats to Save People]] (Two Pointers) (30 min)
	- 🟡 [[Longest Repeating Character Replacement]] (Sliding Window) (30 min)
- [ ] 19:30–21:30 · LeetCode: Sliding Window, Stack, Binary Search (7 problems) 📅 2026-10-20
	- 19:30–20:00 🟡 [[Longest Substring Without Repeating Characters]] (Sliding Window) (30 min)
	- 20:00–20:10 🟢 [[Baseball Game]] (Stack) (10 min)
	- 20:10–20:20 🟢 [[Valid Parentheses]] (Stack) (10 min)
	- 20:20–20:30 🟢 [[Implement Stack Using Queues]] (Stack) (10 min)
	- 20:30–20:40 🟢 [[Implement Queue using Stacks]] (Stack) (10 min)
	- 20:40–21:10 🟡 [[Min Stack]] (Stack) (30 min)
	- 21:10–21:20 🟢 [[Binary Search]] (Binary Search) (10 min)
	- 21:20–21:30 Wrap-up and buffer: add anything you could not solve alone to the Fumbled list in [[STUDYPLAN]]; tick each problem in its section note

### Wed 21 Oct 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-10-21
	- 🟡 [[Permutation In String]] (Sliding Window) (30 min)
	- 🟡 [[Minimum Size Subarray Sum]] (Sliding Window) (30 min)
- [ ] 19:30–21:30 · AI fundamentals 📅 2026-10-21
	- 19:30–19:45 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (LLM intermediate and positional encodings), then check them against the answers
	- 19:45–20:30 Answer out loud, before opening each answer: [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/02-llm-fundamentals/questions|LLM fundamentals questions (Advanced)]]
	- 20:30–21:00 Implement from scratch, no peeking: `05_layernorm_and_softmax.py` (see [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/12-coding-challenges/README|coding challenges]])
	- 21:00–21:30 Tick the LLM & Transformer Fundamentals section(s) of [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/AI-ENGINEER-75|AI Engineer 75]] (answer cold; re-read what you miss)

### Thu 22 Oct 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-10-22
	- 🟡 [[Find K Closest Elements]] (Sliding Window) (30 min)
	- 🟡 [[Evaluate Reverse Polish Notation]] (Stack) (30 min)
- [ ] 19:30–21:30 · ML coding: Pandas basics 📅 2026-10-22
	- 19:30–19:55 [[Pandas]]: load, inspect and clean a small synthetic CSV (dtypes, missing values, duplicates)
	- 19:55–20:30 [[Pandas]]: `groupby` with `agg` and `transform`, and `merge` with every join type
	- 20:30–21:00 [[Pandas]]: `pivot_table`, `melt`, `stack` and `unstack`
	- 21:00–21:30 [[Pandas]]: datetime handling, `resample` and `rolling`

### Fri 23 Oct 2026
Rest day.

### Sat 24 Oct 2026
- [ ] 11:00–13:00 · System design concepts: Data modeling 📅 2026-10-24
	- 11:00–11:50 Read: https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction  (find the sections on data modeling; also search for any key technology named below). Cover: Relational vs document vs wide-column vs key-value vs graph; designing the schema for the access pattern; denormalization
	- 11:50–12:20 Write your one-page summary in [[System Design Concepts]] (section 3) in your own words
	- 12:20–12:45 See it applied: skim how [[Dropbox - Solution|Dropbox]], [[Tinder - Solution|Tinder]], [[Ticketmaster - Solution|Ticketmaster]] use it, and note the decision each one made
	- 12:45–13:00 Answer the self-check questions in the note out loud
- [ ] 14:00–16:00 · System design: Tinder 📅 2026-10-24
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[Distributed Cache - Solution|Distributed Cache]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:20 Read only [[Tinder - Question|Tinder]]; write requirements and scale numbers
	- 14:20–15:05 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 15:05–15:35 Compare with [[Tinder - Solution|Tinder solution]] and its Excalidraw diagrams; list what you missed
	- 15:35–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Sun 25 Oct 2026
- [ ] 11:00–13:00 · AI fundamentals 📅 2026-10-25
	- 11:00–11:15 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (LLM advanced and layernorm), then check them against the answers
	- 11:15–11:55 Read the [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/03-prompt-engineering-and-context/README|Prompt & context engineering crash course]]
	- 11:55–13:00 Answer out loud, before opening each answer: [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/03-prompt-engineering-and-context/questions|Prompt & context engineering questions]]
- [ ] 14:00–16:00 · System design: Ticketmaster 📅 2026-10-25
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[FB News Feed - Solution|FB News Feed]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:20 Read only [[Ticketmaster - Question|Ticketmaster]]; write requirements and scale numbers
	- 14:20–15:05 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 15:05–15:35 Compare with [[Ticketmaster - Solution|Ticketmaster solution]] and its Excalidraw diagrams; list what you missed
	- 15:35–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Mon 26 Oct 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-10-26
	- 🟡 [[Asteroid Collision]] (Stack) (30 min)
	- 🟡 [[Daily Temperatures]] (Stack) (30 min)
- [ ] 19:30–21:30 · Weekly review (spaced repetition) 📅 2026-10-26
	- 19:30–20:30 Spaced coding review: redo cold, 15 min each, no notes. Do these (swap in anything from your Fumbled list): [[Min Stack]] (this week); [[Merge Strings Alternately]] (last week); [[Group Anagrams]] (2 weeks ago); [[Best Time to Buy And Sell Stock]] (last week)
	- 20:30–21:30 Pandas: redo 3 problems from the last Pandas session from memory, 15 min each, then the AI-75 Prompt section quiz


---

## Week 4: Tue 27 Oct 2026 – Mon 2 Nov 2026

**Focus:** Pandas interview problems, prompting and RAG · Online Auction, WhatsApp · LeetCode: Binary Search, Linked List

### Tue 27 Oct 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-10-27
	- 🟡 [[Online Stock Span]] (Stack) (30 min)
	- 🟡 [[Car Fleet]] (Stack) (30 min)
- [ ] 19:30–21:30 · LeetCode: Binary Search, Linked List (7 problems) 📅 2026-10-27
	- 19:30–19:40 🟢 [[Search Insert Position]] (Binary Search) (10 min)
	- 19:40–19:50 🟢 [[Guess Number Higher Or Lower]] (Binary Search) (10 min)
	- 19:50–20:00 🟢 [[Sqrt(x)]] (Binary Search) (10 min)
	- 20:00–20:30 🟡 [[Search a 2D Matrix]] (Binary Search) (30 min)
	- 20:30–20:40 🟢 [[Reverse Linked List]] (Linked List) (10 min)
	- 20:40–20:50 🟢 [[Merge Two Sorted Lists]] (Linked List) (10 min)
	- 20:50–21:00 🟢 [[Linked List Cycle]] (Linked List) (10 min)
	- 21:00–21:30 Wrap-up and buffer: add anything you could not solve alone to the Fumbled list in [[STUDYPLAN]]; tick each problem in its section note

### Wed 28 Oct 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-10-28
	- 🟡 [[Simplify Path]] (Stack) (30 min)
	- 🟡 [[Decode String]] (Stack) (30 min)
- [ ] 19:30–21:30 · AI fundamentals 📅 2026-10-28
	- 19:30–19:45 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (Prompt & context engineering), then check them against the answers
	- 19:45–20:05 Tick the Prompt & Context Engineering section(s) of [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/AI-ENGINEER-75|AI Engineer 75]] (answer cold; re-read what you miss)
	- 20:05–20:50 Read the [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/04-rag-and-retrieval/README|RAG & retrieval crash course]]
	- 20:50–21:30 Answer out loud, before opening each answer: [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/04-rag-and-retrieval/questions|RAG & retrieval questions (Basic)]]

### Thu 29 Oct 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-10-29
	- 🟡 [[Koko Eating Bananas]] (Binary Search) (30 min)
	- 🟡 [[Capacity to Ship Packages Within D Days]] (Binary Search) (30 min)
- [ ] 19:30–21:30 · ML coding: Pandas interview problems 📅 2026-10-29
	- 19:30–20:10 [[Pandas]] interview problems (synthetic data, 20 min each): top-N rows per group; running total and 7-day rolling average
	- 20:10–20:50 [[Pandas]]: keep the latest row per user (dedupe); find users with 3 consecutive active days
	- 20:50–21:30 [[Pandas]]: sessionisation with a 30-minute gap; cohort retention table

### Fri 30 Oct 2026
Rest day.

### Sat 31 Oct 2026
- [ ] 11:00–13:00 · System design concepts: Caching 📅 2026-10-31
	- 11:00–11:50 Read: https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction  (find the sections on caching; also search for any key technology named below). Cover: Cache-aside, write-through, write-back; eviction; invalidation; stampedes and hot keys; CDN caching
	- 11:50–12:20 Write your one-page summary in [[System Design Concepts]] (section 4) in your own words
	- 12:20–12:45 See it applied: skim how [[Distributed Cache - Solution|Distributed Cache]], [[Bitly - Solution|Bitly]], [[FB News Feed - Solution|FB News Feed]] use it, and note the decision each one made
	- 12:45–13:00 Answer the self-check questions in the note out loud
- [ ] 14:00–16:00 · System design: Online Auction 📅 2026-10-31
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[Tinder - Solution|Tinder]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:20 Read only [[Online Auction - Question|Online Auction]]; write requirements and scale numbers
	- 14:20–15:05 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 15:05–15:35 Compare with [[Online Auction - Solution|Online Auction solution]] and its Excalidraw diagrams; list what you missed
	- 15:35–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Sun 1 Nov 2026
- [ ] 11:00–13:00 · AI fundamentals 📅 2026-11-01
	- 11:00–11:15 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (prompting and RAG intro), then check them against the answers
	- 11:15–12:20 Answer out loud, before opening each answer: [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/04-rag-and-retrieval/questions|RAG & retrieval questions (Intermediate)]]
	- 12:20–13:00 Implement from scratch, no peeking: `09_text_chunking.py` (see [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/12-coding-challenges/README|coding challenges]])
- [ ] 14:00–16:00 · System design: WhatsApp 📅 2026-11-01
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[Ticketmaster - Solution|Ticketmaster]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:20 Read only [[WhatsApp - Question|WhatsApp]]; write requirements and scale numbers
	- 14:20–15:05 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 15:05–15:35 Compare with [[WhatsApp - Solution|WhatsApp solution]] and its Excalidraw diagrams; list what you missed
	- 15:35–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Mon 2 Nov 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-11-02
	- 🟡 [[Find Minimum In Rotated Sorted Array]] (Binary Search) (30 min)
	- 🟡 [[Search In Rotated Sorted Array]] (Binary Search) (30 min)
- [ ] 19:30–21:30 · Weekly review (spaced repetition) 📅 2026-11-02
	- 19:30–20:30 Spaced coding review: redo cold, 15 min each, no notes. Do these (swap in anything from your Fumbled list): [[Search a 2D Matrix]] (this week); [[Min Stack]] (last week); [[Best Time to Buy And Sell Stock]] (2 weeks ago); [[Group Anagrams]] (3 weeks ago)
	- 20:30–21:30 AI-75 quiz: Prompt & Context Engineering, then the RAG pipeline diagram from memory


---

## Week 5: Tue 3 Nov 2026 – Mon 9 Nov 2026

**Focus:** PyTorch basics, RAG · Notification System, Dropbox · LeetCode: Linked List, Trees

### Tue 3 Nov 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-11-03
	- 🟡 [[Search In Rotated Sorted Array II]] (Binary Search) (30 min)
	- 🟡 [[Time Based Key Value Store]] (Binary Search) (30 min)
- [ ] 19:30–21:30 · LeetCode: Linked List, Trees (7 problems) 📅 2026-11-03
	- 19:30–20:00 🟡 [[Reorder List]] (Linked List) (30 min)
	- 20:00–20:30 🟡 [[Remove Nth Node From End of List]] (Linked List) (30 min)
	- 20:30–20:40 🟢 [[Binary Tree Inorder Traversal]] (Trees) (10 min)
	- 20:40–20:50 🟢 [[Binary Tree Preorder Traversal]] (Trees) (10 min)
	- 20:50–21:00 🟢 [[Binary Tree Postorder Traversal]] (Trees) (10 min)
	- 21:00–21:10 🟢 [[Invert Binary Tree]] (Trees) (10 min)
	- 21:10–21:20 🟢 [[Maximum Depth of Binary Tree]] (Trees) (10 min)
	- 21:20–21:30 Wrap-up and buffer: add anything you could not solve alone to the Fumbled list in [[STUDYPLAN]]; tick each problem in its section note

### Wed 4 Nov 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-11-04
	- 🟡 [[Copy List With Random Pointer]] (Linked List) (30 min)
	- 🟡 [[Add Two Numbers]] (Linked List) (30 min)
- [ ] 19:30–21:30 · AI fundamentals 📅 2026-11-04
	- 19:30–19:45 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (RAG intermediate and chunking), then check them against the answers
	- 19:45–20:35 Answer out loud, before opening each answer: [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/04-rag-and-retrieval/questions|RAG & retrieval questions (Advanced)]]
	- 20:35–21:30 Implement from scratch, no peeking: `08_semantic_search_rag.py` (see [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/12-coding-challenges/README|coding challenges]])

### Thu 5 Nov 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-11-05
	- 🟡 [[Find The Duplicate Number]] (Linked List) (30 min)
	- 🟡 [[Reverse Linked List II]] (Linked List) (30 min)
- [ ] 19:30–21:30 · ML coding: PyTorch basics 📅 2026-11-05
	- 19:30–20:10 [[Pytorch]]: tensors, shapes, devices, broadcasting and autograd (compute a gradient by hand and check it with `.backward()`)
	- 20:10–20:50 [[Pytorch]]: write an `nn.Module` MLP and train it on a synthetic classification set
	- 20:50–21:30 [[Pytorch]]: write the training loop by hand: forward, loss, `zero_grad`, `backward`, `step`, plus an eval loop with `torch.no_grad()`

### Fri 6 Nov 2026
Rest day.

### Sat 7 Nov 2026
- [ ] 11:00–13:00 · System design concepts: Sharding and partitioning 📅 2026-11-07
	- 11:00–11:50 Read: https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction  (find the sections on sharding and partitioning; also search for any key technology named below). Cover: Range vs hash vs directory sharding; hot spots; resharding; cross-shard queries and joins
	- 11:50–12:20 Write your one-page summary in [[System Design Concepts]] (section 5) in your own words
	- 12:20–12:45 See it applied: skim how [[Distributed Cache - Solution|Distributed Cache]], [[Ad Click Aggregator - Solution|Ad Click Aggregator]], [[WhatsApp - Solution|WhatsApp]] use it, and note the decision each one made
	- 12:45–13:00 Answer the self-check questions in the note out loud
- [ ] 14:00–16:00 · System design: Notification System 📅 2026-11-07
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[Distributed Cache - Solution|Distributed Cache]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:20 Read only [[Notification System - Question|Notification System]]; write requirements and scale numbers
	- 14:20–15:05 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 15:05–15:35 Compare with [[Notification System - Solution|Notification System solution]] and its Excalidraw diagrams; list what you missed
	- 15:35–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Sun 8 Nov 2026
- [ ] 11:00–13:00 · AI fundamentals 📅 2026-11-08
	- 11:00–11:15 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (RAG advanced and the RAG pipeline), then check them against the answers
	- 11:15–12:00 Implement from scratch, no peeking: `17_hybrid_search_and_rerank.py` (see [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/12-coding-challenges/README|coding challenges]])
	- 12:00–12:30 Tick the RAG section(s) of [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/AI-ENGINEER-75|AI Engineer 75]] (answer cold; re-read what you miss)
	- 12:30–13:00 Draw the full production RAG pipeline from memory on an Excalidraw board (ingest, chunk, embed, index, retrieve, rerank, generate, cite, evaluate), then check it against the crash course
- [ ] 14:00–16:00 · System design: Dropbox 📅 2026-11-08
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[WhatsApp - Solution|WhatsApp]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:20 Read only [[Dropbox - Question|Dropbox]]; write requirements and scale numbers
	- 14:20–15:05 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 15:05–15:35 Compare with [[Dropbox - Solution|Dropbox solution]] and its Excalidraw diagrams; list what you missed
	- 15:35–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Mon 9 Nov 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-11-09
	- 🟡 [[Design Circular Queue]] (Linked List) (30 min)
	- 🟡 [[LRU Cache]] (Linked List) (30 min)
- [ ] 19:30–21:30 · Weekly review (spaced repetition) 📅 2026-11-09
	- 19:30–20:30 Spaced coding review: redo cold, 15 min each, no notes. Do these (swap in anything from your Fumbled list): [[Remove Nth Node From End of List]] (this week); [[Search a 2D Matrix]] (last week); [[Min Stack]] (2 weeks ago); [[Group Anagrams]] (4 weeks ago)
	- 20:30–21:30 AI-75 quiz: RAG, then 30 min redoing a NumPy/Pandas problem you flagged


---

## Week 6: Tue 10 Nov 2026 – Mon 16 Nov 2026

**Focus:** PyTorch training, RAG advanced and fine-tuning · YouTube, Uber · LeetCode: Trees, Heap - Priority Queue

### Tue 10 Nov 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-11-10
	- 🟡 [[Delete Node in a BST]] (Trees) (30 min)
	- 🟡 [[Binary Tree Level Order Traversal]] (Trees) (30 min)
- [ ] 19:30–21:30 · LeetCode: Trees, Heap - Priority Queue (7 problems) 📅 2026-11-10
	- 19:30–19:40 🟢 [[Diameter of Binary Tree]] (Trees) (10 min)
	- 19:40–19:50 🟢 [[Balanced Binary Tree]] (Trees) (10 min)
	- 19:50–20:00 🟢 [[Same Tree]] (Trees) (10 min)
	- 20:00–20:10 🟢 [[Subtree of Another Tree]] (Trees) (10 min)
	- 20:10–20:40 🟡 [[Lowest Common Ancestor of a Binary Search Tree]] (Trees) (30 min)
	- 20:40–21:10 🟡 [[Insert into a Binary Search Tree]] (Trees) (30 min)
	- 21:10–21:20 🟢 [[Kth Largest Element In a Stream]] (Heap - Priority Queue) (10 min)
	- 21:20–21:30 Wrap-up and buffer: add anything you could not solve alone to the Fumbled list in [[STUDYPLAN]]; tick each problem in its section note

### Wed 11 Nov 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-11-11
	- 🟡 [[Binary Tree Right Side View]] (Trees) (30 min)
	- 🟡 [[Construct Quad Tree]] (Trees) (30 min)
- [ ] 19:30–21:30 · AI fundamentals 📅 2026-11-11
	- 19:30–19:45 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (hybrid search and RAG review), then check them against the answers
	- 19:45–20:25 Read the [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/05-fine-tuning-and-alignment/README|Fine-tuning & alignment crash course]]
	- 20:25–21:30 Answer out loud, before opening each answer: [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/05-fine-tuning-and-alignment/questions|Fine-tuning & alignment questions (Basic + Intermediate)]]

### Thu 12 Nov 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-11-12
	- 🟡 [[Count Good Nodes In Binary Tree]] (Trees) (30 min)
	- 🟡 [[Validate Binary Search Tree]] (Trees) (30 min)
- [ ] 19:30–21:30 · ML coding: PyTorch training 📅 2026-11-12
	- 19:30–20:00 [[Pytorch]]: custom `Dataset` and `DataLoader`, a train/validation split and accuracy and loss tracking
	- 20:00–20:30 [[Pytorch]]: learning-rate scheduler, gradient clipping, checkpoint save and load
	- 20:30–21:00 [[Pytorch]]: debugging checklist: overfit one batch, check shapes, check for NaNs, check the loss at initialisation
	- 21:00–21:30 [[Pytorch]]: add early stopping and plot the loss curves

### Fri 13 Nov 2026
Rest day.

### Sat 14 Nov 2026
- [ ] 11:00–13:00 · System design concepts: Consistent hashing and replication 📅 2026-11-14
	- 11:00–11:50 Read: https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction  (find the sections on consistent hashing and replication; also search for any key technology named below). Cover: The hash ring, virtual nodes, replication factor, leader-follower, quorum reads and writes
	- 11:50–12:20 Write your one-page summary in [[System Design Concepts]] (section 6) in your own words
	- 12:20–12:45 See it applied: skim how [[Distributed Cache - Solution|Distributed Cache]], [[WhatsApp - Solution|WhatsApp]], [[Metrics Monitoring - Solution|Metrics Monitoring]] use it, and note the decision each one made
	- 12:45–13:00 Answer the self-check questions in the note out loud
- [ ] 14:00–16:00 · System design: YouTube 📅 2026-11-14
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[Notification System - Solution|Notification System]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:20 Read only [[YouTube - Question|YouTube]]; write requirements and scale numbers
	- 14:20–15:05 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 15:05–15:35 Compare with [[YouTube - Solution|YouTube solution]] and its Excalidraw diagrams; list what you missed
	- 15:35–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Sun 15 Nov 2026
- [ ] 11:00–13:00 · AI fundamentals 📅 2026-11-15
	- 11:00–11:15 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (Fine-tuning basics), then check them against the answers
	- 11:15–11:50 Answer out loud, before opening each answer: [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/05-fine-tuning-and-alignment/questions|Fine-tuning & alignment questions (Advanced)]]
	- 11:50–12:10 Tick the Fine-tuning, RLHF & Alignment section(s) of [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/AI-ENGINEER-75|AI Engineer 75]] (answer cold; re-read what you miss)
	- 12:10–13:00 Write a one-page comparison of prompting, RAG, LoRA, full fine-tuning, DPO and GRPO: when to use each, cost, risks
- [ ] 14:00–16:00 · System design: Uber 📅 2026-11-15
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[Ticketmaster - Solution|Ticketmaster]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:20 Read only [[Uber - Question|Uber]]; write requirements and scale numbers
	- 14:20–15:05 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 15:05–15:35 Compare with [[Uber - Solution|Uber solution]] and its Excalidraw diagrams; list what you missed
	- 15:35–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Mon 16 Nov 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-11-16
	- 🟡 [[Kth Smallest Element In a Bst]] (Trees) (30 min)
	- 🟡 [[Construct Binary Tree From Preorder And Inorder Traversal]] (Trees) (30 min)
- [ ] 19:30–21:30 · Weekly review (spaced repetition) 📅 2026-11-16
	- 19:30–20:30 Spaced coding review: redo cold, 15 min each, no notes. Do these (swap in anything from your Fumbled list): [[Insert into a Binary Search Tree]] (this week); [[Remove Nth Node From End of List]] (last week); [[Search a 2D Matrix]] (2 weeks ago); [[Merge Strings Alternately]] (4 weeks ago)
	- 20:30–21:30 PyTorch: type the training loop and scaled dot-product attention from memory, timed (30 min each)


---

## Week 7: Tue 17 Nov 2026 – Mon 23 Nov 2026

**Focus:** PyTorch attention, fine-tuning and agents · Yelp, Web Crawler · LeetCode: Heap - Priority Queue, Tries, Graphs

### Tue 17 Nov 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-11-17
	- 🟡 [[House Robber III]] (Trees) (30 min)
	- 🟡 [[Delete Leaves With a Given Value]] (Trees) (30 min)
- [ ] 19:30–21:30 · LeetCode: Heap - Priority Queue, Tries, Graphs (5 problems) 📅 2026-11-17
	- 19:30–19:40 🟢 [[Last Stone Weight]] (Heap - Priority Queue) (10 min)
	- 19:40–20:10 🟡 [[K Closest Points to Origin]] (Heap - Priority Queue) (30 min)
	- 20:10–20:40 🟡 [[Kth Largest Element In An Array]] (Heap - Priority Queue) (30 min)
	- 20:40–21:10 🟡 [[Implement Trie Prefix Tree]] (Tries) (30 min)
	- 21:10–21:20 🟢 [[Island Perimeter]] (Graphs) (10 min)
	- 21:20–21:30 Wrap-up and buffer: add anything you could not solve alone to the Fumbled list in [[STUDYPLAN]]; tick each problem in its section note

### Wed 18 Nov 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-11-18
	- 🟡 [[Task Scheduler]] (Heap - Priority Queue) (30 min)
	- 🟡 [[Design Twitter]] (Heap - Priority Queue) (30 min)
- [ ] 19:30–21:30 · AI fundamentals 📅 2026-11-18
	- 19:30–19:45 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (Fine-tuning advanced), then check them against the answers
	- 19:45–20:30 Read the [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/06-agents-and-tool-use/README|Agents & tool use crash course]]
	- 20:30–21:30 Answer out loud, before opening each answer: [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/06-agents-and-tool-use/questions|Agents & tool use questions (Basic)]]

### Thu 19 Nov 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-11-19
	- 🟡 [[Single Threaded CPU]] (Heap - Priority Queue) (30 min)
	- 🟡 [[Reorganize String]] (Heap - Priority Queue) (30 min)
- [ ] 19:30–21:30 · ML coding: PyTorch attention 📅 2026-11-19
	- 19:30–20:00 [[Pytorch]]: scaled dot-product attention from scratch (then compare with `ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/12-coding-challenges/01_attention.py` in the AI repo)
	- 20:00–20:40 [[Pytorch]]: multi-head attention with a reshape and a final projection
	- 20:40–21:30 [[Pytorch]]: causal mask, then a full transformer block (LayerNorm, residual connections, MLP)

### Fri 20 Nov 2026
Rest day.

### Sat 21 Nov 2026
- [ ] 11:00–13:00 · System design concepts: CAP, PACELC and transactions 📅 2026-11-21
	- 11:00–11:50 Read: https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction  (find the sections on cap, pacelc and transactions; also search for any key technology named below). Cover: Consistency models; isolation levels; two-phase commit vs saga; idempotent consumers; exactly-once myths
	- 11:50–12:20 Write your one-page summary in [[System Design Concepts]] (section 7) in your own words
	- 12:20–12:45 See it applied: skim how [[Payment System - Solution|Payment System]], [[Ticketmaster - Solution|Ticketmaster]], [[Online Auction - Solution|Online Auction]] use it, and note the decision each one made
	- 12:45–13:00 Answer the self-check questions in the note out loud
- [ ] 14:00–16:00 · System design: Yelp 📅 2026-11-21
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[YouTube - Solution|YouTube]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:20 Read only [[Yelp - Question|Yelp]]; write requirements and scale numbers
	- 14:20–15:05 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 15:05–15:35 Compare with [[Yelp - Solution|Yelp solution]] and its Excalidraw diagrams; list what you missed
	- 15:35–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Sun 22 Nov 2026
- [ ] 11:00–13:00 · AI fundamentals 📅 2026-11-22
	- 11:00–11:15 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (Agents basics), then check them against the answers
	- 11:15–12:00 Answer out loud, before opening each answer: [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/06-agents-and-tool-use/questions|Agents & tool use questions (Intermediate)]]
	- 12:00–13:00 Read the Claude API documentation on tool use, and re-read your tool descriptions from the agent project plan: what makes a tool description good or bad?
- [ ] 14:00–16:00 · System design: Web Crawler 📅 2026-11-22
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[Uber - Solution|Uber]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:20 Read only [[Web Crawler - Question|Web Crawler]]; write requirements and scale numbers
	- 14:20–15:05 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 15:05–15:35 Compare with [[Web Crawler - Solution|Web Crawler solution]] and its Excalidraw diagrams; list what you missed
	- 15:35–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Mon 23 Nov 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-11-23
	- 🟡 [[Longest Happy String]] (Heap - Priority Queue) (30 min)
	- 🟡 [[Car Pooling]] (Heap - Priority Queue) (30 min)
- [ ] 19:30–21:30 · Weekly review (spaced repetition) 📅 2026-11-23
	- 19:30–20:30 Spaced coding review: redo cold, 15 min each, no notes. Do these (swap in anything from your Fumbled list): [[Implement Trie Prefix Tree]] (this week); [[Insert into a Binary Search Tree]] (last week); [[Remove Nth Node From End of List]] (2 weeks ago); [[Min Stack]] (4 weeks ago)
	- 20:30–21:30 AI-75 quiz: Fine-tuning & Alignment, then list the LoRA maths from memory


---

## Week 8: Tue 24 Nov 2026 – Mon 30 Nov 2026

**Focus:** mini GPT, agents and evals · Job Scheduler, Ad Click Aggregator · LeetCode: Graphs

### Tue 24 Nov 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-11-24
	- 🟡 [[Design Add And Search Words Data Structure]] (Tries) (30 min)
	- 🟡 [[Extra Characters in a String]] (Tries) (30 min)
- [ ] 19:30–21:30 · LeetCode: Graphs (5 problems) 📅 2026-11-24
	- 19:30–19:40 🟢 [[Verifying An Alien Dictionary]] (Graphs) (10 min)
	- 19:40–19:50 🟢 [[Find the Town Judge]] (Graphs) (10 min)
	- 19:50–20:20 🟡 [[Number of Islands]] (Graphs) (30 min)
	- 20:20–20:50 🟡 [[Max Area of Island]] (Graphs) (30 min)
	- 20:50–21:20 🟡 [[Clone Graph]] (Graphs) (30 min)
	- 21:20–21:30 Wrap-up and buffer: add anything you could not solve alone to the Fumbled list in [[STUDYPLAN]]; tick each problem in its section note

### Wed 25 Nov 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-11-25
	- 🟡 [[Pacific Atlantic Water Flow]] (Graphs) (30 min)
	- 🟡 [[Surrounded Regions]] (Graphs) (30 min)
- [ ] 19:30–21:30 · AI fundamentals 📅 2026-11-25
	- 19:30–19:45 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (Agents intermediate and tool design), then check them against the answers
	- 19:45–20:30 Answer out loud, before opening each answer: [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/06-agents-and-tool-use/questions|Agents & tool use questions (Advanced)]]
	- 20:30–21:00 Tick the Agents section(s) of [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/AI-ENGINEER-75|AI Engineer 75]] (answer cold; re-read what you miss)
	- 21:00–21:30 Write a one-page note: workflow vs agent, manual loop vs tool runner vs the Claude Agent SDK, and when you would pick each

### Thu 26 Nov 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-11-26
	- 🟡 [[Open The Lock]] (Graphs) (30 min)
	- 🟡 [[Course Schedule]] (Graphs) (30 min)
- [ ] 19:30–21:30 · ML coding: mini GPT 📅 2026-11-26
	- 19:30–20:20 [[Pytorch]]: mini GPT: token and position embeddings, a stack of blocks, and the LM head (see `07_mini_gpt_forward.py` in the AI repo)
	- 20:20–21:00 [[Pytorch]]: train it on a tiny text for a few hundred steps and watch the loss
	- 21:00–21:30 [[Pytorch]]: sampling: greedy, temperature, top-k and top-p, written by hand (see `03_sampling.py`)

### Fri 27 Nov 2026
Rest day.

### Sat 28 Nov 2026
- [ ] 11:00–13:00 · System design concepts: Database indexing and Postgres 📅 2026-11-28
	- 11:00–11:50 Read: https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction  (find the sections on database indexing and postgres; also search for any key technology named below). Cover: B-tree vs LSM tree; composite and covering indexes; GIN; reading a query plan; connection pooling; replication
	- 11:50–12:20 Write your one-page summary in [[System Design Concepts]] (section 8) in your own words
	- 12:20–12:45 See it applied: skim how [[Yelp - Solution|Yelp]], [[Ticketmaster - Solution|Ticketmaster]], [[YouTube - Solution|YouTube]] use it, and note the decision each one made
	- 12:45–13:00 Answer the self-check questions in the note out loud
- [ ] 14:00–16:00 · System design: Job Scheduler 📅 2026-11-28
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[Notification System - Solution|Notification System]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:20 Read only [[Job Scheduler - Question|Job Scheduler]]; write requirements and scale numbers
	- 14:20–15:05 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 15:05–15:35 Compare with [[Job Scheduler - Solution|Job Scheduler solution]] and its Excalidraw diagrams; list what you missed
	- 15:35–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Sun 29 Nov 2026
- [ ] 11:00–13:00 · AI fundamentals 📅 2026-11-29
	- 11:00–11:15 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (Agents advanced), then check them against the answers
	- 11:15–11:55 Read the [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/07-evaluation-and-observability/README|Evaluation & observability crash course]]
	- 11:55–13:00 Answer out loud, before opening each answer: [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/07-evaluation-and-observability/questions|Evaluation & observability questions (Basic)]]
- [ ] 14:00–16:00 · System design: Ad Click Aggregator 📅 2026-11-29
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[Web Crawler - Solution|Web Crawler]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:20 Read only [[Ad Click Aggregator - Question|Ad Click Aggregator]]; write requirements and scale numbers
	- 14:20–15:05 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 15:05–15:35 Compare with [[Ad Click Aggregator - Solution|Ad Click Aggregator solution]] and its Excalidraw diagrams; list what you missed
	- 15:35–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Mon 30 Nov 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-11-30
	- 🟡 [[Course Schedule II]] (Graphs) (30 min)
	- 🟡 [[Graph Valid Tree]] (Graphs) (30 min)
- [ ] 19:30–21:30 · Weekly review (spaced repetition) 📅 2026-11-30
	- 19:30–20:30 Spaced coding review: redo cold, 15 min each, no notes. Do these (swap in anything from your Fumbled list): [[Clone Graph]] (this week); [[Kth Largest Element In An Array]] (last week); [[Insert into a Binary Search Tree]] (2 weeks ago); [[Search a 2D Matrix]] (4 weeks ago)
	- 20:30–21:30 AI-75 quiz: Agents, then re-read your tool descriptions and system prompt


---

## Week 9: Tue 1 Dec 2026 – Mon 7 Dec 2026

**Focus:** Agent project starts, evals · YouTube Top K, Payment System · LeetCode: Graphs, Backtracking

### Tue 1 Dec 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-12-01
	- 🟡 [[Course Schedule IV]] (Graphs) (30 min)
	- 🟡 [[Number of Connected Components In An Undirected Graph]] (Graphs) (30 min)
- [ ] 19:30–21:30 · LeetCode: Graphs, Backtracking (4 problems) 📅 2026-12-01
	- 19:30–20:00 🟡 [[Walls And Gates]] (Graphs) (30 min)
	- 20:00–20:30 🟡 [[Rotting Oranges]] (Graphs) (30 min)
	- 20:30–20:40 🟢 [[Sum of All Subsets XOR Total]] (Backtracking) (10 min)
	- 20:40–21:10 🟡 [[Subsets]] (Backtracking) (30 min)
	- 21:10–21:30 Wrap-up and buffer: add anything you could not solve alone to the Fumbled list in [[STUDYPLAN]]; tick each problem in its section note

### Wed 2 Dec 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-12-02
	- 🟡 [[Redundant Connection]] (Graphs) (30 min)
	- 🟡 [[Accounts Merge]] (Graphs) (30 min)
- [ ] 19:30–21:30 · AI fundamentals 📅 2026-12-02
	- 19:30–19:45 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (Evaluation basics), then check them against the answers
	- 19:45–20:30 Answer out loud, before opening each answer: [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/07-evaluation-and-observability/questions|Evaluation & observability questions (Intermediate + Advanced)]]
	- 20:30–21:30 Implement from scratch, no peeking: `12_eval_metrics.py` (see [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/12-coding-challenges/README|coding challenges]])

### Thu 3 Dec 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-12-03
	- 🟡 [[Evaluate Division]] (Graphs) (30 min)
	- 🟡 [[Minimum Height Trees]] (Graphs) (30 min)
- [ ] 19:30–21:30 · ML coding: agent project (design) 📅 2026-12-03
	- 19:30–21:30 Project: [[Build an Agent with the Claude SDK|Claude agent project]], milestone 1 (design and prompt, 45 min) and the start of milestone 2 (agent loop and tools). Tick the milestone boxes in the project note

### Fri 4 Dec 2026
Rest day.

### Sat 5 Dec 2026
- [ ] 11:00–13:00 · System design concepts: Redis 📅 2026-12-05
	- 11:00–11:50 Read: https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction  (find the sections on redis; also search for any key technology named below). Cover: Data structures; sorted sets; pub/sub; persistence (RDB/AOF); distributed locks and TTLs; clustering
	- 11:50–12:20 Write your one-page summary in [[System Design Concepts]] (section 9) in your own words
	- 12:20–12:45 See it applied: skim how [[Rate Limiter - Solution|Rate Limiter]], [[Ticketmaster - Solution|Ticketmaster]], [[Uber - Solution|Uber]] use it, and note the decision each one made
	- 12:45–13:00 Answer the self-check questions in the note out loud
- [ ] 14:00–16:00 · System design: YouTube Top K 📅 2026-12-05
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[Job Scheduler - Solution|Job Scheduler]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:20 Read only [[YouTube Top K - Question|YouTube Top K]]; write requirements and scale numbers
	- 14:20–15:05 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 15:05–15:35 Compare with [[YouTube Top K - Solution|YouTube Top K solution]] and its Excalidraw diagrams; list what you missed
	- 15:35–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Sun 6 Dec 2026
- [ ] 11:00–13:00 · AI fundamentals 📅 2026-12-06
	- 11:00–11:15 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (Evaluation advanced), then check them against the answers
	- 11:15–11:45 Tick the Evaluation & Observability section(s) of [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/AI-ENGINEER-75|AI Engineer 75]] (answer cold; re-read what you miss)
	- 11:45–12:15 Design the eval plan for your agent project: case categories, metrics, graders, and what you will do when the score drops
	- 12:15–13:00 LLM-as-judge: write down 5 failure modes (position bias, verbosity bias, self-preference and so on) and how you would mitigate each
- [ ] 14:00–16:00 · System design: Payment System 📅 2026-12-06
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[Uber - Solution|Uber]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:20 Read only [[Payment System - Question|Payment System]]; write requirements and scale numbers
	- 14:20–15:05 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 15:05–15:35 Compare with [[Payment System - Solution|Payment System solution]] and its Excalidraw diagrams; list what you missed
	- 15:35–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Mon 7 Dec 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-12-07
	- 🟡 [[Permutations]] (Backtracking) (30 min)
	- 🟡 [[Subsets II]] (Backtracking) (30 min)
- [ ] 19:30–21:30 · Weekly review (spaced repetition) 📅 2026-12-07
	- 19:30–20:30 Spaced coding review: redo cold, 15 min each, no notes. Do these (swap in anything from your Fumbled list): [[Subsets]] (this week); [[Max Area of Island]] (last week); [[Implement Trie Prefix Tree]] (2 weeks ago); [[Remove Nth Node From End of List]] (4 weeks ago)
	- 20:30–21:30 AI-75 quiz: Evaluation & Observability, then review your eval cases


---

## Week 10: Tue 8 Dec 2026 – Mon 14 Dec 2026

**Focus:** Agent loop and guardrails, inference · Metrics Monitoring, Google Docs · LeetCode: Backtracking

### Tue 8 Dec 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-12-08
	- 🟡 [[Permutations II]] (Backtracking) (30 min)
	- 🟡 [[Generate Parentheses]] (Backtracking) (30 min)
- [ ] 19:30–21:30 · LeetCode: Backtracking (3 problems) 📅 2026-12-08
	- 19:30–20:00 🟡 [[Combination Sum]] (Backtracking) (30 min)
	- 20:00–20:30 🟡 [[Combination Sum II]] (Backtracking) (30 min)
	- 20:30–21:00 🟡 [[Combinations]] (Backtracking) (30 min)
	- 21:00–21:30 Wrap-up and buffer: add anything you could not solve alone to the Fumbled list in [[STUDYPLAN]]; tick each problem in its section note

### Wed 9 Dec 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-12-09
	- 🟡 [[Word Search]] (Backtracking) (30 min)
	- 🟡 [[Palindrome Partitioning]] (Backtracking) (30 min)
- [ ] 19:30–21:30 · AI fundamentals 📅 2026-12-09
	- 19:30–19:45 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (Evaluation design for your agent), then check them against the answers
	- 19:45–20:30 Read the [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/08-inference-and-production/README|Inference & production crash course]]
	- 20:30–21:30 Answer out loud, before opening each answer: [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/08-inference-and-production/questions|Inference & production questions (Basic)]]

### Thu 10 Dec 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-12-10
	- 🟡 [[Letter Combinations of a Phone Number]] (Backtracking) (30 min)
	- 🟡 [[Matchsticks to Square]] (Backtracking) (30 min)
- [ ] 19:30–21:30 · ML coding: agent project (loop and guardrails) 📅 2026-12-10
	- 19:30–21:30 Project: [[Build an Agent with the Claude SDK|Claude agent project]], finish milestone 2 (manual loop, then the tool runner version) and milestone 3 (guardrails and safety). Tick the milestone boxes in the project note

### Fri 11 Dec 2026
Rest day.

### Sat 12 Dec 2026
- [ ] 11:00–13:00 · System design concepts: Kafka and message queues 📅 2026-12-12
	- 11:00–11:50 Read: https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction  (find the sections on kafka and message queues; also search for any key technology named below). Cover: Topics, partitions, consumer groups; ordering; delivery semantics; retries and dead-letter queues; Kafka vs SQS
	- 11:50–12:20 Write your one-page summary in [[System Design Concepts]] (section 10) in your own words
	- 12:20–12:45 See it applied: skim how [[Ad Click Aggregator - Solution|Ad Click Aggregator]], [[Notification System - Solution|Notification System]], [[Job Scheduler - Solution|Job Scheduler]] use it, and note the decision each one made
	- 12:45–13:00 Answer the self-check questions in the note out loud
- [ ] 14:00–16:00 · System design: Metrics Monitoring 📅 2026-12-12
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[YouTube Top K - Solution|YouTube Top K]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:20 Read only [[Metrics Monitoring - Question|Metrics Monitoring]]; write requirements and scale numbers
	- 14:20–15:05 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 15:05–15:35 Compare with [[Metrics Monitoring - Solution|Metrics Monitoring solution]] and its Excalidraw diagrams; list what you missed
	- 15:35–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Sun 13 Dec 2026
- [ ] 11:00–13:00 · AI fundamentals 📅 2026-12-13
	- 11:00–11:15 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (Inference basics), then check them against the answers
	- 11:15–12:00 Answer out loud, before opening each answer: [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/08-inference-and-production/questions|Inference & production questions (Intermediate + Advanced)]]
	- 12:00–13:00 Implement from scratch, no peeking: `06_kv_cache.py` (see [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/12-coding-challenges/README|coding challenges]])
- [ ] 14:00–16:00 · System design: Google Docs 📅 2026-12-13
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[Payment System - Solution|Payment System]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:20 Read only [[Google Docs - Question|Google Docs]]; write requirements and scale numbers
	- 14:20–15:05 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 15:05–15:35 Compare with [[Google Docs - Solution|Google Docs solution]] and its Excalidraw diagrams; list what you missed
	- 15:35–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Mon 14 Dec 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-12-14
	- 🟡 [[Partition to K Equal Sum Subsets]] (Backtracking) (30 min)
	- 🟡 [[Network Delay Time]] (Advanced Graphs) (30 min)
- [ ] 19:30–21:30 · Weekly review (spaced repetition) 📅 2026-12-14
	- 19:30–20:30 Spaced coding review: redo cold, 15 min each, no notes. Do these (swap in anything from your Fumbled list): [[Combinations]] (this week); [[Rotting Oranges]] (last week); [[Clone Graph]] (2 weeks ago); [[Insert into a Binary Search Tree]] (4 weeks ago)
	- 20:30–21:30 AI-75 quiz: Inference & Production, then write the KV cache size formula and a worked example


---

## Week 11: Tue 15 Dec 2026 – Mon 21 Dec 2026

**Focus:** Agent evals, inference and safety · FB Live Comments, ChatGPT · LeetCode: Advanced Graphs, 1-D Dynamic Programming

### Tue 15 Dec 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-12-15
	- 🟡 [[Min Cost to Connect All Points]] (Advanced Graphs) (30 min)
	- 🟡 [[Cheapest Flights Within K Stops]] (Advanced Graphs) (30 min)
- [ ] 19:30–21:30 · LeetCode: Advanced Graphs, 1-D Dynamic Programming (5 problems) 📅 2026-12-15
	- 19:30–20:00 🟡 [[Path with Minimum Effort]] (Advanced Graphs) (30 min)
	- 20:00–20:10 🟢 [[Climbing Stairs]] (1-D Dynamic Programming) (10 min)
	- 20:10–20:20 🟢 [[Min Cost Climbing Stairs]] (1-D Dynamic Programming) (10 min)
	- 20:20–20:30 🟢 [[N-th Tribonacci Number]] (1-D Dynamic Programming) (10 min)
	- 20:30–21:00 🟡 [[House Robber]] (1-D Dynamic Programming) (30 min)
	- 21:00–21:30 Wrap-up and buffer: add anything you could not solve alone to the Fumbled list in [[STUDYPLAN]]; tick each problem in its section note

### Wed 16 Dec 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-12-16
	- 🟡 [[Palindromic Substrings]] (1-D Dynamic Programming) (30 min)
	- 🟡 [[Decode Ways]] (1-D Dynamic Programming) (30 min)
- [ ] 19:30–21:30 · AI fundamentals 📅 2026-12-16
	- 19:30–19:45 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (Inference advanced and KV cache), then check them against the answers
	- 19:45–20:10 Implement from scratch, no peeking: `16_semantic_cache.py` (see [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/12-coding-challenges/README|coding challenges]])
	- 20:10–20:50 Implement from scratch, no peeking: `11_rate_limiter_and_retry.py` (see [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/12-coding-challenges/README|coding challenges]])
	- 20:50–21:30 Tick the Inference & Production section(s) of [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/AI-ENGINEER-75|AI Engineer 75]] (answer cold; re-read what you miss)

### Thu 17 Dec 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-12-17
	- 🟡 [[Coin Change]] (1-D Dynamic Programming) (30 min)
	- 🟡 [[Maximum Product Subarray]] (1-D Dynamic Programming) (30 min)
- [ ] 19:30–21:30 · ML coding: agent project (evals) 📅 2026-12-17
	- 19:30–21:30 Project: [[Build an Agent with the Claude SDK|Claude agent project]], milestone 4: the 20-case eval harness, baseline score, and one prompt change measured against it. Tick the milestone boxes in the project note

### Fri 18 Dec 2026
Rest day.

### Sat 19 Dec 2026
- [ ] 11:00–13:00 · System design concepts: Elasticsearch and search 📅 2026-12-19
	- 11:00–11:50 Read: https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction  (find the sections on elasticsearch and search; also search for any key technology named below). Cover: Inverted index; shards and replicas; analyzers; relevance scoring; keeping the index in sync (CDC)
	- 11:50–12:20 Write your one-page summary in [[System Design Concepts]] (section 11) in your own words
	- 12:20–12:45 See it applied: skim how [[Ticketmaster - Solution|Ticketmaster]], [[FB Post Search - Solution|FB Post Search]], [[Yelp - Solution|Yelp]] use it, and note the decision each one made
	- 12:45–13:00 Answer the self-check questions in the note out loud
- [ ] 14:00–16:00 · System design: FB Live Comments 📅 2026-12-19
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[Job Scheduler - Solution|Job Scheduler]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:20 Read only [[FB Live Comments - Question|FB Live Comments]]; write requirements and scale numbers
	- 14:20–15:05 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 15:05–15:35 Compare with [[FB Live Comments - Solution|FB Live Comments solution]] and its Excalidraw diagrams; list what you missed
	- 15:35–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Sun 20 Dec 2026
- [ ] 11:00–13:00 · AI fundamentals 📅 2026-12-20
	- 11:00–11:15 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (Inference caching and rate limiting), then check them against the answers
	- 11:15–11:55 Read the [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/09-safety-security-and-responsible-ai/README|Safety & security crash course]]
	- 11:55–13:00 Answer out loud, before opening each answer: [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/09-safety-security-and-responsible-ai/questions|Safety & security questions]]
- [ ] 14:00–16:00 · System design: ChatGPT 📅 2026-12-20
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[Google Docs - Solution|Google Docs]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:20 Read only [[ChatGPT - Question|ChatGPT]]; write requirements and scale numbers
	- 14:20–15:05 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 15:05–15:35 Compare with [[ChatGPT - Solution|ChatGPT solution]] and its Excalidraw diagrams; list what you missed
	- 15:35–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Mon 21 Dec 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-12-21
	- 🟡 [[Word Break]] (1-D Dynamic Programming) (30 min)
	- 🟡 [[Longest Increasing Subsequence]] (1-D Dynamic Programming) (30 min)
- [ ] 19:30–21:30 · Weekly review (spaced repetition) 📅 2026-12-21
	- 19:30–20:30 Spaced coding review: redo cold, 15 min each, no notes. Do these (swap in anything from your Fumbled list): [[House Robber]] (this week); [[Combination Sum II]] (last week); [[Subsets]] (2 weeks ago); [[Kth Largest Element In An Array]] (4 weeks ago)
	- 20:30–21:30 AI-75 quiz: Safety & Security, then re-read your threat model


---

## Week 12: Tue 22 Dec 2026 – Mon 28 Dec 2026

**Focus:** Agent polish and streaming, safety and multimodal · Instagram, LeetCode · LeetCode: 1-D Dynamic Programming, 2-D Dynamic Programming

### Tue 22 Dec 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-12-22
	- 🟡 [[Partition Equal Subset Sum]] (1-D Dynamic Programming) (30 min)
	- 🟡 [[Combination Sum IV]] (1-D Dynamic Programming) (30 min)
- [ ] 19:30–21:30 · LeetCode: 1-D Dynamic Programming, 2-D Dynamic Programming (3 problems) 📅 2026-12-22
	- 19:30–20:00 🟡 [[House Robber II]] (1-D Dynamic Programming) (30 min)
	- 20:00–20:30 🟡 [[Longest Palindromic Substring]] (1-D Dynamic Programming) (30 min)
	- 20:30–21:00 🟡 [[Unique Paths]] (2-D Dynamic Programming) (30 min)
	- 21:00–21:30 Wrap-up and buffer: add anything you could not solve alone to the Fumbled list in [[STUDYPLAN]]; tick each problem in its section note

### Wed 23 Dec 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-12-23
	- 🟡 [[Perfect Squares]] (1-D Dynamic Programming) (30 min)
	- 🟡 [[Integer Break]] (1-D Dynamic Programming) (30 min)
- [ ] 19:30–21:30 · AI fundamentals 📅 2026-12-23
	- 19:30–19:45 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (Safety), then check them against the answers
	- 19:45–20:15 Tick the Safety & Security section(s) of [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/AI-ENGINEER-75|AI Engineer 75]] (answer cold; re-read what you miss)
	- 20:15–20:50 Write a threat model for your agent project: assets, attackers, prompt-injection paths, tool abuse, data leaks, and the control for each
	- 20:50–21:30 Implement from scratch, no peeking: `18_constrained_json_decoding.py` (see [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/12-coding-challenges/README|coding challenges]])

### Thu 24 Dec 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-12-24
	- 🟡 [[Longest Common Subsequence]] (2-D Dynamic Programming) (30 min)
	- 🟡 [[Last Stone Weight II]] (2-D Dynamic Programming) (30 min)
- [ ] 19:30–21:30 · ML coding: agent project (polish and streaming) 📅 2026-12-24
	- 19:30–20:15 Project: [[Build an Agent with the Claude SDK|Claude agent project]], milestone 5 (README, architecture diagram, design decisions, 3-minute walk-through). Tick the milestone boxes in the project note
	- 20:15–21:30 Stretch goal: stream the response and show tool calls live; add conversation memory and one multi-turn eval case

### Fri 25 Dec 2026
Rest day.

### Sat 26 Dec 2026
- [ ] 11:00–13:00 · System design concepts: DynamoDB and Cassandra 📅 2026-12-26
	- 11:00–11:50 Read: https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction  (find the sections on dynamodb and cassandra; also search for any key technology named below). Cover: Partition and sort keys; hot partitions; tunable consistency; last-write-wins; single-table design
	- 11:50–12:20 Write your one-page summary in [[System Design Concepts]] (section 12) in your own words
	- 12:20–12:45 See it applied: skim how [[Bitly - Solution|Bitly]], [[Tinder - Solution|Tinder]], [[YouTube - Solution|YouTube]] use it, and note the decision each one made
	- 12:45–13:00 Answer the self-check questions in the note out loud
- [ ] 14:00–16:00 · System design: Instagram 📅 2026-12-26
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[FB Live Comments - Solution|FB Live Comments]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:20 Read only [[Instagram - Question|Instagram]]; write requirements and scale numbers
	- 14:20–15:05 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 15:05–15:35 Compare with [[Instagram - Solution|Instagram solution]] and its Excalidraw diagrams; list what you missed
	- 15:35–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Sun 27 Dec 2026
- [ ] 11:00–13:00 · AI fundamentals 📅 2026-12-27
	- 11:00–11:15 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (Safety threat model), then check them against the answers
	- 11:15–11:40 Read the [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/10-multimodal/README|Multimodal crash course]]
	- 11:40–12:20 Answer out loud, before opening each answer: [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/10-multimodal/questions|Multimodal questions]]
	- 12:20–13:00 Implement from scratch, no peeking: `19_speculative_decoding.py` (see [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/12-coding-challenges/README|coding challenges]])
- [ ] 14:00–16:00 · System design: LeetCode 📅 2026-12-27
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[Payment System - Solution|Payment System]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:20 Read only [[LeetCode - Question|LeetCode]]; write requirements and scale numbers
	- 14:20–15:05 Design it out loud on a blank Excalidraw board: entities, API, high-level design, deep dives
	- 15:05–15:35 Compare with [[LeetCode - Solution|LeetCode solution]] and its Excalidraw diagrams; list what you missed
	- 15:35–16:00 Redraw the high-level design from memory and write 3 takeaways in the Fumbled list

### Mon 28 Dec 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-12-28
	- 🟡 [[Best Time to Buy And Sell Stock With Cooldown]] (2-D Dynamic Programming) (30 min)
	- 🟡 [[Coin Change II]] (2-D Dynamic Programming) (30 min)
- [ ] 19:30–21:30 · Weekly review (spaced repetition) 📅 2026-12-28
	- 19:30–20:30 Spaced coding review: redo cold, 15 min each, no notes. Do these (swap in anything from your Fumbled list): [[Unique Paths]] (this week); [[House Robber]] (last week); [[Combinations]] (2 weeks ago); [[Max Area of Island]] (4 weeks ago)
	- 20:30–21:30 System design recall: redraw three designs from weeks 1-4 cold (10 min each) and list 3 deep dives per design, then the AI-75 quiz on weak sections


---

## Week 13: Tue 29 Dec 2026 – Mon 4 Jan 2027

**Focus:** Agent stretch goals, AI case studies · ML system design · LeetCode: 2-D Dynamic Programming, Greedy

### Tue 29 Dec 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-12-29
	- 🟡 [[Target Sum]] (2-D Dynamic Programming) (30 min)
	- 🟡 [[Interleaving String]] (2-D Dynamic Programming) (30 min)
- [ ] 19:30–21:30 · LeetCode: 2-D Dynamic Programming, Greedy (4 problems) 📅 2026-12-29
	- 19:30–20:00 🟡 [[Unique Paths II]] (2-D Dynamic Programming) (30 min)
	- 20:00–20:30 🟡 [[Minimum Path Sum]] (2-D Dynamic Programming) (30 min)
	- 20:30–20:40 🟢 [[Lemonade Change]] (Greedy) (10 min)
	- 20:40–21:10 🟡 [[Maximum Subarray]] (Greedy) (30 min)
	- 21:10–21:30 Wrap-up and buffer: add anything you could not solve alone to the Fumbled list in [[STUDYPLAN]]; tick each problem in its section note

### Wed 30 Dec 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-12-30
	- 🟡 [[Stone Game]] (2-D Dynamic Programming) (30 min)
	- 🟡 [[Stone Game II]] (2-D Dynamic Programming) (30 min)
- [ ] 19:30–21:30 · AI fundamentals 📅 2026-12-30
	- 19:30–19:45 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (Multimodal and speculative decoding), then check them against the answers
	- 19:45–20:15 Read the [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/11-ai-system-design/README|AI system design crash course]]
	- 20:15–21:30 Timed case study mock, 45 min design + 45 min compare: [[01-enterprise-rag-assistant|Enterprise RAG assistant]]: design out loud on a blank board, then compare

### Thu 31 Dec 2026
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2026-12-31
	- 🟡 [[Edit Distance]] (2-D Dynamic Programming) (30 min)
	- 🟡 [[Longest Turbulent Subarray]] (Greedy) (30 min)
- [ ] 19:30–21:30 · ML coding: agent project (MCP and batch evals) 📅 2026-12-31
	- 19:30–20:30 Stretch goal: put the order data behind an MCP server and connect the agent to it with the SDK's MCP helpers
	- 20:30–21:30 Stretch goal: run the eval cases asynchronously, then try the Message Batches API and compare cost and time

### Fri 1 Jan 2027
Rest day.

### Sat 2 Jan 2027
- [ ] 11:00–13:00 · System design concepts: Stream processing and durable execution 📅 2027-01-02
	- 11:00–11:50 Read: https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction  (find the sections on stream processing and durable execution; also search for any key technology named below). Cover: Flink windows, watermarks, checkpoints and state; Temporal workflows and sagas
	- 11:50–12:20 Write your one-page summary in [[System Design Concepts]] (section 13) in your own words
	- 12:20–12:45 See it applied: skim how [[YouTube Top K - Solution|YouTube Top K]], [[Ad Click Aggregator - Solution|Ad Click Aggregator]], [[Job Scheduler - Solution|Job Scheduler]] use it, and note the decision each one made
	- 12:45–13:00 Answer the self-check questions in the note out loud
- [ ] 14:00–16:00 · System design: ML: framework and a recommendation system 📅 2027-01-02
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[Instagram - Solution|Instagram]] and name its 3 hardest deep dives, then check against its diagram
	- 14:10–14:50 Read the ML system design framework: https://www.hellointerview.com/learn/ml-system-design/in-a-hurry/introduction
	- 14:50–15:10 Write the framework in your own words in [[ML System Design]]: problem framing, data and labels, features, model, training, offline and online evaluation, serving, monitoring
	- 15:10–15:55 Design a recommendation system for a video app end to end, out loud on a blank board
	- 15:55–16:00 Write up your design in [[ML System Design]] and list what you would improve

### Sun 3 Jan 2027
- [ ] 11:00–13:00 · AI fundamentals 📅 2027-01-03
	- 11:00–11:15 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (AI system design (enterprise RAG)), then check them against the answers
	- 11:15–12:00 Timed case study mock, 60 min: [[03-customer-support-agent|Customer support agent]]: design out loud on a blank board, then compare
	- 12:00–13:00 Timed case study mock, 60 min: [[07-text-to-sql-agent|Text-to-SQL agent]]: design out loud on a blank board, then compare
- [ ] 14:00–16:00 · System design: ML: video recommendations (candidate generation, ranking, cold start) 📅 2027-01-03
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[LeetCode - Solution|LeetCode]] and name its 3 hardest deep dives, then check against its diagram
	- 14:10–14:25 Frame the problem: product goal, metric, constraints; list the data and labels you would use
	- 14:25–15:25 Design out loud on a blank board: video recommendations (candidate generation, ranking, cold start): features, model choices, training setup, offline metrics, online experiment, serving architecture, monitoring and feedback loop
	- 15:25–15:55 Write the design up in [[ML System Design]], and check your offline and online metrics and failure modes against the framework
	- 15:55–16:00 Redraw the architecture from memory and write 3 takeaways in the Fumbled list

### Mon 4 Jan 2027
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2027-01-04
	- 🟡 [[Jump Game]] (Greedy) (30 min)
	- 🟡 [[Jump Game II]] (Greedy) (30 min)
- [ ] 19:30–21:30 · Weekly review (spaced repetition) 📅 2027-01-04
	- 19:30–20:30 Spaced coding review: redo cold, 15 min each, no notes. Do these (swap in anything from your Fumbled list): [[Maximum Subarray]] (this week); [[Longest Palindromic Substring]] (last week); [[House Robber]] (2 weeks ago); [[Rotting Oranges]] (4 weeks ago)
	- 20:30–21:30 System design recall: redraw three designs from weeks 5-8 cold (10 min each), then the AI-75 quiz on weak sections


---

## Week 14: Tue 5 Jan 2027 – Mon 11 Jan 2027

**Focus:** Agent SDK comparison, AI case studies · ML system design · LeetCode: Greedy, Intervals, Math & Geometry, Bit Manipulation

### Tue 5 Jan 2027
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2027-01-05
	- 🟡 [[Jump Game VII]] (Greedy) (30 min)
	- 🟡 [[Gas Station]] (Greedy) (30 min)
- [ ] 19:30–21:30 · LeetCode: Greedy, Intervals, Math & Geometry, Bit Manipulation (5 problems) 📅 2027-01-05
	- 19:30–20:00 🟡 [[Maximum Sum Circular Subarray]] (Greedy) (30 min)
	- 20:00–20:30 🟡 [[Insert Interval]] (Intervals) (30 min)
	- 20:30–20:40 🟢 [[Excel Sheet Column Title]] (Math & Geometry) (10 min)
	- 20:40–20:50 🟢 [[Greatest Common Divisor of Strings]] (Math & Geometry) (10 min)
	- 20:50–21:00 🟢 [[Single Number]] (Bit Manipulation) (10 min)
	- 21:00–21:30 Wrap-up and buffer: add anything you could not solve alone to the Fumbled list in [[STUDYPLAN]]; tick each problem in its section note

### Wed 6 Jan 2027
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2027-01-06
	- 🟡 [[Hand of Straights]] (Greedy) (30 min)
	- 🟡 [[Dota2 Senate]] (Greedy) (30 min)
- [ ] 19:30–21:30 · AI fundamentals 📅 2027-01-06
	- 19:30–19:45 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (AI case studies (support agent, text-to-SQL)), then check them against the answers
	- 19:45–20:30 Timed case study mock, 60 min: [[10-llm-gateway-and-serving-platform|LLM gateway & serving]]: design out loud on a blank board, then compare
	- 20:30–21:30 Timed case study mock, 60 min: [[02-ai-code-assistant|AI code assistant]]: design out loud on a blank board, then compare

### Thu 7 Jan 2027
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2027-01-07
	- 🟡 [[Merge Triplets to Form Target Triplet]] (Greedy) (30 min)
	- 🟡 [[Partition Labels]] (Greedy) (30 min)
- [ ] 19:30–21:30 · ML coding: agent project (Agent SDK and reviewer agent) 📅 2027-01-07
	- 19:30–20:30 Stretch goal: rebuild the same task with the Claude Agent SDK and write down what each approach gives you
	- 20:30–21:30 Stretch goal: add a reviewer agent that checks refund decisions, and write down when multi-agent is worth it

### Fri 8 Jan 2027
Rest day.

### Sat 9 Jan 2027
- [ ] 11:00–13:00 · System design concepts: Geospatial search and time-series databases 📅 2027-01-09
	- 11:00–11:50 Read: https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction  (find the sections on geospatial search and time-series databases; also search for any key technology named below). Cover: Geohash, quadtree, S2; proximity queries; time-series storage, downsampling, retention
	- 11:50–12:20 Write your one-page summary in [[System Design Concepts]] (section 14) in your own words
	- 12:20–12:45 See it applied: skim how [[Uber - Solution|Uber]], [[Yelp - Solution|Yelp]], [[Metrics Monitoring - Solution|Metrics Monitoring]] use it, and note the decision each one made
	- 12:45–13:00 Answer the self-check questions in the note out loud
- [ ] 14:00–16:00 · System design: ML: search ranking 📅 2027-01-09
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[FB Live Comments - Solution|FB Live Comments]] and name its 3 hardest deep dives, then check against its diagram
	- 14:10–14:25 Frame the problem: product goal, metric, constraints; list the data and labels you would use
	- 14:25–15:25 Design out loud on a blank board: search ranking: features, model choices, training setup, offline metrics, online experiment, serving architecture, monitoring and feedback loop
	- 15:25–15:55 Write the design up in [[ML System Design]], and check your offline and online metrics and failure modes against the framework
	- 15:55–16:00 Redraw the architecture from memory and write 3 takeaways in the Fumbled list

### Sun 10 Jan 2027
- [ ] 11:00–13:00 · AI fundamentals 📅 2027-01-10
	- 11:00–11:15 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (AI case studies (LLM gateway, code assistant)), then check them against the answers
	- 11:15–12:00 AI-assisted interview: read [[AI Assisted Interview]] and watch the video
	- 12:00–13:00 Practice session with the Hello Interview AI coding tutorial: https://www.hellointerview.com/learn/ai-coding/overview/introduction
- [ ] 14:00–16:00 · System design: ML: harmful content or fraud detection 📅 2027-01-10
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[LeetCode - Solution|LeetCode]] and name its 3 hardest deep dives, then check against its diagram
	- 14:10–14:25 Frame the problem: product goal, metric, constraints; list the data and labels you would use
	- 14:25–15:25 Design out loud on a blank board: harmful content or fraud detection: features, model choices, training setup, offline metrics, online experiment, serving architecture, monitoring and feedback loop
	- 15:25–15:55 Write the design up in [[ML System Design]], and check your offline and online metrics and failure modes against the framework
	- 15:55–16:00 Redraw the architecture from memory and write 3 takeaways in the Fumbled list

### Mon 11 Jan 2027
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2027-01-11
	- 🟡 [[Valid Parenthesis String]] (Greedy) (30 min)
	- 🟡 [[Merge Intervals]] (Intervals) (30 min)
- [ ] 19:30–21:30 · Weekly review (spaced repetition) 📅 2027-01-11
	- 19:30–20:30 Spaced coding review: redo cold, 15 min each, no notes. Do these (swap in anything from your Fumbled list): [[Insert Interval]] (this week); [[Minimum Path Sum]] (last week); [[Unique Paths]] (2 weeks ago); [[Combination Sum II]] (4 weeks ago)
	- 20:30–21:30 ML coding: write multi-head attention and a training loop from memory (30 min), then a Pandas window-function problem (30 min)


---

## Week 15: Tue 12 Jan 2027 – Mon 18 Jan 2027

**Focus:** LoRA and beam search, behavioral and company research · general design mocks · LeetCode: timed coding rounds

### Tue 12 Jan 2027
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 40 min in total, any time that suits you) 📅 2027-01-12
	- 🟡 [[Non Overlapping Intervals]] (Intervals) (30 min)
	- 🟢 [[Meeting Rooms]] (Intervals) (10 min)
- [ ] 19:30–21:30 · LeetCode: timed practice round (1 easy + 3 medium, interview conditions) 📅 2027-01-12
	- 19:30–19:40 🟢 [[Merge Strings Alternately]] (Two Pointers): 10 min, then stop and write down your approach and complexity
	- 19:40–20:10 🟡 [[Min Stack]] (Stack): 30 min, then stop and write down your approach and complexity
	- 20:10–20:40 🟡 [[Max Area of Island]] (Graphs): 30 min, then stop and write down your approach and complexity
	- 20:40–21:10 🟡 [[House Robber II]] (1-D Dynamic Programming): 30 min, then stop and write down your approach and complexity
	- 21:10–21:30 Review: read each Solution, note what you missed, add failures to the Fumbled list

### Wed 13 Jan 2027
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2027-01-13
	- 🟡 [[Meeting Rooms II]] (Intervals) (30 min)
	- 🟡 [[Insert Greatest Common Divisors in Linked List]] (Math & Geometry) (30 min)
- [ ] 19:30–21:30 · AI fundamentals 📅 2027-01-13
	- 19:30–19:45 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (AI-assisted interviews), then check them against the answers
	- 19:45–20:15 Read the [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/13-interview-process-and-behavioral/README|Behavioral & interview process crash course]]
	- 20:15–21:30 Write your 5-7 STAR stories in full; see [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/13-interview-process-and-behavioral/questions|Behavioral & interview process questions]]

### Thu 14 Jan 2027
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 40 min in total, any time that suits you) 📅 2027-01-14
	- 🟢 [[Transpose Matrix]] (Math & Geometry) (10 min)
	- 🟡 [[Rotate Image]] (Math & Geometry) (30 min)
- [ ] 19:30–21:30 · ML coding: LoRA and beam search 📅 2027-01-14
	- 19:30–20:30 [[Pytorch]]: LoRA adapter from scratch (see `14_lora_adapter.py`): low-rank matrices, scaling, freezing the base weights
	- 20:30–21:30 Implement beam search (see `15_beam_search.py`) and compare it with sampling

### Fri 15 Jan 2027
Rest day.

### Sat 16 Jan 2027
- [ ] 11:00–13:00 · System design concepts: Vector databases, CDC and blob storage 📅 2027-01-16
	- 11:00–11:50 Read: https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction  (find the sections on vector databases, cdc and blob storage; also search for any key technology named below). Cover: ANN search and HNSW; change data capture; object storage and multipart uploads; pre-signed URLs
	- 11:50–12:20 Write your one-page summary in [[System Design Concepts]] (section 15) in your own words
	- 12:20–12:45 See it applied: skim how [[ChatGPT - Solution|ChatGPT]], [[Dropbox - Solution|Dropbox]], [[YouTube - Solution|YouTube]] use it, and note the decision each one made
	- 12:45–13:00 Answer the self-check questions in the note out loud
- [ ] 14:00–16:00 · System design: Flash Sale (mock) 📅 2027-01-16
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[LeetCode - Solution|LeetCode]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:15 Mock, no peeking: read only [[Flash Sale - Question|Flash Sale]], ask clarifying questions out loud
	- 14:15–15:10 Design it end to end on a blank Excalidraw board: requirements, entities, API, high-level design, 2 deep dives
	- 15:10–15:40 Score yourself against [[Flash Sale - Solution|Flash Sale solution]] and its diagram: list every miss
	- 15:40–16:00 Redraw the high-level design from memory

### Sun 17 Jan 2027
- [ ] 11:00–13:00 · AI fundamentals 📅 2027-01-17
	- 11:00–11:15 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (Behavioral stories), then check them against the answers
	- 11:15–12:00 Company research: [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/14-company-interview-questions/README|company question banks]] for the companies you are targeting
	- 12:00–12:30 Role guides: [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/15-role-guides/README|role guides]]
	- 12:30–13:00 Answer 5 behavioral questions out loud with your STAR stories, recorded
- [ ] 14:00–16:00 · System design: Robinhood (mock) 📅 2027-01-17
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[LeetCode - Solution|LeetCode]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:15 Mock, no peeking: read only [[Robinhood - Question|Robinhood]], ask clarifying questions out loud
	- 14:15–15:10 Design it end to end on a blank Excalidraw board: requirements, entities, API, high-level design, 2 deep dives
	- 15:10–15:40 Score yourself against [[Robinhood - Solution|Robinhood solution]] and its diagram: list every miss
	- 15:40–16:00 Redraw the high-level design from memory

### Mon 18 Jan 2027
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2027-01-18
	- 🟡 [[Spiral Matrix]] (Math & Geometry) (30 min)
	- 🟡 [[Set Matrix Zeroes]] (Math & Geometry) (30 min)
- [ ] 19:30–21:30 · Weekly review (spaced repetition) 📅 2027-01-18
	- 19:30–20:30 Spaced coding review: redo cold, 15 min each, no notes, the 4 problems you scored worst on in the timed rounds or that sit on your Fumbled list
	- 20:30–21:30 AI-assisted interview: do one more practice session with the Hello Interview tutorial, then review your agent project README


---

## Week 16: Tue 19 Jan 2027 – Mon 25 Jan 2027

**Focus:** Timed mocks and final review · general design mocks · LeetCode: timed coding rounds

### Tue 19 Jan 2027
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 20 min in total, any time that suits you) 📅 2027-01-19
	- 🟢 [[Happy Number]] (Math & Geometry) (10 min)
	- 🟢 [[Plus One]] (Math & Geometry) (10 min)
- [ ] 19:30–21:30 · LeetCode: timed practice round (1 easy + 3 medium, interview conditions) 📅 2027-01-19
	- 19:30–19:40 🟢 [[Kth Largest Element In a Stream]] (Heap - Priority Queue): 10 min, then stop and write down your approach and complexity
	- 19:40–20:10 🟡 [[Insert into a Binary Search Tree]] (Trees): 30 min, then stop and write down your approach and complexity
	- 20:10–20:40 🟡 [[Combination Sum]] (Backtracking): 30 min, then stop and write down your approach and complexity
	- 20:40–21:10 🟡 [[Maximum Subarray]] (Greedy): 30 min, then stop and write down your approach and complexity
	- 21:10–21:30 Review: read each Solution, note what you missed, add failures to the Fumbled list

### Wed 20 Jan 2027
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 40 min in total, any time that suits you) 📅 2027-01-20
	- 🟢 [[Roman to Integer]] (Math & Geometry) (10 min)
	- 🟡 [[Pow(x, n)]] (Math & Geometry) (30 min)
- [ ] 19:30–21:30 · AI fundamentals 📅 2027-01-20
	- 19:30–19:45 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (Company research), then check them against the answers
	- 19:45–21:30 Full pass over every unticked item in [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/AI-ENGINEER-75|AI Engineer 75]]: answer cold, re-read what you miss

### Thu 21 Jan 2027
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 60 min in total, any time that suits you) 📅 2027-01-21
	- 🟡 [[Multiply Strings]] (Math & Geometry) (30 min)
	- 🟡 [[Detect Squares]] (Math & Geometry) (30 min)
- [ ] 19:30–21:30 · ML coding: timed mocks 📅 2027-01-21
	- 19:30–20:30 Timed mock: build a small tool-calling agent from scratch in 60 minutes (tools, loop, one guardrail, three test conversations) without looking at your project
	- 20:30–21:30 Timed mock: one NumPy/Pandas problem (30 min) and writing a PyTorch training loop from memory (30 min)

### Fri 22 Jan 2027
Rest day.

### Sat 23 Jan 2027
- [ ] 11:00–13:00 · System design concepts: Numbers to know and estimation 📅 2027-01-23
	- 11:00–11:50 Read: https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction  (find the sections on numbers to know and estimation; also search for any key technology named below). Cover: Latency numbers; QPS, storage and bandwidth estimation; read/write ratios; how to size a cluster
	- 11:50–12:20 Write your one-page summary in [[System Design Concepts]] (section 16) in your own words
	- 12:20–12:45 See it applied: skim how [[Bitly - Solution|Bitly]], [[YouTube - Solution|YouTube]], [[Web Crawler - Solution|Web Crawler]] use it, and note the decision each one made
	- 12:45–13:00 Answer the self-check questions in the note out loud
- [ ] 14:00–16:00 · System design: FB Post Search (mock) 📅 2027-01-23
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[LeetCode - Solution|LeetCode]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:15 Mock, no peeking: read only [[FB Post Search - Question|FB Post Search]], ask clarifying questions out loud
	- 14:15–15:10 Design it end to end on a blank Excalidraw board: requirements, entities, API, high-level design, 2 deep dives
	- 15:10–15:40 Score yourself against [[FB Post Search - Solution|FB Post Search solution]] and its diagram: list every miss
	- 15:40–16:00 Redraw the high-level design from memory

### Sun 24 Jan 2027
- [ ] 11:00–13:00 · AI fundamentals 📅 2027-01-24
	- 11:00–11:15 Recall (spaced review, 15 min): without notes, re-answer out loud the questions you flagged from the last AI session (Full AI Engineer 75 pass), then check them against the answers
	- 11:15–12:00 Read the [[CHEATSHEET]] and skim the [[GLOSSARY]]
	- 12:00–13:00 Re-answer the 10 worst items from your Fumbled list in [[STUDYPLAN]] out loud
- [ ] 14:00–16:00 · System design: Local Delivery Service (mock) 📅 2027-01-24
	- 14:00–14:10 Recall (spaced review): from memory, redraw the high-level design of [[LeetCode - Solution|LeetCode]] and name its 3 hardest deep dives and trade-offs, then check against its diagram
	- 14:10–14:15 Mock, no peeking: read only [[Local Delivery Service - Question|Local Delivery Service]], ask clarifying questions out loud
	- 14:15–15:10 Design it end to end on a blank Excalidraw board: requirements, entities, API, high-level design, 2 deep dives
	- 15:10–15:40 Score yourself against [[Local Delivery Service - Solution|Local Delivery Service solution]] and its diagram: list every miss
	- 15:40–16:00 Redraw the high-level design from memory

### Mon 25 Jan 2027
- [ ] Before 19:00 · Daytime LeetCode (2 problems, about 20 min in total, any time that suits you) 📅 2027-01-25
	- 🟢 [[Number of 1 Bits]] (Bit Manipulation) (10 min)
	- 🟢 [[Counting Bits]] (Bit Manipulation) (10 min)
- [ ] 19:30–21:30 · Weekly review (spaced repetition) 📅 2027-01-25
	- 19:30–20:30 Spaced coding review: redo cold, 15 min each, no notes, the 4 problems you scored worst on in the timed rounds or that sit on your Fumbled list
	- 20:30–21:30 Final prep: read the [[CHEATSHEET]] (30 min), then re-read your Fumbled list in [[STUDYPLAN]] and re-answer the 10 worst items out loud (30 min)

