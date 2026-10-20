# ============================================================
# FILE: 11_testing-nullness.py
# TOPIC: Testing None with assertIsNone and assertIsNotNone
# ============================================================
# STUDY GUIDE
# Predict before running, then execute this file directly.
# Complete the practice exercises and review questions.

import unittest


# LESSON OBJECTIVES
# 1. Recognize None as Python's absence-of-value marker.
# 2. Distinguish None from other falsy values.
# 3. Test functions that return optional values.


def find_position(items, target):
    for index, item in enumerate(items):
        if item == target:
            return index
    return None


# ============================================================
# SECTION 1 — None IS NOT ZERO OR AN EMPTY STRING
# ============================================================
# Python uses None rather than a keyword named null.
# assertIsNone(value) checks value is None.
# assertIsNotNone(value) checks value is not None.

class TestOptionalPosition(unittest.TestCase):
    def test_missing_item_returns_none(self):
        self.assertIsNone(find_position(["a", "b"], "z"))

    def test_first_item_has_position_zero(self):
        result = find_position(["a", "b"], "a")
        self.assertIsNotNone(result)
        self.assertEqual(result, 0)

    def test_empty_sequence_returns_none(self):
        self.assertIsNone(find_position([], "a"))


# ============================================================
# SECTION 2 — FALSY IS A BROADER CATEGORY
# ============================================================
# None, 0, False, "", and [] are all falsy, but only None is None.
# assertFalse(result) would pass for both missing and index zero,
# hiding a distinction that matters for find_position().

class TestNoneDistinction(unittest.TestCase):
    def test_falsy_values_can_still_be_present(self):
        self.assertIsNotNone(0)
        self.assertIsNotNone(False)
        self.assertIsNotNone("")
        self.assertIsNotNone([])


# Functions with no explicit return value return None.
# Mutating methods such as list.append() also return None; inspect
# the list itself when checking their effect.


# ============================================================
# SECTION 3 — PREDICT AND PRACTICE
# ============================================================
# EXERCISE 1: Would assertIsNone(False) pass? ___________________
# EXERCISE 2: Why is index zero a useful boundary test? __________
# CHALLENGE: Test a dictionary lookup that returns None for a missing
# key but returns 0 for a present key. Do not confuse the two results.
# Write your code here:


# ============================================================
# SECTION 4 — FINAL REVIEW
# ============================================================
# 1. Which object represents absence here? _____________________
# 2. Does assertIsNotNone require a truthy value? ________________
# 3. What does a function without a return value return? ________
# KEY TAKEAWAY: Check None explicitly when absence differs from
# legitimate falsy values such as zero.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================

