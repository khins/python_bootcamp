# ============================================================
# FILE: 04_callable-and-interfaces.py
# TOPIC: Type Functions Passed as Arguments
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Describe a callback with Callable.
# 2. Accept a general read-only interface.

# SECTION 1 - UNDERSTAND THE IDEA
# Callable[[str], str] expects one string argument and a string result. Iterable
# allows lists, tuples, and generators when you only need traversal. Sequence
# adds indexed access. Prefer the narrow interface your function actually needs;
# an Iterable is not necessarily reusable or indexable.

# SECTION 2 - WORKED EXAMPLES
from collections.abc import Callable, Iterable

def format_titles(titles: Iterable[str], formatter: Callable[[str], str]) -> list[str]:
    return [formatter(title) for title in titles]

def example_callbacks() -> None:
    print(format_titles((s for s in ["Blue", "Signals"]), str.upper))
    # => ['BLUE', 'SIGNALS']

# example_callbacks()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Write a callback adding "Favorite: " to a title.
# ANSWER / CODE: ______________________________________________
# 2. Explain why Callable[[str], int] is incompatible here.
# ANSWER / CODE: ______________________________________________
# 3. Change a function accepting list[str] to Iterable[str] when no indexing is used.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Annotate behavior you need, including the callback signature.

# ============================================================
# END OF LESSON
# ============================================================
