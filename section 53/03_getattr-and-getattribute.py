# ============================================================
# FILE: 03_getattr-and-getattribute.py
# TOPIC: __getattr__ and __getattribute__
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply __getattr__ and __getattribute__ to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# __getattribute__ participates in every ordinary attribute read. __getattr__ is
# fallback after normal lookup raises AttributeError. Delegate through
# object.__getattribute__ to avoid infinite recursion. Raise AttributeError for
# unknown names so getattr defaults and hasattr behave correctly. Avoid hiding
# real bugs by returning a made-up value for every misspelled name.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
class Settings:
    def __init__(self):
        self.values = {"theme": "dark"}
    def __getattribute__(self, name):
        return object.__getattribute__(self, name)
    def __getattr__(self, name):
        values = object.__getattribute__(self, "values")
        if name in values:
            return values[name]
        raise AttributeError(name)

def example():
    settings = Settings()
    print(settings.theme)  # => dark
    print(getattr(settings, "missing", "default"))  # => default
    print(hasattr(settings, "missing"))  # => False


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Why would reading self.values inside a naive __getattribute__ recurse?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Support one documented alias while rejecting other missing names.
# ANSWER / CODE: ______________________________________________

# 3. What exception signals missing attributes?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: __getattribute__ participates in every ordinary attribute
# read.
# ============================================================
# END OF LESSON
# ============================================================
