# ============================================================
# FILE: 04_mock-versus-magicmock.py
# TOPIC: Mock versus MagicMock
# ============================================================
# STUDY GUIDE
# Predict before running, then run this file directly with Python.
# Complete the exercises and challenges before checking your answers.
# Examples use only the standard library and make no network requests.

import unittest
from unittest.mock import Mock, MagicMock, call, create_autospec, patch


# LESSON OBJECTIVES
# 1. Recognize Python special methods used by protocols.
# 2. Configure MagicMock for containers and context managers.
# 3. Avoid mistaking default protocol behavior for real behavior.


# ============================================================
# SECTION 1 — MAGIC METHODS SUPPORT PYTHON OPERATIONS
# ============================================================
# Special methods such as __len__, __iter__, __enter__, and __exit__
# power len(), iteration, and with statements. MagicMock preconfigures
# many of these supported methods. Mock can be configured with special
# methods explicitly but does not provide the same ready-made defaults.

class TestContainerProtocol(unittest.TestCase):
    def test_length_and_iteration(self):
        items = MagicMock()
        items.__len__.return_value = 2
        items.__iter__.return_value = ["a", "b"]
        self.assertEqual(len(items), 2)
        self.assertEqual(list(items), ["a", "b"])

    def test_membership(self):
        items = MagicMock()
        items.__contains__.return_value = True
        self.assertIn("example", items)


# These methods are configured independently. Setting __len__ to 2
# does not create two entries or make iteration yield two elements.
# A list assigned to __iter__.return_value supports repeated iteration;
# an iterator assigned there can be exhausted after one traversal.


# ============================================================
# SECTION 2 — CONTEXT MANAGERS
# ============================================================
class TestContextManager(unittest.TestCase):
    def test_with_statement(self):
        manager = MagicMock()
        resource = Mock()
        resource.read.return_value = "contents"
        manager.__enter__.return_value = resource
        with manager as opened:
            actual = opened.read()
        self.assertEqual(actual, "contents")
        manager.__enter__.assert_called_once_with()
        manager.__exit__.assert_called_once_with(None, None, None)


# The value assigned after 'as' comes from __enter__(), not necessarily
# from manager itself. __exit__ receives exception details on failure.
# A truthy __exit__ result suppresses an exception; configure deliberately.


# ============================================================
# SECTION 3 — DEFAULTS CAN HIDE MISTAKES
# ============================================================
class TestDefaults(unittest.TestCase):
    def test_default_length_and_truthiness_are_independent(self):
        value = MagicMock()
        self.assertEqual(len(value), 0)
        self.assertTrue(value)


# Choose Mock for simple callable/attribute collaborators and MagicMock
# when the required interface includes supported Python protocols.
# Neither guarantees the real collaborator behaves as configured.


# ============================================================
# SECTION 4 — PRACTICE AND FINAL REVIEW
# ============================================================
# EXERCISE: Why does setting __len__ not configure iteration? ____
# CHALLENGE: Configure a context manager whose resource exposes save().
# Call a real function using that manager and verify save's arguments.
# Write your code here:
#
# 1. Which method supplies the value after 'as'? ________________
# 2. Can a MagicMock with length zero still be truthy? ___________
# KEY TAKEAWAY: MagicMock adds protocol support; configure each
# behavior that matters instead of relying on convenient defaults.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================

