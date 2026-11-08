# ============================================================
# FILE: 02_attribute-lookup.py
# TOPIC: Attribute Lookup Precedence
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply attribute lookup precedence to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# For normal instance lookup, data descriptors take priority over the instance
# mapping; the instance mapping takes priority over non-data descriptors and
# other class attributes. A descriptor with __set__ or __delete__ is a data
# descriptor. Methods are non-data descriptors. Missing lookup can then invoke
# __getattr__. Custom __getattribute__ can alter this normal behavior.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
class DataValue:
    def __get__(self, instance, owner=None):
        return self if instance is None else "descriptor"
    def __set__(self, instance, value):
        raise AttributeError("read only")

class NonDataValue:
    def __get__(self, instance, owner=None):
        return "class default"

class Example:
    data = DataValue()
    other = NonDataValue()

def example():
    item = Example()
    item.__dict__["data"] = "hidden"
    item.other = "instance"
    print(item.data, item.other)  # => descriptor instance


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Which value wins for data and why?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Remove the other instance attribute and predict its next lookup.
# ANSWER / CODE: ______________________________________________

# 3. Does writing directly to __dict__ necessarily bypass descriptor reads?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: For normal instance lookup, data descriptors take priority
# over the instance mapping; the instance mapping takes priority over non-data
# descriptors and other class attributes.
# ============================================================
# END OF LESSON
# ============================================================
