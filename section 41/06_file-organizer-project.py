# ============================================================
# FILE: 06_file-organizer-project.py
# TOPIC: Project: Preview-first File Organizer
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Separate planning from applying.
# 2. Exercise the CLI on temporary sample files.

# SECTION 1 - UNDERSTAND THE IDEA
# organizer.py is a complete CLI. It previews a nonrecursive plan by default;
# --apply COPIES files into organized/text or organized/other while retaining
# originals. It skips source symlinks and rejects existing targets. Run --help
# first. Work on a demo folder. Repeated application reports a collision rather
# than overwriting. A failed batch can be partial; inspect before retrying.

# SECTION 2 - WORKED EXAMPLES
from pathlib import Path
from tempfile import TemporaryDirectory

def example_organizer():
    from organizer import plan, apply
    with TemporaryDirectory() as folder:
        root = Path(folder)
        (root / "notes.txt").write_text("demo", encoding="utf-8")
        actions = plan(root)
        print(len(actions))  # => 1
        print((root / "organized").exists())  # => False: planning has no writes
        apply(actions)
        print((root / "organized/text/notes.txt").read_text(encoding="utf-8"))  # => demo
        print((root / "notes.txt").exists())  # => True

# example_organizer()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Build your own planner with audio/text/other groups.
# ANSWER / CODE: ______________________________________________
# 2. Test preview, empty input, collision, and a missing source directory.
# ANSWER / CODE: ______________________________________________
# 3. Add a manifest describing successful copies and partial failures.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: A reviewable plan and explicit apply step make filesystem work understandable.

# ============================================================
# END OF LESSON
# ============================================================
