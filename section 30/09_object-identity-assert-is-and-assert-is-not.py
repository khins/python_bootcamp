# ============================================================
# FILE: 09_object-identity-assert-is-and-assert-is-not.py
# TOPIC: Object Identity with assertIs and assertIsNot
# ============================================================
# STUDY GUIDE
# Predict before running, then execute this file directly.
# Complete the practice exercises and review questions.

import unittest


# LESSON OBJECTIVES
# 1. Distinguish equality from identity.
# 2. Test shared references and separate copies.
# 3. Avoid identity checks for ordinary numeric/string values.


# ============================================================
# SECTION 1 — SAME VALUE VERSUS SAME OBJECT
# ============================================================
# == compares values. is asks whether references point to one object.
# assertIs(a, b) checks a is b; assertIsNot(a, b) checks a is not b.

class TestIdentity(unittest.TestCase):
    def test_alias_is_same_object(self):
        original = [1, 2]
        alias = original
        self.assertIs(alias, original)

    def test_copy_has_equal_values_but_separate_identity(self):
        original = [1, 2]
        copied = original.copy()
        self.assertEqual(copied, original)
        self.assertIsNot(copied, original)

    def test_mutating_alias_changes_original(self):
        original = []
        alias = original
        alias.append("new")
        self.assertEqual(original, ["new"])
        self.assertIs(alias, original)


# ============================================================
# SECTION 2 — WHEN IDENTITY IS THE REQUIREMENT
# ============================================================
# Identity matters when a function promises to return the same object,
# when checking a shared instance, or when comparing a sentinel.
# A sentinel is a unique object representing a special condition.

MISSING = object()


class TestSentinel(unittest.TestCase):
    def test_missing_key_returns_sentinel(self):
        settings = {}
        result = settings.get("theme", MISSING)
        self.assertIs(result, MISSING)


# Do not use is to compare normal integer/string values. Python may
# reuse some immutable objects; that is not the value contract to test.


# ============================================================
# SECTION 3 — PREDICT AND PRACTICE
# ============================================================
# EXERCISE 1: a = []; b = []; c = a
# Which pass: assertIs(a, c), assertIs(a, b), assertEqual(a, b)?
# ANSWER: ____________________________________________________
# CHALLENGE: Write copy_items(items). Verify equal contents AND
# distinct list identity. Then mutate the copy and check the original.
# Write your code here:


# ============================================================
# SECTION 4 — FINAL REVIEW
# ============================================================
# 1. What does is compare? ____________________________________
# 2. Can equal lists have different identities? _________________
# 3. Does assigning another name create a copy? ________________
# KEY TAKEAWAY: Use equality for contents, identity for references.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================

