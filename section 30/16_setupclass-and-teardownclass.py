# ============================================================
# FILE: 16_setupclass-and-teardownclass.py
# TOPIC: Class Fixtures with setUpClass and tearDownClass
# ============================================================
# STUDY GUIDE
# Predict before running, then execute this file directly.
# Complete the practice exercises and review questions.

import unittest


# LESSON OBJECTIVES
# 1. Prepare a shared fixture for a test class.
# 2. Distinguish per-class and per-test lifecycle methods.
# 3. Avoid leaking mutable state between tests.
# 4. Register class cleanup safely.

from pathlib import Path
from tempfile import TemporaryDirectory


# ============================================================
# SECTION 1 — CLASS METHODS RECEIVE cls
# ============================================================
# In a normal run grouping a class's tests together:
# setUpClass runs once before the class's tests.
# tearDownClass runs once after the class's tests.
# Both use @classmethod and receive cls rather than self.
# setUp and tearDown still run around each individual test.

class TestSharedCatalog(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.directory = TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name) / "catalog.txt"
        cls.path.write_text("apple\nbanana\n", encoding="utf-8")
        # Immutable shared data helps avoid accidental test interference.
        cls.catalog = tuple(cls.path.read_text(encoding="utf-8").splitlines())

    def setUp(self):
        # Each test receives its own mutable working list.
        self.items = list(self.catalog)

    def test_append_to_working_copy(self):
        self.items.append("cherry")
        self.assertEqual(self.items, ["apple", "banana", "cherry"])
        self.assertEqual(self.catalog, ("apple", "banana"))

    def test_original_catalog_contents(self):
        self.assertEqual(self.items, ["apple", "banana"])

    @classmethod
    def tearDownClass(cls):
        cls.directory.cleanup()


# TemporaryDirectory.cleanup() tolerates repeated cleanup here.
# The registered callback protects against failures during later class
# setup. In practice, the callback alone can handle resource disposal;
# the explicit tearDownClass demonstrates the class lifecycle hook.


# ============================================================
# SECTION 2 — TRACE THE NORMAL LIFECYCLE
# ============================================================
# setUpClass
#   setUp -> first test -> tearDown (if defined)
#   setUp -> second test -> tearDown (if defined)
# tearDownClass
# registered class cleanup callbacks
#
# Avoid relying on test order. Custom suites that separate a class's tests
# into multiple groups may invoke its class fixtures more than once.


# ============================================================
# SECTION 3 — FAILURE AND CLEANUP BEHAVIOR
# ============================================================
# If setUpClass raises an exception, its tests and tearDownClass do not run.
# addClassCleanup callbacks already registered still run.
# They run after tearDownClass on the normal path, in reverse registration
# order. Cleanup should handle the resources actually acquired.
# Do not share a mutable list that tests alter without resetting it.
# A class fixture can save costly setup, but shared state adds complexity.
# Prefer per-test fixtures unless sharing has a clear benefit.


# ============================================================
# SECTION 4 — PRACTICE
# ============================================================
# EXERCISE 1: For two normally grouped tests, how many times do
# setUpClass and setUp run respectively? _______________________
# EXERCISE 2: Why copy the tuple into self.items for each test? ___
# EXERCISE 3: Which cleanup runs after a setUpClass failure? _____
# CHALLENGE: Create a shared tuple of three names in setUpClass.
# In setUp, copy it to a list. Test sorting and removing a name in
# separate methods, keeping the shared tuple unchanged.
# Write your code here:


# ============================================================
# SECTION 5 — FINAL REVIEW
# ============================================================
# 1. Which decorator belongs on setUpClass? ____________________
# 2. What does cls refer to? __________________________________
# 3. How do class fixtures differ from per-test fixtures? _______
# 4. Why can mutable class state create order-dependent failures? _
# KEY TAKEAWAY: Share expensive, stable prerequisites at class level;
# keep mutable working state separate for each test.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================

