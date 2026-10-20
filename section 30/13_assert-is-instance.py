# ============================================================
# FILE: 13_assert-is-instance.py
# TOPIC: Type Relationships with assertIsInstance
# ============================================================
# STUDY GUIDE
# Predict before running, then execute this file directly.
# Complete the practice exercises and review questions.

import unittest


# LESSON OBJECTIVES
# 1. Check whether a value is an instance of a class.
# 2. Understand subclass acceptance.
# 3. Distinguish instance checks from exact-type checks.

class Animal:
    pass


class Dog(Animal):
    pass


# ============================================================
# SECTION 1 — CHECK AN INSTANCE RELATIONSHIP
# ============================================================
class TestInstances(unittest.TestCase):
    def test_builtin_types(self):
        self.assertIsInstance([1, 2], list)
        self.assertIsInstance("hello", str)

    def test_subclass_is_also_parent_instance(self):
        pet = Dog()
        self.assertIsInstance(pet, Dog)
        self.assertIsInstance(pet, Animal)

    def test_not_an_instance(self):
        self.assertNotIsInstance("12", int)

    def test_one_of_multiple_types(self):
        self.assertIsInstance(3.5, (int, float))


# assertIsInstance(value, cls) uses isinstance(value, cls).
# It accepts instances of subclasses, not just instances of cls itself.
# A tuple of types allows any one of the listed instance relationships.


# ============================================================
# SECTION 2 — EXACT TYPES ARE A DIFFERENT REQUIREMENT
# ============================================================
class TestExactTypes(unittest.TestCase):
    def test_boolean_is_an_integer_subclass(self):
        self.assertIsInstance(True, int)
        self.assertIs(type(True), bool)
        self.assertIsNot(type(True), int)

    def test_exact_list_type(self):
        result = list(range(3))
        self.assertIs(type(result), list)
        self.assertEqual(result, [0, 1, 2])


# bool is a subclass of int, so isinstance(True, int) is True.
# Use an exact-type check only if that restriction is part of the contract.
# A correct type alone does not prove correct contents or behavior.


# ============================================================
# SECTION 3 — PREDICT AND PRACTICE
# ============================================================
# EXERCISE 1: Would assertIsInstance(Animal(), Dog) pass? _________
# EXERCISE 2: Does assertIsInstance("5", int) convert the string? _
# CHALLENGE: Write a function returning a list of uppercase names.
# Test both the list type and its exact expected contents.
# Write your code here:


# ============================================================
# SECTION 4 — FINAL REVIEW
# ============================================================
# 1. Does assertIsInstance accept subclasses? ___________________
# 2. Why does True satisfy an int instance check? _______________
# 3. How can you demand exactly type int? ______________________
# KEY TAKEAWAY: Instance assertions check class relationships;
# exact-type assertions enforce a narrower contract.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================

