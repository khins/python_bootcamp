# ============================================================
# FILE: 01_big-o.py
# TOPIC: Reason About Growth with Big O
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Define input size before estimating cost.
# 2. Separate time and extra space.

# SECTION 1 - UNDERSTAND THE IDEA
# Big O describes growth as input size n increases, not an exact stopwatch time.
# O(1), O(log n), O(n), O(n log n), and O(n^2) describe common growth patterns.
# A loop over n items is O(n) only when each body operation is bounded. Two
# nested independent n-sized loops usually produce n^2 work. State whether you
# mean worst-case, average-case, or amortized behavior. Constants still matter.

# SECTION 2 - WORKED EXAMPLES
def example_work_counts():
    for n in [10, 100, 1000]:
        print(n, n, n * n)
    # => 10 10 100 / 100 100 10000 / 1000 1000 1000000

# example_work_counts()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Count comparisons in a linear search that misses.
# ANSWER / CODE: ______________________________________________
# 2. Explain why two sequential loops are O(n), not O(n^2).
# ANSWER / CODE: ______________________________________________
# 3. Identify the input-size variable for a dictionary of artists containing track lists.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Complexity is a growth model with stated assumptions.

# ============================================================
# END OF LESSON
# ============================================================
