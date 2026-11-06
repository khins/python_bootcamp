# ============================================================
# FILE: 03_pyproject-and-dependencies.py
# TOPIC: Read pyproject.toml
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Identify build and runtime dependencies.
# 2. Inspect project metadata.

# SECTION 1 - UNDERSTAND THE IDEA
# [build-system] selects tools used to build artifacts. [project] describes the
# distribution, Python requirement, and runtime dependencies. This project has
# no third-party runtime dependencies. A dependency range is not a lockfile.
# Development tools such as pytest need not become runtime requirements.

# SECTION 2 - WORKED EXAMPLES
from pathlib import Path
import tomllib

def example_metadata():
    path = Path(__file__).resolve().parent / "music-catalog" / "pyproject.toml"
    with path.open("rb") as source:
        config = tomllib.load(source)
    print(config["project"]["name"])  # => bootcamp-music-catalog
    print(config["project"]["dependencies"])  # => []
    print(config["build-system"]["build-backend"])  # => setuptools.build_meta

# example_metadata()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Identify the minimum Python version and package version.
# ANSWER / CODE: ______________________________________________
# 2. Explain why setuptools is a build dependency here.
# ANSWER / CODE: ______________________________________________
# 3. Describe where you would record development-only test tools.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Metadata tells installers what the project is and how to build it.

# REFERENCES
# https://packaging.python.org/en/latest/tutorials/packaging-projects/

# ============================================================
# END OF LESSON
# ============================================================
