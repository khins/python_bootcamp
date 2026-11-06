# ============================================================
# FILE: 03_unions-and-optional-values.py
# TOPIC: Narrow Optional Values
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Represent a missing result.
# 2. Narrow a union before using it.

# SECTION 1 - UNDERSTAND THE IDEA
# str | None means either a string or None. Optional[str] means the same thing;
# it does not mean a parameter has a default. Use is None when empty strings
# are valid results. After an explicit check, a type checker can narrow the
# remaining branch to str. Avoid hiding an uncertain type with an unchecked cast.

# SECTION 2 - WORKED EXAMPLES
def find_title(catalog: dict[int, str], album_id: int) -> str | None:
    return catalog.get(album_id)

def display_title(title: str | None) -> str:
    if title is None:
        return "Not found"
    return title.upper()

def example_narrowing() -> None:
    print(display_title(find_title({1: "Signals"}, 1)))  # => SIGNALS
    print(display_title(find_title({}, 2)))              # => Not found
    print(repr(display_title("")))                      # => ''

# example_narrowing()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Write a function returning the first item or None.
# ANSWER / CODE: ______________________________________________
# 2. Contrast if not title with if title is None.
# ANSWER / CODE: ______________________________________________
# 3. Show a union of int and str and narrow with isinstance.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Handle the missing case before using the value as its concrete type.

# ============================================================
# END OF LESSON
# ============================================================
