# ============================================================
# FILE: 01_routes-and-http.py
# TOPIC: Routes and HTTP Responses
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply routes and http responses to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# FastAPI maps an HTTP method and path to a handler. GET reads a resource; POST
# commonly creates one. A returned dictionary is serialized as JSON. TestClient
# runs requests in-process without starting a network server. A context-managed
# client also runs application lifespan startup and shutdown. Start a real local
# server only with the explicit Uvicorn command in the guide.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from fastapi import FastAPI
from fastapi.testclient import TestClient

def example():
    app = FastAPI()
    @app.get("/health")
    def health():
        return {"status": "ok"}
    with TestClient(app) as client:
        response = client.get("/health")
        print(response.status_code, response.json())  # => 200 {'status': 'ok'}


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. How does a route differ from a plain Python function call?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Add /version and test its JSON response.
# ANSWER / CODE: ______________________________________________

# 3. Why use a TestClient context manager?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: FastAPI maps an HTTP method and path to a handler.
# ============================================================
# END OF LESSON
# ============================================================
