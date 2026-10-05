"""Challenge 16 - Semantic Cache with TTL, LRU and Tag Invalidation (Medium)

PROBLEM
-------
Model calls are slow and metered, and query traffic for support or FAQ-style
products is often heavy-tailed, with a head of near-identical questions. That
makes a cache in front of the model one of the cheapest wins available. A
*semantic* cache goes further than a hash map: it serves a stored response
when a new query is close enough to one already answered. Implement:

    SemanticCache(embedder, threshold=0.92, capacity=128, ttl=None,
                  clock=time.monotonic)

        get(query) -> str | None
            L1 exact hit on the canonical key (lowercased, punctuation
            stripped, whitespace collapsed), then L2 cosine nearest neighbour
            over the stored query vectors, which hits only when the best score
            >= threshold. Records exactly one exact_hit, semantic_hit or miss
            per call and marks whichever entry it served as most recently used.

        put(query, response, tags=()) -> None
            Insert or refresh. Over capacity, evict the least recently USED
            entry. With ttl set, an entry dies ttl seconds after the write
            that created or refreshed it, measured with clock().

        invalidate(tag) -> int
            Drop every entry carrying that tag, from both tiers, and return
            how many went: the document-version hook, since when doc 42 is
            re-indexed every cached answer derived from it has to die.

        stats -> CacheStats(exact_hits, semantic_hits, misses, hit_rate)
        len(cache) -> number of live (unexpired) entries

numpy and the standard library only, with the clock injected so TTL behaviour
is testable without sleeping. The embedder is the hashed character n-gram one
from challenge 08: it scores surface overlap rather than meaning, so the test
pairs below are crafted as lexical near-twins.

INTERVIEW NOTES
---------------
A strong solution demonstrates:
- The threshold is a business decision. A miss costs one model call; a false
  hit serves a confidently wrong answer. Support deflection with a feedback
  escape can run loose; billing or legal answers run tight or are not cached
  semantically at all. Set it by measuring false-hit rate per threshold on
  labelled query pairs against an error budget, and re-tune whenever the
  encoder changes: cosine scales differ between embedding models.
- Both tiers must share one store. Deleting from the exact map while leaving
  the vector in the search index is how expired and invalidated answers keep
  getting served, the classic bug in naive semantic caches for RAG. The TTL
  and invalidation tests probe with a paraphrase for exactly that reason.
- Knowing what this is NOT. Provider prompt caching reuses the KV cache of a
  repeated prompt prefix: it cuts input cost and time to first token but
  still decodes a fresh answer, drawn from the same distribution an uncached
  call would use. A response cache skips the model entirely and can be wrong.
  Most stacks want both.
- Eviction by recency of *use*, not of insertion: an OrderedDict plus
  move_to_end on every hit and every write is the whole trick.
- Never cache across tenants, or across system-prompt and model versions.
  Keying on query text alone serves tenant A's answer to tenant B, a data leak
  rather than a cache bug, and an entry that outlives a prompt change serves
  the old behaviour while your rollout metrics measure nothing. So the key is
  hash(model id + decoding params + prompt template version + tool schema
  version + tenant + canonical query): whatever can change the output goes in
  it, whatever cannot stays out or the hit rate collapses. One namespace per
  (model, prompt version, tenant) makes a version bump a namespace drop.
Common mistakes: unbounded growth; expiry checked only on the exact path;
caching a streamed response before the stream completes; caching errors and
refusals; serving a cached answer where the product promises variety, such as
a regenerate button; caching answers that depend on per-user context or live
tool results; embedding before the exact tier is checked, which bills an
embedding on every request; a threshold copied from a blog post.
Follow-ups: in-process L1 plus shared Redis L2 and the coherence problem
between them; writing the new query in as an alias of the entry that served
it; negative caching; an ANN index sharded by namespace; reporting money saved
and false hits rather than hit rate alone.
"""

import string
import time
import zlib
from collections import OrderedDict
from dataclasses import dataclass
from typing import Callable, Iterable

import numpy as np


class HashedNGramEmbedder:
    """Deterministic mock embedding: hashed character n-grams, L2-normalized."""

    def __init__(self, dim: int = 256, n: int = 3):
        self.dim, self.n = dim, n

    def embed(self, text: str) -> np.ndarray:
        text = f" {' '.join(text.lower().split())} "   # mark word boundaries
        vec = np.zeros(self.dim)
        for i in range(max(len(text) - self.n + 1, 0)):
            h = zlib.crc32(text[i:i + self.n].encode("utf-8"))  # stable across processes
            vec[h % self.dim] += 1.0 if (h >> 31) & 1 else -1.0
        norm = np.linalg.norm(vec)
        return vec / norm if norm > 0 else vec


