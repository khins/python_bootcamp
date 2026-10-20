# ============================================================
# FILE: 14_testing-errors-with-assert-raises.py
# TOPIC: Expected Exceptions with assertRaises
# ============================================================
# STUDY GUIDE
# Predict before running, then execute this file directly.
# Complete the practice exercises and review questions.

import unittest


# LESSON OBJECTIVES
# 1. Verify that an operation raises an expected exception.
# 2. Inspect a captured exception and check its message.
# 3. Keep the checked operation narrowly scoped.


def divide(total, count):
    if count == 0:
        raise ValueError("count must not be zero")
    return total / count


# ============================================================
# SECTION 1 — EXPECT AN ERROR AS CORRECT BEHAVIOR
# ============================================================
class TestDivision(unittest.TestCase):
    def test_zero_count_is_rejected(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_valid_division(self):
        self.assertEqual(divide(10, 2), 5)


# The context manager passes if the expected exception (or a subclass)
# occurs inside the block. No exception produces a test failure.
# A different unexpected exception normally produces a test error.
# The expected exception is captured so the test can continue afterward.


# ============================================================
# SECTION 2 — CAPTURE AND INSPECT THE EXCEPTION
# ============================================================
class TestErrorDetails(unittest.TestCase):
    def test_exact_error_message(self):
        with self.assertRaises(ValueError) as caught:
            divide(10, 0)
        self.assertEqual(str(caught.exception), "count must not be zero")

    def test_message_pattern(self):
        with self.assertRaisesRegex(ValueError, r"count.*zero"):
            divide(10, 0)

    def test_callable_form(self):
        self.assertRaises(ValueError, divide, 10, 0)


# Inspect caught.exception AFTER the with block.
# assertRaisesRegex checks a regular-expression match in the message,
# not necessarily equality of the entire message. Use ^ and $ to anchor
# a pattern when appropriate, or assertEqual on str(exception).
# The callable form receives divide itself and then its arguments.
# Wrong: self.assertRaises(ValueError, divide(10, 0))
# That evaluates divide BEFORE assertRaises can capture the exception.


# ============================================================
# SECTION 3 — KEEP THE BLOCK SMALL
# ============================================================
# Put only the operation expected to fail inside the with block.
# Unrelated setup could raise the same exception and create a false pass.
# Code after the failing operation inside that block will not run.
# Do not catch and silently discard the exception yourself in the test.
# Pair rejection tests with valid-input tests to cover both behaviors.


# ============================================================
# SECTION 4 — PRACTICE
# ============================================================
# EXERCISE 1: What happens if divide(10, 0) returns None instead? _
# EXERCISE 2: Where can you inspect caught.exception? ____________
# CHALLENGE: Write parse_age(text) using int(text), then reject negative
# values with ValueError. Test "12", "hello", and "-1". Verify the
# negative-age message without depending on int()'s exact wording.
# Write your code here:


# ============================================================
# SECTION 5 — FINAL REVIEW
# ============================================================
# 1. Can an expected exception represent a passing test? _________
# 2. Does assertRaises accept subclasses of the expected error? _
# 3. Why keep the with block narrow? ___________________________
# 4. What does assertRaisesRegex add? __________________________
# KEY TAKEAWAY: Verify intentional error behavior just as carefully
# as successful results, using focused exception assertions.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================

