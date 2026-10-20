# ============================================================
# FILE: 02_the-assert-statement.py
# TOPIC: The assert Statement
# ============================================================
# LESSON OBJECTIVES
# 1. Write assertions with optional messages.
# 2. Recognize AssertionError.
# 3. Distinguish debugging assertions from required validation.


# ============================================================
# SECTION 1 — ASSERT A CONDITION
# ============================================================
def example_passing_assertion():
    total = 2 + 3
    assert total == 5
    print("The assertion passed.")


# assert expression succeeds when expression is truthy.
# A false expression raises AssertionError and interrupts normal flow.
# It does not return a Boolean result for you to store.


# ============================================================
# SECTION 2 — ADD A FAILURE MESSAGE
# ============================================================
def example_caught_failure():
    try:
        assert 2 + 3 == 6, "Expected a total of six"
    except AssertionError as error:
        print(f"Demonstration caught: {error}")


# Here we catch the failure only to demonstrate it safely.
# Real tests normally let their runner report the failure.
# Correct syntax: assert condition, "helpful message"
# Avoid assert (condition, "message"): that creates a nonempty tuple,
# which is truthy even if condition is False.


# ============================================================
# SECTION 3 — DO NOT USE assert FOR REQUIRED VALIDATION
# ============================================================
# Python can remove assert statements when run with optimization (-O).
# Never rely on them for required input validation or security checks.
# Avoid side effects inside assertions because they may not execute.

def divide(total, count):
    if count == 0:
        raise ValueError("count must not be zero")
    return total / count


# This explicit validation remains active under optimization.
# unittest assertion methods are ordinary method calls and are not
# removed in the way the Python assert statement can be.


# ============================================================
# SECTION 4 — PREDICT AND PRACTICE
# ============================================================
# EXERCISE 1: Which pass: assert [], assert [0], assert "hello"?
# ANSWER: ____________________________________________________
# EXERCISE 2: What exception does assert False raise? ___________
# CHALLENGE: Check that sorted([3, 1, 2]) equals [1, 2, 3]. Add a
# message that explains the expected order if the assertion fails.
# Write your code here:


# ============================================================
# SECTION 5 — FINAL REVIEW
# ============================================================
# 1. Does assert require the literal value True or any truthy value?
# ANSWER: ____________________________________________________
# 2. Why is assert unsuitable for mandatory validation? _________
# 3. What is wrong with assert (False, "Oops")? ________________
# KEY TAKEAWAY: Assertions check assumptions; explicit exceptions
# enforce validation that must always run.

if __name__ == "__main__":
    example_passing_assertion()
    example_caught_failure()
    assert divide(10, 2) == 5

# ============================================================
# END OF LESSON
# ============================================================
