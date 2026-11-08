# ============================================================
# FILE: 02_git-workflows.py
# TOPIC: Reviewable Git Workflows
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply reviewable git workflows to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# Use git status and git diff before staging. Stage the files belonging to one
# coherent change, inspect the staged diff, run relevant checks, then commit with
# a message describing the behavior change. A branch isolates history, not your
# working directory's uncommitted changes automatically. Resolve conflicts by
# understanding both changes and rechecking behavior. Do not commit credentials.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from pathlib import Path

def example():
    commands = ["git status --short", "git diff", "git diff --cached"]
    for command in commands:
        print(command)  # Prints review commands only; executes none.
    print(Path(".git").exists())  # Depends on the directory you run from.


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. What is the difference between staged and unstaged diffs?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Describe the files and tests for one small catalog feature before editing.
# ANSWER / CODE: ______________________________________________

# 3. Why review a staged diff before committing?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: Use git status and git diff before staging.
# ============================================================
# END OF LESSON
# ============================================================
