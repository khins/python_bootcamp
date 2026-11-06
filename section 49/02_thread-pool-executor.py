# ============================================================
# FILE: 02_thread-pool-executor.py
# TOPIC: Run Tasks in a Thread Pool
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Bound running workers.
# 2. Collect ordered map results.

# SECTION 1 - UNDERSTAND THE IDEA
# ThreadPoolExecutor owns a pool of worker threads. Its context manager waits
# for submitted work during shutdown. map yields results in input order even
# if tasks finish in another order. max_workers bounds simultaneously running
# calls, but on Python 3.11 map can eagerly submit the whole input. Lesson 07
# adds a bound on pending submissions as well as active workers.

# SECTION 2 - WORKED EXAMPLES
from concurrent.futures import ThreadPoolExecutor

def uppercase(title):
    return title.upper()

def example_pool():
    with ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(uppercase, ["Signals", "Blue", "Fragile"]))
    print(results)  # => ['SIGNALS', 'BLUE', 'FRAGILE']

# example_pool()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Map a finite simulated I/O function with two workers.
# ANSWER / CODE: ______________________________________________
# 2. Explain why result order does not prove completion order.
# ANSWER / CODE: ______________________________________________
# 3. Describe what max_workers does and does not bound.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Bound worker count and understand submission behavior separately.

# REFERENCES
# https://docs.python.org/3.13/library/concurrent.futures.html

# ============================================================
# END OF LESSON
# ============================================================
