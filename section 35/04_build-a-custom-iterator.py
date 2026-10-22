# ============================================================
# FILE: 04_build-a-custom-iterator.py
# TOPIC: Building a Custom Iterator
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# All examples use the standard library; no packages need installation.

# LESSON OBJECTIVES
# 1. Implement __iter__ and __next__.
# 2. Keep exhaustion permanent.

# SECTION 1 — THE ITERATOR PROTOCOL
class Countdown:
    def __init__(self, start):
        if not isinstance(start, int):
            raise TypeError("start must be an integer")
        if start < 0:
            raise ValueError("start must be nonnegative")
        self.remaining = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.remaining <= 0:
            raise StopIteration
        value = self.remaining
        self.remaining -= 1
        return value


# __iter__ returns this iterator, not a fresh Countdown.
# __next__ returns one item, advances state, and raises StopIteration
# when there are no items. Do not reset remaining in __iter__.


# SECTION 2 — USE BUILT-IN CONSUMERS
def example_countdown():
    countdown = Countdown(3)
    print(iter(countdown) is countdown)  # => True
    print(next(countdown))  # => 3
    print(list(countdown))  # => [2, 1]
    print(list(countdown))  # => []
    print(list(Countdown(0)))  # => []


# example_countdown()


# SECTION 3 — REVIEW THE DESIGN
# This object is a one-pass iterator. A second traversal needs a fresh
# instance. A zero-length countdown is valid and immediately exhausted.
# Because bool subclasses int, this validation accepts True as 1.
# To reject Boolean inputs, explicitly check isinstance(start, bool).

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Implement an iterator that yields multiples of 5 up to a limit.
# ANSWER / CODE: ______________________________________________
# 2. Why must __iter__ return self for this iterator?
# ANSWER / CODE: ______________________________________________
# 3. Add a test that calls next() twice after exhaustion.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: A custom iterator exposes its state through two special methods.

# ============================================================
# END OF LESSON
# ============================================================

