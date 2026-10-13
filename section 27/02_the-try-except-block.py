# ============================================================
# FILE: 02_the-try-except-block.py
# TOPIC: Handling Exceptions with try and except
# ============================================================
# OBJECTIVES
# - Place an operation that may fail inside a try block.
# - Respond to a matching exception inside an except block.
# - Trace successful execution and exception-handling paths.
# - Compare a fallback value with an implicit None return.
# - Understand why catching specific exceptions is preferable to bare except.
#
# STUDY SUMMARY
# - try tells Python to attempt the indented statements in its block.
# - except supplies a handler for exceptions raised during that attempt.
# - If the try block succeeds, Python skips the except block.
# - If a matching exception occurs, Python skips the remaining try statements
#   and executes the handler.
# - A handler can supply a fallback, report the problem, or take another action.
# - pass does nothing; it can serve as the required statement in a block.
# - A function that reaches its end without returning a value returns None.
#
# CLARIFICATIONS TO THE TRANSCRIPT
# - The keywords are try and except, not "try and accept".
# - Both headers end with colons; their bodies must be indented.
# - try and its except clauses must line up at the same indentation level.
# - A try block cannot stand alone: it needs except or finally.
# - A bare except catches all Python exceptions, including KeyboardInterrupt
#   and SystemExit. That can interfere with interrupting or exiting a program.
# - except Exception is narrower than bare except, but still catches many
#   unrelated failures. Prefer the specific exceptions you can handle.
# - The runnable examples below catch ZeroDivisionError and TypeError,
#   which cover the transcript's zero and string inputs.
# - The fallback 5 is an arbitrary design choice, not the result of 5 / 0.
# - pass does not return None itself. The function returns None only if
#   execution reaches its end without an explicit return value.
# - A matching handler does not retry the failed operation automatically.


# ============================================================
# SECTION 1 — START WITH AN OPERATION THAT CAN FAIL
# ============================================================
def divide_without_handling(n):
    return 5 / n


print(divide_without_handling(10))  # => 0.5
print(divide_without_handling(2))   # => 2.5

# Keep these intentional errors commented out:
# divide_without_handling(0)           # ZeroDivisionError: division by zero.
# divide_without_handling("nonsense")  # TypeError: unsupported operand types.
#
# Python must evaluate 5 / n before it can return the result.
# If that evaluation raises an exception, the return does not complete.
# Without a matching handler, the exception propagates to the caller.


# ============================================================
# SECTION 2 — RETURN A FALLBACK WHEN THE OPERATION FAILS
# ============================================================
def divide_five_by_number(n):
    try:
        calculation = 5 / n
    except (ZeroDivisionError, TypeError):
        calculation = 5

    return calculation


print(divide_five_by_number(10))          # => 0.5
print(divide_five_by_number(0))           # => 5
print(divide_five_by_number("nonsense"))  # => 5

# The tuple after except means either named exception is handled.
# The return statement is outside both blocks but still inside the function.
#
# Successful path with n = 10:
# 1. 5 / 10 produces 0.5 and assigns it to calculation.
# 2. Python skips the except block.
# 3. The function returns 0.5.
#
# Handled failure with n = 0:
# 1. 5 / 0 raises ZeroDivisionError before the assignment completes.
# 2. The handler assigns the fallback value 5 to calculation.
# 3. The function returns 5.
#
# calculation exists on both paths that reach the return statement.
# An exception that does not match the handler would propagate instead.


# ============================================================
# SECTION 3 — UNDERSTAND THE TRANSCRIPT'S BARE except
# ============================================================
# The instructor starts with this broader version:
#
# def divide_broadly(n):
#     try:
#         calculation = 5 / n
#     except:
#         calculation = 5
#     return calculation
#
# It returns the same results for the three sample inputs above.
# However, bare except does not communicate which failures are expected
# and can hide unrelated problems or an attempt to interrupt execution.
# The specific handler in Section 2 makes the intended recovery clearer.


# ============================================================
# SECTION 4 — THE REST OF A FAILED try BLOCK IS SKIPPED
# ============================================================
try:
    print("Attempting division")
    result = 5 / 0
    print("Division succeeded")
except ZeroDivisionError:
    print("Cannot divide by zero.")

print("Continuing after the handler")
# => Attempting division
# => Cannot divide by zero.
# => Continuing after the handler

# "Division succeeded" does not print.
# Python does not resume at that line after the handler finishes.
# It continues after the entire try/except statement.


# ============================================================
# SECTION 5 — USE pass AND OBSERVE THE IMPLICIT None
# ============================================================
def divide_or_none(n):
    try:
        return 5 / n
    except (ZeroDivisionError, TypeError):
        pass


