# ============================================================
# FILE: 05_streaming-and-space-tradeoffs.py
# TOPIC: Reduce Intermediate Storage
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Compare list and generator intermediates.
# 2. Account for retained output and caches.

# SECTION 1 - UNDERSTAND THE IDEA
# A generator can avoid storing a transformed list when the consumer needs only
# an aggregate. It is not automatically faster, and it is consumed once. Sorting
# still needs all input; a Counter retains each distinct key. Caches trade memory
# for repeated speed. Measure both time and peak allocation for your workload.

# SECTION 2 - WORKED EXAMPLES
def eager_total(n):
    return sum([i * i for i in range(n)])

def streaming_total(n):
    return sum(i * i for i in range(n))

def example_streaming():
    print(eager_total(10), streaming_total(10))  # => 285 285
    print(eager_total(0), streaming_total(0))    # => 0 0

# example_streaming()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Measure peak allocation for both functions on the same n.
# ANSWER / CODE: ______________________________________________
# 2. Explain why sorted(generator) still materializes data.
# ANSWER / CODE: ______________________________________________
# 3. Identify a cache whose keys grow without a bound.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Remove unnecessary intermediates while accounting for final retained state.

# ============================================================
# END OF LESSON
# ============================================================
