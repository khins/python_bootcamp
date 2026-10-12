# ============================================================
# FILE: 01_intro_exception_handling.py
# TOPIC: Introduction to Exception Handling
# ============================================================
# OBJECTIVES
# - Explain what an exception is and what it means to raise one.
# - Distinguish handled exceptions from unhandled exceptions.
# - Recognize common exception types and read a traceback.
# - Identify predictable failures caused by input or external resources.
# - Prepare for the try/except syntax introduced in the next lesson.
#
# STUDY SUMMARY
# - Exception handling provides a plan for responding to runtime problems.
# - Exceptions are Python objects that carry information about a problem.
# - Python provides exception classes such as ValueError and TypeError.
# - Developers can also define custom exception classes.
# - Raising an exception interrupts the normal flow of execution.
# - A matching handler can respond and allow execution to continue.
# - An unhandled exception normally ends a standalone script and displays
#   a traceback showing where the failure occurred.
# - Failures can result from user input, missing files, network problems,
#   or unavailable services, as well as mistakes in code.
#
# CLARIFICATIONS TO THE TRANSCRIPT
# - The syntax is try/except, not "try accept".
# - Creating an exception object is different from raising it.
# - Raising an exception starts the process of finding a matching handler.
# - Handling an exception does not automatically retry the failed statement
#   or resume at the next statement inside the interrupted try block.
# - Some exceptions signal control flow rather than ordinary errors;
#   this introduction focuses on exceptions that report failures.
# - Interactive shells and applications may catch failures at an outer level,
#   so an unhandled exception does not always close the entire application.
# - Handling expected failures is useful; hiding every error can conceal bugs.
# - Exception handling does not fix logical mistakes that raise no exception.


# ============================================================
# SECTION 1 — RECOGNIZE COMMON EXCEPTIONS
# ============================================================
# Keep these intentional-error examples commented out.
# Uncomment ONE at a time if you want to inspect its traceback.

# ValueError: an argument has an inappropriate value for the operation.
# int("hello")
# int() accepts strings, but "hello" cannot be converted to an integer.

# TypeError: an operation is applied to an inappropriate type.
# "Total: " + 5
# A string cannot be concatenated directly with an integer.

# ZeroDivisionError: division by zero.
# 10 / 0

# IndexError: a sequence index is out of range.
# colors = ["red", "blue"]
# colors[5]

# KeyError: a dictionary key is missing.
# person = {"name": "Vincent"}
# person["age"]

# These corrected operations can run successfully:
print(int("42"))       # => 42
print("Total: " + str(5))  # => Total: 5
print(10 / 2)          # => 5.0


# ============================================================
# SECTION 2 — EXCEPTIONS ARE OBJECTS
# ============================================================
problem = ValueError("The value must be a whole number.")

print(type(problem))                  # => <class 'ValueError'>
print(str(problem))                   # => The value must be a whole number.
print(isinstance(problem, Exception))  # => True

# ValueError is an exception class; problem is an instance of that class.
# Creating this object does not interrupt execution.
# The following statement would raise it:
# raise problem
# Leave that line commented out so the rest of the lesson can run.


# ============================================================
# SECTION 3 — WHAT AN UNHANDLED EXCEPTION DOES
# ============================================================
# If you uncomment this entire example, the last print will not execute:
#
# print("Before the conversion")
# quantity = int("three")
# print("After the conversion")
#
# The conversion raises ValueError. With no matching handler, execution
# leaves this code instead of continuing with the next print statement.
# In a normal standalone script, Python reports the exception and exits.


# ============================================================
# SECTION 4 — READ A TRACEBACK
# ============================================================
# Example traceback (the filename, line number, and formatting may vary):
#
# Traceback (most recent call last):
#   File "example.py", line 2, in <module>
#     quantity = int("three")
# ValueError: invalid literal for int() with base 10: 'three'
#
# Start with the final line:
# - ValueError identifies the exception type.
# - The rest of the line explains the problem.
#
# Then inspect the file, line number, and source expression above it.
# If several functions were involved, the traceback shows the call path
# leading to the failure. The most recent frame appears last.
# Use that information to locate the cause and decide how to respond.
# Exact error-message wording can differ between Python versions.


