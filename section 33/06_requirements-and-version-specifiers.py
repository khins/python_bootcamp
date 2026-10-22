# ============================================================
# FILE: 06_requirements-and-version-specifiers.py
# TOPIC: Recording Dependencies
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# Terminal commands are comments: run them in a terminal, not Python.

# LESSON OBJECTIVES
# 1. Explain version constraints.
# 2. Record an environment for later recreation.

# SECTION 1 — REQUIREMENT LINES
# A requirements file is plain text with one requirement per line.
# Examples of syntax, using a fictional distribution:
# example-library==1.2.3      exact version
# example-library>=1.2,<2     a bounded range
# example-library~=1.2.3     >=1.2.3 and <1.3
# These illustrate syntax; do not install this fictional package.
#
# The section 34 requirements.txt lists requests and beautifulsoup4.
# It is an unpinned starter list, not a reproducible version snapshot.
# Direct dependencies are what your project requests; transitive
# dependencies are packages those dependencies themselves require.

# SECTION 2 — SNAPSHOT THE CLEAN LEARNING ENVIRONMENT
# From the repository root in Windows PowerShell:
# .\.venv\Scripts\python.exe -m pip freeze | Set-Content -Encoding utf8 requirements-snapshot.txt
# .\.venv\Scripts\python.exe -m pip install -r requirements-snapshot.txt
#
# freeze reports installed distributions, including transitive dependencies,
# but normally omits some bootstrap packaging tools. It is not a universal
# lockfile: Python version, platform, indexes, and available artifacts matter.
# Avoid generating a project snapshot from a cluttered global environment.

def example_dependency_categories():
    direct = ["requests", "beautifulsoup4"]
    print(", ".join(direct))  # => requests, beautifulsoup4


# example_dependency_categories()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Explain the difference between ==1.2.3 and >=1.2,<2.
# ANSWER / CODE: ______________________________________________
# 2. Create a snapshot from your learning environment.
# ANSWER / CODE: ______________________________________________
# 3. Why might a frozen file still behave differently on another OS?
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Record dependencies and the Python/platform context together.

# ============================================================
# END OF LESSON
# ============================================================

