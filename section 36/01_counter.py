# ============================================================
# FILE: 01_counter.py
# TOPIC: Count Listening Events
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Count repeated values.
# 2. Distinguish counts from a set.

# SECTION 1 - UNDERSTAND THE IDEA
# Counter is a dictionary subclass mapping each item to a count. Missing keys
# read as zero without insertion. most_common ranks counts; ties follow first
# encounter order. update adds counts rather than replacing existing counts.
# A count of zero can remain stored; len(counter) is the number of stored keys.

# SECTION 2 - WORKED EXAMPLES
from collections import Counter

def example_counts():
    plays = Counter(["Rush", "Yes", "Rush"])
    print(plays.most_common(2))  # => [('Rush', 2), ('Yes', 1)]
    print(plays["Genesis"])    # => 0
    print("Genesis" in plays)   # => False
    plays.update(["Yes", "Yes"])
    print(plays["Yes"])        # => 3
    print(plays.total())        # => 5

# example_counts()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Count titles in a playlist containing duplicates.
# ANSWER / CODE: ______________________________________________
# 2. Predict the count after two update calls.
# ANSWER / CODE: ______________________________________________
# 3. Compare len(plays), sum(plays.values()), and len(set(playlist)).
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Use Counter when frequency matters, not just membership.

# ============================================================
# END OF LESSON
# ============================================================
