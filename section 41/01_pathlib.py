# ============================================================
# FILE: 01_pathlib.py
# TOPIC: Build and Inspect Paths
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Construct paths without manual separators.
# 2. Separate paths from filesystem effects.

# SECTION 1 - UNDERSTAND THE IDEA
# A Path represents a location; constructing it does not create a file. Use /
# to join components, suffix for an extension, and parent for its directory.
# Relative paths are resolved from the working directory, not the script.
# Path(__file__).resolve().parent locates files beside the current script.

# SECTION 2 - WORKED EXAMPLES
from pathlib import Path

def example_paths():
    path = Path("catalog") / "albums.json"
    print(path.name)    # => albums.json
    print(path.stem)    # => albums
    print(path.suffix)  # => .json
    print(path.with_suffix(".csv").name)  # => albums.csv

# example_paths()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Construct a path beside this lesson without creating it.
# ANSWER / CODE: ______________________________________________
# 2. Explain absolute versus relative paths.
# ANSWER / CODE: ______________________________________________
# 3. Inspect name, stem, suffix, and parent of a nested path.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Paths describe locations; explicit methods perform filesystem operations.

# ============================================================
# END OF LESSON
# ============================================================
