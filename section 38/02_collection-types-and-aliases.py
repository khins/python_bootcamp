# ============================================================
# FILE: 02_collection-types-and-aliases.py
# TOPIC: Describe Collections and Records
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Annotate nested collections.
# 2. Use aliases and TypedDict for readable records.

# SECTION 1 - UNDERSTAND THE IDEA
# list[str] describes element types; tuple[str, int] describes fixed positions.
# dict[str, int] gives key and value types. A TypeAlias names a type expression,
# not a new runtime class. TypedDict describes required dictionary fields to a
# checker but does not validate dictionaries at runtime. These examples use
# Python 3.11-compatible syntax rather than the newer type statement.

# SECTION 2 - WORKED EXAMPLES
from typing import TypeAlias, TypedDict

ArtistTotals: TypeAlias = dict[str, int]

class Listen(TypedDict):
    artist: str
    seconds: int

def totals(records: list[Listen]) -> ArtistTotals:
    result: ArtistTotals = {}
    for row in records:
        result[row["artist"]] = result.get(row["artist"], 0) + row["seconds"]
    return result

def example_types() -> None:
    rows: list[Listen] = [{"artist": "Rush", "seconds": 200}]
    print(totals(rows))  # => {'Rush': 200}

# example_types()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Annotate a list of (title, year) tuples.
# ANSWER / CODE: ______________________________________________
# 2. Add a title field to Listen and update the sample.
# ANSWER / CODE: ______________________________________________
# 3. Explain why TypedDict is not an input validator.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Choose collection hints that describe the actual shape of your data.

# ============================================================
# END OF LESSON
# ============================================================
