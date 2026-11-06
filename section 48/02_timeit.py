# ============================================================
# FILE: 02_timeit.py
# TOPIC: Time Small Operations with timeit
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Repeat measurements.
# 2. Keep setup and equivalent work under control.

# SECTION 1 - UNDERSTAND THE IDEA
# timeit repeats a callable and returns elapsed seconds for all repetitions.
# Divide by number for a per-call estimate. repeat runs several trials; inspect
# the spread and a minimum as a lower-bound estimate. Do not time printing.
# Reusing an exhausted generator makes later trials measure different work.

# SECTION 2 - WORKED EXAMPLES
from timeit import repeat

def example_microbenchmark():
    values = list(range(1000))
    times = repeat(lambda: sum(values), number=100, repeat=3)
    print(len(times))  # => 3
    print("best seconds per call:", min(times) / 100)  # Varies.
    print("trial totals:", times)  # Varies.

# example_microbenchmark()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Compare sum(list) and a Python loop on identical data.
# ANSWER / CODE: ______________________________________________
# 2. Show why list(generator) on the same generator gives a misleading benchmark.
# ANSWER / CODE: ______________________________________________
# 3. Move input construction outside timing, then explain when it belongs inside.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Benchmark the same operation repeatedly, with setup costs accounted for.

# ============================================================
# END OF LESSON
# ============================================================
