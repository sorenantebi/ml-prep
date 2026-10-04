"""Challenge 18 - Constrained JSON Decoding with a Schema Walker (Hard)

PROBLEM
-------
Force a model to emit schema-conforming JSON by masking the logits at every
decoding step, so only grammatically valid tokens survive. The vocabulary is
character level, 42 tokens: digits 0-9, lowercase a-z (which also spell the
pieces of `true` and `false`), the characters " { } : , and one EOS token.

Implement:
    SchemaWalker(schema, max_str_len=8, max_int_digits=4)
        `schema` is flat, e.g. {"name": "string", "age": "integer",
        "active": "boolean"}, and the walker accepts exactly
            {"<key1>":<value1>,...,"<keyN>":<valueN>}<EOS>
        keys in schema order, no whitespace, string values of 1..max_str_len
        alphanumeric characters, integers with no leading zeros past a bare 0,
        booleans spelled one character at a time.
        allowed_next() -> set[int]  ids that keep a complete document
                                    reachable, empty only after EOS
        advance(token_id) -> None   consume a token, ValueError if illegal
    mask_logits(logits, allowed) -> np.ndarray
        copy of `logits` with disallowed entries at -inf, input untouched
    constrained_decode(model_fn, walker, max_len=64, rng=None) -> list[int]
        `model_fn(prefix_ids) -> np.ndarray` of shape (VOCAB_SIZE,). Sample from
        softmax(mask_logits(logits, walker.allowed_next())), advance, stop on
        EOS or max_len.

numpy and the standard library only. Mask the logits before the softmax, never
the probabilities after it.

INTERVIEW NOTES
---------------
A strong solution demonstrates:
- The grammar is the decoder. A flat schema is a regular language, so a DFA is
  enough, and so is any non-recursive schema with bounded nesting (it unrolls
  into a bigger regex). Recursive schemas and arbitrary JSON are not: matching
  arbitrarily deep braces needs a stack, so engines such as XGrammar and
  llguidance run a pushdown automaton or an Earley-style parser, while
  regex-first designs compile the regular parts to a DFA.
- Constrained decoding shifts the distribution. Renormalising onto the allowed
  set gives the model's conditional given validity, which is not its belief
  about good content: forcing a key order it did not want, or truncating a
  field, pushes it into low-probability regions and can hurt quality (reported
  mostly on reasoning tasks, and the evidence is mixed). Describing the schema
  in the prompt as well as masking keeps the two closer, and putting a free
  text reasoning field before the answer fields gives the model room to think.
- Cost awareness. The mask is a vocabulary-sized boolean per step, and at 100k+
  vocabularies rebuilding it per token is a visible slice of the step budget.
  Production systems cache masks per parser state, precompute the
  token-to-state transitions offline, and compute the next mask on the CPU
  while the GPU runs the forward pass, so the hot path is a lookup.
Common mistakes: masking after the softmax without renormalising, so the
probabilities no longer sum to 1; using 0.0 instead of -inf, which leaves
disallowed tokens weight exp(0) = 1; dead states, where a legal prefix has no
legal continuation, every logit is -inf and the softmax is NaN; allowing EOS
anywhere, so the model can stop mid-object; letting an integer field open with
a quote because the value grammar is not keyed off the declared type.
Follow-ups: nested objects and arrays with a state stack; regex-constrained
fields; multi-character (BPE) tokens, where one token straddles a grammar
boundary so the mask must be built over token strings; measuring the KL between
the constrained and unconstrained distributions to price the quality cost; why
"JSON mode" (any valid JSON) is weaker than schema-constrained structured
output, and what a hosted API still cannot guarantee (semantic correctness,
values that pass business rules).
"""

import copy
import json
from typing import Callable, Iterable

import numpy as np

# ------------------------------------------------------------------ vocabulary

_STRUCTURAL = ['"', "{", "}", ":", ","]
VOCAB: list[str] = ([str(d) for d in range(10)]
                    + [chr(c) for c in range(ord("a"), ord("z") + 1)]
                    + _STRUCTURAL + ["<eos>"])
TOKEN_TO_ID: dict[str, int] = {tok: i for i, tok in enumerate(VOCAB)}
VOCAB_SIZE = len(VOCAB)

EOS = TOKEN_TO_ID["<eos>"]
QUOTE, LBRACE, RBRACE, COLON, COMMA = (TOKEN_TO_ID[c] for c in _STRUCTURAL)
DIGITS = frozenset(TOKEN_TO_ID[str(d)] for d in range(10))
LETTERS = frozenset(TOKEN_TO_ID[chr(c)] for c in range(ord("a"), ord("z") + 1))
STR_CHARS = DIGITS | LETTERS


