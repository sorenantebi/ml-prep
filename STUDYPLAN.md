---
tags: [studyplan]
---
# Study Plan

Two plans over the same material: a **4-week sprint** (interview is close) and a **3-month plan** (12 weeks, more depth and more mocks). Pick one. Every item is a checkbox with a link to the note that covers it, and ticking it (Tasks plugin) stamps the date you finished it.

**Dated schedules (start Tue 6 Oct 2026, session-by-session with exact problems and times):** [[Schedule - 8 Weeks]] (ends Mon 30 Nov, 102 evening problems + 96 daytime) and [[Schedule - 12 Weeks]] (ends Mon 28 Dec, 131 evening problems + 96 daytime), plus the slower [[Schedule - 16 Weeks]] (ends Mon 25 Jan 2027) that puts system design, AI fundamentals, NumPy/Pandas/PyTorch and the agent project ahead of LeetCode (80 evening problems + 128 daytime), with 🟢 Easy = 10 min, 🟡 Medium = 30 min and 🔴 Hard = 45 min per problem. The plans below are the overview they are built from.

**Project:** build a tool-using agent with the Claude SDK, with prompt, tools, guardrails and an eval harness: [[Build an Agent with the Claude SDK]] (about 5 h, milestones are scheduled in both dated schedules and in the plans below).

**The three pillars** (all in `ML Prep/`)

| Pillar | Where | Size |
|---|---|---|
| Coding | [[NeetCode 250]] (18 sections), [[Numpy]], [[Pandas]], [[Pytorch]], plus the [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/12-coding-challenges/README|coding challenges]] in the AI repo | 250 problems |
| System design | [[General System Design]] (32 problems), [[ML System Design]], AI case studies in [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/11-ai-system-design/README|AI system design]] | 32 + 10 |
| AI fundamentals | [[AI Fundamentals]] -> [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/AI-ENGINEER-75|AI Engineer 75]], ten topic crash courses with question banks | 75 core questions |

Also: [[AI Assisted Interview]] (new-style interviews where you code with an AI tool), the [[CHEATSHEET]] and [[GLOSSARY]] for quick lookups.

## How to use this plan

1. **Weekly rhythm (both plans):** 3 coding sessions, 2-3 system design sessions, 2-3 AI fundamentals sessions, and one review/mock block at the weekend.
2. **Coding:** open the section note, do the 🟢 and 🟡 problems first, 🔴 last. Time-box 20-25 minutes, then read the solution, and redo it cold 3 days later. Do not read the solution first.
3. **System design:** read only the Question note, design it for 35-45 minutes on a blank Excalidraw board, speaking out loud, then compare with the Solution and its diagram. Note what you missed.
4. **AI fundamentals:** read the topic crash course, then answer the questions out loud before opening the collapsed answers.
5. **Spaced repetition:** re-do anything you fumbled 3-4 days later and again a week later. Keep a "fumbled" list at the bottom of this note.
6. Hours are a guide: about **22-25 h/week** for the 4-week sprint (15 of them on coding) and **8-10 h/week** for the 3-month plan. If you have less, drop the items marked (optional).

---

# Plan A: 4-week sprint

Priority is breadth on the highest-signal items: **150 NeetCode problems** (~37 a week, ~5 a day), 8 system design problems, 5 AI case studies, and AI fundamentals via the AI Engineer 75 list.

**Pace for 150 problems:** 20 minutes per problem. If you have no approach after 10 minutes, read the solution, close it, write it from memory, and move on. A ticked box means you understood it, not that you solved it cold. 🔴 problems are skipped (except where noted). In each section, go in list order through the 🟢 and 🟡 problems and stop at the target count. Redo the ones you could not solve on your own at the weekend.

| Week | Sections (problems) | Total |
|---|---|---|
| 1 | Arrays & Hashing 14, Two Pointers 9, Sliding Window 7, Stack 7 | 37 |
| 2 | Binary Search 9, Linked List 10, Trees 19 | 38 |
| 3 | Heap 8, Tries 3, Graphs 15, Backtracking 10, Advanced Graphs 2 | 38 |
| 4 | 1-D DP 12, 2-D DP 8, Greedy 8, Intervals 5, Math & Bit Manipulation 4 | 37 |

