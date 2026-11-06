# ============================================================
# FILE: 01_dataclass-basics.py
# TOPIC: Generate Record Boilerplate
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Define fields and defaults.
# 2. Inspect generated repr and equality.

# SECTION 1 - UNDERSTAND THE IDEA
# @dataclass generates methods such as __init__, __repr__, and __eq__ from
# annotated fields. Non-default fields come before default fields. Annotations
# alone do not validate values. Dataclasses remain ordinary classes: add methods
# where behavior belongs with the data.

# SECTION 2 - WORKED EXAMPLES
from dataclasses import dataclass

@dataclass
class Album:
    title: str
    artist: str
    year: int = 0

    def label(self):
        return f"{self.title} by {self.artist}"

def example_records():
    first = Album("Signals", "Rush", 1982)
    second = Album("Signals", "Rush", 1982)
    print(first)                  # => Album(title='Signals', artist='Rush', year=1982)
    print(first == second)        # => True
    print(first is second)        # => False
    print(first.label())          # => Signals by Rush

# example_records()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Define a Track with title and seconds.
# ANSWER / CODE: ______________________________________________
# 2. Predict equality when one year differs.
# ANSWER / CODE: ______________________________________________
# 3. Explain what dataclass generates and what it does not validate.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Use dataclasses for named records with ordinary class behavior.

# ============================================================
# END OF LESSON
# ============================================================
