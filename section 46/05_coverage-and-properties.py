# ============================================================
# FILE: 05_coverage-and-properties.py
# TOPIC: Coverage and Property-based Testing
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Interpret coverage without equating it to correctness.
# 2. State an invariant for generated inputs.

# SECTION 1 - UNDERSTAND THE IDEA
# Coverage reports which code executed, not whether assertions were good.
# Run with --cov=bootcamp_catalog --cov-branch --cov-report=term-missing.
# Hypothesis generates inputs and shrinks failures to smaller examples. The
# supplied property checks that normalization is idempotent: normalizing twice
# matches normalizing once. Choose domain-appropriate strategies and invariants.

# SECTION 2 - WORKED EXAMPLES
def example_invariant():
    normalize = lambda value: value.strip()
    for value in [" A ", "", "Blue"]:
        assert normalize(normalize(value)) == normalize(value)
    print("invariant holds for these examples")

# example_invariant()
# tests/test_properties.py expands this approach using @given and strategies.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Read uncovered branches and add a behavior test for one meaningful branch.
# ANSWER / CODE: ______________________________________________
# 2. Write a property that adding a distinct valid album increases length by one.
# ANSWER / CODE: ______________________________________________
# 3. Explain why 100% coverage cannot guarantee correctness.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Coverage locates gaps; properties explore general behavior.

# REFERENCES
# https://hypothesis.readthedocs.io/en/latest/quickstart.html

# ============================================================
# END OF LESSON
# ============================================================
