# ============================================================
# FILE: 01_unit-testing.py
# TOPIC: Unit Testing Basics
# ============================================================
# LESSON OBJECTIVES
# 1. Identify a unit of behavior.
# 2. Separate expected results from actual results.
# 3. Organize a test using Arrange, Act, Assert.
#
# Run this file directly. Prediction exercises remain commented out.


def add(a, b):
    return a + b


# ============================================================
# SECTION 1 — WHAT IS A UNIT TEST?
# ============================================================
# A unit test checks a small piece of behavior, such as one function.
# It supplies known inputs and compares the outcome with expectations.
# Tests should be repeatable and independent of other tests.
# Printing a result lets a person inspect it; an assertion lets the
# program detect a mismatch automatically.


# ============================================================
# SECTION 2 — ARRANGE, ACT, ASSERT
# ============================================================
def test_add_positive_numbers():
    # Arrange: prepare inputs and an independently chosen expectation.
    first = 2
    second = 3
    expected = 5
    # Act: exercise the behavior.
    actual = add(first, second)
    # Assert: compare the actual result with the expected result.
    assert actual == expected


# A passing assertion is silent. A failing assertion raises AssertionError.
# Python does not run a test function merely because its name starts
# with test_. Call it or use a test runner that discovers it.


# ============================================================
# SECTION 3 — COVER DIFFERENT CASES
# ============================================================
def test_add_zero():
    assert add(7, 0) == 7


def test_add_negative_numbers():
    assert add(-2, -3) == -5


# These check normal and boundary-related behavior without external files,
# network access, user input, or randomness.
# Avoid deriving the expected answer by repeating the implementation:
# expected = first + second would duplicate the operation being tested.


# ============================================================
# SECTION 4 — PREDICT AND PRACTICE
# ============================================================
# EXERCISE 1: If add() returned a - b, which tests above would fail?
# ANSWER: ____________________________________________________
# EXERCISE 2: Why is a test for zero useful even when 2 + 3 works?
# ANSWER: ____________________________________________________
# CHALLENGE: Write double(number) and tests for positive, zero, and
# negative inputs. State each expected answer before running the tests.
# Write your code here:


# ============================================================
# SECTION 5 — FINAL REVIEW
# ============================================================
# 1. What does a unit test check? ______________________________
# 2. What are Arrange, Act, and Assert responsible for? _________
# 3. Does naming a function test_something automatically run it? _
# 4. Why should tests be repeatable? ___________________________
# KEY TAKEAWAY: Turn expectations into executable checks.

if __name__ == "__main__":
    test_add_positive_numbers()
    test_add_zero()
    test_add_negative_numbers()
    print("All three checks passed.")

# ============================================================
# END OF LESSON
# ============================================================
