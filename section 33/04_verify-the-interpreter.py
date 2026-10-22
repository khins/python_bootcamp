# ============================================================
# FILE: 04_verify-the-interpreter.py
# TOPIC: Verifying the Interpreter
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# Terminal commands are comments: run them in a terminal, not Python.

# LESSON OBJECTIVES
# 1. Identify the running interpreter.
# 2. Diagnose an IDE/terminal interpreter mismatch.

import sys
from pathlib import Path


# SECTION 1 — ASK THE RUNNING PROCESS
def example_interpreter_details():
    print("Executable:", sys.executable)
    print("Version:", sys.version.split()[0])
    print("Environment:", sys.prefix)
    print("Base:", sys.base_prefix)
    print("In venv:", sys.prefix != sys.base_prefix)
    # Paths and version depend on your installation.


# example_interpreter_details()

# SECTION 2 — VERIFY THE PROJECT ENVIRONMENT
def example_expected_interpreter():
    root = Path(__file__).resolve().parent.parent
    expected = root / ".venv" / "Scripts" / "python.exe"
    print("Expected on Windows:", expected)
    print("Actual:", Path(sys.executable).resolve())
    # Compare these paths when imports work in one place but not another.


# example_expected_interpreter()
# In VS Code with the Python extension, select the project's interpreter
# using Python: Select Interpreter. Choose .venv/Scripts/python.exe.
# Check the running process again after selection; an existing terminal
# or independently configured runner may still use a different Python.
# VIRTUAL_ENV alone is not proof: explicit invocation needs no activation.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Compare sys.executable from your IDE and terminal.
# ANSWER / CODE: ______________________________________________
# 2. What does sys.prefix != sys.base_prefix tell you?
# ANSWER / CODE: ______________________________________________
# 3. Why is an activated terminal insufficient proof about an IDE runner?
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Inspect the Python process that actually runs your code.

# ============================================================
# END OF LESSON
# ============================================================

