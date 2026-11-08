# ============================================================
# FILE: 03_typevar-and-generic.py
# TOPIC: TypeVar and Generic Containers
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply typevar and generic containers to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# TypeVar links related argument and return types. Generic[T] parameterizes a
# class so callers can retain element information. These are static contracts,
# not automatic runtime type enforcement. This lesson uses Python 3.11 syntax.
# A function returning T from list[T] expresses a relationship that returning
# object cannot. Empty-input behavior still requires an explicit design.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from typing import Generic, TypeVar

T = TypeVar("T")

class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value
    def get(self) -> T:
        return self.value

def first(items: list[T]) -> T:
    if not items:
        raise ValueError("items must not be empty")
    return items[0]

def example():
    box: Box[str] = Box("Signals")
    print(box.get())  # => Signals
    print(first([2, 3]))  # => 2


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. What relationship does T preserve?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Add replace(value: T) to Box and run a static checker on a wrong-type call.
# ANSWER / CODE: ______________________________________________

# 3. Why does first need an empty-list policy despite its annotation?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: TypeVar links related argument and return types.
# ============================================================
# END OF LESSON
# ============================================================
