# ============================================================
# FILE: 04_documentation-and-deployment.py
# TOPIC: Documenting and Deploying an Application
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply documenting and deploying an application to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# A runnable guide names prerequisites, installation, test commands, startup,
# configuration, and persistence limits. Development --reload is not a production
# process strategy. Deployment needs an ASGI server, process supervision, logs,
# health checks, configuration management, and a tested rollback plan. Database
# migrations are a separate release step, not a per-request operation. Multiple
# workers each have their own in-memory state; the demo SQLite catalog resets.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
import os

def read_port(environment):
    port = int(environment.get("PORT", "8000"))
    if not 1 <= port <= 65535:
        raise ValueError("PORT is outside the valid range")
    return port

def example():
    print(read_port({}))  # => 8000
    print(read_port({"PORT": "8080"}))  # => 8080
    # read_port(os.environ) reads real configuration but does not deploy.


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. What happens to in-memory catalog data after restart?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Write a runbook with startup, health verification, and rollback steps.
# ANSWER / CODE: ______________________________________________

# 3. Why should a deployment document state its persistence assumptions?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: A runnable guide names prerequisites, installation, test
# commands, startup, configuration, and persistence limits.
# ============================================================
# END OF LESSON
# ============================================================
