# ============================================================
# FILE: catching-one-or-more-specific-exceptions.py
# TOPIC: Catching One or More Specific Exceptions
# ============================================================

# LESSON OBJECTIVES
# 1. Catch a particular error rather than every exception.
# 2. Distinguish ZeroDivisionError from TypeError.
# 3. Use multiple except clauses for different error pathways.
# 4. Capture an exception object using "as".
# 5. Group related exceptions in a tuple when appropriate.
# 6. Predict outputs and write your own handlers.


# ============================================================
# SECTION 1 — WHY CATCH SPECIFIC EXCEPTIONS?
# ============================================================

# A bare "except:" catches almost everything, including interrupts.
# Specific except clauses communicate what might go wrong and avoid
# accidentally hiding unrelated programming mistakes.
#
# Syntax:
# try:
#     risky_operation()
# except SomeError:
#     handle_that_error()
#
# The except body runs only if a matching exception occurs in the try.


# ============================================================
# SECTION 2 — THE STARTER FUNCTION
# ============================================================

def divide_five(number):
    return 5 / number


# EXERCISE 1 — PREDICT BEFORE RUNNING
# What happens for each call? Write the result or exception type.
#
# divide_five(10)         ANSWER: ______________________
# divide_five(0)          ANSWER: ______________________
# divide_five("nonsense") ANSWER: ______________________
#
# Uncomment one at a time to observe the behavior.
# print(divide_five(10))
# print(divide_five(0))
# print(divide_five("nonsense"))


# ============================================================
# SECTION 3 — CATCH ONLY ZeroDivisionError
# ============================================================

def safe_divide_zero_only(number):
    try:
        return 5 / number
    except ZeroDivisionError:
        return "You can't divide by zero"


# EXERCISE 2 — PREDICT OUTPUT
# print(safe_divide_zero_only(10))
# print(safe_divide_zero_only(0))
#
# ANSWER 1: ______________________
# ANSWER 2: ______________________
#
# QUESTION: What happens if you pass "nonsense" instead?
# ANSWER: _______________________________________________
#
# Uncomment separately after predicting:
# print(safe_divide_zero_only("nonsense"))


# ============================================================
# SECTION 4 — HANDLE DIFFERENT ERRORS DIFFERENTLY
# ============================================================

def safe_divide(number):
    try:
        return 5 / number
    except ZeroDivisionError:
        return "You can't divide by zero"
    except TypeError as e:
        return f"No dividing by invalid objects: {e}"


# EXERCISE 3 — PREDICT OUTPUT
# print(safe_divide(10))
# print(safe_divide(0))
# print(safe_divide("nonsense"))
#
# ANSWER 1: _______________________________________________
# ANSWER 2: _______________________________________________
# ANSWER 3: _______________________________________________
#
# QUESTION: Why does the third call not enter ZeroDivisionError?
# ANSWER: _________________________________________________


# ============================================================
# SECTION 5 — CAPTURE AN EXCEPTION WITH "as"
# ============================================================

# In "except TypeError as e:", e is the exception object.
# Converting it to text gives Python's error description.
# The name "e" is conventional; "error" is also valid.

# EXERCISE 4 — FILL IN THE BLANKS
# Finish the function so it includes Python's error message.

def explain_type_error(number):
    try:
        return 5 / number
    except TypeError as error:
        # Replace pass with an f-string using error.
        pass


# TEST AFTER COMPLETING:
# print(explain_type_error("nonsense"))


# ============================================================
# SECTION 6 — GROUP MULTIPLE EXCEPTIONS IN A TUPLE
# ============================================================

def safe_divide_grouped(number):
    try:
        return 5 / number
    except (ZeroDivisionError, TypeError) as e:
        return f"Something went wrong. The error was: {e}"


# EXERCISE 5 — PREDICT THE DIFFERENCE
# print(safe_divide_grouped(0))
# print(safe_divide_grouped("nonsense"))
#
# ANSWER 1: _______________________________________________
# ANSWER 2: _______________________________________________
#
# QUESTION: What part of the returned message is identical?
# ANSWER: _________________________________________________
#
# QUESTION: What part depends on the exception raised?
# ANSWER: _________________________________________________


# ============================================================
# SECTION 7 — WHEN SHOULD ERRORS BE GROUPED?
# ============================================================

# Use separate except clauses when each error needs a distinct response.
# Group errors in a tuple when the handling is genuinely the same.
#
# EXERCISE 6 — THINK ABOUT DESIGN
# A calculator receives either a zero denominator or a string.
# Would you use separate handlers or one grouped handler if you
# wanted to give a different user message for each case?
#
# ANSWER: _________________________________________________
# WHY: ____________________________________________________


# ============================================================
# SECTION 8 — CODING CHALLENGE 1: SAFE DIVISION
# ============================================================

# Write a function divide_numbers(numerator, denominator).
# Requirements:
# - Return numerator / denominator when valid.
# - Return "Cannot divide by zero" for ZeroDivisionError.
# - Return "Invalid input type" for TypeError.
# - Use TWO separate except clauses.

def divide_numbers(numerator, denominator):
    # Write your code here.
    pass


# TEST AFTER COMPLETING:
# print(divide_numbers(12, 3))       # 4.0
# print(divide_numbers(12, 0))       # Cannot divide by zero
# print(divide_numbers(12, "three")) # Invalid input type


# ============================================================
# SECTION 9 — CODING CHALLENGE 2: GROUPED HANDLER
# ============================================================

# Write a function reciprocal(value) that returns 1 / value.
# Catch both ZeroDivisionError and TypeError in ONE except clause.
# Return a string beginning "Calculation failed: " followed by
# the exception's own message.

def reciprocal(value):
    # Write your code here.
    pass


# TEST AFTER COMPLETING:
# print(reciprocal(4))
# print(reciprocal(0))
# print(reciprocal("bad"))


# ============================================================
# SECTION 10 — CODING CHALLENGE 3: ANOTHER ERROR TYPE
# ============================================================

# int("hello") raises ValueError, which is different from
# the TypeError and ZeroDivisionError examples above.
#
# Write parse_whole_number(text):
# - Convert text with int(text).
# - Catch ValueError and return "Not a whole number".
# - Let other unexpected errors propagate.

def parse_whole_number(text):
    # Write your code here.
    pass


# TEST AFTER COMPLETING:
# print(parse_whole_number("42"))
# print(parse_whole_number("hello"))


# ============================================================
# SECTION 11 — FINAL REVIEW: FILL IN THE BLANKS
# ============================================================

# 1. A division by zero raises ________________________.
# 2. Dividing an integer by a string raises ____________.
# 3. The keyword for handling an exception is __________.
# 4. The keyword that binds an exception object is ______.
# 5. Multiple exception classes can be grouped in a ______.
# 6. Code that may raise an exception goes in the ______ block.
# 7. An except clause executes only for a __________ error.
# 8. Catching specific exceptions helps avoid hiding ________.
# 9. If handlers need different responses, use __________ clauses.
# 10. If handlers do exactly the same thing, consider ________.


# ============================================================
# SECTION 12 — KEY CONCEPTS
# ============================================================

# try:                 Attempt code that may raise an exception.
# except ErrorType:    Handle that particular exception type.
# except ErrorType as e:
#                      Access the actual exception object.
# except (A, B) as e:  Handle either of two specified types.
#
# IMPORTANT: An exception not matched by any except clause
# propagates to the caller rather than being silently handled.
#
# END OF LESSON
