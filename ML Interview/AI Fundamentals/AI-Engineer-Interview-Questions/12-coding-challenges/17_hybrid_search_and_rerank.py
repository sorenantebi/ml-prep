"""Challenge 17 - Hybrid Search: BM25, Reciprocal Rank Fusion, MMR (Medium)

PROBLEM
-------
Dense retrieval tends to miss exact identifiers (error codes, SKUs, function
names). Lexical retrieval misses paraphrases. Hybrid search runs both and
fuses the results. Implement the three pieces.

1. bm25_scores(query_tokens, corpus_tokens, k1=1.5, b=0.75) -> np.ndarray
   Okapi BM25 over pre-tokenized documents, one score per document:
       score(d) = sum_t idf(t) * tf(t,d) * (k1 + 1)
                  / (tf(t,d) + k1 * (1 - b + b * len(d) / avgdl))
       idf(t) = ln(1 + (N - df(t) + 0.5) / (df(t) + 0.5))   non-negative form
   Unseen terms contribute nothing, a term repeated in the query counts once,
   b controls length normalization, k1 sets how fast tf saturates.

2. reciprocal_rank_fusion(rankings, k=60) -> list[int]
   Fuse ranked id lists from independent retrievers, ranks counting from 1:
       rrf(d) = sum over lists of 1 / (k + rank(d))
   A document missing from a list contributes nothing from that list. Return
   doc ids best first, ties broken by id so the output is deterministic.

3. mmr(query_vec, doc_vecs, candidate_ids, lambda_=0.5, k=5) -> list[int]
   Maximal Marginal Relevance re-ranking. Greedily pick the candidate that
   maximises, until k are chosen:
       lambda_ * sim(q, d) - (1 - lambda_) * max sim(d, s) over selected s
   Rows of doc_vecs are L2-normalized, so sim is a dot product. The first pick
   has an empty selected set and falls back to pure query similarity.

The dense side reuses the hashed n-gram embedder from the semantic search
challenge, so the whole thing runs on numpy alone.

INTERVIEW NOTES
---------------
A strong solution demonstrates:
- Why the "+ 1" idf variant matters: the classic Robertson idf goes negative
  once a term is in more than half the corpus, so containing it can rank a
  document below one that does not.
- What the knobs do. b=0 switches length normalization off, and tf saturates at
  idf * (k1 + 1) however often a term repeats, unlike cosine over raw counts.
- That RRF fuses ranks, not scores: a BM25 score of 3.0 and a cosine of 0.4 are
  not comparable, and any weighted sum re-scores the corpus the moment either
  scorer is recalibrated. k damps each list's head, so a small k lets one
  rank-1 vote dominate while k=60 (the value from Cormack et al., 2009)
  rewards consensus. RRF is the zero-tuning default, not the ceiling: with
  labelled queries, a tuned convex combination of normalised scores can beat
  it, at the cost of re-tuning whenever a scorer changes.
- That MMR is greedy, trades relevance against redundancy, and collapses to
  plain top-k at lambda_=1.0, which is the cheapest way to test it.
Common mistakes: idf that can go negative; forgetting avgdl so long documents
win; recomputing document frequency per document instead of once per term; RRF
summing similarities instead of reciprocal ranks; MMR measuring redundancy
against the mean of the selected set rather than the max, which lets a cluster
in by attrition. Follow-ups: weighted RRF when one retriever is stronger; a
cross-encoder second stage over the fused top-50, and its latency budget;
per-field BM25 weights (BM25F); learned sparse retrieval such as SPLADE as the
lexical leg; whether MMR runs before or after the reranker, and which
relevance score it should then use.
"""

import math
import re
import zlib
from collections import Counter, defaultdict

import numpy as np


class HashedNGramEmbedder:
    """Deterministic mock embedding: hashed character n-grams, L2-normalized."""

    def __init__(self, dim: int = 256, n: int = 3):
        self.dim, self.n = dim, n

    def embed(self, text: str) -> np.ndarray:
        text = f" {' '.join(text.lower().split())} "   # normalize, mark boundaries
        vec = np.zeros(self.dim)
        for i in range(max(len(text) - self.n + 1, 0)):
            h = zlib.crc32(text[i:i + self.n].encode("utf-8"))  # stable across runs
            vec[h % self.dim] += 1.0 if (h >> 31) & 1 else -1.0
        norm = np.linalg.norm(vec)
        return vec / norm if norm > 0 else vec

    def embed_batch(self, texts: list[str]) -> np.ndarray:
        return np.stack([self.embed(t) for t in texts])


