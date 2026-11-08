# ============================================================
# FILE: 01_formatting-and-linting.py
# TOPIC: Formatting versus Linting
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply formatting versus linting to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# A formatter standardizes layout; a linter finds selected suspicious patterns.
# Neither proves the program meets requirements. Use a check-only mode before
# changing unfamiliar code. Keep tool configuration and compatible versions in
# version control. Limit adoption to a chosen project rather than reformatting
# an entire learning repository accidentally. Ruff commands are in the guide.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
import ast

def example():
    source = "def add(a, b):\n    return a + b\n"
    tree = ast.parse(source)
    print(isinstance(tree, ast.Module))  # => True
    # Syntax validity does not prove add satisfies a business requirement.


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Which tool changes presentation and which reports suspicious code?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Run a check-only linter on one copy of a lesson and explain a finding.
# ANSWER / CODE: ______________________________________________

# 3. Why can syntactically valid code still be wrong?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: A formatter standardizes layout; a linter finds selected
# suspicious patterns.
# ============================================================
# END OF LESSON
# ============================================================
