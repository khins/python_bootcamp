# ============================================================
# FILE: 01_why-virtual-environments.py
# TOPIC: Why Projects Need Virtual Environments
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# Terminal commands are comments: run them in a terminal, not Python.

# LESSON OBJECTIVES
# 1. Explain dependency isolation.
# 2. Distinguish an environment from source code.

# SECTION 1 — TWO PROJECTS, DIFFERENT DEPENDENCIES
# A dependency is a package your code needs. Two projects may require
# incompatible versions. A venv gives each project its own installation
# location. It uses an existing Python installation as its base.
# A venv is not a virtual machine, container, or security sandbox.
# It does not isolate access to files, networking, or operating-system tools.

def example_project_requirements():
    projects = {"catalog": "library version A", "report": "library version B"}
    for name, requirement in projects.items():
        print(f"{name}: {requirement}")
    # => catalog: library version A
    # => report: library version B


# example_project_requirements()

# SECTION 2 — KEEP SOURCE OUTSIDE THE ENVIRONMENT
# project/
#     .venv/          generated interpreter/package files
#     main.py         your source code
#     requirements.txt
# Recreate .venv when necessary; keep main.py and dependency records.
# Standard-library modules such as pathlib need no pip installation.
# Third-party distributions such as requests must be installed.
# REFERENCE: https://docs.python.org/3/library/venv.html

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Why might installing everything globally cause conflicts?
# ANSWER / CODE: ______________________________________________
# 2. Sketch a project layout with source outside .venv.
# ANSWER / CODE: ______________________________________________
# 3. Does a venv prevent a program from reading your other files?
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: An environment isolates installed dependencies for a project.

# ============================================================
# END OF LESSON
# ============================================================

