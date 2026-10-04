"""Challenge 11 - Token-Bucket Rate Limiter + Retry with Backoff (Medium)

PROBLEM
-------
LLM APIs throttle you (HTTP 429). Implement the two client-side primitives
every production caller needs, designed for deterministic testing:

1. TokenBucket(capacity, refill_rate, clock=time.monotonic)
     - starts full; refills continuously at `refill_rate` tokens/second,
       capped at `capacity`
     - try_acquire(tokens=1) -> bool          (non-blocking)
     - time_until_available(tokens=1) -> float seconds
     - both raise ValueError if tokens > capacity: no wait can satisfy it
     - `clock` is injectable so tests can use fake time.

2. RateLimitError(retry_after: float | None = None) - exception carrying the
   server's optional Retry-After hint.

3. retry(max_attempts=5, base_delay=1.0, max_delay=30.0,
         retryable=(RateLimitError,), sleep=time.sleep, rng=random.random)
     - decorator implementing exponential backoff with FULL jitter:
           delay = rng() * min(max_delay, base_delay * 2**attempt)
     - if the caught exception has retry_after set, wait at least that long
     - re-raise the last exception after max_attempts failures
     - `sleep` and `rng` are injectable for tests.

INTERVIEW NOTES
---------------
A strong solution demonstrates:
- Lazy refill (compute elapsed * rate on access) instead of a background
  thread - simpler, exact, and trivially testable.
- Why FULL jitter: deterministic exponential backoff synchronizes retries of
  many clients into thundering-herd waves; sampling uniformly in [0, cap]
  decorrelates them (the classic AWS Architecture Blog result).
- Honouring Retry-After: the server knows its window, and retrying inside it
  burns attempts on guaranteed 429s, so take max(hint, jittered delay). Real
  headers may carry seconds or an HTTP-date; parse both.
- LLM limits are usually two buckets, requests per minute AND tokens per
  minute. try_acquire(tokens=n) exists so one bucket can be charged the
  request's estimated prompt plus max output tokens, not just 1 per call.
- Dependency injection of clock/sleep/rng - the difference between a test
  suite that runs in milliseconds and one that actually sleeps.
Common mistakes: sleeping before the FIRST attempt; off-by-one so the code
sleeps after the final failure; int token counts that leak fractional refill;
jitter as +/- 10% of a fixed delay (barely decorrelates); no max_delay cap,
so with a 1 s base the 13th retry may wait over an hour (cap 2**12 s);
a request larger than `capacity`, which no amount of waiting can satisfy and
which must fail fast rather than loop on 429s;
retrying non-idempotent side effects (a tool call that already fired) as if
they were reads.
Follow-ups: make the bucket thread-safe; add an async variant; distributed
limiting across processes (Redis + Lua); a retry budget or circuit breaker so
a sustained outage does not multiply load by max_attempts; read the
provider's remaining-requests and remaining-tokens response headers (names
vary by provider) to throttle proactively instead of reactively.
"""

import functools
import random
import time
from typing import Callable


class RateLimitError(Exception):
    """Client-visible 429. May carry the server's Retry-After hint (seconds)."""

    def __init__(self, message: str = "rate limited", retry_after: float | None = None):
        super().__init__(message)
        self.retry_after = retry_after


class TokenBucket:
    def __init__(self, capacity: float, refill_rate: float,
                 clock: Callable[[], float] = time.monotonic):
        if capacity <= 0 or refill_rate <= 0:
            raise ValueError("capacity and refill_rate must be positive")
        self.capacity = float(capacity)
        self.refill_rate = float(refill_rate)
        self.clock = clock
        self._tokens = float(capacity)  # start full: allows an initial burst
        self._last = clock()

    def _refill(self) -> None:
        now = self.clock()
        self._tokens = min(self.capacity, self._tokens + (now - self._last) * self.refill_rate)
        self._last = now

    def _check(self, tokens: float) -> None:
        if tokens > self.capacity:
            raise ValueError(f"{tokens} tokens can never fit a bucket of {self.capacity}")

    def try_acquire(self, tokens: float = 1.0) -> bool:
        self._check(tokens)
        self._refill()
        if self._tokens >= tokens:
            self._tokens -= tokens
            return True
        return False

    def time_until_available(self, tokens: float = 1.0) -> float:
        self._check(tokens)
        self._refill()
        return max(0.0, (tokens - self._tokens) / self.refill_rate)


def retry(max_attempts: int = 5, base_delay: float = 1.0, max_delay: float = 30.0,
          retryable: tuple[type[Exception], ...] = (RateLimitError,),
          sleep: Callable[[float], None] = time.sleep,
          rng: Callable[[], float] = random.random):
    """Exponential backoff with full jitter; honours exc.retry_after if present."""
    if max_attempts < 1:
        raise ValueError("max_attempts must be >= 1")

    def decorator(fn: Callable) -> Callable:
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return fn(*args, **kwargs)
                except retryable as exc:
                    if attempt == max_attempts - 1:
                        raise  # exhausted: surface the last error
                    cap = min(max_delay, base_delay * (2 ** attempt))
                    delay = rng() * cap  # full jitter: uniform in [0, cap]
                    hint = getattr(exc, "retry_after", None)
                    if hint is not None:
                        delay = max(delay, hint)
                    sleep(delay)
        return wrapper
    return decorator


