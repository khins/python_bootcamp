# ============================================================
# FILE: 01_descriptors.py
# TOPIC: Descriptors and Managed Attributes
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply descriptors and managed attributes to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# A descriptor implements __get__, __set__, or __delete__ and is stored on a
# class. Python invokes it during attribute access. __set_name__ learns the name
# given in the owner class. Store per-instance values on each instance, not in
# the shared descriptor itself. Class access passes instance=None to __get__.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
class Nonnegative:
    def __set_name__(self, owner, name):
        self.storage_name = "_" + name
    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return getattr(instance, self.storage_name)
    def __set__(self, instance, value):
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("expected a nonnegative integer")
        setattr(instance, self.storage_name, value)

class Track:
    seconds = Nonnegative()
    def __init__(self, seconds):
        self.seconds = seconds

def example():
    first, second = Track(90), Track(120)
    first.seconds = 100
    print(first.seconds, second.seconds)  # => 100 120


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Why is storage_name kept on the descriptor but the value on the instance?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Reject negative assignment and confirm the old value remains.
# ANSWER / CODE: ______________________________________________

# 3. Why handle instance=None?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: A descriptor implements __get__, __set__, or __delete__ and is
# stored on a class.
# ============================================================
# END OF LESSON
# ============================================================
