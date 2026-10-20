# ============================================================
# FILE: 12_testing-inclusion.py
# TOPIC: Membership with assertIn and assertNotIn
# ============================================================
# STUDY GUIDE
# Predict before running, then execute this file directly.
# Complete the practice exercises and review questions.

import unittest


# LESSON OBJECTIVES
# 1. Check membership in containers.
# 2. Recognize dictionary-key and string-substring membership.
# 3. Distinguish membership from complete contents or counts.


# ============================================================
# SECTION 1 — MEMBERSHIP ASSERTIONS
# ============================================================
# assertIn(member, container) checks member in container.
# assertNotIn(member, container) checks member not in container.

class TestMembership(unittest.TestCase):
    def test_list_contains_added_item(self):
        items = ["milk"]
        items.append("bread")
        self.assertIn("bread", items)

    def test_removed_item_is_absent(self):
        items = ["milk", "bread"]
        items.remove("milk")
        self.assertNotIn("milk", items)

    def test_set_membership(self):
        self.assertIn("read", {"read", "write"})

    def test_substring_membership(self):
        self.assertIn("thon", "Python")
        self.assertNotIn("python", "Python")


# String membership checks a substring and is case-sensitive.


# ============================================================
# SECTION 2 — DICTIONARY MEMBERSHIP CHECKS KEYS
# ============================================================
class TestDictionaryMembership(unittest.TestCase):
    def test_key_and_value_membership(self):
        person = {"name": "Ada", "age": 36}
        self.assertIn("name", person)
        self.assertNotIn("Ada", person)
        self.assertIn("Ada", person.values())
        self.assertIn(("name", "Ada"), person.items())


# ============================================================
# SECTION 3 — MEMBERSHIP IS NOT A COMPLETE CONTENT CHECK
# ============================================================
# assertIn("a", ["a", "a", "b"]) says nothing about count or order.
# Use assertEqual(actual, expected) when the exact ordered list matters.
# Use assertCountEqual(actual, expected) when order does not matter but
# the values AND their occurrence counts must match.

class TestContents(unittest.TestCase):
    def test_same_entries_different_order(self):
        self.assertCountEqual(["a", "b", "a"], ["b", "a", "a"])


# ============================================================
# SECTION 4 — PRACTICE
# ============================================================
# EXERCISE 1: Would assertIn("", "Python") pass? _______________
# EXERCISE 2: Does assertIn("a", values) prove it occurs once? ___
# CHALLENGE: Test a function that adds a tag only if it is absent.
# Check membership after the first call and the exact count after a repeat.
# Write your code here:


# ============================================================
# SECTION 5 — FINAL REVIEW
# ============================================================
# 1. Which operator does assertIn express? _____________________
# 2. What does membership check in a dictionary? ________________
# 3. How can you compare contents ignoring order but not counts? _
# KEY TAKEAWAY: Membership checks presence; use stronger assertions
# when counts, order, or complete contents are part of the requirement.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================