class FakeClock:
    """Deterministic monotonic clock for tests."""

    def __init__(self, start: float = 0.0):
        self.t = start

    def __call__(self) -> float:
        return self.t

    def advance(self, dt: float) -> None:
        self.t += dt


if __name__ == "__main__":
    # 1. Bucket allows an initial burst, then throttles until refill.
    clock = FakeClock()
    bucket = TokenBucket(capacity=5, refill_rate=1.0, clock=clock)
    assert all(bucket.try_acquire() for _ in range(5)), "burst up to capacity"
    assert not bucket.try_acquire(), "6th immediate request must be rejected"
    assert abs(bucket.time_until_available() - 1.0) < 1e-9
    clock.advance(2.0)                       # refills 2 tokens
    assert bucket.try_acquire() and bucket.try_acquire()
    assert not bucket.try_acquire()
    clock.advance(100.0)                     # refill is capped at capacity
    assert sum(bucket.try_acquire() for _ in range(10)) == 5

    # 2. Retry succeeds after N simulated 429s; sleeps recorded, no real time.
    sleeps: list[float] = []
    attempts = {"n": 0}

    @retry(max_attempts=5, base_delay=1.0, max_delay=30.0,
           sleep=sleeps.append, rng=lambda: 0.5)
    def flaky() -> str:
        attempts["n"] += 1
        if attempts["n"] <= 3:
            raise RateLimitError()
        return "ok"

    assert flaky() == "ok"
    assert attempts["n"] == 4
    assert sleeps == [0.5, 1.0, 2.0]         # rng=0.5 -> half of caps 1, 2, 4

    # 3. Full jitter stays within [0, min(max_delay, base * 2**attempt)].
    sleeps.clear()
    r = random.Random(1234)
    always_429 = retry(max_attempts=6, base_delay=1.0, max_delay=4.0,
                       sleep=sleeps.append, rng=r.random)(
        lambda: (_ for _ in ()).throw(RateLimitError()))
    try:
        always_429()
        assert False, "must raise after exhausting attempts"
    except RateLimitError:
        pass
    assert len(sleeps) == 5, "no sleep after the final attempt"
    for attempt, d in enumerate(sleeps):
        assert 0.0 <= d <= min(4.0, 2.0 ** attempt)

    # 4. Retry-After hint is honoured as a floor on the delay.
    sleeps.clear()
    calls = {"n": 0}

    @retry(max_attempts=3, base_delay=1.0, sleep=sleeps.append, rng=lambda: 0.0)
    def hinted() -> str:
        calls["n"] += 1
        if calls["n"] == 1:
            raise RateLimitError(retry_after=7.5)
        return "ok"

    assert hinted() == "ok"
    assert sleeps == [7.5], "jitter said 0.0 but server hint must win"

    # 5. Integration: retry drives fake time forward until the bucket refills.
    clock = FakeClock()
    bucket = TokenBucket(capacity=1, refill_rate=0.5, clock=clock)  # 1 token / 2s

    def guarded_api() -> str:
        if not bucket.try_acquire():
            raise RateLimitError(retry_after=bucket.time_until_available())
        return "response"

    call = retry(max_attempts=4, base_delay=0.1, sleep=clock.advance,
                 rng=lambda: 0.0)(guarded_api)
    assert call() == "response"              # consumes the only token at t=0
    assert call() == "response"              # 429 -> waits retry_after -> succeeds
    assert abs(clock.t - 2.0) < 1e-9

    # 6. Non-retryable exceptions propagate immediately: one call, no sleep.
    sleeps.clear()
    boom_calls = {"n": 0}

    @retry(max_attempts=5, sleep=sleeps.append)
    def boom() -> None:
        boom_calls["n"] += 1
        raise KeyError("nope")

    try:
        boom()
        assert False, "KeyError must propagate"
    except KeyError:
        pass
    assert boom_calls["n"] == 1 and sleeps == [], "non-retryable must not retry"

    # 7. Fractional refill is kept, and a weighted acquire (TPM-style) waits for
    #    exactly the missing tokens.
    clock = FakeClock()
    tpm = TokenBucket(capacity=1000, refill_rate=10.0, clock=clock)
    assert tpm.try_acquire(900) and not tpm.try_acquire(150)
    assert abs(tpm.time_until_available(150) - 5.0) < 1e-9   # 50 short at 10/s
    clock.advance(0.25)                                       # 2.5 tokens, not 2
    assert abs(tpm.time_until_available(150) - 4.75) < 1e-9

    # 8. A request bigger than the bucket fails fast instead of waiting forever.
    for oversized in (tpm.try_acquire, tpm.time_until_available):
        try:
            oversized(1001)
            assert False, "tokens > capacity must be rejected"
        except ValueError:
            pass

    print("All tests passed.")
