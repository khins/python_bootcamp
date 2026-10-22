# ============================================================
# FILE: 08_troubleshooting-and-final-challenge.py
# TOPIC: Environment Troubleshooting and Review
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# Terminal commands are comments: run them in a terminal, not Python.

# LESSON OBJECTIVES
# 1. Diagnose common setup failures.
# 2. Prepare the environment for section 34.

import importlib.util
import sys


# SECTION 1 — A SMALL DIAGNOSTIC
def example_diagnostics():
    print("Python:", sys.executable)
    print("Virtual environment:", sys.prefix != sys.base_prefix)
    for module in ("requests", "bs4"):
        spec = importlib.util.find_spec(module)
        print(module, "not found" if spec is None else spec.origin)
    # A local requests.py can resolve successfully but shadow the real package.


# example_diagnostics()

# SECTION 2 — FOLLOW THE EVIDENCE
# ModuleNotFoundError: check sys.executable, then that Python's pip show.
# Activation blocked: use .venv/Scripts/python.exe directly.
# python not found: on Windows try py; otherwise locate/configure Python.
# pip missing in an environment: inspect creation errors; where supported,
# run that interpreter with -m ensurepip --upgrade before trying pip again.
# Import resolves to your own file: rename the conflicting source module.
# Installation fails: read the first meaningful error; check connectivity,
# supported Python versions, and platform requirements before reinstalling.

# SECTION 3 — FINAL CHALLENGE
# 1. Create or reuse the root .venv.
# 2. Install section 34 dependencies:
# .\.venv\Scripts\python.exe -m pip install -r "section 34/requirements.txt"
# 3. Select that interpreter in your IDE.
# 4. Run example_diagnostics and explain each result.
# 5. Save a requirements snapshot and record your Python version.
# 6. Recreate a second environment and verify imports there.
# Keep notes explaining each command rather than only copying commands.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. A terminal imports bs4 but your IDE cannot. What do you compare first?
# ANSWER / CODE: ______________________________________________
# 2. How do you use an environment without activating it?
# ANSWER / CODE: ______________________________________________
# 3. Complete the six-step challenge and explain the difference between venv and pip.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Diagnose interpreter selection before changing installed packages.

# ============================================================
# END OF LESSON
# ============================================================

