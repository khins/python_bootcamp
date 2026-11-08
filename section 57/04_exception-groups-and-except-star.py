# ============================================================
# FILE: 04_exception-groups-and-except-star.py
# TOPIC: ExceptionGroup and except*
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply exceptiongroup and except* to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# ExceptionGroup represents multiple Exception instances, possibly nested.
# except* matches and partitions leaves by type while preserving group structure.
# Several except* clauses can handle different parts of one group. Unhandled
# parts propagate. You cannot mix except and except* clauses on the same try.
# Use nested try statements when both styles are needed. BaseExceptionGroup is
# broader and can contain cancellation or other BaseException subclasses.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
def example():
    try:
        raise ExceptionGroup("batch", [ValueError("bad value"), TypeError("bad type")])
    except* ValueError as errors:
        print("value failures:", len(errors.exceptions))  # => value failures: 1
    except* TypeError as errors:
        print("type failures:", len(errors.exceptions))  # => type failures: 1


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Can both except* clauses run for one group?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Nest groups and explain why top-level length is not always leaf count.
# ANSWER / CODE: ______________________________________________

# 3. What happens to an unmatched subgroup?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: ExceptionGroup represents multiple Exception instances,
# possibly nested.
# ============================================================
# END OF LESSON
# ============================================================
