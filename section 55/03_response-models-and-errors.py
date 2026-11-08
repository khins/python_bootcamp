# ============================================================
# FILE: 03_response-models-and-errors.py
# TOPIC: Response Models and API Errors
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply response models and api errors to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# response_model defines output serialization and validation. A missing catalog
# record is a 404; an invalid path integer produces 422. HTTPException communicates
# an intentional HTTP error. Unexpected exceptions should be logged internally,
# not exposed with database credentials or tracebacks. Output models also avoid
# accidentally returning internal fields. This demo has no authentication and is
# for local study, not public deployment as-is.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from fastapi.testclient import TestClient
from catalog_api import create_app

def example():
    with TestClient(create_app()) as client:
        print(client.get("/albums/999").status_code)  # => 404
        print(client.get("/albums/wrong").status_code)  # => 422
        print(client.get("/albums").json())  # => []


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Why are missing records and malformed IDs different errors?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Add a response-only field while keeping input validation separate.
# ANSWER / CODE: ______________________________________________

# 3. Why should internal exception text not become a public error response?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: response_model defines output serialization and validation.
# ============================================================
# END OF LESSON
# ============================================================