_PUNCT = str.maketrans("", "", string.punctuation)


def canonical_key(text: str) -> str:
    """Lowercase, drop punctuation, collapse whitespace."""
    return " ".join(text.lower().translate(_PUNCT).split())


@dataclass
class CacheStats:
    exact_hits: int = 0
    semantic_hits: int = 0
    misses: int = 0

    @property
    def hit_rate(self) -> float:
        total = self.exact_hits + self.semantic_hits + self.misses
        return (self.exact_hits + self.semantic_hits) / total if total else 0.0


@dataclass
class _Entry:
    response: str
    vector: np.ndarray
    tags: frozenset[str]
    expires_at: float | None


class SemanticCache:
    """Two-tier cache: exact key first, cosine nearest neighbour second."""

    def __init__(self, embedder: HashedNGramEmbedder, threshold: float = 0.92,
                 capacity: int = 128, ttl: float | None = None,
                 clock: Callable[[], float] = time.monotonic):
        if capacity < 1:
            raise ValueError("capacity must be >= 1")
        self.embedder, self.threshold = embedder, threshold
        self.capacity, self.ttl, self.clock = capacity, ttl, clock
        # Key order is recency of use; the front of the dict is the next victim.
        self._entries: OrderedDict[str, _Entry] = OrderedDict()
        self._stats = CacheStats()

    @property
    def stats(self) -> CacheStats:
        return self._stats

    def __len__(self) -> int:
        self._expire()
        return len(self._entries)

    def _expire(self) -> None:
        # Linear sweep; a real cache leans on store-level key expiry instead.
        if self.ttl is None:
            return
        now = self.clock()
        for key in [k for k, e in self._entries.items()
                    if e.expires_at is not None and e.expires_at <= now]:
            del self._entries[key]

    def put(self, query: str, response: str, tags: Iterable[str] = ()) -> None:
        self._expire()
        key = canonical_key(query)
        expires_at = None if self.ttl is None else self.clock() + self.ttl
        self._entries[key] = _Entry(response, self.embedder.embed(key),
                                    frozenset(tags), expires_at)
        self._entries.move_to_end(key)          # a write counts as a use
        while len(self._entries) > self.capacity:
            self._entries.popitem(last=False)   # evict least recently used

    def get(self, query: str) -> str | None:
        self._expire()
        key = canonical_key(query)
        entry = self._entries.get(key)          # L1: costs no embedding
        if entry is not None:
            self._entries.move_to_end(key)
            self._stats.exact_hits += 1
            return entry.response
        if self._entries:                       # L2: cosine nearest neighbour
            keys = list(self._entries)
            matrix = np.stack([self._entries[k].vector for k in keys])
            scores = matrix @ self.embedder.embed(key)   # rows are unit norm
            best = int(np.argmax(scores))
            if scores[best] >= self.threshold:
                self._entries.move_to_end(keys[best])
                self._stats.semantic_hits += 1
                return self._entries[keys[best]].response
        self._stats.misses += 1
        return None

    def invalidate(self, tag: str) -> int:
        # Both tiers read one store, so a single delete removes the entry from
        # the exact map and from the vector search space together.
        doomed = [k for k, e in self._entries.items() if tag in e.tags]
        for key in doomed:
            del self._entries[key]
        return len(doomed)


class FakeClock:
    """Injectable clock so TTL tests never sleep."""

    def __init__(self, now: float = 0.0): self.now = now
    def __call__(self) -> float: return self.now
    def advance(self, seconds: float) -> None: self.now += seconds


