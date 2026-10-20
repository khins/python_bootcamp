# ============================================================
# FILE: 01_mock-introduction.py
# TOPIC: Introduction to Test Doubles and Mock
# ============================================================
# STUDY GUIDE
# Predict before running, then run this file directly with Python.
# Complete the exercises and challenges before checking your answers.
# Examples use only the standard library and make no network requests.

import unittest
from unittest.mock import Mock, MagicMock, call, create_autospec, patch


# LESSON OBJECTIVES
# 1. Explain why a test replaces an external dependency.
# 2. Create a configurable, observable test double.
# 3. Test real behavior while controlling its collaborator.


# ============================================================
# SECTION 1 — WHAT IS A TEST DOUBLE?
# ============================================================
# A test double stands in for a collaborator used by the code under test.
# It can replace a slow, unavailable, or unpredictable dependency.
# A stub supplies prepared answers; a spy records interactions; a fake
# has a simplified working implementation. Mock supports configurable
# answers and recorded calls, so it can serve several of these roles.
# unittest.mock is a module; Mock is a class within it.


def greeting_for_user(user_id, lookup):
    profile = lookup(user_id)
    return f"Hello, {profile['name']}!"


# ============================================================
# SECTION 2 — INJECT THE DEPENDENCY
# ============================================================
class TestGreeting(unittest.TestCase):
    def test_greeting_uses_profile(self):
        lookup = Mock(return_value={"name": "Ada"})
        actual = greeting_for_user(7, lookup)
        self.assertEqual(actual, "Hello, Ada!")
        lookup.assert_called_once_with(7)


# greeting_for_user is real code. Only lookup is replaced.
# Passing a collaborator as an argument is dependency injection.
# No database, server, or real account is needed for this test.
# The assertion about the result checks behavior; the call assertion
# checks an interaction that matters to that behavior.


# ============================================================
# SECTION 3 — DEFAULT MOCKS ARE FLEXIBLE
# ============================================================
class TestMockBasics(unittest.TestCase):
    def test_default_return_value_is_a_mock(self):
        dependency = Mock()
        result = dependency("input")
        self.assertIsInstance(result, Mock)
        self.assertIs(result, dependency.return_value)


# Calling a plain Mock normally returns another mock, not None.
# Reading ordinary unspecified attributes creates child mocks lazily.
# This flexibility can hide misspelled method names. Later lessons use
# spec, spec_set, and autospec to constrain doubles to real interfaces.


# ============================================================
# SECTION 4 — PRACTICE
# ============================================================
# EXERCISE: What is real and what is replaced in TestGreeting?
# ANSWER: ____________________________________________________
# CHALLENGE: Write display_balance(account_id, fetch_balance). Return
# a formatted message. Supply a Mock with a fixed balance and verify
# both the message and the account ID passed to fetch_balance.
# Write your code here:


# ============================================================
# SECTION 5 — FINAL REVIEW
# ============================================================
# 1. What does a test double replace? __________________________
# 2. Why avoid replacing the very behavior being tested? ________
# 3. What does an unconfigured Mock call return? _______________
# KEY TAKEAWAY: Control collaborators while exercising real code.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================

