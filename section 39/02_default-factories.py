# ============================================================
# FILE: 02_default-factories.py
# TOPIC: Give Each Instance Its Own List
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Use field(default_factory=...).
# 2. Avoid shared mutable defaults.

# SECTION 1 - UNDERSTAND THE IDEA
# Mutable fields need a factory so each instance starts with a fresh object.
# Pass list, not list(). The factory is called when the instance needs a default.
# If callers explicitly supply the same list to two instances, that list is
# still shared: default_factory is not automatic copying of supplied arguments.

# SECTION 2 - WORKED EXAMPLES
from dataclasses import dataclass, field

@dataclass
class Playlist:
    name: str
    titles: list[str] = field(default_factory=list)

def example_factories():
    first, second = Playlist("Morning"), Playlist("Evening")
    first.titles.append("YYZ")
    print(first.titles)                 # => ['YYZ']
    print(second.titles)                # => []
    print(first.titles is second.titles) # => False

# example_factories()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Add a fresh metadata dictionary to each playlist.
# ANSWER / CODE: ______________________________________________
# 2. Demonstrate deliberate sharing by passing the same list twice.
# ANSWER / CODE: ______________________________________________
# 3. Explain why field(default_factory=list()) is incorrect.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: A factory creates a default per instance, not a copy of every argument.

# ============================================================
# END OF LESSON
# ============================================================
