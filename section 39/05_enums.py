# ============================================================
# FILE: 05_enums.py
# TOPIC: Represent a Fixed Set of Choices
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Create and compare enum members.
# 2. Convert external values deliberately.

# SECTION 1 - UNDERSTAND THE IDEA
# Enum gives names to a fixed set of distinct values. Members are not plain
# strings: compare to the member, serialize .value, and validate by constructing
# from a value. EnumName["MEMBER"] looks up a name; EnumName("value") looks up a
# value. Unknown values raise ValueError rather than creating new members.

# SECTION 2 - WORKED EXAMPLES
from enum import Enum

class Format(Enum):
    CD = "cd"
    VINYL = "vinyl"
    DIGITAL = "digital"

def example_enum():
    choice = Format("vinyl")
    print(choice is Format.VINYL)  # => True
    print(choice.name)             # => VINYL
    print(choice.value)            # => vinyl
    print(choice == "vinyl")       # => False
    try:
        Format("cassette")
    except ValueError:
        print("unsupported format")  # => unsupported format

# example_enum()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Define a playback status enum.
# ANSWER / CODE: ______________________________________________
# 2. Convert a lowercase input string to a member and handle failure.
# ANSWER / CODE: ______________________________________________
# 3. Explain member names versus stored values.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Enums make allowed choices explicit and invalid choices visible.

# ============================================================
# END OF LESSON
# ============================================================
