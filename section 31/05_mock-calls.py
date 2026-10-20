# ============================================================
# FILE: 05_mock-calls.py
# TOPIC: Recording and Verifying Mock Calls
# ============================================================
# STUDY GUIDE
# Predict before running, then run this file directly with Python.
# Complete the exercises and challenges. No live services are used.

import unittest
from unittest.mock import Mock, MagicMock, call, create_autospec, patch


# LESSON OBJECTIVES
# 1. Inspect call counts and arguments.
# 2. Verify single calls and sequences of calls.
# 3. Distinguish exact call histories from partial checks.
# 4. Reset history without accidentally assuming configuration is reset.


# ============================================================
# SECTION 1 — COMMON CALL ASSERTIONS
# ============================================================
class TestCallAssertions(unittest.TestCase):
    def test_one_call(self):
        send = Mock()
        send("Ada", urgent=True)
        send.assert_called_once_with("Ada", urgent=True)
        self.assertTrue(send.called)
        self.assertEqual(send.call_count, 1)
        self.assertEqual(send.call_args, call("Ada", urgent=True))

    def test_no_calls(self):
        send = Mock()
        send.assert_not_called()

    def test_last_call_and_any_call(self):
        send = Mock()
        send("first")
        send("second")
        send.assert_called_with("second")
        send.assert_any_call("first")
        self.assertEqual(send.call_count, 2)


# assert_called_with checks the LAST call, not the only call.
# assert_called_once checks count, but not arguments.
# assert_called_once_with checks both. Successful assertion methods
# return normally; do not wrap them in assertTrue().


# ============================================================
# SECTION 2 — VERIFY ORDER AND COMPLETE HISTORY
# ============================================================
class TestCallSequences(unittest.TestCase):
    def test_exact_direct_calls(self):
        save = Mock()
        save("a")
        save("b")
        self.assertEqual(save.call_args_list, [call("a"), call("b")])

    def test_child_method_history(self):
        client = Mock()
        client.connect()
        client.send("hello")
        client.close()
        self.assertEqual(client.mock_calls,
                         [call.connect(), call.send("hello"), call.close()])
        client.assert_has_calls([call.connect(), call.send("hello")])


# call_args_list records direct calls to that mock.
# mock_calls also includes calls through child mocks and return values.
# assert_has_calls checks the expected sequential group by default;
# extra calls before or after it are allowed. any_order=True relaxes order.
# Compare complete call lists when extra calls must cause failure.


# ============================================================
# SECTION 3 — RESET HISTORY
# ============================================================
class TestReset(unittest.TestCase):
    def test_reset_preserves_return_value_by_default(self):
        fetch = Mock(return_value=10)
        fetch()
        fetch.reset_mock()
        fetch.assert_not_called()
        self.assertEqual(fetch(), 10)


# reset_mock() clears call history, not return_value or side_effect by
# default. A fresh mock per test is usually clearer than sharing one.


# ============================================================
# SECTION 4 — PRACTICE AND FINAL REVIEW
# ============================================================
# EXERCISE: Can assert_called_with pass after three calls? _______
# CHALLENGE: Test a function that logs "start", processes an item,
# then logs "end". Verify the exact logger call_args_list.
# Write your code here:
#
# 1. Which assertion checks zero calls? ________________________
# 2. Does assert_has_calls forbid all extra calls? ______________
# 3. Does reset_mock() erase return_value by default? ___________
# KEY TAKEAWAY: Select a call assertion that expresses exactly how
# much of the interaction contract matters.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================

