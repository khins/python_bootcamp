# ============================================================
# FILE: 03_frozen-and-validation.py
# TOPIC: Frozen Records and Validation
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Validate in __post_init__.
# 2. Understand shallow immutability.

# SECTION 1 - UNDERSTAND THE IDEA
# frozen=True rejects ordinary field assignment but is not deep immutability:
# a list stored in a frozen object can still change. Prefer immutable field
# values for value objects. __post_init__ runs after generated initialization
# and can enforce domain rules. Frozen does not mean every object is hashable;
# its fields must support hashing too.

# SECTION 2 - WORKED EXAMPLES
from dataclasses import dataclass, FrozenInstanceError

@dataclass(frozen=True)
class Track:
    title: str
    seconds: int

    def __post_init__(self):
        if not self.title.strip():
            raise ValueError("title is required")
        if type(self.seconds) is not int or self.seconds < 0:
            raise ValueError("seconds must be a nonnegative integer")

def example_frozen():
    track = Track("YYZ", 200)
    try:
        track.seconds = 10
    except FrozenInstanceError:
        print("cannot reassign")  # => cannot reassign
    try:
        Track("YYZ", -1)
    except ValueError as error:
        print(error)  # => seconds must be a nonnegative integer

# example_frozen()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Reject an empty title in a new value class.
# ANSWER / CODE: ______________________________________________
# 2. Explain why frozen with a list field is only shallow protection.
# ANSWER / CODE: ______________________________________________
# 3. Use dataclasses.replace to create a changed copy.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Frozen fields and validated values solve different problems.

# ============================================================
# END OF LESSON
# ============================================================
