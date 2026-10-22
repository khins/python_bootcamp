# ============================================================
# FILE: 11_generator-cleanup-and-delayed-errors.py
# TOPIC: Cleanup and Delayed Errors
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# All examples use the standard library; no packages need installation.

# LESSON OBJECTIVES
# 1. Recognize errors that occur during consumption.
# 2. Close a partially consumed generator explicitly.

from contextlib import closing


# SECTION 1 — BODY VALIDATION IS DEFERRED
def positive_countdown(start):
    if start < 1:
        raise ValueError("start must be positive")
    while start:
        yield start
        start -= 1


def example_delayed_error():
    values = positive_countdown(0)
    print("Created")  # => Created; the body has not run yet.
    try:
        next(values)
    except ValueError as error:
        print(error)  # => start must be positive


# example_delayed_error()
# If callers need immediate validation, validate in an ordinary outer
# function and return a generator created by a separate inner function.


# SECTION 2 — CLEANUP AFTER PARTIAL CONSUMPTION
def tracked_items():
    print("Started")
    try:
        yield "Signals"
        yield "Blue"
    finally:
        print("Cleaned up")


def example_explicit_close():
    items = tracked_items()
    print(next(items))  # => Started, then Signals
    items.close()      # => Cleaned up
    print(next(items, "Finished"))  # => Finished


# example_explicit_close()


# SECTION 3 — GUARANTEE CLOSE ON LEAVING A BLOCK
def example_closing_context():
    with closing(tracked_items()) as items:
        print(next(items))  # => Started, then Signals
    # => Cleaned up


# example_closing_context()
# close() on a suspended generator initiates termination and runs its
# active finally cleanup. Do not yield another value while closing.
# Closing a generator that has never started does not enter its body.
# A loop's break alone is not a deterministic cleanup mechanism.
# contextlib.closing calls close() on block exit; section 37 develops
# context managers in depth. Prefer explicit file ownership when streaming.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. When does positive_countdown(0) raise: creation or first next()?
# ANSWER / CODE: ______________________________________________
# 2. Add a break inside a closing block and predict the cleanup order.
# ANSWER / CODE: ______________________________________________
# 3. Why should a file-owning generator not rely on garbage collection?
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Lazy execution defers errors, so plan resource lifetimes explicitly.

# ============================================================
# END OF LESSON
# ============================================================

