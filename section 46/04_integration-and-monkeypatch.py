# ============================================================
# FILE: 04_integration-and-monkeypatch.py
# TOPIC: Test Files and CLI Interactions
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Exercise real temporary storage.
# 2. Patch a narrow failure boundary.

# SECTION 1 - UNDERSTAND THE IDEA
# An integration test combines components, such as CLI plus validation plus JSON
# storage. Use real temporary files for storage behavior. monkeypatch can force
# an otherwise rare os.replace failure; patch the name where the code looks it
# up. capsys captures terminal output. Verify data preservation as well as errors.

# SECTION 2 - WORKED EXAMPLES
def example_test_plan():
    behaviors = ["add/list round trip", "corrupt file preserved", "replace failure cleanup"]
    print(len(behaviors))  # => 3

# example_test_plan()
# Runnable examples: tests/test_cli.py and test_replace_failure_cleans_temporary_file.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Test adding a duplicate through main and check its exit code.
# ANSWER / CODE: ______________________________________________
# 2. Force a write failure and verify existing catalog bytes remain unchanged.
# ANSWER / CODE: ______________________________________________
# 3. Explain which checks belong in unit tests and which need integration.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Exercise real boundaries, and simulate failures precisely.

# ============================================================
# END OF LESSON
# ============================================================
