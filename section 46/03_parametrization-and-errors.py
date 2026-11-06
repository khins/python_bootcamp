# ============================================================
# FILE: 03_parametrization-and-errors.py
# TOPIC: Test a Family of Inputs
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Parametrize boundary cases.
# 2. Check expected exception types.

# SECTION 1 - UNDERSTAND THE IDEA
# pytest.mark.parametrize runs one behavior check with several inputs.
# pytest.raises verifies failure type and optionally message content. Include
# boundaries and tricky types, such as bool versus int. The supplied invalid-year
# test covers text, None, bool, and out-of-range values; add valid boundaries too.

# SECTION 2 - WORKED EXAMPLES
def example_boundaries():
    cases = [1800, 1982, 2100]
    print([1800 <= year <= 2100 for year in cases])  # => [True, True, True]

# example_boundaries()
# See tests/test_core.py for real @pytest.mark.parametrize and pytest.raises.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Add parametrized checks for years 1800 and 2100.
# ANSWER / CODE: ______________________________________________
# 2. Add whitespace-only title and artist cases.
# ANSWER / CODE: ______________________________________________
# 3. Explain why catching Exception can let the wrong failure pass a test.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Boundary tables make the input contract visible.

# ============================================================
# END OF LESSON
# ============================================================
