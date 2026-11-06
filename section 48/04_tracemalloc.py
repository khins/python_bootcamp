# ============================================================
# FILE: 04_tracemalloc.py
# TOPIC: Measure Python Allocation Peaks
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Read current and peak traced memory.
# 2. Recognize measurement boundaries.

# SECTION 1 - UNDERSTAND THE IDEA
# tracemalloc tracks Python allocations made after tracing starts. Current
# memory is what remains traced; peak is the largest traced total during the
# interval. It is not process RSS and may omit native allocations. A snapshot
# can group allocations by source line. Stop tracing when the experiment ends.

# SECTION 2 - WORKED EXAMPLES
import tracemalloc

def example_memory():
    tracemalloc.start()
    try:
        values = [str(n) for n in range(2000)]
        current, peak = tracemalloc.get_traced_memory()
        print(peak >= current > 0)  # => True
        print(len(values))         # => 2000
        for statistic in tracemalloc.take_snapshot().statistics("lineno")[:2]:
            print(statistic)       # Source paths, sizes, and counts vary.
    finally:
        tracemalloc.stop()

# example_memory()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Compare tracing before versus after building the input.
# ANSWER / CODE: ______________________________________________
# 2. Delete a large result and inspect current versus peak.
# ANSWER / CODE: ______________________________________________
# 3. Explain why a shallow sys.getsizeof is not a nested object total.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: State what memory a tool measures and when observation begins.

# ============================================================
# END OF LESSON
# ============================================================
