# ============================================================
# FILE: 06_partial.py
# TOPIC: Configure Functions with partial
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Pre-fill function arguments.
# 2. Keep the original callable reusable.

# SECTION 1 - UNDERSTAND THE IDEA
# partial creates a callable with selected arguments already supplied. This is
# useful when an API expects a function with fewer arguments. It does not call
# the original function at creation time. Later keywords can override stored
# keywords; positional arguments are prepended, so avoid duplicate assignments.

# SECTION 2 - WORKED EXAMPLES
from functools import partial

def label(title, *, artist, prefix="Playing"):
    return f"{prefix}: {title} by {artist}"

def example_partial():
    rush_label = partial(label, artist="Rush")
    print(rush_label("YYZ"))  # => Playing: YYZ by Rush
    print(rush_label("Blue", artist="Joni Mitchell"))
    # => Playing: Blue by Joni Mitchell

# example_partial()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Create a callable that always uses prefix="Favorite".
# ANSWER / CODE: ______________________________________________
# 2. Explain partial versus immediately calling label.
# ANSWER / CODE: ______________________________________________
# 3. Pass a configured callable to map.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: partial packages configuration into a reusable callable.

# ============================================================
# END OF LESSON
# ============================================================
