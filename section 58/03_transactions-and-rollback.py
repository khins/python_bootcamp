# ============================================================
# FILE: 03_transactions-and-rollback.py
# TOPIC: Transactions, Rollback, and Savepoints
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply transactions, rollback, and savepoints to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# Transactions group changes into a commit or rollback. Psycopg normally begins
# one even for SELECT; avoid leaving connections idle in transaction. After a
# statement error, roll back before further commands. A transaction context rolls
# back when an exception exits it. Catch outside the context when rollback is
# required. Nested transaction contexts can create savepoints. The opt-in database
# test demonstrates rollback and a savepoint using a temporary table only.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from unittest.mock import MagicMock

def save_pair(connection):
    with connection.transaction():
        connection.execute("INSERT INTO study_values VALUES (%s)", ("first",))
        connection.execute("INSERT INTO study_values VALUES (%s)", ("second",))

def example():
    connection = MagicMock()
    save_pair(connection)
    print(connection.execute.call_count)  # => 2
    connection.transaction.return_value.__exit__.assert_called_once_with(None, None, None)
    # This verifies control flow only, not real database atomicity.


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Why catch outside a transaction context?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Run the opt-in integration test against an isolated test database.
# ANSWER / CODE: ______________________________________________

# 3. What does a mocked context manager fail to prove?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: Transactions group changes into a commit or rollback.
# ============================================================
# END OF LESSON
# ============================================================
