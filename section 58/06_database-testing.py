# ============================================================
# FILE: 06_database-testing.py
# TOPIC: Offline Tests versus Database Integration Tests
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply offline tests versus database integration tests to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# Offline API tests inject MemoryCatalog and verify routing, validation, and
# status codes. They do not prove SQL syntax, constraints, pooling, or real server
# behavior. The optional integration test requires STUDY_TEST_DATABASE_URL and
# uses a connection-local temporary table, a forced rollback, and a savepoint.
# It is skipped unless explicitly configured. It tests driver transaction behavior,
# not the complete migrated catalog; add full-schema integration coverage before
# using this project beyond local study.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from fastapi.testclient import TestClient
from postgres_catalog import create_app
from test_postgres_catalog import fake_resource

def example():
    with TestClient(create_app(fake_resource)) as client:
        print(client.get("/albums").json())  # => []
        print(client.get("/albums/99").status_code)  # => 404


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. What can a fake not verify?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: In a dedicated database, test the migrated adapter for duplicate albums and rollback.
# ANSWER / CODE: ______________________________________________

# 3. Why must integration tests never silently select a production database?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: Offline API tests inject MemoryCatalog and verify routing,
# validation, and status codes.
# ============================================================
# END OF LESSON
# ============================================================
