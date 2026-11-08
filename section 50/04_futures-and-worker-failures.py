# ============================================================
# FILE: 04_futures-and-worker-failures.py
# TOPIC: Collecting Worker Failures
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply collecting worker failures to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# submit returns a Future. Calling result retrieves the result or raises the
# worker's exception in the parent. as_completed yields completed futures;
# completion order is not guaranteed. A normal task exception need not destroy
# the pool. An abruptly terminated worker can cause BrokenProcessPool instead.
# A wait timeout does not stop a running task. cancel only succeeds before work
# starts; leaving the executor context normally still waits for running work.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from concurrent.futures import ProcessPoolExecutor, as_completed

def reciprocal(value):
    return 1 / value

def example():
    outcomes = {}
    with ProcessPoolExecutor(max_workers=2) as pool:
        jobs = {pool.submit(reciprocal, value): value for value in [2, 0, 4]}
        for future in as_completed(jobs):
            value = jobs[future]
            try:
                outcomes[value] = future.result()
            except ZeroDivisionError:
                outcomes[value] = "invalid"
    print(sorted(outcomes.items()))  # => [(0, 'invalid'), (2, 0.5), (4, 0.25)]


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Where is the task exception observed?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Return separate success and failure dictionaries for a batch.
# ANSWER / CODE: ______________________________________________

# 3. Why is a result timeout not a hard task deadline?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: submit returns a Future.
# ============================================================
# END OF LESSON
# ============================================================
