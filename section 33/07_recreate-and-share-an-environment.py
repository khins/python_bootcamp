# ============================================================
# FILE: 07_recreate-and-share-an-environment.py
# TOPIC: Recreating and Sharing Environments
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# Terminal commands are comments: run them in a terminal, not Python.

# LESSON OBJECTIVES
# 1. Recreate an environment from dependency records.
# 2. Decide which project files belong in version control.

# SECTION 1 — RECREATE IN A NEW DIRECTORY
# From the repository root, after lesson 06:
# py -m venv .venv-rebuild
# .\.venv-rebuild\Scripts\python.exe -m pip install -r requirements-snapshot.txt
# .\.venv-rebuild\Scripts\python.exe -m pip check
# .\.venv-rebuild\Scripts\python.exe -c "import requests, bs4; print('Imports OK')"
# => Imports OK, if installation succeeded.
#
# Keep the original environment while verifying the new one.
# Reuse the same Python version when comparing reproducibility.
# A venv often contains absolute paths. Recreate it after moving projects
# instead of copying the environment folder to another computer.

# SECTION 2 — SOURCE CONTROL
# Commit source, tests, dependency records, and setup instructions.
# Suggested entries in the repository's .gitignore:
# .venv/
# .venv-rebuild/
# __pycache__/
# *.pyc
#
# These are suggested edits for the exercise, not changes made by this file.
# Recent Python versions can create a venv-local ignore file, but explicit
# project ignore rules also document your intent across interpreter versions.
# Never store your only copy of source code inside a generated environment.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Rebuild the environment and verify both imports.
# ANSWER / CODE: ______________________________________________
# 2. Which files would you send to a classmate?
# ANSWER / CODE: ______________________________________________
# 3. Explain why sharing .venv itself is unreliable.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Share source and dependency records; recreate generated environments.

# ============================================================
# END OF LESSON
# ============================================================