def decode_tokens(ids: Iterable[int]) -> str:
    return "".join("" if i == EOS else VOCAB[i] for i in ids)


def encode_text(text: str) -> list[int]:
    return [TOKEN_TO_ID[c] for c in text]


# ------------------------------------------------------------------ schema walker


class SchemaWalker:
    """DFA over a flat JSON schema: which token ids keep the output valid."""

    def __init__(self, schema: dict[str, str], max_str_len: int = 8,
                 max_int_digits: int = 4) -> None:
        bad_type = any(t not in ("string", "integer", "boolean") for t in schema.values())
        bad_key = any(not k or any(TOKEN_TO_ID.get(c, -1) not in LETTERS for c in k)
                      for k in schema)
        if not schema or bad_type or bad_key:
            raise ValueError("need lowercase keys and string/integer/boolean types")
        self.schema, self.keys = dict(schema), list(schema)
        self.max_str_len, self.max_int_digits = max_str_len, max_int_digits
        self.reset()

    def reset(self) -> None:
        self.state = "start"   # position in the grammar
        self.field = 0         # index into self.keys
        self.pos = 0           # offset inside a key or a boolean literal
        self.count = 0         # characters emitted in the current value
        self.literal = ""      # boolean literal committed to by its first char
        self.zero = False      # the integer value opened with a bare 0
        self.tokens: list[int] = []

    def state_key(self) -> tuple:
        """Identity of the DFA state, ignoring the token history."""
        return (self.state, self.field, self.pos, self.count, self.literal, self.zero)

    @property
    def done(self) -> bool:
        return self.state == "done"

    def allowed_next(self) -> set[int]:
        s = self.state
        # After a value: a comma if fields remain, otherwise the closing brace.
        sep = {COMMA} if self.field < len(self.keys) - 1 else {RBRACE}
        if s == "start":
            return {LBRACE}
        if s in ("key_quote", "str_open"):
            return {QUOTE}
        if s == "key_chars":
            key = self.keys[self.field]
            return {TOKEN_TO_ID[key[self.pos]]} if self.pos < len(key) else {QUOTE}
        if s == "colon":
            return {COLON}
        if s == "str_body":
            chars = STR_CHARS if self.count < self.max_str_len else set()
            return set(chars) | ({QUOTE} if self.count else set())  # no empty strings
        if s == "int_body":
            more = self.count < self.max_int_digits and not self.zero
            return (set(DIGITS) if self.count == 0 or more else set()) | (
                sep if self.count else set())
        if s == "bool_body":
            if not self.literal:
                return {TOKEN_TO_ID["t"], TOKEN_TO_ID["f"]}
            return ({TOKEN_TO_ID[self.literal[self.pos]]}
                    if self.pos < len(self.literal) else sep)
        if s == "sep":
            return sep
        return {EOS} if s == "end" else set()   # "done": nothing follows EOS

    def advance(self, token_id: int) -> None:
        if token_id not in self.allowed_next():
            raise ValueError(f"token {VOCAB[token_id]!r} illegal in state {self.state!r}")
        self.tokens.append(token_id)
        s, closing = self.state, token_id == QUOTE
        if s in ("start", "key_quote"):
            self.state, self.pos = "key_chars" if s == "key_quote" else "key_quote", 0
        elif s == "key_chars":
            self.state, self.pos = ("colon", 0) if closing else (s, self.pos + 1)
        elif s == "colon":
            self.state = {"string": "str_open", "integer": "int_body",
                          "boolean": "bool_body"}[self.schema[self.keys[self.field]]]
            self.count, self.pos, self.literal, self.zero = 0, 0, "", False
        elif s == "str_open":
            self.state = "str_body"
        elif s == "str_body":
            self.state, self.count = ("sep", 0) if closing else (s, self.count + 1)
        elif s == "int_body":
            if token_id in DIGITS:
                self.zero = self.count == 0 and token_id == TOKEN_TO_ID["0"]
                self.count += 1
            else:
                self._separator(token_id)
        elif s == "bool_body":
            if not self.literal:
                self.literal = "true" if token_id == TOKEN_TO_ID["t"] else "false"
                self.pos = 1
            elif self.pos < len(self.literal):
                self.pos += 1
            else:
                self._separator(token_id)
        elif s == "sep":
            self._separator(token_id)
        elif s == "end":
            self.state = "done"

    def _separator(self, token_id: int) -> None:
        self.count, self.pos, self.literal, self.zero = 0, 0, "", False
        if token_id == COMMA:
            self.field, self.state = self.field + 1, "key_quote"
        else:
            self.state = "end"


