# ============================================================
# FILE: 01_pytest-and-assertions.py
# TOPIC: Test Behavior with pytest
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Use test discovery and plain assertions.
# 2. Read a failure as evidence.

# SECTION 1 - UNDERSTAND THE IDEA
# pytest discovers test_*.py files and test_* functions. Assertions describe
# observable behavior. The supplied tests target section 45's installed package.
# Run the scoped suite from the repository root:
# .\.venv\Scripts\python.exe -m pytest -c "section 46/pytest.ini" "section 46/tests"
# Do not run every old practice script as a test suite; many intentionally fail.

# SECTION 2 - WORKED EXAMPLES
def normalize_title(title):
    return title.strip()

def example_assertion():
    assert normalize_title(" Signals ") == "Signals"
    assert normalize_title("") == ""
    print("checks passed")  # => checks passed

# example_assertion()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Read tests/test_core.py and explain the behavior each test protects.
# ANSWER / CODE: ______________________________________________
# 2. In a scratch copy, change an expected result and inspect the failure diff.
# ANSWER / CODE: ______________________________________________
# 3. Explain why checking only a return type misses many bugs.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Tests should describe outcomes rather than mirror implementation steps.

# ============================================================
# END OF LESSON
# ============================================================
