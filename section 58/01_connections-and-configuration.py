# ============================================================
# FILE: 01_connections-and-configuration.py
# TOPIC: PostgreSQL Connections and Configuration
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply postgresql connections and configuration to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# PostgreSQL is a separate database server; installing Psycopg installs a driver,
# not the server. Keep connection URLs in environment configuration, not source.
# Use a dedicated study database and role. Connection context managers delimit
# lifetimes and transaction cleanup. Importing the project never connects; its
# application lifespan connects only when explicitly started. Do not print DSNs.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
import os

def require_database_url(environment):
    value = environment.get("STUDY_DATABASE_URL")
    if not value:
        raise RuntimeError("STUDY_DATABASE_URL is required")
    return value

def example():
    try:
        require_database_url({})
    except RuntimeError:
        print("configuration is missing")
    print(bool(require_database_url({"STUDY_DATABASE_URL": "configured-placeholder"})))
    # Real use: require_database_url(os.environ); do not log its value.


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Why is the driver not the database server?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Validate required configuration without printing credentials.
# ANSWER / CODE: ______________________________________________

# 3. Which resource owns closing a connection?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: PostgreSQL is a separate database server; installing Psycopg
# installs a driver, not the server.
# ============================================================
# END OF LESSON
# ============================================================
