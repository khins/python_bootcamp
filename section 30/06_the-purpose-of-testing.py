# ============================================================
# FILE: 06_the-purpose-of-testing.py
# TOPIC: Why We Test Code
# ============================================================
# STUDY GUIDE
# Read the sections, predict the results, then run this file directly.
# Examples use unittest and require no third-party packages.
# Complete practice exercises before checking your answers by running.

import unittest


# LESSON OBJECTIVES
# 1. Explain regression protection and executable requirements.
# 2. Choose useful normal, boundary, and invalid cases.
# 3. Distinguish unit, integration, and end-to-end tests.


def shipping_cost(subtotal):
    if subtotal < 0:
        raise ValueError("subtotal must not be negative")
    return 0 if subtotal >= 50 else 5


# ============================================================
# SECTION 1 — CAPTURE A REQUIREMENT
# ============================================================
# Requirement: free shipping at 50 or above; otherwise shipping is 5.
# Negative subtotals are invalid. Values here are simplified whole units.
# Choose expectations from the requirement, not by copying the function.

class TestShippingCost(unittest.TestCase):
    def test_below_free_shipping_boundary(self):
        self.assertEqual(shipping_cost(49), 5)

    def test_exact_free_shipping_boundary(self):
        self.assertEqual(shipping_cost(50), 0)

    def test_above_free_shipping_boundary(self):
        self.assertEqual(shipping_cost(51), 0)

    def test_zero_subtotal(self):
        self.assertEqual(shipping_cost(0), 5)

    def test_negative_subtotal(self):
        with self.assertRaises(ValueError):
            shipping_cost(-1)


# ============================================================
# SECTION 2 — PREVENT REGRESSIONS
# ============================================================
# A regression breaks behavior that previously worked.
# If >= accidentally becomes >, the boundary test detects the problem.
# Tests support refactoring: you can change implementation while checking
# that externally observable behavior still satisfies the requirement.
# A passing suite does not prove that all possible bugs are absent.


# ============================================================
# SECTION 3 — DIFFERENT LEVELS OF TESTING
# ============================================================
# Unit: check a small behavior in isolation, such as shipping_cost().
# Integration: check components working together, such as saving an order
# and loading it from a database.
# End-to-end: check a complete user flow through the running system.
# Each level finds different problems. Keep unit tests fast and independent
# of live services. Avoid tests that depend on other tests' changes.


# ============================================================
# SECTION 4 — PRACTICE
# ============================================================
# EXERCISE 1: Which test catches changing >= to >? _______________
# EXERCISE 2: Can high code coverage alone prove correctness? Why?
# ANSWER: ____________________________________________________
# CHALLENGE: Write admission_price(age): reject negative ages, charge
# 0 below age 5 and 10 otherwise. Test ages -1, 0, 4, 5, and 6.
# Write your code here:


# ============================================================
# SECTION 5 — FINAL REVIEW
# ============================================================
# 1. What is a regression? ____________________________________
# 2. Why test the exact boundary? ______________________________
# 3. Where should expected answers come from? __________________
# 4. Does a passing suite guarantee no bugs? ___________________
# KEY TAKEAWAY: Good tests preserve behavior and make requirements
# concrete; their value comes from meaningful cases, not just quantity.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================