def tokenize(text: str) -> list[str]:
    """Lowercase alphanumeric runs. No stemming, which is the point of test 2b."""
    return re.findall(r"[a-z0-9]+", text.lower())


def bm25_idf(n_docs: int, df: int) -> float:
    """Non-negative inverse document frequency, as used by Lucene."""
    return math.log(1.0 + (n_docs - df + 0.5) / (df + 0.5))


def bm25_scores(query_tokens: list[str], corpus_tokens: list[list[str]],
                k1: float = 1.5, b: float = 0.75) -> np.ndarray:
    n_docs = len(corpus_tokens)
    if n_docs == 0:
        return np.zeros(0)
    lengths = np.array([len(doc) for doc in corpus_tokens], dtype=float)
    avgdl = float(lengths.mean())
    counts = [Counter(doc) for doc in corpus_tokens]
    # The length factor carries no term, so hoist it out of the term loop.
    norm = k1 * (1 - b + b * (lengths / avgdl if avgdl > 0 else np.ones(n_docs)))
    scores = np.zeros(n_docs)
    for term in dict.fromkeys(query_tokens):        # dedupe, insertion ordered
        df = sum(1 for c in counts if term in c)
        if df == 0:
            continue                                # unseen term adds nothing
        tf = np.array([c.get(term, 0) for c in counts], dtype=float)
        scores += bm25_idf(n_docs, df) * tf * (k1 + 1) / (tf + norm)
    return scores


def rank_by_score(scores: np.ndarray) -> list[int]:
    """Doc ids a retriever would return: positive scores only, best first."""
    # A zero BM25 score means no query term hit the posting list, so the
    # document was never retrieved and must not enter the fusion at all.
    order = sorted(range(len(scores)), key=lambda i: (-scores[i], i))
    return [i for i in order if scores[i] > 0]


def reciprocal_rank_fusion(rankings: list[list[int]], k: int = 60) -> list[int]:
    fused: dict[int, float] = defaultdict(float)
    for ranking in rankings:
        for rank, doc_id in enumerate(ranking, start=1):
            fused[doc_id] += 1.0 / (k + rank)
    return sorted(fused, key=lambda doc_id: (-fused[doc_id], doc_id))


def mmr(query_vec: np.ndarray, doc_vecs: np.ndarray, candidate_ids: list[int],
        lambda_: float = 0.5, k: int = 5) -> list[int]:
    if not 0.0 <= lambda_ <= 1.0:
        raise ValueError("lambda_ must be in [0, 1]")
    cands = list(candidate_ids)
    k = min(k, len(cands))
    if k == 0:
        return []
    vecs = doc_vecs[cands]
    sim_q = vecs @ query_vec          # relevance, computed once
    sim_dd = vecs @ vecs.T            # redundancy, computed once
    selected: list[int] = []          # positions within `cands`
    remaining = list(range(len(cands)))
    while len(selected) < k:
        if not selected:
            objective = sim_q[remaining]         # empty max term, pure relevance
        else:
            redundancy = sim_dd[np.ix_(remaining, selected)].max(axis=1)
            objective = lambda_ * sim_q[remaining] - (1 - lambda_) * redundancy
        best = remaining[int(np.argmax(objective))]   # argmax breaks ties leftward
        selected.append(best)
        remaining.remove(best)
    return [cands[pos] for pos in selected]


# A support knowledge base. Doc 0 is the only page for E4021, doc 1 is a decoy
# an n-gram embedder loves, doc 6 answers the throttling question in words that
# query never uses, and docs 12 to 14 are near-duplicates of each other.
CORPUS = [
    "E4021 is the error you get when one uploaded file is larger than the limit "
    "your plan allows for a single upload.",
    "Errors and codes E4020 and E4022 are reserved and never sent to clients.",
    "Every failed response carries a machine readable code and a request id you "
    "can quote in a support ticket.",
    "The status code alone rarely explains a failure, so read the message next to it.",
    "Our reference table maps each code prefix to the team that owns it.",
    "The log rotates daily, which keeps an error hunt from becoming an archaeology dig.",
    "The client throttles each retry so a flaky upload never floods the server.",
    "Exponential backoff spreads repeated calls out over a widening window.",
    "Set a per-file size limit in the console before you enable public sharing.",
    "Streaming a response token by token cuts the time to first byte.",
    "Batch small calls together to stay under the per-minute quota.",
    "A code review is required before any change reaches the release branch.",
    "Rotate your API key from the dashboard every ninety days.",
    "Rotate your API key from the dashboard every 90 days.",
    "Rotate the API key from the dashboard at least every ninety days.",
]


if __name__ == "__main__":
    EMBEDDER = HashedNGramEmbedder(dim=256, n=3)
    CORPUS_TOKENS = [tokenize(doc) for doc in CORPUS]
    DOC_VECS = EMBEDDER.embed_batch(CORPUS)
    GOLD_CODE, DECOY, GOLD_PARAPHRASE, DUPES = 0, 1, 6, {12, 13, 14}

    # 1. BM25 against the formula written out by hand.
    tiny = [["a", "b"], ["a", "a", "c", "d"]]
    k1, b, avgdl = 1.5, 0.75, 3.0
    idf_a = math.log(1 + (2 - 2 + 0.5) / (2 + 0.5))
    assert np.allclose(bm25_scores(["a"], tiny), [
        idf_a * 1 * (k1 + 1) / (1 + k1 * (1 - b + b * 2 / avgdl)),
        idf_a * 2 * (k1 + 1) / (2 + k1 * (1 - b + b * 4 / avgdl))])
    assert np.all(bm25_scores(["zzz"], tiny) == 0.0)               # unseen term
    # A term repeated in the query is one clause, not two.
    assert np.allclose(bm25_scores(["a", "a"], tiny), bm25_scores(["a"], tiny))

    # idf stays non-negative for a term in every document, so containing the term
    # is never worse than lacking it. Robertson idf here is log(0.5 / 3.5) < 0.
    universal = [["the", "error", "log"], ["the", "code"], ["the", "quota", "the"]]
    assert bm25_idf(3, 1) > bm25_idf(3, 2) > bm25_idf(3, 3) > 0.0
    assert np.all(bm25_scores(["the"], universal) > bm25_scores(["gone"], universal))

    # Length normalization, and term frequency saturating at idf * (k1 + 1).
    pair = [["x", "y"], ["x"] + ["y"] * 9]
    same_tf, flat = bm25_scores(["x"], pair), bm25_scores(["x"], pair, b=0.0)
    assert same_tf[0] > same_tf[1] and abs(flat[0] - flat[1]) < 1e-12
    once, many = bm25_scores(["x"], [["x"]])[0], bm25_scores(["x"], [["x"] * 50])[0]
    assert once < many < bm25_idf(1, 1) * (k1 + 1) and many < 50 * once

    # 2. The argument for hybrid search, on one corpus. Exact identifier: BM25
    #    wins on a rare token, the embedder is fooled by the neighbouring code
    #    numbers in doc 1 and ranks the gold page second.
    lex = bm25_scores(tokenize("error code E4021"), CORPUS_TOKENS)
    dense = DOC_VECS @ EMBEDDER.embed("error code E4021")
    lex_rank, dense_rank = rank_by_score(lex), rank_by_score(dense)
    assert lex_rank[0] == GOLD_CODE and lex[GOLD_CODE] > 1.5 * lex[lex_rank[1]]
    assert dense_rank[0] == DECOY and dense_rank[1] == GOLD_CODE
    assert reciprocal_rank_fusion([lex_rank, dense_rank])[0] == GOLD_CODE

    # Pure paraphrase: "throttling retried uploads" shares no token with any
    # document, so BM25 retrieves nothing, while the embedder still matches
    # throttles / retry / upload on character n-grams. RRF wins both ways.
    lex_p = bm25_scores(tokenize("throttling retried uploads"), CORPUS_TOKENS)
    dense_p = rank_by_score(DOC_VECS @ EMBEDDER.embed("throttling retried uploads"))
    assert np.all(lex_p == 0.0) and rank_by_score(lex_p) == []
    assert dense_p[0] == GOLD_PARAPHRASE
    assert reciprocal_rank_fusion([rank_by_score(lex_p), dense_p])[0] == GOLD_PARAPHRASE

    # 3. RRF reads ranks, so a monotone rescaling of either scorer leaves the
    #    fusion untouched. A raw score sum does not survive the same treatment.
    baseline = reciprocal_rank_fusion([lex_rank, dense_rank])
    scaled_lex = rank_by_score(np.sqrt(lex) * 100.0)     # monotone, fixes zero
    scaled_dense = rank_by_score(dense ** 3)             # monotone, sign preserving
    for two_lists in ([scaled_lex, dense_rank], [lex_rank, scaled_dense],
                      [scaled_lex, scaled_dense]):
        assert reciprocal_rank_fusion(two_lists) == baseline
    assert int(np.argmax(lex + dense)) == GOLD_CODE
    assert int(np.argmax(lex + 100 * dense)) == DECOY    # same ranks, wrong answer

    # 4. RRF arithmetic: agreement beats one strong vote, and k decides how much
    #    the head of each list is favoured.
    lists = [[0, 1, 2, 3, 4], [4, 1, 3, 2, 0]]
    assert reciprocal_rank_fusion(lists) == [1, 0, 4, 2, 3]   # 1/62+1/62 > 1/61+1/65
    assert reciprocal_rank_fusion(lists, k=0)[0] == 0         # 1/1+1/5 dominates
    assert reciprocal_rank_fusion(lists, k=0).index(1) == 2   # consensus demoted
    assert reciprocal_rank_fusion([[7], []]) == [7] and reciprocal_rank_fusion([]) == []

    # 5. MMR on the same corpus. Docs 12 to 14 state one fact three ways, so
    #    plain top-k spends the whole context window on it. lambda_=1.0 drops the
    #    redundancy term and must reproduce that top-k exactly.
    key_query = EMBEDDER.embed("how often should I rotate the api key")
    candidates, sims = list(range(len(CORPUS))), DOC_VECS @ key_query
    plain_top3 = sorted(candidates, key=lambda i: (-sims[i], i))[:3]
    assert set(plain_top3) == DUPES
    assert mmr(key_query, DOC_VECS, candidates, lambda_=1.0, k=3) == plain_top3

    # lambda_=0.0 optimises for diversity alone: one member of the cluster, then
    # the documents least like it. lambda_=0.5 still leads with the best match.
    diverse = mmr(key_query, DOC_VECS, candidates, lambda_=0.0, k=3)
    assert len(set(diverse) & DUPES) == 1 and len(set(diverse)) == 3
    balanced = mmr(key_query, DOC_VECS, candidates, lambda_=0.5, k=3)
    assert balanced[0] == plain_top3[0] and len(set(balanced) & DUPES) == 1

    # 6. Redundancy is a max over the selected set, not a mean. Unit rows: doc 3
    #    duplicates doc 0 (cosine 0.9) but is unlike the rest, while doc 4 is
    #    mildly similar to all three picks. max rejects doc 3, a mean would not.
    geo = np.array([[1.0, 0, 0, 0], [0, 1.0, 0, 0], [0, 0, 1.0, 0],
                    [0.9, 0, 0, math.sqrt(0.19)],
                    [0.35, 0.35, 0.35, math.sqrt(1 - 3 * 0.35 ** 2)]])
    assert mmr(geo[0], geo, [0, 1, 2, 3, 4], lambda_=0.0, k=4) == [0, 1, 2, 4]

    # 7. Candidate set respected, k clamped, lambda_ validated.
    subset = mmr(key_query, DOC_VECS, [1, 3, 5], lambda_=0.5, k=2)
    assert set(subset) <= {1, 3, 5} and len(subset) == 2
    assert len(mmr(key_query, DOC_VECS, [0, 3], k=9)) == 2
    assert mmr(key_query, DOC_VECS, [], k=3) == []
    try:
        mmr(key_query, DOC_VECS, candidates, lambda_=1.5); assert False
    except ValueError:
        pass

    print("All tests passed.")
