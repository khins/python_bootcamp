# ============================================================
# FILE: 03_cprofile.py
# TOPIC: Locate Expensive Functions with cProfile
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Read total versus cumulative time.
# 2. Profile a complete workflow.

# SECTION 1 - UNDERSTAND THE IDEA
# cProfile records function call counts and timings. tottime excludes time in
# subcalls; cumtime includes it. Sort by cumulative time to locate expensive
# paths, then inspect their children. Profiling introduces overhead and is for
# attribution, while timeit helps compare focused alternatives.

# SECTION 2 - WORKED EXAMPLES
import cProfile
import pstats
from io import StringIO

def workload():
    return sum(number * number for number in range(5000))

def example_profile():
    profiler = cProfile.Profile()
    result = profiler.runcall(workload)
    output = StringIO()
    pstats.Stats(profiler, stream=output).strip_dirs().sort_stats("cumulative").print_stats(5)
    print(result)  # => 41654167500
    print(output.getvalue())  # Calls/timings and function paths vary.

# example_profile()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Profile your section 36 analyzer.
# ANSWER / CODE: ______________________________________________
# 2. Identify the difference between a slow caller and a slow function body.
# ANSWER / CODE: ______________________________________________
# 3. Use call counts to find unexpectedly repeated work.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Profile to locate work before choosing what to optimize.

# ============================================================
# END OF LESSON
# ============================================================
