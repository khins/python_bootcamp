# ============================================================
# FILE: 07_the-else-and-finally-blocks.py
# TOPIC: The else and finally Blocks
# ============================================================
# LESSON OBJECTIVES
# 1. Add else and finally clauses to a try/except statement.
# 2. Predict which blocks run on success and on failure.
# 3. Keep try blocks focused on operations that may fail.
# 4. Understand how finally supports cleanup.
#
# Run each example separately by uncommenting its function call.


# ============================================================
# SECTION 1 — FOUR BLOCKS, FOUR PURPOSES
# ============================================================
# try:     Attempt an operation that may raise an exception.
# except:  Handle a matching exception from the try block.
# else:    Run after the try block completes normally.
# finally: Run when leaving the statement, including on failure.
#
# The headers align and end with colons; their bodies are indented.
# Use at most one else and one finally clause per try statement.
# else follows the except clauses and requires at least one except.
# finally comes last and can also be used with try alone.


# ============================================================
# SECTION 2 — else RUNS WHEN try SUCCEEDS
# ============================================================
def example_success():
    x = 10

    try:
        print(x + 5)
    except NameError:
        print("Some variable is not defined.")
    else:
        print("This will print if there is no error in the try.")


# PREDICT BEFORE RUNNING:
# 1. __________________________________________________
# 2. __________________________________________________
# example_success()
#
# The addition succeeds, so Python prints 15, skips except,
# and executes else.


# ============================================================
# SECTION 3 — else IS SKIPPED WHEN try RAISES AN EXCEPTION
# ============================================================
def example_missing_variable():
    # x = 10  # Uncomment to switch to the successful path.

    try:
        print(x + 5)
    except NameError:
        print("Some variable is not defined.")
    else:
        print("This will print if there is no error in the try.")


# This example assumes no global variable named x exists.
# The x in example_success is local to that separate function.
#
# EXERCISE 1 — PREDICT
# Which block handles the undefined name? ______________
# Will the else block run? _____________________________
# example_missing_variable()
#
# Handling an exception does not make else run afterward.
# else depends on the try block completing normally.


# ============================================================
# SECTION 4 — WHY USE else INSTEAD OF A LONGER try?
# ============================================================
# Keep try focused on the operation whose errors you intend to handle.
# Put follow-up work in else when it depends on that operation succeeding.
# This makes the success path clear and avoids catching unrelated errors
# from the follow-up work with the same except clauses.


def example_conversion(text):
    try:
        number = int(text)
    except ValueError:
        print("Please provide a whole number.")
    else:
        print(f"Five more is {number + 5}.")


# example_conversion("10")
# example_conversion("hello")
#
# EXERCISE 2 — EXPLAIN
# Why is only the conversion inside try?
# ANSWER: _____________________________________________
#
# An exception raised in else is not caught by the preceding except
# clauses. It propagates outward; finally still runs if present.


# ============================================================
# SECTION 5 — finally RUNS ON SUCCESS AND FAILURE
# ============================================================
def example_all_blocks(text):
    try:
        number = int(text)
    except ValueError:
        print("Conversion failed.")
    else:
        print(f"Converted number: {number}")
    finally:
        print("This will print with or without an exception.")
        print("Closing a file (illustration only).")


# The messages illustrate cleanup; this function opens no real file.
# example_all_blocks("10")
# example_all_blocks("hello")
#
# EXERCISE 3 — TRACE BOTH PATHS
# For "10", list the blocks that run in order:
# ANSWER: _____________________________________________
# For "hello", list the blocks that run in order:
# ANSWER: _____________________________________________
# Which two messages appear in both cases?
# ANSWER: _____________________________________________


# ============================================================
# SECTION 6 — finally DOES NOT HANDLE AN EXCEPTION
# ============================================================
# Cleanup and error handling are different responsibilities.
# If an exception is not handled, finally runs before it propagates.


def example_unhandled_error():
    try:
        raise ValueError("The operation failed.")
    finally:
        print("Cleanup runs before the error propagates.")


# CAUTION: Deliberately raises an uncaught ValueError.
# example_unhandled_error()
#
# EXERCISE 4 — EXPLAIN
# Does executing finally mean the error has been handled?
# ANSWER: _____________________________________________


# ============================================================
# SECTION 7 — CLEANUP AFTER USING A FILE
# ============================================================
# If processing fails, a close() call placed later in try is skipped.
# finally provides a place to close an already-opened file on either path.


def read_first_line(path):
    file = open(path, encoding="utf-8")
    try:
        return file.readline()
    finally:
        file.close()


# Pass the path of an existing text file to try this example:
# print(read_first_line("section 21/album_labels.txt"))
#
# open is before try: if opening fails, there is no open file to close.
# After a successful open, finally closes the file even if reading fails.
# It also runs before the pending return completes.
# For ordinary file handling, a with statement manages closing for you:
#
# with open(path, encoding="utf-8") as file:
#     first_line = file.readline()
#
# Avoid return statements in finally: they can replace an earlier return
# value or suppress a pending exception.
# "Always runs" refers to normal Python control flow; abrupt process
# termination or a power failure can prevent cleanup from running.


# ============================================================
# SECTION 8 — CODING CHALLENGE: DIVISION WITH CLEANUP
# ============================================================
# Complete the function below:
# 1. Divide 10 by number inside try.
# 2. Catch ZeroDivisionError and print a helpful message.
# 3. Print the result inside else.
# 4. Print "Attempt complete." inside finally.


def division_challenge(number):
    # Write your code here.
    pass


# division_challenge(2)
# division_challenge(0)
#
# Predict the output for each call before running it.
# ANSWER: _____________________________________________


# ============================================================
# SECTION 9 — FINAL REVIEW
# ============================================================
# 1. Which block runs only when try completes normally? ________
# 2. Which block handles a matching exception? _________________
# 3. Which block performs cleanup on success or failure? _______
# 4. Does else run after except handles an error? ______________
# 5. Why should try blocks generally stay short? _______________
# 6. Does finally alone catch an exception? ____________________
# 7. Why might closing a file at the end of try fail to happen?
# ANSWER: ____________________________________________________
# 8. Are errors raised in else caught by the preceding except?
# ANSWER: ____________________________________________________
#
# KEY TAKEAWAY:
# Use except for recovery, else for work after a successful try,
# and finally for cleanup when leaving the statement.
# ============================================================
# END OF LESSON
# ============================================================
