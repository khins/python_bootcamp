# ============================================================
# FILE: 04_the-unittest-module.py
# TOPIC: Organizing Tests with unittest
# ============================================================
# LESSON OBJECTIVES
# 1. Define a unittest.TestCase subclass.
# 2. Write test methods with descriptive names.
# 3. Run a suite and distinguish failures from errors.

import unittest


def multiply(a, b):
    return a * b


# ============================================================
# SECTION 1 — DEFINE A TEST CASE
# ============================================================
class TestMultiply(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiplication_by_zero(self):
        self.assertEqual(multiply(8, 0), 0)

    def test_negative_number(self):
        self.assertEqual(multiply(-2, 3), -6)


# Inherit from unittest.TestCase to obtain assertion methods.
# Test method names begin with test_. self refers to the test instance.
# The runner executes each test and summarizes results.
# Keep tests independent; do not rely on one method running before another.


# ============================================================
# SECTION 2 — RUN THIS LESSON
# ============================================================
# From the repository root, with Python installed:
# python "section 30/04_the-unittest-module.py"
# The main block below runs these tests only when this file is executed
# directly, not when another module imports it.
# verbosity=2 shows individual test names.
# Normal project test files often use names such as test_multiply.py.
# These numbered lessons preserve the course naming style, so run
# them directly; default discovery looks for test*.py, not these names.


# ============================================================
# SECTION 3 — UNDERSTAND THE REPORT
# ============================================================
# PASS: the test finished without a failure, error, or skip.
# FAILURE: an assertion was not satisfied.
# ERROR: an unexpected exception, such as a NameError, interrupted it.
# SKIP: the runner intentionally did not execute the test normally.
# A failing test stops at its failed assertion; the runner normally
# continues with other tests so you can see additional problems.
# An expected exception checked with assertRaises is a passing outcome.


# ============================================================
# SECTION 4 — PREDICT AND PRACTICE
# ============================================================
# EXERCISE 1: Rename a test method to check_positive_numbers.
# Will the default loader still recognize it as a test? __________
# EXERCISE 2: If multiply returns a + b, which tests above fail?
# ANSWER: ____________________________________________________
# CHALLENGE: Add test_two_negative_numbers expecting a positive result.
# Add it inside TestMultiply, then run the file again.


# ============================================================
# SECTION 5 — FINAL REVIEW
# ============================================================
# 1. Which class should test cases inherit from? ________________
# 2. What prefix identifies test methods? ______________________
# 3. How does a failure differ from an error? __________________
# 4. Why use the __main__ guard? _______________________________
# KEY TAKEAWAY: unittest runs independent test methods and reports
# their outcomes using a consistent structure.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================
