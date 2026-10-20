# ============================================================
# FILE: 08_the-patch-function.py
# TOPIC: patch() as a Context Manager
# ============================================================
# STUDY GUIDE
# Predict before running, then run this file directly with Python.
# Complete the exercises and challenges. No live services are used.

import unittest
from unittest.mock import Mock, MagicMock, call, create_autospec, patch


# LESSON OBJECTIVES
# 1. Temporarily replace a dependency looked up by production code.
# 2. Configure and inspect the created mock.
# 3. Verify restoration after a patch scope ends.


def read_temperature():
    return 18  # A deterministic stand-in; no real sensor is contacted.


def temperature_message():
    return f"Temperature: {read_temperature()} C"


# ============================================================
# SECTION 1 — PATCH A LOOKUP DURING A with BLOCK
# ============================================================
class TestTemperature(unittest.TestCase):
    def test_overridden_temperature(self):
        target = f"{__name__}.read_temperature"
        with patch(target, return_value=25) as mocked_read:
            self.assertEqual(temperature_message(), "Temperature: 25 C")
            mocked_read.assert_called_once_with()
        self.assertEqual(read_temperature(), 18)

    def test_restored_after_exception(self):
        with self.assertRaises(RuntimeError):
            with patch(f"{__name__}.read_temperature", return_value=99):
                raise RuntimeError("demonstration")
        self.assertEqual(read_temperature(), 18)


# patch(target) resolves a dotted name and temporarily replaces that
# attribute. For these synchronous functions it creates a MagicMock by
# default. The variable after 'as' receives the replacement mock.
# Exiting the context restores the original attribute, including when
# the body raises. The original function itself is not rewritten.
# __name__ supplies this lesson's module name, including '__main__'
# when run directly, avoiding hard-coded numbered lesson filenames.


# ============================================================
# SECTION 2 — SUPPLY A SPECIFIC REPLACEMENT
# ============================================================
class TestExplicitReplacement(unittest.TestCase):
    def test_simple_fake_function(self):
        def fake_read():
            return -5
        with patch(f"{__name__}.read_temperature", new=fake_read):
            self.assertEqual(temperature_message(), "Temperature: -5 C")


# new= supplies your own replacement rather than asking patch to build
# a mock. A plain fake function has no mock call-assertion methods.
# Patch only the dependency; leave temperature_message real.


# ============================================================
# SECTION 3 — PRACTICE AND FINAL REVIEW
# ============================================================
# EXERCISE: What does read_temperature() return after each patch? _
# CHALLENGE: Add a function classifying temperature below zero as
# "freezing". Patch readings of -1, 0, and 1 to test the boundary.
# Write your code here:
#
# 1. What does the 'as' variable receive? _______________________
# 2. Does patch rewrite the original function body? _____________
# 3. Does restoration happen when the with block raises? ________
# KEY TAKEAWAY: A patch temporarily replaces a named dependency
# within a controlled scope and restores the original afterward.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================

