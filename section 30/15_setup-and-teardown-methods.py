# ============================================================
# FILE: 15_setup-and-teardown-methods.py
# TOPIC: Per-Test Fixtures with setUp and tearDown
# ============================================================
# STUDY GUIDE
# Predict before running, then execute this file directly.
# Complete the practice exercises and review questions.

import unittest


# LESSON OBJECTIVES
# 1. Prepare fresh state before each test.
# 2. Clean up resources after each test.
# 3. Understand lifecycle behavior when setup fails.
# 4. Register reliable cleanup with addCleanup().

from pathlib import Path
from tempfile import TemporaryDirectory


# ============================================================
# SECTION 1 — A FRESH FIXTURE FOR EACH TEST
# ============================================================
# A fixture is the state/resources needed to run a test.
# Names are case-sensitive: setUp and tearDown, not setup/teardown.
# Normal sequence: setUp -> one test method -> tearDown.
# unittest uses a separate TestCase instance for each test method.

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ["milk"]

    def test_append_item(self):
        self.cart.append("bread")
        self.assertEqual(self.cart, ["milk", "bread"])

    def test_initial_contents(self):
        self.assertEqual(self.cart, ["milk"])


# setUp constructs a fresh list every time, so one test's append
# cannot affect the next test. No tearDown is needed for this plain list.
# Do not write empty cleanup methods just to follow a template.


# ============================================================
# SECTION 2 — RELEASE RESOURCES WITH tearDown
# ============================================================
class TestTemporaryFile(unittest.TestCase):
    def setUp(self):
        self.directory = TemporaryDirectory()
        # Register cleanup immediately in case later setup fails.
        # TemporaryDirectory.cleanup() is safe to call again here.
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "note.txt"
        self.path.write_text("hello", encoding="utf-8")

    def tearDown(self):
        self.directory.cleanup()

    def test_file_contents(self):
        self.assertEqual(self.path.read_text(encoding="utf-8"), "hello")

    def test_file_exists(self):
        self.assertTrue(self.path.is_file())


# This example creates only temporary test data and removes it afterward.
# If setUp succeeds, tearDown runs even when the test fails or errors.
# If setUp raises, the test body and tearDown do not run.
# Registered addCleanup callbacks still run if setUp fails after their
# registration. They also run after tearDown, even if tearDown raises.
# Cleanup callbacks run in reverse registration order (last in, first out).
# In ordinary code, registering directory.cleanup alone is enough;
# both approaches appear here to illustrate their lifecycle relationship.


# ============================================================
# SECTION 3 — KEEP TESTS INDEPENDENT
# ============================================================
# Shared setup should contain prerequisites, not another test's work.
# Never depend on the order of test method names for correctness.
# Keep tests' key actions and expected results visible in each test.
# For simple tests, local variables may be clearer than a fixture.


# ============================================================
# SECTION 4 — PRACTICE
# ============================================================
# EXERCISE 1: How many times does setUp run for two cart tests? ___
# EXERCISE 2: Does tearDown run after a test assertion fails? _____
# EXERCISE 3: Does tearDown run if setUp itself raises? __________
# CHALLENGE: Create a fresh dictionary in setUp. In one test modify
# it; in another assert the original contents. Both must pass independently.
# Write your code here:


# ============================================================
# SECTION 5 — FINAL REVIEW
# ============================================================
# 1. What is a fixture? _______________________________________
# 2. When does setUp run? _____________________________________
# 3. Why register cleanup immediately after resource creation? __
# 4. In which order do cleanup callbacks run? __________________
# KEY TAKEAWAY: Use fresh per-test state and reliable cleanup so
# tests do not affect one another, even when something fails.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================

