# ============================================================
# FILE: 02_context-and-tracebacks.py
# TOPIC: Exception Context and Tracebacks
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply exception context and tracebacks to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# Raising an exception while handling another sets implicit __context__. Explicit
# from sets __cause__. from None suppresses the implicit context in the displayed
# traceback; it does not erase the stored context. Use suppression deliberately
# when a lower-level failure adds no useful information to a public boundary.
# Keep diagnostic detail in internal logs without returning sensitive internals.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
def translate():
    try:
        int("bad")
    except ValueError:
        raise RuntimeError("conversion failed") from None

def example():
    try:
        translate()
    except RuntimeError as error:
        print(type(error.__context__).__name__)  # => ValueError
        print(error.__suppress_context__)  # => True


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Does from None delete the original exception object?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Compare formatted tracebacks with and without explicit chaining.
# ANSWER / CODE: ______________________________________________

# 3. Why should public errors and internal diagnostics have different detail?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: Raising an exception while handling another sets implicit
# __context__.
# ============================================================
# END OF LESSON
# ============================================================
