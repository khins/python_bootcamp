# ============================================================
# FILE: 01_parameter-and-return-hints.py
# TOPIC: Annotate Function Contracts
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Add parameter and return hints.
# 2. Separate static checking from runtime enforcement.

# SECTION 1 - UNDERSTAND THE IDEA
# Type hints document expected values for readers and static tools. Python does
# not enforce these annotations at ordinary call time. A function returning no
# meaningful value uses -> None. A checker needs annotated code to find many
# mistakes; hints are not a replacement for validation or behavior tests.

# SECTION 2 - WORKED EXAMPLES
def label(title: str, year: int) -> str:
    return f"{title} ({year})"

def example_annotations() -> None:
    print(label("Signals", 1982))  # => Signals (1982)
    print(label.__annotations__["return"] is str)  # => True

# example_annotations()
# label("Signals", "1982") is a static type error despite working with this f-string.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Annotate a seconds-to-minutes function.
# ANSWER / CODE: ______________________________________________
# 2. Explain why a type checker can reject code Python still runs.
# ANSWER / CODE: ______________________________________________
# 3. Annotate a function that prints but does not return a value.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Hints express a contract; runtime checks enforce external input.

# ============================================================
# END OF LESSON
# ============================================================
