# ============================================================
# FILE: 05_run-a-static-checker.py
# TOPIC: Run mypy and Interpret Diagnostics
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Run a checker separately from Python.
# 2. Repair errors rather than silencing them.

# SECTION 1 - UNDERSTAND THE IDEA
# Use the environment setup in learning-guide.txt, then run these PowerShell
# commands from the repository root:
# .\.venv\Scripts\python.exe -m mypy --strict "section 38/typed_catalog.py"
# The supplied corrected project should report success. To practice a failure,
# copy it into a scratch file and change one call to supply a string duration.
# Run mypy on that file, read the line/error category, then repair the contract.
# Do not scatter type: ignore or Any merely to obtain a green report.

# SECTION 2 - WORKED EXAMPLES
def total_seconds(durations: list[int]) -> int:
    return sum(durations)

def example_checked_function() -> None:
    print(total_seconds([100, 200]))  # => 300
    print(total_seconds([]))          # => 0

# example_checked_function()
# Wrong in a scratch file: total_seconds(["100"])
# mypy should flag a list item with incompatible type str (expected int).
# Exact diagnostic wording can vary across checker releases.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Run the corrected project through mypy --strict.
# ANSWER / CODE: ______________________________________________
# 2. Introduce and repair a wrong argument type in a copy.
# ANSWER / CODE: ______________________________________________
# 3. Explain why passing static checks does not prove an algorithm is correct.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Use diagnostics to refine contracts and then test runtime behavior.

# REFERENCES
# https://mypy.readthedocs.io/en/stable/getting_started.html

# ============================================================
# END OF LESSON
# ============================================================
