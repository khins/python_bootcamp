# ============================================================
# FILE: 05_build-and-inspect-a-wheel.py
# TOPIC: Build a Distributable Wheel
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Build from pyproject metadata.
# 2. Verify an artifact outside an editable checkout.

# SECTION 1 - UNDERSTAND THE IDEA
# Install build into your environment, then from the repository root:
# .\.venv\Scripts\python.exe -m build "section 45/music-catalog"
# The dist directory receives a wheel and source distribution. A wheel is an
# installable archive; it is not your virtual environment. Install the wheel
# into a fresh environment and run --help from outside the project directory.
# This exercise builds locally; it does not publish to a package index.

# SECTION 2 - WORKED EXAMPLES
from pathlib import Path
from zipfile import ZipFile

def inspect_wheel(path):
    with ZipFile(path) as archive:
        return sorted(name for name in archive.namelist() if name.endswith(".py"))

def example_artifacts():
    dist = Path(__file__).resolve().parent / "music-catalog" / "dist"
    wheels = sorted(dist.glob("*.whl"))
    print(len(wheels))  # => 0 before building; normally 1 after the first build
    if wheels:
        print("bootcamp_catalog/core.py" in inspect_wheel(wheels[0]))  # => True

# example_artifacts()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Build a wheel and inspect its included Python modules.
# ANSWER / CODE: ______________________________________________
# 2. Install the wheel in another environment and run the CLI.
# ANSWER / CODE: ______________________________________________
# 3. Explain why a passing editable-install test can miss packaging mistakes.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Test the distribution artifact as well as the source checkout.

# ============================================================
# END OF LESSON
# ============================================================
