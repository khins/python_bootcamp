# ============================================================
# FILE: 03_futures-results-and-failures.py
# TOPIC: Collect Results and Exceptions
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Associate futures with task identifiers.
# 2. Handle failures per task.

# SECTION 1 - UNDERSTAND THE IDEA
# submit returns a Future. result returns its value or re-raises the worker's
# exception. as_completed yields completed futures; relative order can vary.
# A failed task need not discard successful ones. Keep a future-to-input mapping
# so each error can be attributed without guessing from completion order.

# SECTION 2 - WORKED EXAMPLES
from concurrent.futures import ThreadPoolExecutor, as_completed

def read_record(identifier):
    if identifier == "bad":
        raise ValueError("invalid record")
    return identifier.upper()

def example_futures():
    successes, failures = {}, {}
    with ThreadPoolExecutor(max_workers=2) as pool:
        pending = {pool.submit(read_record, key): key for key in ["a", "bad", "b"]}
        for future in as_completed(pending):
            key = pending[future]
            try:
                successes[key] = future.result()
            except ValueError as error:
                failures[key] = str(error)
    print(sorted(successes.items()))  # => [('a', 'A'), ('b', 'B')]
    print(failures)                   # => {'bad': 'invalid record'}

# example_futures()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Return task ids alongside values.
# ANSWER / CODE: ______________________________________________
# 2. Add a second failure and verify successes are retained.
# ANSWER / CODE: ______________________________________________
# 3. Explain why catching errors only around submit misses worker exceptions.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Retrieve each future and tie every outcome to its input.

# ============================================================
# END OF LESSON
# ============================================================
