# ============================================================
# FILE: 07_skipping-tests-and-expected-failures.py
# TOPIC: Skipping Tests and Expected Failures
# ============================================================
# STUDY GUIDE
# Read the sections, predict the results, then run this file directly.
# Examples use unittest and require no third-party packages.
# Complete practice exercises before checking your answers by running.

import unittest


# LESSON OBJECTIVES
# 1. Skip tests explicitly or conditionally.
# 2. Mark a demonstration of a known failure as expected.
# 3. Recognize unexpected success as a signal to update a test.

import sys


# ============================================================
# SECTION 1 — SKIP WITH A REASON
# ============================================================
class TestSkipping(unittest.TestCase):
    @unittest.skip("Demonstration: this test is intentionally disabled")
    def test_disabled_example(self):
        self.fail("The skipped test body never runs")

    @unittest.skipIf(sys.platform == "win32", "Example requires non-Windows")
    def test_non_windows_condition(self):
        self.assertNotEqual(sys.platform, "win32")

    @unittest.skipUnless(sys.platform == "win32", "Example requires Windows")
    def test_windows_condition(self):
        self.assertEqual(sys.platform, "win32")

    def test_runtime_skip(self):
        available = False  # A simulated unavailable dependency.
        if not available:
            self.skipTest("Demo dependency is unavailable")
        self.fail("Not reached in this example")


# ============================================================
# SECTION 2 — EXPECTED FAILURES STILL EXECUTE
# ============================================================
class TestExpectedFailure(unittest.TestCase):
    @unittest.expectedFailure
    def test_known_bug_demonstration(self):
        # Deliberately wrong result to demonstrate the report category.
        actual = 2 + 2
        self.assertEqual(actual, 5)


# A skipped test does not execute its normal test body.
# An expected-failure test runs, and a failure/error in its test body
# is recorded as expected. Failures in setup/teardown are not covered.
# This file intentionally reports skips and one expected failure.
# Expected failures do not make the suite unsuccessful by themselves.


# ============================================================
# SECTION 3 — UNEXPECTED SUCCESS
# ============================================================
# If a test marked expectedFailure passes, unittest reports an
# unexpected success, which makes the run unsuccessful.
# After fixing a known bug, remove the decorator and keep the test.
# Use expectedFailure to track known problems, not to hide new failures.
# "Exposed failures" is interpreted here as the unittest feature
# called expected failures; ordinary failures remain visible in reports.


# ============================================================
# SECTION 4 — PRACTICE
# ============================================================
# EXERCISE 1: Which tests are skipped on your operating system?
# ANSWER: ____________________________________________________
# EXERCISE 2: Change expected 5 to 4 in the known-bug test. Predict
# the report, then run it. Remove the decorator to make it a normal pass.
# CHALLENGE: Add a conditionally skipped test controlled by a Boolean
# RUN_OPTIONAL_TESTS. Give the skip a clear reason.


# ============================================================
# SECTION 5 — FINAL REVIEW
# ============================================================
# 1. Does a skipped test body execute? __________________________
# 2. Does an expected-failure test body execute? ________________
# 3. What happens when an expected-failure test passes? _________
# 4. Why should skips include reasons? _________________________
# KEY TAKEAWAY: Skips describe unavailable or excluded tests;
# expected failures track known problems that still need fixing.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================

