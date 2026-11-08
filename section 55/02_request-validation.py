# ============================================================
# FILE: 02_request-validation.py
# TOPIC: Request Validation with Pydantic
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply request validation with pydantic to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# A Pydantic model declares expected request fields and constraints. FastAPI
# validates incoming request bodies and returns 422 for invalid data. Validation
# can include coercion unless strict rules are configured. String length alone
# does not reject whitespace-only text; the project adds a stripping validator.
# Annotations document a boundary; do not assume they replace domain rules.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from fastapi.testclient import TestClient
from catalog_api import create_app

def example():
    with TestClient(create_app()) as client:
        good = client.post("/albums", json={"title": "Blue", "artist": "Joni Mitchell"})
        bad = client.post("/albums", json={"title": " ", "artist": "Rush"})
        print(good.status_code, bad.status_code)  # => 201 422


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Why reject whitespace after stripping?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Add a bounded release-year field and boundary tests.
# ANSWER / CODE: ______________________________________________

# 3. What is the difference between absent and empty fields?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: A Pydantic model declares expected request fields and
# constraints.
# ============================================================
# END OF LESSON
# ============================================================
