# ============================================================
# FILE: 05_assert-equal.py
# TOPIC: Comparing Values with assertEqual
# ============================================================
# STUDY GUIDE
# Read the sections, predict the results, then run this file directly.
# Examples use unittest and require no third-party packages.
# Complete practice exercises before checking your answers by running.

import unittest


# LESSON OBJECTIVES
# 1. Compare actual and expected values.
# 2. Recognize sequence order and dictionary equality.
# 3. Handle approximate floating-point results.


# ============================================================
# SECTION 1 — assertEqual IS A METHOD, NOT A MODULE
# ============================================================
# self.assertEqual(actual, expected) checks actual == expected.
# It reports useful differences when values do not match.
# Prefer this to assertTrue(actual == expected), which gives less context.

class TestEquality(unittest.TestCase):
    def test_integer_result(self):
        self.assertEqual(sum([2, 3, 4]), 9)

    def test_string_result(self):
        self.assertEqual("python".upper(), "PYTHON")

    def test_list_order(self):
        self.assertEqual(sorted([3, 1, 2]), [1, 2, 3])

    def test_dictionary_contents(self):
        self.assertEqual({"a": 1, "b": 2}, {"b": 2, "a": 1})

    def test_decimal_calculation(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=7)


# ============================================================
# SECTION 2 — EQUALITY DEPENDS ON THE VALUES
# ============================================================
# List equality includes order: [1, 2] != [2, 1].
# Dictionaries compare key/value contents, not insertion order.
# A tuple and a list with the same entries are not equal.
# Equality does not always require matching types: 1 == 1.0 is True.
# assertEqual checks equality, not whether both names refer to one object.


# ============================================================
# SECTION 3 — FLOATING-POINT APPROXIMATION
# ============================================================
# Binary floating-point cannot represent many decimal fractions exactly.
# assertAlmostEqual is useful when the expected behavior permits rounding.
# places=7 checks the rounded difference to seven decimal places;
# it does NOT mean seven significant digits.
# Alternatively use delta=0.001 for an absolute tolerance.
# Choose a tolerance that matches the requirement; do not simply increase
# tolerance until an incorrect calculation passes.


# ============================================================
# SECTION 4 — PREDICT AND PRACTICE
# ============================================================
# EXERCISE 1: Would assertEqual([1, 2], [2, 1]) pass? ____________
# EXERCISE 2: Would assertEqual(1, 1.0) pass? ___________________
# CHALLENGE: Write normalize_name(text) using strip() and title().
# Test "  ada lovelace  ", an empty string, and an already formatted name.
# Write your code here:


# ============================================================
# SECTION 5 — FINAL REVIEW
# ============================================================
# 1. Which operator does assertEqual express? __________________
# 2. Does equality prove object identity? ______________________
# 3. Why might floats need an approximate assertion? ____________
# KEY TAKEAWAY: Choose assertions that describe the expected value
# and provide helpful failure details.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================

