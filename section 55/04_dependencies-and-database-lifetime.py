# ============================================================
# FILE: 04_dependencies-and-database-lifetime.py
# TOPIC: Dependency Injection and Database Lifetimes
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply dependency injection and database lifetimes to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# Depends resolves a collaborator for a request. The app lifespan owns the study
# SQLite connection, and shutdown closes it. Synchronous handlers run blocking
# SQLite work without blocking the event loop directly. check_same_thread=False
# only permits cross-thread use; the project also serializes shared access with
# a lock. A production database typically uses per-request pooled connections.
# The in-memory catalog resets every app restart and is not durable storage.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from fastapi.testclient import TestClient
from catalog_api import create_app, get_store

class FakeCatalog:
    def list_all(self):
        return [{"id": 1, "title": "Signals", "artist": "Rush"}]

def example():
    app = create_app()
    app.dependency_overrides[get_store] = lambda: FakeCatalog()
    try:
        with TestClient(app) as client:
            print(client.get("/albums").json()[0]["title"])  # => Signals
    finally:
        app.dependency_overrides.clear()


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Who closes the connection?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Override get_store to return a missing record and test 404.
# ANSWER / CODE: ______________________________________________

# 3. Why does disabling SQLite thread checks not provide synchronization?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: Depends resolves a collaborator for a request.
# ============================================================
# END OF LESSON
# ============================================================