If 22-25 h/week is too much, cut in this order: the AI coding challenges, the optional extras, then Advanced AI questions.

## Week 1: Core patterns and the model

**Goal:** fluent in array/string patterns, the URL-shortener style design, and how a transformer works.

**Coding**
- [ ] [[01 Arrays & Hashing|Arrays & Hashing]]: 14 problems
- [ ] [[02 Two Pointers|Two Pointers]]: 9 problems
- [ ] [[03 Sliding Window|Sliding Window]]: 7 problems
- [ ] [[04 Stack|Stack]]: 7 problems
- [ ] [[Numpy]] quick pass (broadcasting, indexing, vectorisation)

**System design**
- [ ] Read the framework and core concepts: [Hello Interview delivery framework](https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction)
- [ ] 🟢 [[Bitly - Question|Bitly]] ([[Bitly - Solution|answer]])
- [ ] 🟡 [[Rate Limiter - Question|Rate Limiter]] ([[Rate Limiter - Solution|answer]])

**AI fundamentals**
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/01-ml-and-dl-foundations/README|ML & DL foundations]] + [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/01-ml-and-dl-foundations/questions|questions]] (full pass)
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/02-llm-fundamentals/README|LLM fundamentals]] + [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/02-llm-fundamentals/questions|questions]] (Basic + Intermediate)
- [ ] Implement from scratch: `01_attention.py`, `03_sampling.py` (see [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/12-coding-challenges/README|coding challenges]])
- [ ] AI Engineer 75: ML & DL foundations, LLM & Transformer fundamentals sections in [[AI-ENGINEER-75|AI Engineer 75]]

**Weekend review**
- [ ] Redo the 8 problems you could not solve on your own, cold
- [ ] Re-explain self-attention and the KV cache out loud, without notes

## Week 2: Retrieval, prompting and concurrency-style design

**Coding**
- [ ] [[05 Binary Search|Binary Search]]: 9 problems
- [ ] [[06 Linked List|Linked List]]: 10 problems
- [ ] [[07 Trees|Trees]]: 19 problems
- [ ] [[Pandas]] quick pass (groupby, merge, window functions)

**System design**
- [ ] 🟡 [[FB News Feed - Question|FB News Feed]] ([[FB News Feed - Solution|answer]])
- [ ] 🟡 [[Ticketmaster - Question|Ticketmaster]] ([[Ticketmaster - Solution|answer]])
- [ ] AI case study: [[01-enterprise-rag-assistant|Enterprise RAG assistant]]

**AI fundamentals**
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/03-prompt-engineering-and-context/README|Prompt & context engineering]] + [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/03-prompt-engineering-and-context/questions|questions]]
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/04-rag-and-retrieval/README|RAG & retrieval]] + [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/04-rag-and-retrieval/questions|questions]] (full pass)
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/05-fine-tuning-and-alignment/README|Fine-tuning & alignment]] + [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/05-fine-tuning-and-alignment/questions|questions]] (crash course + Basic/Intermediate)
- [ ] Implement: `08_semantic_search_rag.py`, `09_text_chunking.py`
- [ ] AI Engineer 75: Prompt & context, RAG, Fine-tuning sections

**Weekend review**
- [ ] Redo the 8 problems you could not solve on your own, plus fumbled questions
- [ ] Draw the RAG pipeline from memory (ingest, chunk, embed, retrieve, rerank, generate, cite)

## Week 3: Agents, evals, production and real-time systems

**Coding**
- [ ] [[08 Heap - Priority Queue|Heap / Priority Queue]]: 8 problems
- [ ] [[11 Graphs|Graphs]]: 15 problems
- [ ] [[09 Backtracking|Backtracking]]: 10 problems
- [ ] [[10 Tries|Tries]]: 3 problems
- [ ] [[12 Advanced Graphs|Advanced Graphs]]: 2 problems
- [ ] [[Pytorch]] quick pass (tensors, autograd, a training loop)