# ------------------------------------------------------------------ masked sampling


def mask_logits(logits: np.ndarray, allowed: Iterable[int]) -> np.ndarray:
    out = np.array(logits, dtype=np.float64, copy=True)
    keep = np.zeros(out.shape, dtype=bool)
    for token_id in allowed:
        keep[token_id] = True
    out[~keep] = -np.inf
    return out


def softmax(x: np.ndarray) -> np.ndarray:
    finite = x[np.isfinite(x)]
    if finite.size == 0:
        raise ValueError("every token is masked out: the walker is in a dead state")
    e = np.exp(x - finite.max())                # exp(-inf) is exactly 0.0
    return e / e.sum()


def constrained_decode(model_fn: Callable[[list[int]], np.ndarray], walker: SchemaWalker,
                       max_len: int = 64,
                       rng: np.random.Generator | None = None) -> list[int]:
    rng = np.random.default_rng(0) if rng is None else rng
    out: list[int] = []
    for _ in range(max_len):
        allowed = walker.allowed_next()
        if not allowed:
            break
        probs = softmax(mask_logits(np.asarray(model_fn(out), dtype=np.float64), allowed))
        token_id = int(rng.choice(VOCAB_SIZE, p=probs))
        out.append(token_id)
        walker.advance(token_id)
        if token_id == EOS:
            break
    return out


