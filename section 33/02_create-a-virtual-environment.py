# ============================================================
# FILE: 02_create-a-virtual-environment.py
# TOPIC: Creating an Environment
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# Terminal commands are comments: run them in a terminal, not Python.

# LESSON OBJECTIVES
# 1. Create a venv using the intended interpreter.
# 2. Locate its interpreter and package directory.

# SECTION 1 — WINDOWS POWERSHELL
# Start in the bootcamp repository root. Create one shared learning
# environment at the root so sections 33 and 34 can use it.
# These are TERMINAL commands; do not paste the leading #.
#
# py --version
# py -m venv .venv
# .\.venv\Scripts\python.exe --version
#
# If py is unavailable but python works, use python -m venv .venv.
# If neither works, configure an installed interpreter before proceeding.
# Choose a version already installed when using py -3.X -m venv .venv;
# 3.X is a placeholder, not a literal command.
#
# macOS/Linux equivalent (bash/zsh):
# python3 -m venv .venv
# ./.venv/bin/python --version

# SECTION 2 — INSPECT THE RESULT
from pathlib import Path


def example_environment_layout():
    root = Path(__file__).resolve().parent.parent
    environment = root / ".venv"
    print(environment)
    print((environment / "pyvenv.cfg").is_file())
    # => True after creating the root environment.
    print((environment / "Scripts" / "python.exe").is_file())
    # => True for the Windows environment used in these lessons.


# example_environment_layout()
# Windows normally stores packages under .venv/Lib/site-packages.
# POSIX systems use bin for executables and a versioned lib directory.
# pyvenv.cfg records information about the base installation.
# Do not edit generated environment files as a way to change Python.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Create the root .venv and inspect pyvenv.cfg.
# ANSWER / CODE: ______________________________________________
# 2. Where are the Windows interpreter and installed packages?
# ANSWER / CODE: ______________________________________________
# 3. Does creating a venv automatically activate it?
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Create an environment with the interpreter you intend to use.

# ============================================================
# END OF LESSON
# ============================================================