**System design**
- [ ] 🔴 [[WhatsApp - Question|WhatsApp]] ([[WhatsApp - Solution|answer]])
- [ ] 🟡 [[Web Crawler - Question|Web Crawler]] ([[Web Crawler - Solution|answer]])
- [ ] AI case studies: [[03-customer-support-agent|Customer support agent]], [[07-text-to-sql-agent|Text-to-SQL agent]]

**AI fundamentals**
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/06-agents-and-tool-use/README|Agents & tool use]] + [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/06-agents-and-tool-use/questions|questions]] (full pass)
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/07-evaluation-and-observability/README|Evaluation & observability]] + [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/07-evaluation-and-observability/questions|questions]] (do not skip: most senior-signalling topic)
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/08-inference-and-production/README|Inference & production]] + [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/08-inference-and-production/questions|questions]]
- [ ] Implement: `06_kv_cache.py`, `10_agent_loop.py`, `12_eval_metrics.py`
- [ ] [[Build an Agent with the Claude SDK|Claude agent project]]: milestone 1 (design and prompt) and milestone 2 (agent loop and tools, manual loop first)
- [ ] AI Engineer 75: Agents, Evaluation, Inference sections

**Weekend review**
- [ ] One full 45-minute system design mock (pick a problem you have not done)
- [ ] Redo fumbled items

## Week 4: Design, safety, mocks and polish

**Coding**
- [ ] [[13 1-D Dynamic Programming|1-D Dynamic Programming]]: 12 problems
- [ ] [[14 2-D Dynamic Programming|2-D Dynamic Programming]]: 8 problems
- [ ] [[15 Greedy|Greedy]]: 8 problems
- [ ] [[16 Intervals|Intervals]]: 5 problems
- [ ] [[17 Math & Geometry|Math & Geometry]] and [[18 Bit Manipulation|Bit Manipulation]]: 4 problems in total
- [ ] Redo your 15 hardest earlier problems cold (the weekly redo lists add up to this)

**System design**
- [ ] 🔴 [[Uber - Question|Uber]] ([[Uber - Solution|answer]])
- [ ] 🔴 [[Distributed Cache - Question|Distributed Cache]] ([[Distributed Cache - Solution|answer]])
- [ ] AI case studies: [[10-llm-gateway-and-serving-platform|LLM gateway & serving]], [[02-ai-code-assistant|AI code assistant]]
- [ ] Read [[AI Assisted Interview]] and try one practice session

**AI fundamentals**
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/09-safety-security-and-responsible-ai/README|Safety & security]] + [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/10-multimodal/README|Multimodal]] crash courses
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/11-ai-system-design/README|AI system design]] framework, then 2 AI case studies above as timed mocks
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/13-interview-process-and-behavioral/README|Behavioral & interview process]] + [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/13-interview-process-and-behavioral/questions|questions]]: write 5-7 STAR stories
- [ ] Implement: `07_mini_gpt_forward.py`, `13_streaming_parser.py`
- [ ] Complete the remaining unticked items in [[AI-ENGINEER-75|AI Engineer 75]]
- [ ] [[Build an Agent with the Claude SDK|Claude agent project]]: milestone 3 (guardrails), milestone 4 (20-case eval harness) and milestone 5 (README and 3-minute walk-through)

**Final days**
- [ ] Full mock loop with the [[mock-interview-kit|mock interview kit]]: one coding problem cold, one design prompt, behavioral answers out loud
- [ ] Night before: [[CHEATSHEET]] only

---

# Plan B: 3-month plan (12 weeks)

Three months of ~8-10 h/week. Month 1 builds foundations, month 2 adds depth, month 3 is polish and mocks. This plan covers all of NeetCode's 🟢/🟡 problems, ~22 system design problems and every AI fundamentals topic.

## Month 1: Foundations (weeks 1-4)

**Milestone by end of month:** comfortable with arrays/strings/stack/binary search/linked lists; can structure a system design answer; can explain transformers, tokenization and sampling.

### Week 1: Arrays and the framework

**Coding**
- [ ] [[01 Arrays & Hashing|Arrays & Hashing]]: all 🟢 + 🟡
- [ ] [[Numpy]] quick pass

**System design**
- [ ] Read the [Hello Interview delivery framework and core concepts](https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction) (networking, API design, data modeling, caching, sharding, consistent hashing, CAP)
- [ ] 🟢 [[Bitly - Question|Bitly]] ([[Bitly - Solution|answer]])

**AI fundamentals**
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/01-ml-and-dl-foundations/README|ML & DL foundations]] + [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/01-ml-and-dl-foundations/questions|questions]]
- [ ] [[AI-ENGINEER-75|AI Engineer 75]]: tick the ML & DL foundations section

### Week 2: Pointers, windows and the LLM

**Coding**
- [ ] [[02 Two Pointers|Two Pointers]]: all 🟢 + 🟡
- [ ] [[03 Sliding Window|Sliding Window]]: all 🟢 + 🟡

**System design**
- [ ] 🟡 [[Rate Limiter - Question|Rate Limiter]] ([[Rate Limiter - Solution|answer]])
- [ ] 🔴 [[Distributed Cache - Question|Distributed Cache]] ([[Distributed Cache - Solution|answer]])

**AI fundamentals**
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/02-llm-fundamentals/README|LLM fundamentals]] + [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/02-llm-fundamentals/questions|questions]] (full pass)
- [ ] Implement: `01_attention.py`, `03_sampling.py` ([[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/12-coding-challenges/README|coding challenges]])

### Week 3: Stack, binary search and prompting

**Coding**
- [ ] [[04 Stack|Stack]]: all 🟢 + 🟡
- [ ] [[05 Binary Search|Binary Search]]: all 🟢 + 🟡

**System design**
- [ ] 🟡 [[FB News Feed - Question|FB News Feed]] ([[FB News Feed - Solution|answer]])
- [ ] 🟡 [[Tinder - Question|Tinder]] ([[Tinder - Solution|answer]])

**AI fundamentals**
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/02-llm-fundamentals/README|LLM fundamentals]] + [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/02-llm-fundamentals/questions|questions]]: Advanced questions
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/03-prompt-engineering-and-context/README|Prompt & context engineering]] + [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/03-prompt-engineering-and-context/questions|questions]]
- [ ] Implement: `02_bpe_tokenizer.py`, `04_positional_encodings.py`, `05_layernorm_and_softmax.py`

**Weekend**
- [ ] Redo your 8 hardest problems cold; log the fumbled ones below

### Week 4: Linked lists, booking systems and RAG basics

**Coding**
- [ ] [[06 Linked List|Linked List]]: all 🟢 + 🟡
- [ ] [[Pandas]] quick pass

**System design**
- [ ] 🟡 [[Ticketmaster - Question|Ticketmaster]] ([[Ticketmaster - Solution|answer]])
- [ ] 🟡 [[Online Auction - Question|Online Auction]] ([[Online Auction - Solution|answer]])

**AI fundamentals**
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/04-rag-and-retrieval/README|RAG & retrieval]]: crash course + Basic questions
- [ ] Implement: `08_semantic_search_rag.py`, `09_text_chunking.py`

**Weekend**
- [ ] Month 1 checkpoint: one 45-minute design mock + one cold coding problem, record how you did

## Month 2: Depth (weeks 5-8)

**Milestone by end of month:** trees and graphs are routine; you can design real-time, messaging and media systems and discuss trade-offs; you understand RAG, fine-tuning, agents and evals in depth.

### Week 5: Trees and messaging

**Coding**
- [ ] [[07 Trees|Trees]]: all 🟢 + 🟡

**System design**
- [ ] 🔴 [[WhatsApp - Question|WhatsApp]] ([[WhatsApp - Solution|answer]])
- [ ] 🟡 [[Notification System - Question|Notification System]] ([[Notification System - Solution|answer]])

**AI fundamentals**
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/04-rag-and-retrieval/README|RAG & retrieval]] + [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/04-rag-and-retrieval/questions|questions]] (Intermediate + Advanced)
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/05-fine-tuning-and-alignment/README|Fine-tuning & alignment]] + [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/05-fine-tuning-and-alignment/questions|questions]]
- [ ] Implement: `14_lora_adapter.py`

### Week 6: Heaps, tries and media

**Coding**
- [ ] [[08 Heap - Priority Queue|Heap / Priority Queue]]: all 🟢 + 🟡
- [ ] [[10 Tries|Tries]]: all 4
- [ ] [[Pytorch]] quick pass

**System design**
- [ ] 🟡 [[Dropbox - Question|Dropbox]] ([[Dropbox - Solution|answer]])
- [ ] 🟡 [[YouTube - Question|YouTube]] ([[YouTube - Solution|answer]])

**AI fundamentals**
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/06-agents-and-tool-use/README|Agents & tool use]] + [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/06-agents-and-tool-use/questions|questions]]
- [ ] AI case study: [[01-enterprise-rag-assistant|Enterprise RAG assistant]]
- [ ] Implement: `10_agent_loop.py`
- [ ] [[Build an Agent with the Claude SDK|Claude agent project]]: milestone 1 (design and prompt) and milestone 2 (agent loop and tools)

### Week 7: Graphs, location and evals

**Coding**
- [ ] [[11 Graphs|Graphs]]: all 🟢 + 🟡

**System design**
- [ ] 🔴 [[Uber - Question|Uber]] ([[Uber - Solution|answer]])
- [ ] 🟡 [[Yelp - Question|Yelp]] ([[Yelp - Solution|answer]])

**AI fundamentals**
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/07-evaluation-and-observability/README|Evaluation & observability]] + [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/07-evaluation-and-observability/questions|questions]] (do not skip)
- [ ] Implement: `12_eval_metrics.py`, `17_hybrid_search_and_rerank.py`
- [ ] [[Build an Agent with the Claude SDK|Claude agent project]]: milestone 3 (guardrails) and milestone 4 (evals)

### Week 8: Backtracking, crawling and production

**Coding**
- [ ] [[09 Backtracking|Backtracking]]: all 🟢 + 🟡 (🔴 optional)
- [ ] [[12 Advanced Graphs|Advanced Graphs]]: 3 problems (optional)

**System design**
- [ ] 🟡 [[Web Crawler - Question|Web Crawler]] ([[Web Crawler - Solution|answer]])
- [ ] 🟡 [[Job Scheduler - Question|Job Scheduler]] ([[Job Scheduler - Solution|answer]])

**AI fundamentals**
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/08-inference-and-production/README|Inference & production]] + [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/08-inference-and-production/questions|questions]]
- [ ] Implement: `06_kv_cache.py`, `11_rate_limiter_and_retry.py`, `16_semantic_cache.py`
- [ ] [[Build an Agent with the Claude SDK|Claude agent project]]: milestone 5 (polish, README, 3-minute walk-through)

**Weekend**
- [ ] Month 2 checkpoint: two design mocks (one general, one AI case study such as [[03-customer-support-agent|customer support agent]]) and one timed 2-problem coding set

## Month 3: Polish and mocks (weeks 9-12)

**Milestone by end of month:** DP/intervals/greedy covered, data-heavy and payment designs done, safety, multimodal and behavioral prepared, and several full mock loops completed.

### Week 9: DP and data pipelines

**Coding**
- [ ] [[13 1-D Dynamic Programming|1-D Dynamic Programming]]: all 🟢 + 🟡

**System design**
- [ ] 🔴 [[Ad Click Aggregator - Question|Ad Click Aggregator]] ([[Ad Click Aggregator - Solution|answer]])
- [ ] 🔴 [[YouTube Top K - Question|YouTube Top K]] ([[YouTube Top K - Solution|answer]])

**AI fundamentals**
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/09-safety-security-and-responsible-ai/README|Safety & security]] crash course + questions
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/10-multimodal/README|Multimodal]] crash course
- [ ] Implement: `15_beam_search.py`, `18_constrained_json_decoding.py`, `19_speculative_decoding.py` (optional)

### Week 10: 2-D DP, money and AI design

**Coding**
- [ ] [[14 2-D Dynamic Programming|2-D Dynamic Programming]]: 🟢 + 🟡 (as many as you can)
- [ ] [[15 Greedy|Greedy]]: all 🟢 + 🟡

**System design**
- [ ] 🔴 [[Payment System - Question|Payment System]] ([[Payment System - Solution|answer]])
- [ ] 🔴 [[Metrics Monitoring - Question|Metrics Monitoring]] ([[Metrics Monitoring - Solution|answer]])

**AI fundamentals**
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/11-ai-system-design/README|AI system design]] framework + 3 case studies as timed mocks: [[02-ai-code-assistant|AI code assistant]], [[07-text-to-sql-agent|Text-to-SQL agent]], [[10-llm-gateway-and-serving-platform|LLM gateway]]

### Week 11: Intervals, collaboration, behavioral and AI-assisted coding

**Coding**
- [ ] [[16 Intervals|Intervals]]: all 7
- [ ] [[17 Math & Geometry|Math & Geometry]] and [[18 Bit Manipulation|Bit Manipulation]]: a few each (optional)

**System design**
- [ ] 🔴 [[Google Docs - Question|Google Docs]] ([[Google Docs - Solution|answer]])
- [ ] 🔴 [[FB Live Comments - Question|FB Live Comments]] ([[FB Live Comments - Solution|answer]])
- [ ] 🔴 [[ChatGPT - Question|ChatGPT]] ([[ChatGPT - Solution|answer]])

**AI fundamentals**
- [ ] [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/13-interview-process-and-behavioral/README|Behavioral & interview process]] + [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/13-interview-process-and-behavioral/questions|questions]]: write 5-7 STAR stories
- [ ] Read [[AI Assisted Interview]] and run one practice session
- [ ] Company research: [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/14-company-interview-questions/README|company question banks]] and [[ML Prep/AI Fundamentals/AI-Engineer-Interview-Questions/15-role-guides/README|role guides]]

### Week 12: Mock loops and final review

**Coding**
- [ ] Redo your 15 hardest coding problems cold, timed (25 min each)
- [ ] One coding round simulation: 2 problems in 50 minutes

**System design**
- [ ] Two full 45-minute design mocks on problems you have not done before
- [ ] Review the diagrams of your top 5 designs and redraw 2 from memory

**AI fundamentals**
- [ ] Finish every item in [[AI-ENGINEER-75|AI Engineer 75]]
- [ ] Full mock loop with the [[mock-interview-kit|mock interview kit]]
- [ ] Night before: [[CHEATSHEET]] only

## Bonus system design problems (any week with spare time)

- [ ] 🟡 [[Instagram - Question|Instagram]] ([[Instagram - Solution|answer]])
- [ ] 🟡 [[News Aggregator - Question|News Aggregator]] ([[News Aggregator - Solution|answer]])
- [ ] 🟡 [[Strava - Question|Strava]] ([[Strava - Solution|answer]])
- [ ] 🟡 [[Online Chess - Question|Online Chess]] ([[Online Chess - Solution|answer]])
- [ ] 🟡 [[Local Delivery Service - Question|Local Delivery Service]] ([[Local Delivery Service - Solution|answer]])
- [ ] 🟡 [[Price Tracking Service - Question|Price Tracking Service]] ([[Price Tracking Service - Solution|answer]])
- [ ] 🟡 [[LeetCode - Question|LeetCode]] ([[LeetCode - Solution|answer]])
- [ ] 🔴 [[Flash Sale - Question|Flash Sale]] ([[Flash Sale - Solution|answer]])
- [ ] 🔴 [[FB Post Search - Question|FB Post Search]] ([[FB Post Search - Solution|answer]])
- [ ] 🔴 [[Robinhood - Question|Robinhood]] ([[Robinhood - Solution|answer]])

## ML system design (both plans)

[[ML System Design]] is still empty in this vault. Work through [Hello Interview's ML system design](https://www.hellointerview.com/learn/ml-system-design/in-a-hurry/introduction) in the last two weeks of either plan, and write short notes there as you go (recommendation, ranking, search, fraud/anomaly detection).

- [ ] Read the ML system design framework
- [ ] Do 2-3 ML design problems and write your notes into [[ML System Design]]

## Fumbled list

Questions and problems you got wrong or could not finish. Re-quiz only these on later passes.

- [ ] 