# ============================================================
# SECTION 5 — PREVIEW: HANDLE A PREDICTABLE FAILURE
# ============================================================
# The next lesson explores try/except in detail.
# This small example shows what handling a failure makes possible.

user_input = "three"

try:
    quantity = int(user_input)
    print(f"Requested quantity: {quantity}")
except ValueError:
    print("Please enter a whole number, such as 3.")

print("The program can continue.")
# => Please enter a whole number, such as 3.
# => The program can continue.

# Python attempts the statements in try.
# When int(user_input) raises ValueError, it skips the rest of that try block.
# The matching except block handles the exception by displaying guidance.
# Execution then continues after the try/except statement.
# This example does not retry the conversion or assign a fallback quantity.
# If user_input were "3", the try block would finish and except would be skipped.


# ============================================================
# SECTION 6 — FAILURES ARE NOT ALWAYS PROGRAMMING MISTAKES
# ============================================================
# Predictable situations include:
# - A user enters text where a number is required.
# - A requested file does not exist.
# - A network request times out.
# - A database service is temporarily unavailable.
#
# The appropriate response depends on the operation and the program:
# - Ask for corrected input.
# - Explain that a file could not be found.
# - Retry a temporary failure when doing so is appropriate.
# - Stop an operation with a useful message when it cannot be completed.
#
# Different libraries may use different exception classes for failures.
# Catch the specific exceptions you understand and can respond to.
# Do not assume that every failure should be ignored or retried.


# ============================================================
# SECTION 7 — AN EXCEPTION IS DIFFERENT FROM A LOGIC ERROR
# ============================================================
price = 10
quantity = 3

incorrect_total = price + quantity
correct_total = price * quantity

print(incorrect_total)  # => 13
print(correct_total)    # => 30
# Both operations are valid Python, so neither raises an exception.
# Adding instead of multiplying is a logic error for this calculation.
# Exception handling cannot identify every incorrect result.


# ============================================================
# SECTION 8 — PRACTICE: PREDICT, EXPLAIN, THEN RUN
# ============================================================
# Write predictions in ANSWER comments before uncommenting examples.
# Keep intentional errors commented unless you are inspecting one at a time.

# EXERCISE 1 — IDENTIFY THE EXCEPTION
# Name the exception each expression would raise:
# 1. int("banana")
# 2. "Age: " + 25
# 3. 8 / 0
# 4. ["a", "b"][10]
# 5. {"name": "Maya"}["phone"]
# ANSWER:


# EXERCISE 2 — CREATE OR RAISE?
# Does this code interrupt execution? Why or why not?
# error = TypeError("Unexpected value type.")
# print("Still running")
# What statement would raise the stored exception?
# ANSWER:


# EXERCISE 3 — TRACE AN UNHANDLED FAILURE
# Which messages print before execution stops?
# print("Starting")
# number = int("nope")
# print("Finished")
# ANSWER:


# EXERCISE 4 — CHANGE THE INPUT
# In Section 5, change user_input to "3" and predict the output.
# Does the except block run? Does the final print still execute?
# ANSWER:


# EXERCISE 5 — INTERPRET THE TRACEBACK
# In Section 4, identify the exception type, the failing operation,
# and the value that caused the failure.
# What would you inspect first when seeing a longer traceback?
# ANSWER:


# EXERCISE 6 — PLAN A RESPONSE
# Suggest a useful response for each situation:
# 1. A user enters "two" when asked for an integer quantity.
# 2. A file the user selected has been moved or deleted.
# 3. A remote service temporarily stops responding.
# Which situations might permit another attempt, and under what conditions?
# ANSWER:


# OPTIONAL CHALLENGE — FAILURE WITHOUT AN EXCEPTION
# Give your own example of valid Python that produces the wrong result
# because the logic is incorrect. Explain why try/except would not fix it.
# ANSWER:


# ============================================================
# SECTION 9 — FINAL REVIEW
# ============================================================
# 1. An exception is a Python __________ that can report a runtime problem.
# 2. To signal an exception, Python __________ it.
# 3. Does creating an exception object automatically raise it?
# 4. What usually happens to a standalone script with an unhandled exception?
# 5. What information can you find in a traceback?
# 6. The keywords for the next lesson are try and __________.
# 7. Does handling an exception automatically retry the failed statement?
# 8. Can external circumstances cause exceptions in otherwise valid code?
# ANSWER:
