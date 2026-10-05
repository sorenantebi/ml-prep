---
tags: [hub, system-design]
---
# System Design Concepts

One section per concept, studied in the Saturday 11:00 concept sessions of [[Schedule - 16 Weeks]]. For each: read the source, then fill in the section in your own words (a page at most), answer the self-check questions out loud, and look at how three of the designs in [[General System Design]] use it.

Source: [Hello Interview system design](https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction) (core concepts, key technologies and advanced topics).

## 1. Networking essentials

**Cover:** TCP vs UDP; HTTP/1.1 vs HTTP/2 vs HTTP/3; WebSocket vs SSE vs long polling; DNS; L4 vs L7 load balancers; CDN

**See it applied in:** [[WhatsApp - Solution|WhatsApp]], [[FB Live Comments - Solution|FB Live Comments]], [[YouTube - Solution|YouTube]]

**Self-check**
- [ ] When do you pick SSE over WebSocket, and what breaks at 1M connections?
- [ ] What does an L7 load balancer give you that L4 does not?

**My notes**

- 

## 2. API design

**Cover:** REST vs gRPC vs GraphQL; pagination (cursor vs offset); idempotency keys; versioning; rate limiting

**See it applied in:** [[Rate Limiter - Solution|Rate Limiter]], [[Payment System - Solution|Payment System]], [[FB News Feed - Solution|FB News Feed]]

**Self-check**
- [ ] Why is cursor pagination better than offset for feeds?
- [ ] How does an idempotency key make a payment retry safe?

**My notes**

- 

## 3. Data modeling

**Cover:** Relational vs document vs wide-column vs key-value vs graph; designing the schema for the access pattern; denormalization

**See it applied in:** [[Dropbox - Solution|Dropbox]], [[Tinder - Solution|Tinder]], [[Ticketmaster - Solution|Ticketmaster]]

**Self-check**
- [ ] How do you choose a partition key from the access pattern?
- [ ] When is denormalizing worth the write cost?

**My notes**

- 

## 4. Caching

**Cover:** Cache-aside, write-through, write-back; eviction; invalidation; stampedes and hot keys; CDN caching

**See it applied in:** [[Distributed Cache - Solution|Distributed Cache]], [[Bitly - Solution|Bitly]], [[FB News Feed - Solution|FB News Feed]]

**Self-check**
- [ ] How do you stop a cache stampede on a viral key?
- [ ] What are the failure modes of write-back caching?

**My notes**

- 

## 5. Sharding and partitioning

**Cover:** Range vs hash vs directory sharding; hot spots; resharding; cross-shard queries and joins

**See it applied in:** [[Distributed Cache - Solution|Distributed Cache]], [[Ad Click Aggregator - Solution|Ad Click Aggregator]], [[WhatsApp - Solution|WhatsApp]]

**Self-check**
- [ ] How do you reshard without downtime?
- [ ] How do you run a top-K query across shards?

**My notes**

- 

## 6. Consistent hashing and replication

**Cover:** The hash ring, virtual nodes, replication factor, leader-follower, quorum reads and writes

**See it applied in:** [[Distributed Cache - Solution|Distributed Cache]], [[WhatsApp - Solution|WhatsApp]], [[Metrics Monitoring - Solution|Metrics Monitoring]]

**Self-check**
- [ ] What problem do virtual nodes solve?
- [ ] What do R + W > N quorums guarantee, and what do they not?

**My notes**

- 

## 7. CAP, PACELC and transactions

**Cover:** Consistency models; isolation levels; two-phase commit vs saga; idempotent consumers; exactly-once myths

**See it applied in:** [[Payment System - Solution|Payment System]], [[Ticketmaster - Solution|Ticketmaster]], [[Online Auction - Solution|Online Auction]]

**Self-check**
- [ ] What does each isolation level allow (dirty, non-repeatable, phantom reads)?
- [ ] When would you choose a saga over 2PC?

**My notes**

- 

## 8. Database indexing and Postgres

**Cover:** B-tree vs LSM tree; composite and covering indexes; GIN; reading a query plan; connection pooling; replication

