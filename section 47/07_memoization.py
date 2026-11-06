# ============================================================
# FILE: 07_memoization.py
# TOPIC: Avoid Repeated Subproblems
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Compare repeated recursion with memoization.
# 2. Account for cache storage and recursion depth.

# SECTION 1 - UNDERSTAND THE IDEA
# Memoization stores results by input. Naive Fibonacci repeats many subproblems;
# a cached version computes each n once. It still uses recursion and cache
# space, so an iterative version may be preferable. For growing integers,
# arithmetic itself is not truly constant-cost; simple complexity models often
# count arithmetic operations separately from their bit cost.

# SECTION 2 - WORKED EXAMPLES
from functools import cache

@cache
def fibonacci(n):
    if type(n) is not int or n < 0:
        raise ValueError("n must be a nonnegative integer")
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def example_memoization():
    fibonacci.cache_clear()
    print(fibonacci(10))  # => 55
    print(fibonacci.cache_info().currsize)  # => 11

# example_memoization()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Implement an iterative version retaining only two previous values.
# ANSWER / CODE: ______________________________________________
# 2. Explain why caching a random or time-dependent function changes behavior.
# ANSWER / CODE: ______________________________________________
# 3. Compare cache size with the number of distinct subproblems.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Memoization trades retained results for avoided work.

# ============================================================
# END OF LESSON
# ============================================================
