# ============================================================
# FILE: 05_install-and-inspect-packages.py
# TOPIC: Installing and Inspecting Packages
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# Terminal commands are comments: run them in a terminal, not Python.

# LESSON OBJECTIVES
# 1. Install dependencies into the intended venv.
# 2. Distinguish distribution names from import names.

# SECTION 1 — INSTALL WITH THE ENVIRONMENT'S PYTHON
# From the repository root in PowerShell:
# .\.venv\Scripts\python.exe -m pip install requests beautifulsoup4
# .\.venv\Scripts\python.exe -m pip show requests beautifulsoup4
# .\.venv\Scripts\python.exe -m pip list
# .\.venv\Scripts\python.exe -m pip check
#
# -m runs a module using that Python. A bare pip command can belong
# to a different installation. pip check checks dependency compatibility;
# it does not test your application or audit package security.
# Install the distribution beautifulsoup4; import the module bs4.

# SECTION 2 — INSPECT WITHOUT IMPORTING THE PACKAGES
from importlib.metadata import PackageNotFoundError, version


def example_installed_versions():
    for distribution in ("requests", "beautifulsoup4"):
        try:
            print(distribution, version(distribution))
        except PackageNotFoundError:
            print(distribution, "is not installed in this interpreter")
    # Installed versions vary. Missing-package messages are intentional.


# example_installed_versions()
# Do not name your own files requests.py or bs4.py: they can shadow imports.
# REFERENCE: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Install the two packages and inspect their locations with pip show.
# ANSWER / CODE: ______________________________________________
# 2. Which name belongs in pip install: bs4 or beautifulsoup4?
# ANSWER / CODE: ______________________________________________
# 3. Explain why python -m pip helps avoid interpreter mismatches.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Install distributions with the same Python that runs your program.

# ============================================================
# END OF LESSON
# ============================================================