if __name__ == "__main__":
    SCHEMA = {"name": "string", "age": "integer", "active": "boolean"}
    WANT = {"string": str, "integer": int, "boolean": bool}

    def conforms(text: str) -> bool:
        """Parses as JSON, keys in schema order, values of the declared types."""
        try:
            pairs = json.loads(text, object_pairs_hook=list)
        except Exception:
            return False
        return (isinstance(pairs, list) and [k for k, _ in pairs] == list(SCHEMA)
                # bool subclasses int, so compare the exact type.
                and all(type(v) is WANT[t] for (_, v), t in zip(pairs, SCHEMA.values())))

    def is_json(text: str) -> bool:
        try:
            json.loads(text)
        except Exception:
            return False
        return True

    def noise_model(seed: int) -> Callable[[list[int]], np.ndarray]:
        gen = np.random.default_rng(seed)
        return lambda prefix: gen.uniform(-5.0, 5.0, VOCAB_SIZE)

    def walk(prefix: str, schema: dict = SCHEMA, **kw) -> SchemaWalker:
        walker = SchemaWalker(schema, **kw)
        for token_id in encode_text(prefix):
            walker.advance(token_id)
        return walker

    # 1. THE KILLER TEST: pure noise in, schema-conforming JSON out. The same
    #    sampler on the same seeds without the mask never conforms, and its
    #    output is rarely even JSON.
    free_conforming = free_parsed = 0
    for trial in range(500):
        ids = constrained_decode(noise_model(1000 + trial), SchemaWalker(SCHEMA),
                                 max_len=64, rng=np.random.default_rng(trial))
        assert ids[-1] == EOS, f"trial {trial} hit max_len: {decode_tokens(ids)!r}"
        assert conforms(decode_tokens(ids)), f"trial {trial}: {decode_tokens(ids)!r}"
        model, rng, free = noise_model(1000 + trial), np.random.default_rng(trial), []
        while len(free) < 64 and EOS not in free:
            free.append(int(rng.choice(VOCAB_SIZE, p=softmax(model(free)))))
        free_conforming += conforms(decode_tokens(free))
        free_parsed += is_json(decode_tokens(free))
    assert free_conforming == 0, "unconstrained sampling should never hit the schema"
    assert free_parsed <= 5, "random text should almost never parse as JSON at all"

    # 2. No dead states: exhaustive walk of the DFA, every live state has a move.
    start = SchemaWalker(SCHEMA)
    seen, frontier, terminal = {start.state_key()}, [start], 0
    while frontier:
        walker = frontier.pop()
        allowed = walker.allowed_next()
        if walker.done:
            terminal += 1
            assert not allowed
            continue
        assert allowed, f"dead state: {walker.state_key()}"
        probs = softmax(mask_logits(np.zeros(VOCAB_SIZE), allowed))  # NaN if all -inf
        assert np.count_nonzero(probs) == len(allowed)
        assert abs(probs.sum() - 1.0) < 1e-12
        for token_id in allowed:
            nxt = copy.deepcopy(walker)
            nxt.advance(token_id)
            if nxt.state_key() not in seen:
                seen.add(nxt.state_key())
                frontier.append(nxt)
    assert terminal == 1 and len(seen) > 30     # the DFA really was explored

    # 3. Required keys come out in schema order, and the value grammar is keyed
    #    off the declared type: an integer field cannot open with a quote.
    letter = TOKEN_TO_ID
    for prefix, want in [
            ("", {LBRACE}),
            ('{', {QUOTE}),
            ('{"', {letter["n"]}),                        # only "name" may start
            ('{"name":"', set(STR_CHARS)),                # no empty string values
            ('{"name":"bob","', {letter["a"]}),           # then "age", not "active"
            ('{"name":"bob","age":', set(DIGITS)),        # no quote, no letter, no EOS
            ('{"name":"bob","age":0', {COMMA}),           # bare 0 cannot grow to 07
            ('{"name":"bob","age":41,"active":', {letter["t"], letter["f"]}),
            ('{"name":"bob","age":41,"active":f', {letter["a"]}),   # literal forced
            ('{"name":"bob","age":41,"active":false', {RBRACE}),
            ('{"name":"bob","age":41,"active":false}', {EOS})]:     # EOS only at the end
        assert walk(prefix).allowed_next() == want, prefix
    for prefix, bad in [('{"', "a"), ('{"name":"bob","age":', '"'), ('{"name', "}")]:
        try:
            walk(prefix).advance(TOKEN_TO_ID[bad])
            assert False, f"accepted {bad!r} after {prefix!r}"
        except ValueError:
            pass
    done = walk('{"name":"bob","age":41,"active":false}')
    done.advance(EOS)
    assert done.done and done.allowed_next() == set()

    # 4. A model desperate to stop early is still held to the schema.
    def eager_eos(prefix: list[int]) -> np.ndarray:
        logits = np.full(VOCAB_SIZE, -10.0)
        logits[EOS], logits[RBRACE] = 50.0, 40.0
        return logits

    ids = constrained_decode(eager_eos, SchemaWalker(SCHEMA),
                             rng=np.random.default_rng(7))
    assert conforms(decode_tokens(ids)) and decode_tokens(ids).startswith('{"name":"')

    # 5. Masking happens on the logits, before the softmax: the masked
    #    distribution is exactly the original conditioned on the allowed set.
    logits = np.random.default_rng(11).normal(0.0, 3.0, VOCAB_SIZE)
    allowed = sorted(walk('{"name":"a').allowed_next())
    blocked = sorted(set(range(VOCAB_SIZE)) - set(allowed))
    assert blocked, "this state must block something for the test to mean anything"
    masked_probs, full = softmax(mask_logits(logits, allowed)), softmax(logits)
    assert np.allclose(masked_probs[allowed], full[allowed] / full[allowed].sum())
    assert np.all(masked_probs[blocked] == 0.0) and abs(masked_probs.sum() - 1.0) < 1e-12
    # Zeroing probabilities after the softmax leaves an unnormalised vector; only
    # renormalising recovers the same conditional.
    post_hoc = full.copy()
    post_hoc[blocked] = 0.0
    assert post_hoc.sum() < 1.0 - 1e-6
    assert np.allclose(post_hoc / post_hoc.sum(), masked_probs)
    # Masking with 0.0 instead of -inf leaves blocked tokens weight exp(0) = 1.
    # Shown on the integer state, where only the ten digits are legal.
    int_allowed = sorted(walk('{"name":"a","age":').allowed_next())
    int_blocked = sorted(set(range(VOCAB_SIZE)) - set(int_allowed))
    flat = np.full(VOCAB_SIZE, -2.0)
    flat[TOKEN_TO_ID["7"]] = 1.0
    zeroed = flat.copy()
    zeroed[int_blocked] = 0.0
    assert softmax(zeroed)[int_blocked].sum() > 0.8   # most mass escapes the grammar
    assert softmax(mask_logits(flat, int_allowed))[int_blocked].sum() == 0.0
    before = logits.copy()
    mask_logits(logits, allowed)
    assert np.array_equal(logits, before)             # mask_logits does not mutate

    # 6. Other schemas: a lone boolean, and a tighter string budget.
    ids = constrained_decode(noise_model(3), SchemaWalker({"ok": "boolean"}),
                             max_len=32, rng=np.random.default_rng(5))
    assert decode_tokens(ids) in ('{"ok":true}', '{"ok":false}'), decode_tokens(ids)
    assert walk('{"tag":"ab', {"tag": "string"}, max_str_len=2).allowed_next() == {QUOTE}

    print("All tests passed.")
