# ============================================================
# FILE: 03_serialization-and-task-overhead.py
# TOPIC: Serialization and Task Granularity
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply serialization and task granularity to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# Process pools serialize callables, arguments, and results with pickle. Use
# module-level functions and simple data. Lambdas, local functions, open file
# handles, and active database connections are unsuitable task payloads.
# Serialize data, not live resources; open needed resources in the worker.
# Larger chunks can reduce scheduling overhead but reduce load balancing.
# Never unpickle untrusted bytes. Pickle is a Python transfer format, not a
# safe general interchange format for external input.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
import pickle
from concurrent.futures import ProcessPoolExecutor

def record_size(record):
    return len(record["plays"])

def example():
    records = [{"title": "Signals", "plays": [1, 2]}, {"title": "Blue", "plays": []}]
    restored = pickle.loads(pickle.dumps(records))  # Locally created trusted data.
    with ProcessPoolExecutor(max_workers=2) as pool:
        print(list(pool.map(record_size, restored, chunksize=2)))  # => [2, 0]


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. What must be serializable besides task arguments?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Vary chunksize on many small records and measure without assuming a winner.
# ANSWER / CODE: ______________________________________________

# 3. Why should a worker receive a file path instead of an open file?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: Process pools serialize callables, arguments, and results with
# pickle.
# ============================================================
# END OF LESSON
# ============================================================
