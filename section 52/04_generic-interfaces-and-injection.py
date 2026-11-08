# ============================================================
# FILE: 04_generic-interfaces-and-injection.py
# TOPIC: Generic Interfaces and Dependency Injection
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply generic interfaces and dependency injection to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# A read-only source can be covariant: a source of a specific subtype can serve
# where a source of a broader type is requested. Mutable containers are generally
# invariant because both reading and writing must be safe. Dependency injection
# passes a collaborator instead of constructing it deep inside business logic.
# Keep the interface narrow so tests and adapters need only relevant operations.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from typing import Protocol, TypeVar

T_co = TypeVar("T_co", covariant=True)

class Source(Protocol[T_co]):
    def get(self, key: str) -> T_co: ...

class TitleSource:
    def get(self, key: str) -> str:
        return "Signals"

def title_label(source: Source[str], key: str) -> str:
    return f"Album: {source.get(key)}"

def example():
    print(title_label(TitleSource(), "1"))  # => Album: Signals


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Why might a writable interface need invariant T?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Inject a fake source that raises KeyError and test the caller policy.
# ANSWER / CODE: ______________________________________________

# 3. What coupling is removed by passing source as an argument?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: A read-only source can be covariant: a source of a specific
# subtype can serve where a source of a broader type is requested.
# ============================================================
# END OF LESSON
# ============================================================
