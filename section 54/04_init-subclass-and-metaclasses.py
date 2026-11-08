# ============================================================
# FILE: 04_init-subclass-and-metaclasses.py
# TOPIC: __init_subclass__ and Metaclasses
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply __init_subclass__ and metaclasses to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# __init_subclass__ runs when a subclass is created and suits inherited validation
# or registration. Call super cooperatively when supporting multiple inheritance.
# A metaclass controls class creation itself; type is the usual metaclass. Most
# registration tasks need only decorators or __init_subclass__, not a metaclass.
# Metaclass combinations can conflict, so use them only when simpler hooks cannot
# express the requirement.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
class NamedPlugin:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not isinstance(getattr(cls, "name", None), str):
            raise TypeError("plugins need a string name")

class Upper(NamedPlugin):
    name = "upper"

class Marked(type):
    def __new__(mcls, name, bases, namespace):
        namespace["created_by_hook"] = True
        return super().__new__(mcls, name, bases, namespace)

class Example(metaclass=Marked):
    pass

def example():
    print(Upper.name, Example.created_by_hook)  # => upper True


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Which hook can validate subclasses without a custom metaclass?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Define an invalid subclass inside try/except and observe when it fails.
# ANSWER / CODE: ______________________________________________

# 3. Explain why class creation and instance creation are different events.
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: __init_subclass__ runs when a subclass is created and suits
# inherited validation or registration.
# ============================================================
# END OF LESSON
# ============================================================
