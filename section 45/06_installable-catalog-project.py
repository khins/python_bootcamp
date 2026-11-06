# ============================================================
# FILE: 06_installable-catalog-project.py
# TOPIC: Project: Installable Music Catalog
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Run a full add/list flow.
# 2. Handle invalid and corrupt data predictably.

# SECTION 1 - UNDERSTAND THE IDEA
# The complete companion package is in music-catalog. Install it using lesson 04
# before this example. Its JSON store validates before replacing the destination
# and uses a neighboring temporary file. It supports a single writer; concurrent
# read-modify-write requires locking or a database. Missing files mean an empty
# catalog; corrupt existing files are reported rather than silently discarded.

# SECTION 2 - WORKED EXAMPLES
from pathlib import Path
from tempfile import TemporaryDirectory

def example_packaged_project():
    from bootcamp_catalog.cli import main
    with TemporaryDirectory() as folder:
        path = str(Path(folder) / "catalog.json")
        print(main(["--catalog", path, "add", "Signals", "Rush", "1982"]))
        # => Added 1 album / 0 (two lines)
        print(main(["--catalog", path, "list"]))
        # => Signals by Rush (1982) / 0 (two lines)

# example_packaged_project()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Package your own previous catalog with separate UI/core/storage modules.
# ANSWER / CODE: ______________________________________________
# 2. Test duplicate additions and corrupted JSON without losing prior bytes.
# ANSWER / CODE: ______________________________________________
# 3. Build/install a wheel and repeat the add/list flow in a temporary folder.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Deliver an application through a verified package, not just a runnable file.

# ============================================================
# END OF LESSON
# ============================================================
