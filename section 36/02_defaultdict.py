# ============================================================
# FILE: 02_defaultdict.py
# TOPIC: Group Records with defaultdict
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Build grouped lists.
# 2. Recognize when a factory runs.

# SECTION 1 - UNDERSTAND THE IDEA
# A defaultdict calls its factory when a missing key is accessed with [].
# Pass list, not list(): each new key gets its own list. get() does not invoke
# the factory. Reading a missing key with [] changes the dictionary.

# SECTION 2 - WORKED EXAMPLES
from collections import defaultdict

def example_groups():
    groups = defaultdict(list)
    for artist, title in [("Rush", "YYZ"), ("Yes", "Roundabout"), ("Rush", "Limelight")]:
        groups[artist].append(title)
    print(dict(groups))  # => {'Rush': ['YYZ', 'Limelight'], 'Yes': ['Roundabout']}
    print(groups.get("Genesis"))  # => None
    print("Genesis" in groups)    # => False
    print(groups["Genesis"])     # => []
    print("Genesis" in groups)    # => True

# example_groups()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Group album titles by decade.
# ANSWER / CODE: ______________________________________________
# 2. Use defaultdict(int) to total synthetic listening seconds.
# ANSWER / CODE: ______________________________________________
# 3. Explain why defaultdict(list()) is incorrect.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Factories create defaults only when a missing indexed key is requested.

# ============================================================
# END OF LESSON
# ============================================================
