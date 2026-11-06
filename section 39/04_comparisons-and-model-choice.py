# ============================================================
# FILE: 04_comparisons-and-model-choice.py
# TOPIC: Ordering and Choosing a Model
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Explain generated field ordering.
# 2. Choose dictionaries, named tuples, or dataclasses.

# SECTION 1 - UNDERSTAND THE IDEA
# order=True compares fields in declaration order, like a tuple of fields.
# field(compare=False) excludes a field from generated comparisons. If sorting
# by one business criterion, an explicit key often communicates better.
# Dictionaries suit flexible external records; named tuples suit compact fixed
# positional records; dataclasses suit named fields with defaults and behavior.

# SECTION 2 - WORKED EXAMPLES
from dataclasses import dataclass, field

@dataclass(order=True)
class RankedAlbum:
    year: int
    title: str
    notes: str = field(default="", compare=False)

def example_ordering():
    albums = [RankedAlbum(1982, "Signals"), RankedAlbum(1971, "Fragile")]
    print([a.title for a in sorted(albums)])  # => ['Fragile', 'Signals']
    print(RankedAlbum(1982, "Signals", "A") == RankedAlbum(1982, "Signals", "B"))
    # => True

# example_ordering()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Sort Album objects by artist without order=True.
# ANSWER / CODE: ______________________________________________
# 2. Choose a model for an API response and justify it.
# ANSWER / CODE: ______________________________________________
# 3. Predict how moving title before year changes default ordering.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Generated comparisons follow field definitions, not inferred business rules.

# ============================================================
# END OF LESSON
# ============================================================
