# ============================================================
# FILE: 10_testing-truthiness.py
# TOPIC: Testing Truthiness with assertTrue and assertFalse
# ============================================================
# STUDY GUIDE
# Predict before running, then execute this file directly.
# Complete the practice exercises and review questions.

import unittest


# LESSON OBJECTIVES
# 1. Assert truthiness and falsiness.
# 2. Distinguish truthy values from the literal Boolean True.
# 3. Prefer specific assertions when they communicate more detail.


# ============================================================
# SECTION 1 — TRUTHINESS IS NOT A TYPE CHECK
# ============================================================
# assertTrue(value) checks bool(value) is True.
# assertFalse(value) checks bool(value) is False.
# Neither requires value itself to be a Boolean.

class TestTruthiness(unittest.TestCase):
    def test_nonempty_values_are_truthy(self):
        self.assertTrue([0])
        self.assertTrue("False")
        self.assertTrue(-1)

    def test_empty_and_zero_values_are_falsy(self):
        self.assertFalse([])
        self.assertFalse("")
        self.assertFalse(0)
        self.assertFalse(None)

    def test_boolean_predicate(self):
        self.assertTrue("123".isdigit())
        self.assertFalse("abc".isdigit())


# [0] is truthy because the list is nonempty, even though its item is falsy.
# "False" is truthy because it is a nonempty string, not Boolean False.


# ============================================================
# SECTION 2 — REQUIRE AN EXACT BOOLEAN WHEN APPROPRIATE
# ============================================================
class TestExactBoolean(unittest.TestCase):
    def test_predicate_returns_true(self):
        result = "123".isdigit()
        self.assertIs(result, True)


# assertIs(result, True) requires the actual True object.
# assertEqual(result, True) can also accept 1 because 1 == True.
# Use the assertion matching your public return-value contract.
# For equality, prefer assertEqual(a, b) over assertTrue(a == b).


# ============================================================
# SECTION 3 — PREDICT AND PRACTICE
# ============================================================
# EXERCISE 1: Would assertFalse("0") pass? Why? _________________
# EXERCISE 2: Would assertTrue([False]) pass? Why? _______________
# CHALLENGE: Write has_items(items), returning bool(items).
# Test empty and nonempty lists and require exact Boolean results.
# Write your code here:


# ============================================================
# SECTION 4 — FINAL REVIEW
# ============================================================
# 1. Does assertTrue require type bool? ________________________
# 2. Is a nonempty list containing None truthy? _________________
# 3. Which assertion requires the literal True object? __________
# KEY TAKEAWAY: Truthiness describes conditional behavior, not
# whether the value is literally True or False.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================