**See it applied in:** [[Yelp - Solution|Yelp]], [[Ticketmaster - Solution|Ticketmaster]], [[YouTube - Solution|YouTube]]

**Self-check**
- [ ] Why does column order in a composite index matter?
- [ ] What does a sequential scan in EXPLAIN tell you?

**My notes**

- 

## 9. Redis

**Cover:** Data structures; sorted sets; pub/sub; persistence (RDB/AOF); distributed locks and TTLs; clustering

**See it applied in:** [[Rate Limiter - Solution|Rate Limiter]], [[Ticketmaster - Solution|Ticketmaster]], [[Uber - Solution|Uber]]

**Self-check**
- [ ] How would you build a leaderboard and a rate limiter with Redis?
- [ ] What are the risks of a Redis-based distributed lock?

**My notes**

- 

## 10. Kafka and message queues

**Cover:** Topics, partitions, consumer groups; ordering; delivery semantics; retries and dead-letter queues; Kafka vs SQS

**See it applied in:** [[Ad Click Aggregator - Solution|Ad Click Aggregator]], [[Notification System - Solution|Notification System]], [[Job Scheduler - Solution|Job Scheduler]]

**Self-check**
- [ ] How do you preserve ordering per key at scale?
- [ ] What does at-least-once mean for your consumer design?

**My notes**

- 

## 11. Elasticsearch and search

**Cover:** Inverted index; shards and replicas; analyzers; relevance scoring; keeping the index in sync (CDC)

**See it applied in:** [[Ticketmaster - Solution|Ticketmaster]], [[FB Post Search - Solution|FB Post Search]], [[Yelp - Solution|Yelp]]

**Self-check**
- [ ] Why is Elasticsearch not your primary database?
- [ ] How do you keep the search index consistent with the source of truth?

**My notes**

- 

## 12. DynamoDB and Cassandra

**Cover:** Partition and sort keys; hot partitions; tunable consistency; last-write-wins; single-table design

**See it applied in:** [[Bitly - Solution|Bitly]], [[Tinder - Solution|Tinder]], [[YouTube - Solution|YouTube]]

**Self-check**
- [ ] How do you design keys to avoid a hot partition?
- [ ] What does tunable consistency let you trade?

**My notes**

- 

## 13. Stream processing and durable execution

**Cover:** Flink windows, watermarks, checkpoints and state; Temporal workflows and sagas

**See it applied in:** [[YouTube Top K - Solution|YouTube Top K]], [[Ad Click Aggregator - Solution|Ad Click Aggregator]], [[Job Scheduler - Solution|Job Scheduler]]

**Self-check**
- [ ] What do watermarks do, and what happens to late events?
- [ ] When do you pick a durable workflow over a cron job and a queue?

**My notes**

- 

## 14. Geospatial search and time-series databases

**Cover:** Geohash, quadtree, S2; proximity queries; time-series storage, downsampling, retention

**See it applied in:** [[Uber - Solution|Uber]], [[Yelp - Solution|Yelp]], [[Metrics Monitoring - Solution|Metrics Monitoring]]

**Self-check**
- [ ] Compare geohash and quadtree for nearby-driver search.
- [ ] Why do time-series databases struggle with high-cardinality labels?

**My notes**

- 

## 15. Vector databases, CDC and blob storage

**Cover:** ANN search and HNSW; change data capture; object storage and multipart uploads; pre-signed URLs

**See it applied in:** [[ChatGPT - Solution|ChatGPT]], [[Dropbox - Solution|Dropbox]], [[YouTube - Solution|YouTube]]

**Self-check**
- [ ] What is the recall vs latency trade-off in ANN indexes?
- [ ] How does CDC avoid dual writes?

**My notes**

- 

## 16. Numbers to know and estimation

**Cover:** Latency numbers; QPS, storage and bandwidth estimation; read/write ratios; how to size a cluster

**See it applied in:** [[Bitly - Solution|Bitly]], [[YouTube - Solution|YouTube]], [[Web Crawler - Solution|Web Crawler]]

**Self-check**
- [ ] Estimate storage and QPS for a service with 100M daily users.
- [ ] How many requests per second can one machine realistically handle?

**My notes**

- 
