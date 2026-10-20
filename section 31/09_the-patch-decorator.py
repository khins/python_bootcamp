# ============================================================
# FILE: 09_the-patch-decorator.py
# TOPIC: @patch on Test Methods
# ============================================================
# STUDY GUIDE
# Predict before running, then run this file directly with Python.
# Complete the exercises and challenges. No live services are used.

import unittest
from unittest.mock import Mock, MagicMock, call, create_autospec, patch


# LESSON OBJECTIVES
# 1. Apply a patch for the duration of a test method.
# 2. Receive an automatically created mock as an argument.
# 3. Understand argument injection and explicit replacements.


def lookup_name(user_id):
    return "Local User"  # Local stand-in, not a live lookup.


def welcome(user_id):
    return f"Welcome, {lookup_name(user_id)}!"


# ============================================================
# SECTION 1 — DECORATE A TEST METHOD
# ============================================================
class TestWelcome(unittest.TestCase):
    @patch(f"{__name__}.lookup_name", return_value="Ada")
    def test_preconfigured_name(self, mocked_lookup):
        self.assertEqual(welcome(7), "Welcome, Ada!")
        mocked_lookup.assert_called_once_with(7)

    @patch(f"{__name__}.lookup_name")
    def test_configure_inside_method(self, mocked_lookup):
        mocked_lookup.return_value = "Grace"
        self.assertEqual(welcome(8), "Welcome, Grace!")
        mocked_lookup.assert_called_once_with(8)


# The patch is active during the decorated method invocation and is
# restored when it finishes. The created mock is passed after self.
# Do not omit the mock parameter when patch creates a mock for you.
# A method decorator does not wrap setUp or tearDown; those occur outside
# the method invocation. Use fixture-managed patches for that wider scope.


# ============================================================
# SECTION 2 — EXPLICIT new DOES NOT INJECT AN EXTRA MOCK
# ============================================================
def fixed_name(user_id):
    return "Guest"


class TestExplicitNew(unittest.TestCase):
    @patch(f"{__name__}.lookup_name", new=fixed_name)
    def test_explicit_function(self):
        self.assertEqual(welcome(100), "Welcome, Guest!")


# Because a replacement was supplied with new=, patch does not add a
# generated-mock argument. return_value= instead configures a generated
# mock and therefore does still inject that mock argument.


# ============================================================
# SECTION 3 — PRACTICE AND FINAL REVIEW
# ============================================================
# EXERCISE: Why does test_explicit_function have no mocked_lookup parameter?
# ANSWER: ____________________________________________________
# CHALLENGE: Decorate a test with a lookup mock that raises LookupError.
# Verify welcome propagates that exception and passes the requested ID.
# Write your code inside a TestCase subclass:
#
# 1. When is the patch restored? _______________________________
# 2. Does a test-method decorator patch its setUp method? _______
# 3. What is the difference between new= and return_value=? _____
# KEY TAKEAWAY: @patch keeps whole-method patches concise; remember
# which replacements create and inject a mock argument.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================