if __name__ == "__main__":
    embedder = HashedNGramEmbedder(dim=256, n=3)

    def sim(a: str, b: str) -> float:
        return float(embedder.embed(canonical_key(a)) @ embedder.embed(canonical_key(b)))

    AUDIT_Q = "What is the retention period for audit logs on the enterprise plan?"
    AUDIT_A = "Audit logs are retained for 400 days on the enterprise plan."
    AUDIT_PARA = "What is the retention period for audit logs in the enterprise plan?"
    PASSWORD_Q, PASSWORD_A = "How do I reset my password?", "Use the Forgot password link."

    # 1. Exact tier: casing, punctuation and spacing are canonicalised away.
    cache = SemanticCache(embedder)
    cache.put(PASSWORD_Q, PASSWORD_A)
    assert cache.get("  how do i RESET my password ") == PASSWORD_A
    assert (cache.stats.exact_hits, cache.stats.semantic_hits) == (1, 0)

    # 2. A paraphrase above the threshold hits the semantic tier.
    cache.put(AUDIT_Q, AUDIT_A, tags=("doc:42",))
    assert sim(AUDIT_Q, AUDIT_PARA) > 0.92          # the pair really is that close
    assert cache.get(AUDIT_PARA) == AUDIT_A and cache.stats.semantic_hits == 1

    # 3. A distant query misses instead of serving the nearest thing available.
    assert cache.get("What is the boiling point of water at sea level?") is None
    assert cache.stats.misses == 1 and abs(cache.stats.hit_rate - 2 / 3) < 1e-12

    # 4. The threshold is the precision/recall knob. One crafted pair, two
    #    settings: the strings barely move, one word flips the answer.
    FREE_Q = "Does the free plan include API access?"
    PAID_Q = "Does the paid plan include API access?"
    FREE_A = "No, API access starts on the Pro plan."
    assert 0.80 < sim(FREE_Q, PAID_Q) < 0.92
    strict = SemanticCache(embedder, threshold=0.92)
    strict.put(FREE_Q, FREE_A)
    assert strict.get(PAID_Q) is None and strict.stats.misses == 1   # refuses it
    lenient = SemanticCache(embedder, threshold=0.80)                # serves it: recall
    lenient.put(FREE_Q, FREE_A)                                      # bought with a
    assert lenient.get(PAID_Q) == FREE_A and lenient.stats.semantic_hits == 1  # wrong answer

    # 5. TTL expiry on an advanced fake clock, in BOTH tiers.
    clock = FakeClock()
    ttl_cache = SemanticCache(embedder, ttl=60.0, clock=clock)
    ttl_cache.put(AUDIT_Q, AUDIT_A)
    ttl_cache.put(PASSWORD_Q, PASSWORD_A)
    clock.advance(59.0)
    assert ttl_cache.get(AUDIT_Q) == AUDIT_A        # still inside the window
    clock.advance(2.0)
    assert ttl_cache.get(PASSWORD_Q) is None        # the exact path honours expiry
    assert ttl_cache.get(AUDIT_PARA) is None        # and so does the vector search
    assert len(ttl_cache) == 0
    ttl_cache.put(AUDIT_Q, AUDIT_A)
    clock.advance(40.0)
    ttl_cache.put(AUDIT_Q, AUDIT_A)                 # a rewrite re-arms the TTL
    clock.advance(40.0)
    assert ttl_cache.get(AUDIT_Q) == AUDIT_A        # would be dead on the old one

    # 6. LRU evicts the least recently USED, not the least recently inserted.
    #    Exact hit, semantic hit and rewrite all count as uses.
    WATER_Q = "What is the boiling point of water?"
    REGIONS_Q = "Which regions support GPU inference?"
    COST_Q = "How much does the enterprise plan cost?"
    lru = SemanticCache(embedder, capacity=3)
    lru.put(PASSWORD_Q, "A")
    lru.put(WATER_Q, "B")
    lru.put(AUDIT_Q, "C")
    assert lru.get(PASSWORD_Q) == "A"               # exact hit on the oldest write
    lru.put(COST_Q, "D")                            # evicts WATER, not PASSWORD
    assert len(lru) == 3 and lru.get(WATER_Q) is None
    assert lru.get(PASSWORD_Q) == "A"               # survives: recently used
    assert lru.get(AUDIT_PARA) == "C"               # a semantic hit is a use too,
    lru.put(REGIONS_Q, "E")                         # so this evicts COST, not AUDIT
    assert lru.get(AUDIT_Q) == "C" and lru.get(COST_Q) is None
    lru.put(PASSWORD_Q, "A2")                       # and so is a rewrite,
    lru.put("Where can I download the SDK?", "F")   # so this evicts REGIONS
    assert lru.get(PASSWORD_Q) == "A2" and lru.get(REGIONS_Q) is None

    # 7. Tag invalidation drops exactly the tagged entries. The paraphrase probe is
    #    the point: forget the vector store and the cache keeps answering from a
    #    document version that no longer says that.
    rag = SemanticCache(embedder)
    rag.put(AUDIT_Q, AUDIT_A, tags=("doc:42", "tenant:acme"))
    rag.put("Who signs off on audit log retention changes?", "The security lead.",
            tags=("doc:42",))
    rag.put(WATER_Q, "100 C at sea level.", tags=("doc:7",))
    rag.put(PASSWORD_Q, PASSWORD_A)                 # untagged, must survive
    assert rag.invalidate("doc:42") == 2 and len(rag) == 2
    assert rag.get(AUDIT_Q) is None and rag.get(AUDIT_PARA) is None
    assert rag.get(WATER_Q) == "100 C at sea level." and rag.get(PASSWORD_Q) == PASSWORD_A
    assert rag.invalidate("doc:42") == 0 and rag.invalidate("doc:7") == 1  # idempotent

    print("All tests passed.")
