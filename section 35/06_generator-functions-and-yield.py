# ============================================================
# FILE: 06_generator-functions-and-yield.py
# TOPIC: Generator Functions and yield
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# All examples use the standard library; no packages need installation.

# LESSON OBJECTIVES
# 1. Write a generator function.
# 2. Observe suspension and local state.

# SECTION 1 — yield SUSPENDS A FUNCTION
def countdown(start):
    while start > 0:
        yield start
        start -= 1


def example_generator_countdown():
    numbers = countdown(3)
    print(next(numbers))  # => 3
    print(next(numbers))  # => 2
    print(list(numbers))  # => [1]
    print(list(countdown(0)))  # => []


# example_generator_countdown()
# Calling countdown creates a generator object, which is an iterator.
# Its body starts when you ask for the first value.
# yield supplies a value and pauses; locals and execution position remain.
# On resumption, execution continues immediately after the yield.
# Reaching the end of the function exhausts the generator.


# SECTION 2 — WATCH WHEN THE BODY RUNS
def announce_albums():
    print("Starting")
    yield "Signals"
    print("Resuming")
    yield "Blue"
    print("Finished")


def example_execution_order():
    albums = announce_albums()
    print("Created")      # => Created
    print(next(albums))   # => Starting, then Signals (separate lines)
    print(next(albums))   # => Resuming, then Blue
    print(next(albums, "No more"))  # => Finished, then No more


# example_execution_order()
# Generator syntax replaces the manual state bookkeeping in Countdown.
# It does not automatically make data reusable: create a new generator
# object for a new traversal.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Write a generator yielding squares from 1 through a supplied limit.
# ANSWER / CODE: ______________________________________________
# 2. Explain how yield differs from return.
# ANSWER / CODE: ______________________________________________
# 3. Predict the output if announce_albums() is called but never consumed.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: yield pauses execution and preserves the function's local state.

# ============================================================
# END OF LESSON
# ============================================================

