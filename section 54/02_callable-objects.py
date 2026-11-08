# ============================================================
# FILE: 02_callable-objects.py
# TOPIC: Callable Objects with __call__
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply callable objects with __call__ to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# An instance implementing __call__ can be used like a function while retaining
# state. This can simplify configured strategies. callable checks whether an
# object appears callable; it does not prove every argument list is valid.
# Stateful callables can make tests order-dependent if shared carelessly.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
class Prefixer:
    def __init__(self, prefix):
        self.prefix = prefix
        self.calls = 0
    def __call__(self, text):
        self.calls += 1
        return f"{self.prefix}: {text}"

def example():
    label = Prefixer("Album")
    print(label("Signals"))  # => Album: Signals
    print(label.calls, callable(label))  # => 1 True


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. How does __call__ differ from __init__?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Build a callable that validates a numeric range.
# ANSWER / CODE: ______________________________________________

# 3. When would a plain function or closure be clearer?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: An instance implementing __call__ can be used like a function
# while retaining state.
# ============================================================
# END OF LESSON
# ============================================================
