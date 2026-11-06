# ============================================================
# FILE: 04_sorting-and-key-functions.py
# TOPIC: Sort with Explicit Keys
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Use stable sorting.
# 2. Avoid unnecessary repeated key work.

# SECTION 1 - UNDERSTAND THE IDEA
# Python sorting is stable: equal keys retain their input order. sorted creates
# a new list; list.sort mutates and returns None. Python's built-in sort has
# O(n log n) worst-case time and can exploit existing order. A key function is
# computed once per input item for that sort, not once per comparison.

# SECTION 2 - WORKED EXAMPLES
def example_sorting():
    rows = [{"title": "B", "year": 1982}, {"title": "A", "year": 1982},
            {"title": "C", "year": 1971}]
    print([r["title"] for r in sorted(rows, key=lambda r: r["year"])])
    # => ['C', 'B', 'A']: the 1982 tie preserves input order
    print([r["title"] for r in sorted(rows, key=lambda r: (r["year"], r["title"]))])
    # => ['C', 'A', 'B']

# example_sorting()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Sort by artist and descending year using a tuple key.
# ANSWER / CODE: ______________________________________________
# 2. Explain the extra memory implication of sorted.
# ANSWER / CODE: ______________________________________________
# 3. Implement insertion sort on five numbers, then explain why it is not your default for large input.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Use the built-in sort and state tie-breaking rules explicitly.

# ============================================================
# END OF LESSON
# ============================================================
