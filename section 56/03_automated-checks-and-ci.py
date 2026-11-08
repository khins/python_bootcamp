# ============================================================
# FILE: 03_automated-checks-and-ci.py
# TOPIC: Automated Checks and Continuous Integration
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply automated checks and continuous integration to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# CI runs repeatable checks on a clean machine. It reveals missing dependencies
# and assumptions hidden in a developer's environment. A failing command must
# produce a nonzero exit status. The supplied workflow-demo.yml is a reference,
# not an activated workflow. It tests only the section-55 project; earlier
# exercise files may intentionally contain unfinished or invalid practice code.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
import subprocess
import sys

def example():
    result = subprocess.run([sys.executable, "-c", "print('check passed')"],
                            capture_output=True, text=True, check=True)
    print(result.stdout.strip())  # => check passed


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Why use check=True?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Add a second project-specific check to a copy of the workflow.
# ANSWER / CODE: ______________________________________________

# 3. Why should CI avoid depending on a developer database?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: CI runs repeatable checks on a clean machine.
# ============================================================
# END OF LESSON
# ============================================================
