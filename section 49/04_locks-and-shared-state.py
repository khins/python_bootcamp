# ============================================================
# FILE: 04_locks-and-shared-state.py
# TOPIC: Protect a Shared Invariant
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Recognize read-modify-write races.
# 2. Lock the complete critical section.

# SECTION 1 - UNDERSTAND THE IDEA
# A shared counter increment is a read-modify-write sequence. The GIL does not
# make your multi-step application invariant safe. Lock around the whole state
# transition, not just the final assignment. Prefer workers returning independent
# values and one collector updating shared results when possible.

# SECTION 2 - WORKED EXAMPLES
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

def example_locked_counter():
    state = {"count": 0}
    lock = Lock()
    def increment(_):
        with lock:
            state["count"] += 1
    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(increment, range(100)))
    print(state["count"])  # => 100

# example_locked_counter()
# An unprotected example may appear correct in some runs; that is not proof of safety.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Protect a pair of related counters with one lock.
# ANSWER / CODE: ______________________________________________
# 2. Refactor workers to return counts and aggregate in the calling thread.
# ANSWER / CODE: ______________________________________________
# 3. Explain why holding a lock during network I/O reduces concurrency.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Protect the invariant, or avoid sharing mutable state.

# ============================================================
# END OF LESSON
# ============================================================
