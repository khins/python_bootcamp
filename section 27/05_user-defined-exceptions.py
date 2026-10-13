# ============================================================
# FILE: user-defined-exceptions.py
# TOPIC: User-Defined Exceptions
# ============================================================
# LESSON OBJECTIVES
# 1. Create a custom exception class.
# 2. Understand why custom exceptions inherit from Exception.
# 3. Raise and catch your own exception types.
# 4. Reuse descriptive errors throughout a codebase.
# 5. Practice identifying errors and predicting output.

# ============================================================
# SECTION 1 — WHY CREATE CUSTOM EXCEPTIONS?
# ============================================================
# Custom exceptions help you:
# - Reuse the same error type in multiple places.
# - Describe problems specific to your application.
# - Catch specific problems instead of every possible error.
#
# Python's built-in exceptions are classes. Custom application
# exceptions generally inherit from Exception (not BaseException).

# ============================================================
# SECTION 2 — DEFINE A CUSTOM EXCEPTION
# ============================================================
class NegativeNumbersError(Exception):
    """Raised when one or more inputs violate a positivity rule."""
    pass

# This class inherits exception behavior from Exception.
# It does not need a custom __init__ method for this example.
#
# EXERCISE 1 — FILL IN THE BLANKS
# 1. NegativeNumbersError is a subclass of __________.
# 2. The keyword used to define a class is __________.
# 3. The keyword used to trigger an exception is __________.
# 4. The keyword used to catch an exception is __________.

# ============================================================
# SECTION 3 — RAISING A CUSTOM EXCEPTION
# ============================================================
# Both forms are valid:
# raise NegativeNumbersError
# raise NegativeNumbersError("Inputs must be positive")
#
# Python instantiates an exception class if you raise the class.
# The instance form lets you supply a helpful error message.
#
# EXERCISE 2 — PREDICT
# What type of exception will this code raise?
#
# raise NegativeNumbersError("No negative values allowed")
#
# ANSWER:
# _________________________________________________

# ============================================================
# SECTION 4 — THE INSTRUCTOR'S ADDITION EXAMPLE
# ============================================================
# The lesson checks a <= 0 or b <= 0, so ZERO is rejected too.
# That is a 'strictly positive' rule, not just a 'nonnegative' rule.

def add_positive_numbers(a, b):
    try:
        if a <= 0 or b <= 0:
            raise NegativeNumbersError
        return a + b
    except NegativeNumbersError:
        return "Shame on you. Not valid."

# Run these after predicting the results:
# print(add_positive_numbers(5, 2))
# print(add_positive_numbers(-5, -2))
# print(add_positive_numbers(0, 4))
#
# EXERCISE 3 — PREDICT OUTPUT
# 1. _________________________________________________
# 2. _________________________________________________
# 3. _________________________________________________
# Why does zero trigger the exception?
# ANSWER:
# _________________________________________________

# ============================================================
# SECTION 5 — CAPTURE THE ERROR WITH 'as'
# ============================================================
# This separate example includes a descriptive error message.

def add_with_message(a, b):
    try:
        if a <= 0 or b <= 0:
            raise NegativeNumbersError("Both inputs must be greater than zero")
        return a + b
    except NegativeNumbersError as error:
        return f"Invalid input: {error}"

# print(add_with_message(3, 4))
# print(add_with_message(-1, 4))
#
# EXERCISE 4 — EXPLAIN
# What does 'as error' make available inside the except block?
# ANSWER:
# _________________________________________________

# ============================================================
# SECTION 6 — EXCEPTIONS ARE PART OF AN INHERITANCE HIERARCHY
# ============================================================
# NegativeNumbersError -> Exception -> BaseException -> object
#
# A handler for NegativeNumbersError catches this specific type.
# A handler for Exception can catch it too, but is less specific.
#
# EXERCISE 5 — PREDICT WHICH HANDLER RUNS

def identify_exception():
    try:
        raise NegativeNumbersError("Example")
    except NegativeNumbersError:
        return "Custom handler"
    except Exception:
        return "General handler"

# print(identify_exception())
# ANSWER:
# _________________________________________________

# ============================================================
# SECTION 7 — CHALLENGE 1: DEFINE YOUR OWN EXCEPTION
# ============================================================
# Create a class named InvalidAgeError that inherits Exception.
# Give it a docstring describing when it should be raised.
#
# class InvalidAgeError(...):
#     ...
#
# Write your code below:


# ============================================================
# SECTION 8 — CHALLENGE 2: VALIDATE AN AGE
# ============================================================
# Implement register_age(age):
# - If age is less than 0, raise InvalidAgeError.
# - Otherwise return f"Age registered: {age}".
# - Do NOT catch the exception inside this function.
#
# Tip: Finish Challenge 1 first.

def register_age(age):
    # Write your code here.
    pass

# Test after implementing:
# print(register_age(25))
# print(register_age(-3))  # Expected: custom exception
#
# QUESTION: Why might the caller catch an exception instead
# of having register_age() catch its own exception?
# ANSWER:
# _________________________________________________

# ============================================================
# SECTION 9 — CHALLENGE 3: HANDLE YOUR CUSTOM ERROR
# ============================================================
# Implement safe_register_age(age):
# - Call register_age(age) inside try.
# - Catch ONLY InvalidAgeError.
# - Return a helpful message if that error occurs.
# - Return the normal result for a valid age.

def safe_register_age(age):
    # Write your code here.
    pass

# Test after implementing:
# print(safe_register_age(25))
# print(safe_register_age(-3))

# ============================================================
# SECTION 10 — REUSING EXCEPTIONS ACROSS MODULES
# ============================================================
# Larger projects often store related exceptions in a module.
# For example, a file called app_exceptions.py might contain:
#
# class InvalidAgeError(Exception):
#     """Raised when an age is invalid."""
#     pass
#
# Another module can import that exception:
# from app_exceptions import InvalidAgeError
#
# The instructor points to Django's database migration exceptions
# as a real-world example of descriptive, reusable error classes.
# Some custom errors can inherit from a more specific built-in
# exception such as ValueError when that relationship makes sense.
#
# EXERCISE 6 — EXPLAIN
# Why might a large application keep exception classes
# together in a separate exceptions.py module?
# ANSWER:
# _________________________________________________

# ============================================================
# SECTION 11 — FINAL REVIEW
# ============================================================
# 1. Why create a custom exception instead of always using ValueError?
# ANSWER: ___________________________________________
#
# 2. Which built-in class is the usual parent of custom errors?
# ANSWER: ___________________________________________
#
# 3. What does 'raise NegativeNumbersError' do?
# ANSWER: ___________________________________________
#
# 4. What does 'except NegativeNumbersError' catch?
# ANSWER: ___________________________________________
#
# 5. What is the benefit of a descriptive exception class name?
# ANSWER: ___________________________________________
#
# 6. In the instructor's example, is zero accepted?
# ANSWER: ___________________________________________
#
# 7. Can one custom exception be imported into several modules?
# ANSWER: ___________________________________________

# ============================================================
# KEY TAKEAWAYS
# ============================================================
# Custom exceptions are ordinary classes that inherit from
# Exception (or one of its suitable subclasses).
#
# Use 'raise' to signal an error and 'except' to handle it.
#
# Descriptive exception names communicate what went wrong and
# allow different parts of a program to handle the same problem.
# ============================================================
# END OF LESSON
# ============================================================
