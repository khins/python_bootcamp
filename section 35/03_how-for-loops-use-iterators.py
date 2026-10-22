# ============================================================
# FILE: 03_how-for-loops-use-iterators.py
# TOPIC: How for Loops Consume Iterators
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# All examples use the standard library; no packages need installation.

# LESSON OBJECTIVES
# 1. Connect for loops to the iterator protocol.
# 2. Explain early exits and shared iterator state.

# SECTION 1 — APPROXIMATE A for LOOP
def example_manual_loop():
    cursor = iter(["Signals", "Blue"])
    while True:
        try:
            album = next(cursor)
        except StopIteration:
            break
        print(album)
    # => Signals
    # => Blue


# example_manual_loop()
# A for loop obtains an iterator and repeatedly requests the next item.
# Keep the try block narrow: StopIteration from unrelated loop-body code
# should not accidentally be mistaken for exhaustion of this iterator.


# SECTION 2 — break DOES NOT RESET THE POSITION
def example_break_and_resume():
    cursor = iter([10, 20, 30])
    for number in cursor:
        print(number)  # => 10
        break
    print(next(cursor))  # => 20
    print(list(cursor))  # => [30]


# example_break_and_resume()


# SECTION 3 — TWO NAMES CAN SHARE ONE POSITION
def example_shared_cursor():
    cursor = iter(["a", "b", "c"])
    alias = cursor
    print(next(cursor))  # => a
    print(next(alias))   # => b
    print(list(cursor))  # => ['c']


# example_shared_cursor()
# This connects to section 16: assignment binds another name to the
# same iterator. It does not create an independent traversal.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Rewrite the manual loop as a for loop.
# ANSWER / CODE: ______________________________________________
# 2. Predict two consecutive for loops over the same iterator.
# ANSWER / CODE: ______________________________________________
# 3. Contrast alias = cursor with alias = iter(original_list).
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Loops and next() advance the same underlying iterator state.

# ============================================================
# END OF LESSON
# ============================================================

