# ============================================================
# FILE: 05_groupby.py
# TOPIC: Group Consecutive Items
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Recognize adjacency-based grouping.
# 2. Sort by the same grouping key.

# SECTION 1 - UNDERSTAND THE IDEA
# groupby groups consecutive equal keys, not every matching item everywhere.
# Sort by the grouping key when you want one group per key. Each group iterator
# shares the underlying input: consume it before advancing the outer iterator.
# Sorting requires materializing the data and costs O(n log n).

# SECTION 2 - WORKED EXAMPLES
from itertools import groupby

def example_grouping():
    artists = ["Rush", "Yes", "Rush"]
    print([(key, len(list(group))) for key, group in groupby(artists)])
    # => [('Rush', 1), ('Yes', 1), ('Rush', 1)]
    print([(key, len(list(group))) for key, group in groupby(sorted(artists))])
    # => [('Rush', 2), ('Yes', 1)]

# example_grouping()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Group records by artist using key=lambda record: record["artist"].
# ANSWER / CODE: ______________________________________________
# 2. Compare groupby with defaultdict for unsorted input.
# ANSWER / CODE: ______________________________________________
# 3. Explain why saving unconsumed group iterators can lose access to their items.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: groupby recognizes runs; it is not a general dictionary grouping operation.

# ============================================================
# END OF LESSON
# ============================================================
