# ============================================================
# FILE: 04_relationships-constraints-and-migrations.py
# TOPIC: Relationships, Constraints, and Migrations
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply relationships, constraints, and migrations to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# The project schema has artists and albums connected by a foreign key. NOT NULL,
# CHECK, and UNIQUE constraints enforce rules even when clients bypass the API.
# A foreign key does not automatically create an index on the referencing column;
# the migration adds one. Versioned migrations evolve a schema deliberately.
# 001_catalog.sql is a one-time transactional migration, not idempotent startup
# DDL. Back up durable data and plan compatible changes before later migrations.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from pathlib import Path

def example():
    migration = Path(__file__).with_name("001_catalog.sql").read_text(encoding="utf-8")
    print("REFERENCES artists(id)" in migration)  # => True
    print("UNIQUE (artist_id, title)" in migration)  # => True
    # Reading this file does not execute it against a database.


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Why enforce uniqueness in the database as well as the application?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Draft a second migration adding a nullable release_year and a CHECK constraint.
# ANSWER / CODE: ______________________________________________

# 3. Why is CREATE TABLE at every request not a migration strategy?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: The project schema has artists and albums connected by a
# foreign key.
# ============================================================
# END OF LESSON
# ============================================================
