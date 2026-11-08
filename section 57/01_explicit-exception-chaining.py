# ============================================================
# FILE: 01_explicit-exception-chaining.py
# TOPIC: Explicit Exception Chaining
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply explicit exception chaining to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# raise DomainError(...) from original preserves a causal link while exposing a
# higher-level operation failure. __cause__ holds the explicit cause. A bare
# raise in an except block re-raises the active exception and preserves its
# traceback without adding a new raise site as raise error does. Catch only what
# you can interpret, recover from, or enrich with meaningful context.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
class CatalogError(Exception):
    pass

def parse_count(text):
    try:
        return int(text)
    except ValueError as error:
        raise CatalogError("invalid play count") from error

def example():
    try:
        parse_count("many")
    except CatalogError as error:
        print(type(error.__cause__).__name__)  # => ValueError


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. What is stored in __cause__?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Wrap a KeyError with an operation-specific exception and inspect the cause.
# ANSWER / CODE: ______________________________________________

# 3. When should you use bare raise instead of creating a new exception?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: raise DomainError(...) from original preserves a causal link
# while exposing a higher-level operation failure.
# ============================================================
# END OF LESSON
# ============================================================
