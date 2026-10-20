# ============================================================
# FILE: 03_the-side-effect-attribute.py
# TOPIC: Configuring side_effect
# ============================================================
# STUDY GUIDE
# Predict before running, then run this file directly with Python.
# Complete the exercises and challenges before checking your answers.
# Examples use only the standard library and make no network requests.

import unittest
from unittest.mock import Mock, MagicMock, call, create_autospec, patch


# LESSON OBJECTIVES
# 1. Raise an exception from a mock.
# 2. Return a sequence of answers.
# 3. Compute results from call arguments.
# 4. Understand precedence over return_value.


# ============================================================
# SECTION 1 — SIMULATE AN ERROR
# ============================================================
class TestSideEffects(unittest.TestCase):
    def test_raise_exception(self):
        fetch = Mock(side_effect=TimeoutError("service unavailable"))
        with self.assertRaisesRegex(TimeoutError, "unavailable"):
            fetch("record")
        fetch.assert_called_once_with("record")

    def test_sequence_of_answers(self):
        fetch = Mock(side_effect=[10, 20, 30])
        self.assertEqual(fetch(), 10)
        self.assertEqual(fetch(), 20)
        self.assertEqual(fetch(), 30)
        with self.assertRaises(StopIteration):
            fetch()

    def test_error_then_success(self):
        fetch = Mock(side_effect=[TimeoutError("try again"), "ready"])
        with self.assertRaises(TimeoutError):
            fetch()
        self.assertEqual(fetch(), "ready")


# A call is recorded even if its side_effect raises an exception.
# An iterable is consumed one item per call; exceptions in it are raised.
# Exhaustion raises StopIteration for these synchronous mocks.


# ============================================================
# SECTION 2 — USE A FUNCTION
# ============================================================
def price_for_item(name):
    return {"tea": 3, "coffee": 4}[name]


class TestComputedAnswers(unittest.TestCase):
    def test_arguments_reach_side_effect(self):
        price = Mock(side_effect=price_for_item)
        self.assertEqual(price("tea"), 3)
        self.assertEqual(price("coffee"), 4)

    def test_side_effect_takes_precedence(self):
        fetch = Mock(return_value="fallback", side_effect=lambda: "computed")
        self.assertEqual(fetch(), "computed")
        fetch.side_effect = None
        self.assertEqual(fetch(), "fallback")


# Assign the function itself, not the result of calling it.
# A side-effect function's None result is returned as None; it does not
# automatically fall back to return_value. Returning unittest.mock.DEFAULT
# explicitly requests normal return-value handling instead.


# ============================================================
# SECTION 3 — PRACTICE
# ============================================================
# EXERCISE: What happens on call three with side_effect=[1, 2]? ___
# CHALLENGE: Use side_effect to model two failures followed by success.
# Write a real function that tries at most three times and test it.
# Also cover the case where every attempt fails.
# Write your code here:


# ============================================================
# SECTION 4 — FINAL REVIEW
# ============================================================
# 1. Name three supported forms of side_effect. ________________
# 2. Are calls that raise exceptions recorded? _________________
# 3. How do you clear side_effect? _____________________________
# KEY TAKEAWAY: side_effect models changing answers, errors, and
# argument-dependent behavior without using a live dependency.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================

