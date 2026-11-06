# ============================================================
# FILE: 07_cache-and-lru-cache.py
# TOPIC: Cache Repeated Computation
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Inspect cache hits and misses.
# 2. Choose a cache size and invalidation policy.

# SECTION 1 - UNDERSTAND THE IDEA
# cache is unbounded memoization; lru_cache(maxsize=N) evicts least recently
# used entries. Arguments must be hashable. Cached return objects are reused,
# so mutable results can leak changes between callers. Do not cache a changing
# file/API result indefinitely. cache_clear removes stored results and stats.

# SECTION 2 - WORKED EXAMPLES
from functools import cache, lru_cache

@cache
def triangular(n):
    return n * (n + 1) // 2

@lru_cache(maxsize=2)
def normalize_artist(name):
    return name.strip().casefold()

def example_cache():
    triangular.cache_clear()
    print(triangular(10), triangular(10))  # => 55 55
    info = triangular.cache_info()
    print(info.hits, info.misses)          # => 1 1
    normalize_artist.cache_clear()
    for name in ["Rush", "Yes", "Blue"]:
        normalize_artist(name)
    print(normalize_artist.cache_info().currsize)  # => 2

# example_cache()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Predict hits after calls A, B, A to the bounded cache.
# ANSWER / CODE: ______________________________________________
# 2. Explain why a list cannot be a cache key.
# ANSWER / CODE: ______________________________________________
# 3. Describe when caching costs more memory than it saves time.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Cache stable results with a deliberate size and lifetime.

# ============================================================
# END OF LESSON
# ============================================================
