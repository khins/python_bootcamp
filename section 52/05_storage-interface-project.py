# ============================================================
# FILE: 05_storage-interface-project.py
# TOPIC: Project: Swap Storage Implementations
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply project: swap storage implementations to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# storage_project.py implements a shared save/load contract with an in-memory
# mapping and SQLite. Both define missing keys as None and saving an existing
# key as replacement. An interface alone cannot guarantee those semantics;
# run the same behavior checks against both implementations. SQLite resources
# are explicitly closed. Parameters protect values from being treated as SQL.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from storage_project import MemoryStore, SQLiteStore, contract

def example():
    contract(MemoryStore())
    database = SQLiteStore()
    try:
        contract(database)
    finally:
        database.close()
    print("adapter checks passed")


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Why must missing-key semantics match across adapters?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Add delete to both adapters and extend the shared checks.
# ANSWER / CODE: ______________________________________________

# 3. Which real database behavior is not proven by an in-memory fake?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: storage_project.py implements a shared save/load contract with
# an in-memory mapping and SQLite.
# ============================================================
# END OF LESSON
# ============================================================