print(divide_or_none(10))          # => 0.5
print(divide_or_none(0))           # => None
print(divide_or_none("nonsense"))  # => None

# For valid input, the return inside try exits the function with the quotient.
# For a handled failure, the quotient is never produced.
# The handler does nothing, then the function reaches its end and returns None.
# An explicit return None in the handler would make that choice more visible.
#
# Silently ignoring a failure is appropriate only when that is an intentional
# part of the function's behavior. Callers need to know None is possible.


# ============================================================
# SECTION 6 — pass DOES NOT EXIT THE FUNCTION
# ============================================================
def describe_division(n):
    try:
        return 5 / n
    except (ZeroDivisionError, TypeError):
        pass

    return "No result available"


print(describe_division(0))   # => No result available
print(describe_division(10))  # => 0.5
# After pass, execution continues with the next statement.
# Here that statement explicitly returns a message, so the result is not None.


# ============================================================
# SECTION 7 — ONLY MATCHING EXCEPTIONS ARE HANDLED
# ============================================================
# Keep this intentional-error example commented out:
#
# try:
#     result = 5 / "nonsense"
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
#
# The division raises TypeError, not ZeroDivisionError.
# This handler would not run. Python would look for a matching handler
# further out, including in callers; otherwise the exception remains unhandled.
#
# Keep try blocks focused on the operation you intend to handle.
# This makes it easier to tell which statement raised the expected exception.


# ============================================================
# SECTION 8 — CHOOSE A RESPONSE THAT FITS THE FUNCTION
# ============================================================
# The lesson demonstrates two choices:
# - divide_five_by_number returns 5 for the handled failures.
# - divide_or_none returns None for the handled failures.
#
# Neither choice is a universal answer to invalid division.
# A function could instead report the problem, ask for corrected input,
# or let the exception reach a caller that knows how to respond.
#
# A fallback may look like a legitimate result:
print(divide_five_by_number(1))  # => 5.0 (successful division)
print(divide_five_by_number(0))  # => 5   (fallback)
# Those values compare equal. Callers should not rely on a quotient of 5
# to determine whether the operation succeeded.


# ============================================================
# SECTION 9 — PRACTICE: PREDICT, EXPLAIN, THEN RUN
# ============================================================
# Write predictions in ANSWER comments before uncommenting the examples.
# Keep intentional-error examples commented out unless inspecting them.

# EXERCISE 1 — PREDICT THE FALLBACK RESULTS
# print(divide_five_by_number(5))
# print(divide_five_by_number(-2))
# print(divide_five_by_number(0))
# print(divide_five_by_number("5"))
# Does division automatically convert the string "5" to a number?
# ANSWER:


# EXERCISE 2 — TRACE EXECUTION
# Which messages print, and in what order?
# try:
#     print("A")
#     value = 10 / 0
#     print("B")
# except ZeroDivisionError:
#     print("C")
# print("D")
# ANSWER:


# EXERCISE 3 — COMPARE RETURN VALUES
# print(divide_five_by_number(0))
# print(divide_or_none(0))
# print(describe_division(0))
# Explain why the same invalid input produces three different results.
# ANSWER:


# EXERCISE 4 — MATCH THE EXCEPTION
# In Section 7, why does except ZeroDivisionError not catch the problem?
# Which exception type would the handler need to include?
# ANSWER:


# EXERCISE 5 — EXPLAIN pass
# Does pass return None, retry the calculation, or simply do nothing?
# Why does divide_or_none return None for zero while describe_division
# returns a message for the same input?
# ANSWER:


# EXERCISE 6 — WRITE YOUR OWN HANDLER
# Define convert_to_integer(text).
# Use int(text) inside try and catch ValueError specifically.
# Return the converted integer on success and None for an invalid string.
# Test with "12", "-4", and "hello".
# Write your code below:


# OPTIONAL CHALLENGE — SEPARATE CONVERSION FROM DIVISION
# Write divide_from_text(text) that converts text to a float, then divides
# 5 by that number. Identify which exceptions "hello" and "0" would raise.
# Handle those specific failures with an explicit return None.
# Test with "2", "0", and "hello", and explain each result.
# ANSWER:


# ============================================================
# SECTION 10 — FINAL REVIEW
# ============================================================
# 1. The __________ block contains the operation Python should attempt.
# 2. A matching __________ block runs when an exception occurs.
# 3. Does except run when every statement in try succeeds?
# 4. What happens to the remaining try statements after an exception?
# 5. Why is bare except broader than needed for these division examples?
# 6. What does a function return if it reaches its end without return?
# 7. Does pass automatically exit a function?
# 8. Is the fallback 5 a mathematical result of dividing by zero?
# ANSWER:
