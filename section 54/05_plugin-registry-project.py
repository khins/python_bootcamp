# ============================================================
# FILE: 05_plugin-registry-project.py
# TOPIC: Project: Inspectable Plugin Registry
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply project: inspectable plugin registry to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# plugin_registry.py uses an explicit registry object and class decorator. It
# checks that an unbound run method can accept self and text; this does not prove
# its semantics, return type, or constructor requirements. Registration happens
# at import, but running a plugin is explicit. Unknown plugin names raise KeyError.
# Do not automatically import arbitrary untrusted code as a plugin discovery step.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from plugin_registry import registry

def example():
    print(registry.run("upper", "Signals"))  # => SIGNALS
    print(registry.run("strip", " Blue "))  # => Blue


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Which errors can signature binding detect?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Add a reverse plugin and tests for duplicate and unknown names.
# ANSWER / CODE: ______________________________________________

# 3. Why choose a class decorator instead of a metaclass here?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: plugin_registry.py uses an explicit registry object and class
# decorator.
# ============================================================
# END OF LESSON
# ============================================================
