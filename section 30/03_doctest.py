# ============================================================
# FILE: 03_doctest.py
# TOPIC: Executable Examples with doctest
# ============================================================
# LESSON OBJECTIVES
# 1. Put interactive examples in a docstring.
# 2. Compare actual output with documented output.
# 3. Run doctest and interpret its results.

import doctest


# ============================================================
# SECTION 1 — DOCUMENT A FUNCTION WITH EXAMPLES
# ============================================================
def double(number):
    """Return twice the supplied number.

    >>> double(3)
    6
    >>> double(0)
    0
    >>> double(-4)
    -8
    """
    return number * 2


# >>> marks an interactive Python input. The following line is the
# expected output. doctest executes the input and compares the text.
# The examples also help readers understand how to call the function.


# ============================================================
# SECTION 2 — REPRESENTATION MATTERS
# ============================================================
def greet(name):
    """Build a greeting.

    >>> greet("Ada")
    'Hello, Ada!'
    >>> print(greet("Ada"))
    Hello, Ada!
    """
    return f"Hello, {name}!"


# A returned string is displayed using its representation, with quotes.
# print() writes the contents without those surrounding quotes.
# By default, whitespace and output text matter. Blank output lines
# can be represented with <BLANKLINE> in expected doctest output.
# Keep examples deterministic: current times and unseeded randomness
# make exact expected text difficult to maintain.


# ============================================================
# SECTION 3 — RUN AND READ THE RESULTS
# ============================================================
# Run this file directly for verbose results using the main block below.
# Or, from the repository root with Python installed:
# python -m doctest -v "section 30/03_doctest.py"
# The -v option reports each example, including passing examples.
# A mismatch shows expected versus actual output.
# doctest.testmod() returns counts named failed and attempted.
# Our main block exits with a nonzero status if any example fails.


# ============================================================
# SECTION 4 — PREDICT AND PRACTICE
# ============================================================
# EXERCISE 1: Why does greet("Ada") show quotes but print(...) does not?
# ANSWER: ____________________________________________________
# EXERCISE 2: Change one expected answer temporarily. Run the file,
# inspect the failure, then restore the correct expectation.
# CHALLENGE: Write square(number) with docstring examples for 3, 0,
# and -2. Run doctest to check all three examples.
# Write your code here:


# ============================================================
# SECTION 5 — FINAL REVIEW
# ============================================================
# 1. What does >>> mark? ______________________________________
# 2. Does doctest compare output text or only numeric meaning? ___
# 3. What does verbose mode add? _______________________________
# 4. Why are deterministic examples useful? ____________________
# KEY TAKEAWAY: doctest keeps small documented examples executable.
# Use a dedicated test suite for more extensive behavior checks.

if __name__ == "__main__":
    results = doctest.testmod(verbose=True)
    raise SystemExit(1 if results.failed else 0)

# ============================================================
# END OF LESSON
# ============================================================
