# ============================================================
# FILE: 07_verifying-doubles-with-spec-and-autospec.py
# TOPIC: Verifying Doubles with spec, spec_set, and autospec
# ============================================================
# STUDY GUIDE
# Predict before running, then run this file directly with Python.
# Complete the exercises and challenges. No live services are used.

import unittest
from unittest.mock import Mock, MagicMock, call, create_autospec, patch


# LESSON OBJECTIVES
# 1. Constrain doubles to an interface.
# 2. Distinguish attribute restrictions from signature checking.
# 3. Recognize what an interface-aware double cannot verify.

class Catalog:
    def fetch(self, item_id, *, include_archived=False):
        raise NotImplementedError("Interface example only")


# ============================================================
# SECTION 1 — spec RESTRICTS ATTRIBUTE LOOKUP
# ============================================================
class TestSpec(unittest.TestCase):
    def test_unknown_method_is_rejected(self):
        catalog = Mock(spec=Catalog)
        catalog.fetch.return_value = {"name": "Tea"}
        self.assertEqual(catalog.fetch(7), {"name": "Tea"})
        with self.assertRaises(AttributeError):
            catalog.fecth(7)  # Intentional typo caught by spec.

    def test_spec_alone_allows_new_attribute_assignment(self):
        catalog = Mock(spec=Catalog)
        catalog.extra = 10
        self.assertEqual(catalog.extra, 10)


# ============================================================
# SECTION 2 — spec_set ALSO RESTRICTS ASSIGNMENT
# ============================================================
class TestSpecSet(unittest.TestCase):
    def test_unknown_attribute_assignment_is_rejected(self):
        catalog = Mock(spec_set=Catalog)
        with self.assertRaises(AttributeError):
            catalog.extra = 10


# Spec restrictions alone are not the same as validating call signatures.
# Attributes created only inside a real instance's __init__ may not be
# visible in a class spec. Choose the interface source thoughtfully.


# ============================================================
# SECTION 3 — autospec CHECKS CALL SIGNATURES
# ============================================================
class TestAutospec(unittest.TestCase):
    def test_correct_signature(self):
        catalog = create_autospec(Catalog, instance=True, spec_set=True)
        catalog.fetch.return_value = {"name": "Tea"}
        self.assertEqual(catalog.fetch(7, include_archived=True), {"name": "Tea"})
        catalog.fetch.assert_called_once_with(7, include_archived=True)

    def test_missing_argument(self):
        catalog = create_autospec(Catalog, instance=True)
        with self.assertRaises(TypeError):
            catalog.fetch()

    def test_keyword_only_argument(self):
        catalog = create_autospec(Catalog, instance=True)
        with self.assertRaises(TypeError):
            catalog.fetch(7, True)


# instance=True models an instance: callers do not supply self manually.
# Autospec checks signatures, not annotated types or return-value shapes.
# A mock can still return impossible data if you configure it that way.
# Introspection can interact with properties/descriptors; avoid interfaces
# whose attribute access performs unsafe side effects during inspection.


# ============================================================
# SECTION 4 — PRACTICE AND FINAL REVIEW
# ============================================================
# EXERCISE: Which catches a misspelled method? Which catches a missing
# required argument: spec or autospec?
# ANSWER: ____________________________________________________
# CHALLENGE: Define a Notifier interface with send(address, message).
# Build an autospecced instance and test rejection of a one-argument call.
# Write your code here:
#
# 1. What extra restriction does spec_set provide? ______________
# 2. Does autospec prove the real service behaves correctly? ____
# KEY TAKEAWAY: Interface-aware doubles catch drift and typos,
# but integration tests still matter for real collaborator behavior.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================

