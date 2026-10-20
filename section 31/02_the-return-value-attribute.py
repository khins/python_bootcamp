# ============================================================
# FILE: 02_the-return-value-attribute.py
# TOPIC: Configuring return_value
# ============================================================
# STUDY GUIDE
# Predict before running, then run this file directly with Python.
# Complete the exercises and challenges before checking your answers.
# Examples use only the standard library and make no network requests.

import unittest
from unittest.mock import Mock, MagicMock, call, create_autospec, patch


# LESSON OBJECTIVES
# 1. Set the result of calling a mock.
# 2. Configure child methods and factory results.
# 3. Distinguish attributes from call return values.


# ============================================================
# SECTION 1 — return_value IS THE CALL RESULT
# ============================================================
class TestReturnValue(unittest.TestCase):
    def test_configure_after_creation(self):
        fetch = Mock()
        fetch.return_value = 42
        self.assertEqual(fetch(), 42)
        self.assertEqual(fetch("another input"), 42)

    def test_configure_in_constructor(self):
        fetch = Mock(return_value=None)
        self.assertIsNone(fetch())

    def test_same_mutable_result_is_reused(self):
        fetch = Mock(return_value=[])
        first = fetch()
        first.append("new")
        self.assertIs(fetch(), first)
        self.assertEqual(fetch(), ["new"])


# return_value is not a formula based on arguments: every ordinary call
# returns the configured object. Use side_effect for argument-dependent
# behavior, sequential answers, exceptions, or fresh results per call.


# ============================================================
# SECTION 2 — ATTRIBUTES VERSUS METHODS
# ============================================================
class TestChildConfiguration(unittest.TestCase):
    def test_response_attributes_and_method(self):
        response = Mock()
        response.status_code = 200
        response.json.return_value = {"name": "Ada"}
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"name": "Ada"})
        response.json.assert_called_once_with()

    def test_factory_returns_configured_instance(self):
        factory = Mock()
        factory.return_value.read.return_value = "file contents"
        reader = factory("demo.txt")
        self.assertEqual(reader.read(), "file contents")
        factory.assert_called_once_with("demo.txt")


# response.status_code is read directly. response.json() calls a method.
# factory.return_value represents the object returned by factory(...).
# Configuring factory.read.return_value would affect a different path.


# ============================================================
# SECTION 3 — PRACTICE
# ============================================================
# EXERCISE: What differs between mock.result = 5 and
# mock.result.return_value = 5?
# ANSWER: ____________________________________________________
# CHALLENGE: Configure a repository double so get_names() returns
# ["Ada", "Grace"]. Test a real function that joins these names.
# Write your code here:


# ============================================================
# SECTION 4 — FINAL REVIEW
# ============================================================
# 1. Does return_value vary automatically with arguments? _______
# 2. Does a mutable return_value create a new object per call? ___
# 3. How do you explicitly make a mock return None? _____________
# KEY TAKEAWAY: Configure the exact attribute or call path that
# your production code uses.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================

