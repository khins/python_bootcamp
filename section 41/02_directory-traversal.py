# ============================================================
# FILE: 02_directory-traversal.py
# TOPIC: Traverse a Directory Tree
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Compare iterdir, glob, and rglob.
# 2. Make reporting deterministic.

# SECTION 1 - UNDERSTAND THE IDEA
# iterdir lists immediate children, glob matches a pattern, and rglob searches
# recursively. Filter directories versus files and sort results when output
# order matters. Traversal is not a snapshot: files may change between listing
# and access. Permission errors and symbolic links need an explicit policy.

# SECTION 2 - WORKED EXAMPLES
from pathlib import Path
from tempfile import TemporaryDirectory

def example_traversal():
    with TemporaryDirectory() as folder:
        root = Path(folder)
        (root / "nested").mkdir()
        (root / "one.txt").write_text("one", encoding="utf-8")
        (root / "nested" / "two.txt").write_text("two", encoding="utf-8")
        print(sorted(p.name for p in root.glob("*.txt")))  # => ['one.txt']
        print(sorted(p.relative_to(root).as_posix() for p in root.rglob("*.txt")))
        # => ['nested/two.txt', 'one.txt']

# example_traversal()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Report file sizes for a temporary tree.
# ANSWER / CODE: ______________________________________________
# 2. Compare glob("*.txt") with rglob("*.txt").
# ANSWER / CODE: ______________________________________________
# 3. Decide whether to follow links and explain the risk of cycles.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Traversal needs a scope, ordering policy, and error policy.

# ============================================================
# END OF LESSON
# ============================================================
