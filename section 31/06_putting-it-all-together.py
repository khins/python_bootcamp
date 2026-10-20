# ============================================================
# FILE: 06_putting-it-all-together.py
# TOPIC: A Complete Unit Test with Controlled Collaborators
# ============================================================
# STUDY GUIDE
# Predict before running, then run this file directly with Python.
# Complete the exercises and challenges. No live services are used.

import unittest
from unittest.mock import Mock, MagicMock, call, create_autospec, patch


# LESSON OBJECTIVES
# 1. Combine prepared answers, failures, and interaction checks.
# 2. Exercise real branching and retry behavior.
# 3. Cover success, recovery, and permanent failure.


def send_order_summary(order_id, repository, notifier):
    """Retry one timed-out lookup, then notify with the order total."""
    for attempt in range(2):
        try:
            order = repository.fetch(order_id)
            break
        except TimeoutError:
            if attempt == 1:
                raise
    message = f"Order {order_id}: {order['total']}"
    notifier.send(order["email"], message)
    return message


# ============================================================
# SECTION 1 — SUCCESS WITHOUT A RETRY
# ============================================================
class TestOrderSummary(unittest.TestCase):
    def setUp(self):
        self.repository = Mock()
        self.notifier = Mock()
        self.order = {"total": 25, "email": "learner@example.test"}

    def test_success(self):
        self.repository.fetch.return_value = self.order
        result = send_order_summary(7, self.repository, self.notifier)
        self.assertEqual(result, "Order 7: 25")
        self.repository.fetch.assert_called_once_with(7)
        self.notifier.send.assert_called_once_with(
            "learner@example.test", "Order 7: 25")

    # ========================================================
    # SECTION 2 — TRANSIENT FAILURE, THEN RECOVERY
    # ========================================================
    def test_timeout_then_success(self):
        self.repository.fetch.side_effect = [TimeoutError(), self.order]
        result = send_order_summary(7, self.repository, self.notifier)
        self.assertEqual(result, "Order 7: 25")
        self.assertEqual(self.repository.fetch.call_args_list, [call(7), call(7)])
        self.notifier.send.assert_called_once_with(
            "learner@example.test", "Order 7: 25")

    # ========================================================
    # SECTION 3 — PERMANENT FAILURE STOPS THE WORKFLOW
    # ========================================================
    def test_two_timeouts_propagate_without_notification(self):
        self.repository.fetch.side_effect = TimeoutError("unavailable")
        with self.assertRaises(TimeoutError):
            send_order_summary(7, self.repository, self.notifier)
        self.assertEqual(self.repository.fetch.call_count, 2)
        self.notifier.send.assert_not_called()

    def test_other_errors_are_not_retried(self):
        self.repository.fetch.side_effect = ValueError("invalid order")
        with self.assertRaises(ValueError):
            send_order_summary(7, self.repository, self.notifier)
        self.repository.fetch.assert_called_once_with(7)
        self.notifier.send.assert_not_called()


# The notifier is only a Mock: no messages are actually sent.
# Test the real workflow, not a mocked send_order_summary function.
# Local mocks make each test independent and keep retries instantaneous.


# ============================================================
# SECTION 4 — PRACTICE AND FINAL REVIEW
# ============================================================
# EXERCISE: Why is assert_not_called useful on the failure path? __
# CHALLENGE: Add a test where notifier.send raises RuntimeError.
# Verify it propagates and repository.fetch is not retried.
# Write your code inside the test class:
#
# 1. Which collaborator determines whether lookup succeeds? _____
# 2. Which exception is eligible for retry? _____________________
# 3. Why test an exception that must not be retried? ____________
# KEY TAKEAWAY: Combine output and interaction checks to cover
# real success and failure paths with controlled collaborators.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================

