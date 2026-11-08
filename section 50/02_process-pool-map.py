# ============================================================
# FILE: 02_process-pool-map.py
# TOPIC: ProcessPoolExecutor and Ordered Results
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply processpoolexecutor and ordered results to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# Executor.map applies an importable callable to inputs. Results follow input
# order even if workers finish out of order. The context manager shuts workers
# down and waits for submitted work. Limit worker count rather than assuming
# more workers always help. map returns an iterator; consume it inside the scope.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from concurrent.futures import ProcessPoolExecutor

def sum_squares(limit):
    return sum(number * number for number in range(limit))

def example():
    inputs = [3, 4, 5]
    with ProcessPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(sum_squares, inputs))
    print(results)  # => [5, 14, 30]


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Does result order prove completion order?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Compare results with an ordinary list comprehension, including empty input.
# ANSWER / CODE: ______________________________________________

# 3. What work does exiting the executor context perform?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: Executor.map applies an importable callable to inputs.
# ============================================================
# END OF LESSON
# ============================================================
