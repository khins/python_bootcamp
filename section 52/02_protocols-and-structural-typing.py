# ============================================================
# FILE: 02_protocols-and-structural-typing.py
# TOPIC: Protocols and Structural Typing
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply protocols and structural typing to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# A Protocol describes operations a type checker expects. A class can satisfy it
# without inheriting from it: this is structural typing. An annotation does not
# validate an object at runtime. runtime_checkable enables limited isinstance
# checks for attribute presence, not full signature or return-type checking.
# Avoid treating runtime protocol checks as input validation.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from typing import Protocol

class Reader(Protocol):
    def load(self, key: str) -> str: ...

class DictionaryReader:
    def load(self, key: str) -> str:
        return {"title": "Blue"}[key]

def display(reader: Reader) -> str:
    return reader.load("title").upper()

def example():
    print(display(DictionaryReader()))  # => BLUE


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Why does DictionaryReader not need to inherit Reader?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Make a second implementation satisfying Reader with different data.
# ANSWER / CODE: ______________________________________________

# 3. Which errors require static checking rather than merely running Python?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: A Protocol describes operations a type checker expects.
# ============================================================
# END OF LESSON
# ============================================================
