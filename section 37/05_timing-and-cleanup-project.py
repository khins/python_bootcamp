# ============================================================
# FILE: 05_timing-and-cleanup-project.py
# TOPIC: Project: Timing Context Manager
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Measure elapsed time even on failure.
# 2. Use an injectable clock for deterministic checks.

# SECTION 1 - UNDERSTAND THE IDEA
# perf_counter measures elapsed duration; wall-clock date/time is unnecessary.
# Store the measurement in finally so exceptions still get timed. Injecting a
# clock lets tests verify exact arithmetic without sleeping. The timer does
# not suppress failures. Real elapsed times vary between machines and runs.

# SECTION 2 - WORKED EXAMPLES
from contextlib import contextmanager
from time import perf_counter

@contextmanager
def timed(clock=perf_counter):
    result = {}
    start = clock()
    try:
        yield result
    finally:
        result["elapsed"] = clock() - start

def example_timing():
    ticks = iter([10.0, 10.25])
    with timed(lambda: next(ticks)) as result:
        total = sum(range(10))
    print(total, result["elapsed"])  # => 45 0.25
    ticks = iter([20.0, 20.5])
    try:
        with timed(lambda: next(ticks)) as failed:
            raise ValueError("simulated failure")
    except ValueError:
        print(failed["elapsed"])     # => 0.5

# example_timing()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Build a class-based timer exposing elapsed after exit.
# ANSWER / CODE: ______________________________________________
# 2. Combine timing with a file manager and verify both cleanup and elapsed on error.
# ANSWER / CODE: ______________________________________________
# 3. Explain why checking an exact real duration is a fragile test.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Reliable timing and reliable cleanup both account for exceptions.

# ============================================================
# END OF LESSON
# ============================================================
