# ============================================================
# FILE: 02_parameterized-queries.py
# TOPIC: Parameterized Queries and Identifiers
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply parameterized queries and identifiers to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# Psycopg uses %s placeholders for values regardless of the Python value type.
# Pass values separately as a tuple or mapping; do not interpolate with f-strings
# or Python %. A single-item tuple needs a trailing comma. Placeholders cannot
# represent table or column identifiers; use psycopg.sql.Identifier with a trusted
# selection policy. Do not put quotes around a %s value placeholder.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from unittest.mock import Mock

def lookup(connection, title):
    return connection.execute("SELECT id FROM albums WHERE title=%s", (title,))

def example():
    connection = Mock()
    lookup(connection, "O'Reilly")
    connection.execute.assert_called_once_with(
        "SELECT id FROM albums WHERE title=%s", ("O'Reilly",))
    print("SQL and values stayed separate")


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Why is quoting a placeholder wrong?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Construct a two-parameter query without merging values into SQL.
# ANSWER / CODE: ______________________________________________

# 3. Why are identifiers different from values?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: Psycopg uses %s placeholders for values regardless of the
# Python value type.
# ============================================================
# END OF LESSON
# ============================================================
