# ============================================================
# FILE: 03_shutil-and-temporary-files.py
# TOPIC: Copy Files in a Sandbox
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Use temporary directories for examples.
# 2. Distinguish copying from moving.

# SECTION 1 - UNDERSTAND THE IDEA
# shutil.copy2 copies data and attempts to preserve metadata; it is not a full
# backup system. move relocates a path and may copy/delete across filesystems.
# Existing destinations can be overwritten by some operations, so check your
# policy first. These examples only operate inside a fresh temporary directory.

# SECTION 2 - WORKED EXAMPLES
from pathlib import Path
from tempfile import TemporaryDirectory
import shutil

def example_copy():
    with TemporaryDirectory() as folder:
        root = Path(folder)
        source, target = root / "original.txt", root / "copy.txt"
        source.write_text("Rush", encoding="utf-8")
        shutil.copy2(source, target)
        print(source.exists(), target.read_text(encoding="utf-8"))  # => True Rush
        moved = root / "moved.txt"
        shutil.move(str(target), str(moved))
        print(target.exists(), moved.exists())  # => False True
    print(root.exists())  # => False

# example_copy()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Copy a binary fixture and compare its bytes.
# ANSWER / CODE: ______________________________________________
# 2. Reject an existing destination before copying.
# ANSWER / CODE: ______________________________________________
# 3. Explain why move should not be tested on your real music library.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Practice file mutations in disposable directories with explicit destinations.

# ============================================================
# END OF LESSON
# ============================================================
