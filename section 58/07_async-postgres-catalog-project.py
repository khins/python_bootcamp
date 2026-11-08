# ============================================================
# FILE: 07_async-postgres-catalog-project.py
# TOPIC: Project: Async PostgreSQL Music Catalog
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply project: async postgresql music catalog to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# postgres_catalog.py extends the section-55 API design with awaited storage,
# a normalized PostgreSQL schema, a lifespan-managed pool, and a 409 duplicate
# response. Artist and album creation share a transaction. SQL uses separate
# parameters. Run offline tests first; then explicitly configure and migrate a
# study database for a live run. The Windows entry point selects an event loop
# compatible with Psycopg's async support. This teaching API has no authentication,
# pagination, or production deployment setup and should remain local.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from fastapi.testclient import TestClient
from postgres_catalog import create_app
from test_postgres_catalog import fake_resource

def example():
    with TestClient(create_app(fake_resource)) as client:
        payload = {"title": "Signals", "artist": "Rush"}
        print(client.post("/albums", json=payload).status_code)  # => 201
        print(client.post("/albums", json=payload).status_code)  # => 409


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Why must artist and album creation share a transaction?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Add pagination with deterministic ordering and tests.
# ANSWER / CODE: ______________________________________________

# 3. Plan migration, integration checks, pool sizing, and rollback before deployment.
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: postgres_catalog.py extends the section-55 API design with
# awaited storage, a normalized PostgreSQL schema, a lifespan-managed pool,
# and a 409 duplicate response.
# ============================================================
# END OF LESSON
# ============================================================
