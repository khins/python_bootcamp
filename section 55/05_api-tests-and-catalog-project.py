# ============================================================
# FILE: 05_api-tests-and-catalog-project.py
# TOPIC: Project: Tested Music Catalog API
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply project: tested music catalog api to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# catalog_api.py contains a worked application and test_catalog_api.py exercises
# create, list, retrieve, validation, missing IDs, and dependency overrides.
# Each test opens a fresh application with fresh SQLite state. Run tests using
# unittest discovery as shown in the guide. The API uses parameterized SQL and
# returns 201 on creation. Add features incrementally with behavior-focused tests.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from fastapi.testclient import TestClient
from catalog_api import create_app

def example():
    with TestClient(create_app()) as client:
        album = client.post("/albums", json={"title": "Signals", "artist": "Rush"}).json()
        print(client.get(f"/albums/{album['id']}").json() == album)  # => True


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Why does each test need isolated data?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Implement DELETE with 204 on success and 404 when absent; test both.
# ANSWER / CODE: ______________________________________________

# 3. Which guarantees require tests against the real storage adapter?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: catalog_api.py contains a worked application and
# test_catalog_api.py exercises create, list, retrieve, validation, missing
# IDs, and dependency overrides.
# ============================================================
# END OF LESSON
# ============================================================
