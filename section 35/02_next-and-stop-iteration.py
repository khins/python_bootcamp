# ============================================================
# FILE: 02_next-and-stop-iteration.py
# TOPIC: next() and StopIteration
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# All examples use the standard library; no packages need installation.

# LESSON OBJECTIVES
# 1. Detect iterator exhaustion.
# 2. Use next() with a default value.

# SECTION 1 — NO MORE ITEMS
def example_exhaustion():
    cursor = iter(["Signals"])
    print(next(cursor))  # => Signals
    try:
        next(cursor)
    except StopIteration:
        print("Finished")  # => Finished
    print(list(cursor))    # => []


# example_exhaustion()
# Once an iterator is exhausted, later next() calls remain exhausted.
# Calling iter(cursor) does not rewind it.


# SECTION 2 — A DEFAULT REPLACES THE EXCEPTION
def example_default():
    cursor = iter([None, "Blue"])
    missing = object()  # A unique marker that cannot equal an input by identity.
    first = next(cursor, missing)
    print(first is None)     # => True
    print(first is missing)  # => False
    print(next(cursor, missing))  # => Blue
    print(next(cursor, missing) is missing)  # => True


# example_default()
# next(cursor, default) returns default only when the cursor is exhausted.
# Using None as the default is ambiguous if None is a valid input item.
# A unique sentinel and an identity check resolve that ambiguity.


# SECTION 3 — A DEFAULT DOES NOT CATCH EVERY ERROR
# next(123, "done") still raises TypeError because 123 is not an iterator.
# The default handles StopIteration, not arbitrary failures.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Consume an empty iterator with and without a default.
# ANSWER / CODE: ______________________________________________
# 2. Why is None sometimes a poor exhaustion marker?
# ANSWER / CODE: ______________________________________________
# 3. After consuming one item from iter([1, 2, 3]), predict list(cursor).
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Exhaustion is normal; distinguish it from an actual data value.

# ============================================================
# END OF LESSON
# ============================================================

