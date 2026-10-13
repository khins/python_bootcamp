# ============================================================
# FILE: exception-inheritance-hierarchies.py
# TOPIC: Custom Exception Inheritance Hierarchies
# ============================================================
# LESSON OBJECTIVES
# 1. Create a base exception class that inherits from Exception.
# 2. Define more specific exception subclasses.
# 3. Understand sibling exception classes.
# 4. Predict which except blocks catch which exceptions.
# 5. Decide when to catch a specific error or its parent.
#
# Run each exercise separately by uncommenting its function call.
# Exercises with deliberate uncaught exceptions are labeled clearly.

# ============================================================
# SECTION 1 — WHY BUILD AN EXCEPTION HIERARCHY?
# ============================================================
# Related errors can be organized into parent and child classes.
# For example:
#
# Exception
#    |
#  Mistake
#   /   \
# StupidMistake  SillyMistake
#
# Both specific errors are TYPES OF Mistake.
# They are siblings: neither is a subclass of the other.


# ============================================================
# SECTION 2 — DEFINE THE BASE AND CHILD EXCEPTIONS
# ============================================================
class Mistake(Exception):
    """Base class for this lesson's custom mistakes."""
    pass


class StupidMistake(Mistake):
    """A more specific kind of Mistake."""
    pass


class SillyMistake(Mistake):
    """Another kind of Mistake."""
    pass


# EXERCISE 1 — FILL IN THE BLANKS
# Mistake inherits from: ______________________
# StupidMistake inherits from: ________________
# SillyMistake and StupidMistake are: __________
# Does StupidMistake inherit from SillyMistake? _______


# ============================================================
# SECTION 3 — CATCH A SPECIFIC EXCEPTION
# ============================================================
def example_specific_exception():
    try:
        raise StupidMistake("Extra stupid mistake")
    except StupidMistake as e:
        print(f"Caught the error: {e}")


# PREDICT BEFORE RUNNING:
# OUTPUT: ___________________________________________
# example_specific_exception()


# ============================================================
# SECTION 4 — SIBLING EXCEPTIONS DO NOT CATCH EACH OTHER
# ============================================================
def example_sibling_mismatch():
    try:
        raise StupidMistake("Extra stupid mistake")
    except SillyMistake as e:
        print(f"Caught the error: {e}")


# EXERCISE 2 — PREDICT
# Will the except SillyMistake block execute? ___________
# What exception remains uncaught? ____________________
# What happens if you run this function? _______________
# CAUTION: Deliberately raises an uncaught exception.
# example_sibling_mismatch()


# ============================================================
# SECTION 5 — THE PARENT CATCHES BOTH CHILD EXCEPTIONS
# ============================================================
def example_parent_catches_children():
    try:
        raise StupidMistake("Extra stupid mistake")
    except Mistake as e:
        print(f"Caught the error: {e}")

    try:
        raise SillyMistake("Super silly mistake")
    except Mistake as e:
        print(f"Caught the error: {e}")


# EXERCISE 3 — PREDICT BOTH LINES
# 1. __________________________________________________
# 2. __________________________________________________
# Why does except Mistake catch both? __________________
# example_parent_catches_children()


# ============================================================
# SECTION 6 — ORDER OF except CLAUSES
# ============================================================
# Python tests except clauses from top to bottom.
# A child exception should generally be caught BEFORE its parent
# when you want a separate response for each.

def example_exception_order():
    try:
        raise StupidMistake("An avoidable mistake")
    except StupidMistake:
        print("Specific handler")
    except Mistake:
        print("General handler")


# EXERCISE 4 — PREDICT
# Which handler runs? __________________________________
# What if the Mistake handler were placed first? _______
# example_exception_order()


# ============================================================
# SECTION 7 — CHECK THE CLASS RELATIONSHIPS
# ============================================================
def example_class_relationships():
    print(issubclass(StupidMistake, Mistake))
    print(issubclass(SillyMistake, Exception))
    print(issubclass(StupidMistake, SillyMistake))
    error = StupidMistake("Oops")
    print(isinstance(error, Mistake))


# EXERCISE 5 — PREDICT FOUR BOOLEAN RESULTS
# 1. __________  2. __________  3. __________  4. __________
# example_class_relationships()


# ============================================================
# SECTION 8 — CODING CHALLENGE 1: DATABASE ERRORS
# ============================================================
# The lesson suggests real-world categories such as database errors.
# Create three classes:
#   DatabaseError(Exception)
#   DatabaseReadError(DatabaseError)
#   DatabaseWriteError(DatabaseError)
# Add short docstrings and use pass.
#
# Write your code here:
#
# class DatabaseError(...):
#     ...


# ============================================================
# SECTION 9 — CODING CHALLENGE 2: CATCH A CHILD WITH A PARENT
# ============================================================
# After finishing Section 8, complete this function.
# 1. Raise DatabaseReadError with a descriptive message.
# 2. Catch it using the PARENT DatabaseError class.
# 3. Print the captured error message using "as e".

def database_read_challenge():
    # Write your code here.
    pass


# database_read_challenge()


# ============================================================
# SECTION 10 — CODING CHALLENGE 3: DIFFERENT RESPONSES
# ============================================================
# Complete the function so it reacts differently to each error.
# If operation == "read", raise DatabaseReadError.
# If operation == "write", raise DatabaseWriteError.
# Catch each specific error in its own except clause.
# Print a different explanation for each case.

def database_operation_challenge(operation):
    # Write your code here.
    pass


# After completing the function, test:
# database_operation_challenge("read")
# database_operation_challenge("write")


# ============================================================
# SECTION 11 — DESIGN DECISIONS
# ============================================================
# EXERCISE 6 — EXPLAIN IN YOUR OWN WORDS
#
# When would you catch DatabaseError rather than DatabaseReadError?
# ANSWER:
# ____________________________________________________________
#
# When would separate read and write handlers be preferable?
# ANSWER:
# ____________________________________________________________
#
# Why is catching Exception broader than catching DatabaseError?
# ANSWER:
# ____________________________________________________________


# ============================================================
# SECTION 12 — FINAL REVIEW
# ============================================================
# Fill in the blanks:
#
# 1. Custom application exceptions usually inherit from ________.
# 2. A shared base exception can group several ________ errors.
# 3. Two subclasses with the same parent are called ________.
# 4. except Mistake catches Mistake and its ________.
# 5. except SillyMistake does NOT catch ________.
# 6. To print an exception's message, use except X as ________.
# 7. Python checks except clauses from ________ to ________.
# 8. To handle child exceptions separately, list the more
#    ________ handlers before the more ________ handler.
# 9. A base error like DatabaseError can make error handling
#    more ________ across a larger application.
#
# KEY TAKEAWAY:
# An exception subclass IS A type of its parent exception.
# Catching the parent also catches its descendants, but
# catching one sibling does not catch another sibling.
# ============================================================
# END OF LESSON
# ============================================================
