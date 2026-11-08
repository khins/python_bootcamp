# ============================================================
# FILE: 01_process-isolation.py
# TOPIC: Process Isolation
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply process isolation to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# A process has its own Python interpreter and address space. Changing a worker's
# list does not change the parent's list. Return results explicitly. Processes
# can run CPU-heavy Python work in parallel on standard GIL-enabled CPython.
# Starting processes and transferring data costs time; small jobs may be slower.
# Windows starts fresh interpreters. Worker functions must be importable module-
# level functions, and pool creation must be protected by the __main__ guard.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

def add_worker_item(items):
    items.append("worker")
    return items

def example():
    original = ["parent"]
    with ProcessPoolExecutor(max_workers=1,
                             mp_context=multiprocessing.get_context("spawn")) as pool:
        result = pool.submit(add_worker_item, original).result()
    print(original)  # => ['parent']
    print(result)    # => ['parent', 'worker']


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Why does the original list stay unchanged?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Return a modified dictionary from a worker and compare both copies.
# ANSWER / CODE: ______________________________________________

# 3. Why must pool creation stay inside a guarded call on Windows?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: A process has its own Python interpreter and address space.
# ============================================================
# END OF LESSON
# ============================================================
