# ============================================================
# FILE: 10_patching-functions-and-stacked-decorators.py
# TOPIC: Patching Functions: autospec, Stacked Decorators, and Fixtures
# ============================================================
# STUDY GUIDE
# Predict before running, then run this file directly with Python.
# Complete the exercises and challenges. No live services are used.

import unittest
from unittest.mock import Mock, MagicMock, call, create_autospec, patch


# LESSON OBJECTIVES
# 1. Patch multiple collaborating functions.
# 2. Match stacked decorators to injected arguments.
# 3. Preserve call signatures with autospec=True.
# 4. Manage a patch across setup and test execution.


def fetch_total(order_id):
    return 25  # Local stand-in only.


def format_total(total, *, currency="USD"):
    return f"{currency} {total}"


def order_label(order_id):
    return format_total(fetch_total(order_id), currency="USD")


# ============================================================
# SECTION 1 — STACKED DECORATORS INJECT BOTTOM-UP
# ============================================================
class TestOrderLabel(unittest.TestCase):
    @patch(f"{__name__}.format_total", autospec=True)
    @patch(f"{__name__}.fetch_total", autospec=True)
    def test_two_dependencies(self, mocked_fetch, mocked_format):
        mocked_fetch.return_value = 40
        mocked_format.return_value = "USD 40"
        self.assertEqual(order_label(7), "USD 40")
        mocked_fetch.assert_called_once_with(7)
        mocked_format.assert_called_once_with(40, currency="USD")

    @patch(f"{__name__}.fetch_total", autospec=True)
    def test_missing_argument_is_rejected(self, mocked_fetch):
        with self.assertRaises(TypeError):
            fetch_total()
        mocked_fetch.assert_not_called()


# The decorator nearest the function supplies the first mock argument
# after self. The next decorator supplies the next argument.
# autospec=True preserves the original function's call signature for
# validation. It does not validate return-value types or business rules.
# This test checks orchestration, not the real formatting implementation;
# format_total should also have its own real-behavior tests.


# ============================================================
# SECTION 2 — START A PATCH IN setUp AND REGISTER CLEANUP
# ============================================================
class TestFixturePatch(unittest.TestCase):
    def setUp(self):
        patcher = patch(f"{__name__}.fetch_total", autospec=True)
        self.mocked_fetch = patcher.start()
        self.addCleanup(patcher.stop)
        self.mocked_fetch.return_value = 12

    def test_real_formatter_with_patched_fetch(self):
        self.assertEqual(order_label(3), "USD 12")
        self.mocked_fetch.assert_called_once_with(3)


# start() activates a patch until stop() is called. Register cleanup
# immediately after starting so later setup failures still restore it.
# A test-method @patch decorator is usually simpler for one test;
# fixture-managed patching can share setup across several test methods.
# Each test here still receives a fresh patch and call history.


# ============================================================
# SECTION 3 — PRACTICE AND FINAL REVIEW
# ============================================================
# EXERCISE: Reverse the two decorators. How must the parameters change?
# ANSWER: ____________________________________________________
# CHALLENGE: Patch only fetch_total and keep format_total real. Test
# values 0 and 50, verifying the actual formatted output in each case.
# Write your code here:
#
# 1. In what order are stacked mocks injected? _________________
# 2. What does autospec=True add? ______________________________
# 3. Why register patcher.stop with addCleanup? _________________
# KEY TAKEAWAY: Keep patch scopes clear, preserve real signatures,
# and avoid replacing behavior that the test needs to exercise.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================

