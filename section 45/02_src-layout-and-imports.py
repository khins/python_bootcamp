# ============================================================
# FILE: 02_src-layout-and-imports.py
# TOPIC: Understand the src Layout
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Distinguish a project name from an import name.
# 2. Install before importing a src package.

# SECTION 1 - UNDERSTAND THE IDEA
# The distribution is bootcamp-music-catalog; the import package is
# bootcamp_catalog. Source lives under music-catalog/src/bootcamp_catalog.
# A src layout helps avoid accidentally testing code merely because the working
# directory is the project root. Install into your environment; do not patch
# sys.path in the application. Relative imports inside the package use a dot.

# SECTION 2 - WORKED EXAMPLES
from pathlib import Path

def example_layout():
    project = Path(__file__).resolve().parent / "music-catalog"
    package = project / "src" / "bootcamp_catalog"
    print(package.name)                  # => bootcamp_catalog
    print((package / "core.py").is_file())  # => True
    print((project / "pyproject.toml").is_file())  # => True

# example_layout()
# Inspect the real source tree beside these lessons, then install via lesson 04.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Explain why distribution names can contain hyphens but import names cannot.
# ANSWER / CODE: ______________________________________________
# 2. Trace from __main__.py to cli.main to storage.load.
# ANSWER / CODE: ______________________________________________
# 3. Try importing the installed package from a different directory.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: The project distribution and Python import package are distinct names.

# ============================================================
# END OF LESSON
# ============================================================
