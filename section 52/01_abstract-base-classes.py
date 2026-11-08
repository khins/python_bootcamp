# ============================================================
# FILE: 01_abstract-base-classes.py
# TOPIC: Abstract Base Classes
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply abstract base classes to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# An ABC makes required operations explicit through abstractmethod. A subclass
# cannot be instantiated while abstract methods remain unimplemented. It does
# not enforce matching signatures or validate every returned value. An abstract
# method may have a reusable body, but the subclass still must override it.
# Use an ABC when nominal inheritance and shared behavior suit the design.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def load(self, key):
        raise NotImplementedError

class MemoryStorage(Storage):
    def load(self, key):
        return {"album": "Signals"}[key]

def example():
    print(MemoryStorage().load("album"))  # => Signals
    try:
        Storage()
    except TypeError:
        print("abstract class cannot be instantiated")


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Does ABC enforce the return type?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Add an abstract save method and implement a concrete store.
# ANSWER / CODE: ______________________________________________

# 3. When is ordinary composition simpler than inheritance?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: An ABC makes required operations explicit through
# abstractmethod.
# ============================================================
# END OF LESSON
# ============================================================
