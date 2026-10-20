# ============================================================
# FILE: 08_assert-not-equal-and-custom-messages.py
# TOPIC: assertNotEqual and Custom Failure Messages
# ============================================================
# STUDY GUIDE
# Read the sections, predict the results, then run this file directly.
# Examples use unittest and require no third-party packages.
# Complete practice exercises before checking your answers by running.

import unittest


# LESSON OBJECTIVES
# 1. Assert that two values differ.
# 2. Add context using the msg argument.
# 3. Avoid weak checks when an exact answer is known.


# ============================================================
# SECTION 1 — CHECK VALUE INEQUALITY
# ============================================================
class TestDifferentValues(unittest.TestCase):
    def test_uppercase_changes_lowercase_text(self):
        original = "python"
        result = original.upper()
        self.assertNotEqual(result, original)
        self.assertEqual(result, "PYTHON")

    def test_distinct_identifiers(self):
        first = {"id": 10, "name": "Ada"}
        second = {"id": 11, "name": "Grace"}
        self.assertNotEqual(first["id"], second["id"],
                            msg="Different records should have different IDs")


# assertNotEqual(a, b) checks a != b. It does not check identity.
# Two distinct list objects can have equal contents and therefore fail
# assertNotEqual. Use assertIsNot when distinct objects are required.


# ============================================================
# SECTION 2 — WRITE USEFUL MESSAGES
# ============================================================
class TestMessages(unittest.TestCase):
    def test_trimmed_username(self):
        raw = "  ada  "
        actual = raw.strip()
        self.assertEqual(actual, "ada", msg=f"Trimming failed for input {raw!r}")


# msg is shown when the assertion fails, not on every passing check.
# By default, unittest appends your message to its standard details.
# Explain the scenario or requirement; "test failed" adds little context.
# Avoid including secrets or private data in messages.


# ============================================================
# SECTION 3 — INEQUALITY CAN BE TOO WEAK
# ============================================================
# assertNotEqual(add(2, 3), 0) would accept many incorrect results.
# If the expected result is 5, assertEqual(actual, 5) is stronger.
# Use inequality when differing values are the behavior that matters.


# ============================================================
# SECTION 4 — PREDICT AND PRACTICE
# ============================================================
# EXERCISE 1: Would assertNotEqual([1], [1]) pass? _______________
# EXERCISE 2: Would assertNotEqual(1, 1.0) pass? ________________
# CHALLENGE: Write a function that replaces spaces with underscores.
# Test an exact expected result and add an input-specific failure message.
# Write your code here:


# ============================================================
# SECTION 5 — FINAL REVIEW
# ============================================================
# 1. Which operator does assertNotEqual express? ________________
# 2. When is msg displayed? ___________________________________
# 3. Why can inequality be weaker than an exact expected answer? _
# KEY TAKEAWAY: Check the requirement directly and add messages
# that explain the case when the built-in details are not enough.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================

