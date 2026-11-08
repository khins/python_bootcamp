# ============================================================
# FILE: 01_inspect-and-signatures.py
# TOPIC: Inspecting Callable Signatures
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply inspecting callable signatures to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# inspect.signature describes parameters, defaults, and annotations. Signature.bind
# checks whether supplied arguments fit a signature without calling the function.
# It does not enforce annotation types. Inspecting members can trigger descriptors;
# inspect.getattr_static avoids normal dynamic attribute access when appropriate.
# Introspection helps tools and diagnostics, but does not replace clear interfaces.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
import inspect

def label(title: str, *, prefix="Album") -> str:
    return f"{prefix}: {title}"

def example():
    signature = inspect.signature(label)
    arguments = signature.bind("Signals", prefix="Now")
    print(dict(arguments.arguments))  # => {'title': 'Signals', 'prefix': 'Now'}
    try:
        signature.bind()
    except TypeError:
        print("missing argument")


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Does bind call label?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Apply defaults to bound arguments and inspect the result.
# ANSWER / CODE: ______________________________________________

# 3. Why might inspecting attributes have side effects?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: inspect.signature describes parameters, defaults, and
# annotations.
# ============================================================
# END OF LESSON
# ============================================================
