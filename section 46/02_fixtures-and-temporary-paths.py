# ============================================================
# FILE: 02_fixtures-and-temporary-paths.py
# TOPIC: Use Fixtures for Fresh Test State
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Request fixtures by parameter name.
# 2. Isolate file effects with tmp_path.

# SECTION 1 - UNDERSTAND THE IDEA
# A fixture supplies setup to a test; default function scope creates fresh state
# per test. tmp_path gives a temporary Path. conftest.py shares fixtures without
# manual imports. Use yield fixtures when cleanup is needed after a test, and
# put cleanup in finally when appropriate. Avoid hidden ordering dependencies.

# SECTION 2 - WORKED EXAMPLES
def example_fresh_data():
    def make_album():
        return {"title": "Signals"}
    first, second = make_album(), make_album()
    first["title"] = "Changed"
    print(second["title"])  # => Signals

# example_fresh_data()
# Open tests/conftest.py and tests/test_storage.py for runnable pytest fixtures.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Add a fixture with two album records.
# ANSWER / CODE: ______________________________________________
# 2. Use tmp_path to prove loading a missing file does not create it.
# ANSWER / CODE: ______________________________________________
# 3. Explain how session-scoped mutable data could leak between tests.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Fresh fixtures prevent tests from depending on one another.

# REFERENCES
# https://docs.pytest.org/en/stable/how-to/fixtures.html

# ============================================================
# END OF LESSON
# ============================================================
