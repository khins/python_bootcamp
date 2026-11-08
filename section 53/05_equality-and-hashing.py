# ============================================================
# FILE: 05_equality-and-hashing.py
# TOPIC: Equality and Hashing Contracts
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply equality and hashing contracts to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# Equal hashable objects must have equal hashes. Unequal objects may share a hash.
# A key's equality/hash-relevant state must remain stable while it is in a set or
# dictionary. Defining __eq__ without an appropriate __hash__ usually makes the
# class unhashable. Frozen dataclasses are useful for immutable value objects,
# but their fields must also be hashable to hash the instance.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from dataclasses import dataclass

@dataclass(frozen=True)
class AlbumKey:
    artist: str
    title: str

def example():
    first = AlbumKey("Rush", "Signals")
    second = AlbumKey("Rush", "Signals")
    print(first == second, hash(first) == hash(second))  # => True True
    print(len({first, second}))  # => 1


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Do matching hashes prove equality?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Compare a mutable dataclass with a frozen one as dictionary keys.
# ANSWER / CODE: ______________________________________________

# 3. Why is hashing a mutable title dangerous?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: Equal hashable objects must have equal hashes.
# ============================================================
# END OF LESSON
# ============================================================
