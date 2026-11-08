# ============================================================
# FILE: 04_slots.py
# TOPIC: Controlling Instance Layout with __slots__
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply controlling instance layout with __slots__ to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# __slots__ declares fixed instance attributes and can avoid an instance __dict__.
# It is a layout tool, not immutability or access control. An unslotted subclass
# usually gains a dictionary again. Slots from bases remain available. Include
# __weakref__ when instances must support weak references and a base does not
# already provide that support. Measure memory before assuming a benefit.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
class Point:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x, self.y = x, y

def example():
    point = Point(2, 3)
    point.x = 4
    print(point.x)  # => 4
    try:
        point.label = "home"
    except AttributeError:
        print("undeclared attribute rejected")


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Does __slots__ prevent changing x?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Compare an unslotted subclass and a subclass with __slots__ = ().
# ANSWER / CODE: ______________________________________________

# 3. When would a normal dictionary-backed instance be simpler?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: __slots__ declares fixed instance attributes and can avoid an
# instance __dict__.
# ============================================================
# END OF LESSON
# ============================================================
