# ============================================================
# FILE: 04_editable-installs-and-entry-points.py
# TOPIC: Install and Run the CLI
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Use editable installation during development.
# 2. Connect a command name to a callable.

# SECTION 1 - UNDERSTAND THE IDEA
# From the repository root in PowerShell:
# .\.venv\Scripts\python.exe -m pip install -e "section 45/music-catalog"
# .\.venv\Scripts\python.exe -m bootcamp_catalog --help
# .\.venv\Scripts\bootcamp-catalog.exe --help
# Editable installation uses your source tree during development. Entry points
# are installed wrappers calling cli.main; its integer return becomes status.
# Changing package metadata may require reinstalling even with an editable install.

# SECTION 2 - WORKED EXAMPLES
def example_entry_point():
    target = "bootcamp_catalog.cli:main"
    module, function = target.split(":")
    print(module, function)  # => bootcamp_catalog.cli main

# example_entry_point()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Install the sample and run both help commands.
# ANSWER / CODE: ______________________________________________
# 2. Explain why python cli.py differs from python -m bootcamp_catalog.
# ANSWER / CODE: ______________________________________________
# 3. Add an entry point only in a practice copy and reinstall it.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Install commands connect package metadata to application entry functions.

# ============================================================
# END OF LESSON
# ============================================================
