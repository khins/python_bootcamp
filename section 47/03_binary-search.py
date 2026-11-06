# ============================================================
# FILE: 03_binary-search.py
# TOPIC: Search Sorted Data with bisect
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Use insertion positions carefully.
# 2. Include preprocessing in the cost model.

# SECTION 1 - UNDERSTAND THE IDEA
# Binary search halves the remaining range each step: O(log n) comparisons on
# an indexable sorted sequence. bisect_left returns an insertion position, not
# proof of a match. Verify bounds and equality. Sorting costs O(n log n), and
# inserting into a list still costs O(n) despite fast position lookup.

# SECTION 2 - WORKED EXAMPLES
from bisect import bisect_left

def contains_title(sorted_titles, title):
    position = bisect_left(sorted_titles, title)
    return position < len(sorted_titles) and sorted_titles[position] == title

def example_binary():
    titles = sorted(["Signals", "Blue", "Fragile"])
    print(contains_title(titles, "Blue"))     # => True
    print(contains_title(titles, "Missing"))  # => False
    print(contains_title([], "Blue"))        # => False

# example_binary()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Find the first duplicate using bisect_left.
# ANSWER / CODE: ______________________________________________
# 2. Explain why binary search on unsorted input is invalid.
# ANSWER / CODE: ______________________________________________
# 3. Compare one search versus thousands when sorting is needed first.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Fast lookup depends on maintaining the sorted-data invariant.

# ============================================================
# END OF LESSON
# ============================================================
