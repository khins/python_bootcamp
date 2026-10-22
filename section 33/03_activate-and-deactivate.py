# ============================================================
# FILE: 03_activate-and-deactivate.py
# TOPIC: Activation and Deactivation
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# Terminal commands are comments: run them in a terminal, not Python.

# LESSON OBJECTIVES
# 1. Activate a venv in the correct shell.
# 2. Use an environment without activation.

# SECTION 1 — ACTIVATION CHANGES COMMAND LOOKUP
# From the repository root, Windows PowerShell:
# .\.venv\Scripts\Activate.ps1
# python --version
# python -m pip --version
# deactivate
#
# Windows Command Prompt:
# .venv\Scripts\activate.bat
#
# macOS/Linux bash/zsh:
# source .venv/bin/activate
#
# Activation puts the environment's executable directory first on PATH.
# It applies to the current shell; a new terminal may need activation.
# deactivate restores shell settings. It does not delete packages.

# SECTION 2 — ACTIVATION IS OPTIONAL
# If PowerShell blocks Activate.ps1, use the interpreter directly:
# .\.venv\Scripts\python.exe -m pip --version
# .\.venv\Scripts\python.exe "section 33/04_verify-the-interpreter.py"
# There is no need to change execution policy to use this approach.
# A quoted executable path needs PowerShell's call operator:
# & "C:\path with spaces\.venv\Scripts\python.exe" --version

import sys


def example_current_interpreter():
    print(sys.executable)  # Actual running Python, not just a prompt label.
    print(sys.prefix != sys.base_prefix)  # => True when running in a venv.


# example_current_interpreter()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Activate, inspect the interpreter, and deactivate.
# ANSWER / CODE: ______________________________________________
# 2. Run this file with the environment's explicit interpreter path.
# ANSWER / CODE: ______________________________________________
# 3. Why does closing a terminal not uninstall dependencies?
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Activation is a convenience; the chosen executable controls Python.

# ============================================================
# END OF LESSON
# ============================================================

