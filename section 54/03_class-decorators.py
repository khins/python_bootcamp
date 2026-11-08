# ============================================================
# FILE: 03_class-decorators.py
# TOPIC: Class Decorators
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply class decorators to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# A class decorator receives the newly created class and returns the object bound
# to its name. It can register or annotate a class without changing its metaclass.
# Returning the same class preserves its identity. Prefer an explicit decorator
# when opt-in behavior is clearer than automatic global registration.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
registry = {}

def register(cls):
    if cls.__name__ in registry:
        raise ValueError("duplicate plugin")
    registry[cls.__name__] = cls
    return cls

@register
class Uppercase:
    def run(self, text):
        return text.upper()

def example():
    print(registry["Uppercase"]().run("blue"))  # => BLUE


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. When does registration occur?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Add a second plugin and reject a duplicate registration.
# ANSWER / CODE: ______________________________________________

# 3. Why must a decorator return something deliberately?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: A class decorator receives the newly created class and returns
# the object bound to its name.
# ============================================================
# END OF LESSON
# ============================================================
