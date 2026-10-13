# ============================================================
# FILE: 04_the-raise-keyword.py
# TOPIC: Raising Exceptions Explicitly
# ============================================================
# OBJECTIVES
# - Use raise to signal that an operation's requirements are not met.
# - Create an exception with a descriptive message.
# - Catch an explicitly raised exception with except.
# - Distinguish raising an exception from returning a value.
# - Separate validation inside a function from handling in its caller.
#
# STUDY SUMMARY
# - raise explicitly triggers an exception.
# - Use ValueError for an argument of an appropriate type but invalid value.
# - Use TypeError when an argument's type is inappropriate for the operation.
# - An exception's message can explain which requirement was violated.
# - except ValueError as error binds the caught exception object to error.
# - Printing or formatting that object displays its message.
# - Validation can stop an operation before its main calculation begins.
#
# CLARIFICATIONS TO THE TRANSCRIPT
# - The keyword is raise, not "arrays"; the handler keyword is except.
# - raise accepts an exception instance or an exception class derived from
#   BaseException. Raising a class instantiates it without arguments.
# - A bare raise is also valid inside an active exception handler: it
#   re-raises the current exception. That is different from raising a new one.
# - You do not need a try block in order to raise an exception.
# - A handler may be inside the function or further out in its callers.
# - Raising an exception interrupts normal execution; it does not return
#   the exception as a normal function result.
# - Positive means greater than zero, so zero is invalid in this lesson.
# - The simple arithmetic examples assume ordinary int or float inputs.
#   The positivity check is not comprehensive type or numeric validation.
# - Custom exception classes are introduced in the next lesson.


# ============================================================
# SECTION 1 — CREATE AN EXCEPTION WITH A MESSAGE
# ============================================================
problem = ValueError("Both numbers must be positive.")

print(type(problem))  # => <class 'ValueError'>
print(str(problem))   # => Both numbers must be positive.
# Creating the object alone does not raise it.
# Keep this unhandled example commented out:
# raise problem


# ============================================================
# SECTION 2 — RAISE AND CATCH WITHIN THE SAME FUNCTION
# ============================================================
def add_positive_numbers(a, b):
    try:
        if a <= 0 or b <= 0:
            raise ValueError(
                "One or both values are invalid. Both numbers must be positive."
            )

        return a + b
    except ValueError as error:
        return f"Caught the ValueError: {error}"


print(add_positive_numbers(10, 5))  # => 15
print(add_positive_numbers(-2, 3))
# => Caught the ValueError: One or both values are invalid. Both numbers must be positive.
print(add_positive_numbers(3, -8))
# => Caught the ValueError: One or both values are invalid. Both numbers must be positive.
print(add_positive_numbers(0, 5))
# => Caught the ValueError: One or both values are invalid. Both numbers must be positive.

# The handler catches the ValueError just as it would one raised by Python.
# error refers to the exception object, not only a string.
# The formatted string includes that object's message.


# ============================================================
# SECTION 3 — TRACE THE TWO EXECUTION PATHS
# ============================================================
# For add_positive_numbers(10, 5):
# 1. Neither number is less than or equal to zero.
# 2. The if body is skipped, so no exception is raised.
# 3. return a + b returns 15 and exits the function.
# 4. The except block does not run.
#
# For add_positive_numbers(-2, 3):
# 1. a <= 0 is True.
# 2. raise ValueError(...) interrupts the try block.
# 3. return a + b is skipped.
# 4. The matching except block returns an explanatory string.
#
# This teaching example returns a number on success and a string on failure.
# Callers must account for those different result types.
# Another design is to return the sum on success and let the caller handle
# an exception on failure, as shown below.


# ============================================================
# SECTION 4 — LET THE CALLER HANDLE THE EXCEPTION
# ============================================================
def positive_sum(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Both numbers must be positive.")

    return a + b


print(positive_sum(4, 6))  # => 10

try:
    result = positive_sum(-4, 6)
    print(result)
except ValueError as error:
    print(f"Cannot calculate the sum: {error}")
# => Cannot calculate the sum: Both numbers must be positive.

# The function defines valid input; the caller decides how to respond.
# The try block surrounds the function call, not the raise statement itself.
# print(result) is skipped because positive_sum raises before returning.
# Without a matching handler, the exception would continue propagating.


# ============================================================
# SECTION 5 — RAISE AN INSTANCE OR AN EXCEPTION CLASS
# ============================================================
try:
    raise ValueError("A descriptive message")
except ValueError as error:
    print(str(error))  # => A descriptive message

try:
    raise ValueError
except ValueError as error:
    print(type(error).__name__)  # => ValueError
    print(repr(str(error)))      # => ''

# raise ValueError is allowed: Python constructs the exception for us.
# Supplying an instance lets us include a useful message.
# Keep this intentional error commented out:
# raise "Invalid input"  # TypeError: exceptions must derive from BaseException.
# A plain string is not an exception object.


# ============================================================
# SECTION 6 — VALUE ERRORS AND TYPE ERRORS ARE DIFFERENT
# ============================================================
# A negative number has a suitable numeric type but violates our value rule.
# A string cannot be compared with zero using <= in these functions.

try:
    positive_sum("10", 5)
except TypeError:
    print("The comparison requires suitable numeric inputs.")
# => The comparison requires suitable numeric inputs.

# This TypeError comes from the comparison, before our explicit raise.
# The ValueError handler inside add_positive_numbers would not catch it.
# Neither function automatically converts numeric strings to numbers.
# A function can explicitly raise TypeError too when validating its inputs.


# ============================================================
# SECTION 7 — VALIDATE BEFORE DOING THE MAIN WORK
# ============================================================
# The transcript shows this pattern in a machine-learning library.
# This independent teaching example illustrates the idea without requiring
# that library or reproducing a particular version of its source code.

def prepare_settings(method, angle):
    if method not in ("barnes_hut", "exact"):
        raise ValueError("method must be 'barnes_hut' or 'exact'.")

    if not 0 <= angle <= 1:
        raise ValueError("angle must be between 0 and 1, inclusive.")

    return f"Ready: method={method}, angle={angle}"


print(prepare_settings("exact", 0.5))
# => Ready: method=exact, angle=0.5

try:
    prepare_settings("unknown", 0.5)
except ValueError as error:
    print(error)
# => method must be 'barnes_hut' or 'exact'.

try:
    prepare_settings("exact", 1.5)
except ValueError as error:
    print(error)
# => angle must be between 0 and 1, inclusive.

# Raising early prevents the later work from running with invalid settings.
# If both settings are invalid, the first failed check raises first.


# ============================================================
# SECTION 8 — PRACTICE: PREDICT, EXPLAIN, THEN RUN
# ============================================================
# Write predictions in ANSWER comments before uncommenting examples.
# Keep unhandled-error examples commented unless inspecting them individually.

# EXERCISE 1 — PREDICT RESULTS
# For each call, predict the return value of the Section 2 function.
# add_positive_numbers(2, 7)
# add_positive_numbers(0, 7)
# add_positive_numbers(2, -7)
# add_positive_numbers(1.5, 2.5)
# ANSWER:


# EXERCISE 2 — CHOOSE THE EXCEPTION
# Which is more appropriate, ValueError or TypeError?
# 1. A function expects a positive integer but receives -3.
# 2. A function expects an integer but receives a list.
# Explain the difference between an inappropriate value and type.
# ANSWER:


# EXERCISE 3 — CREATE VERSUS RAISE
# What prints? Which statement would raise the stored exception?
# error = ValueError("Too small")
# print("Created the exception")
# ANSWER:


# EXERCISE 4 — TRACE PROPAGATION
# Predict the printed messages and their order.
# try:
#     print("Starting")
#     positive_sum(0, 4)
#     print("Finished the addition")
# except ValueError as error:
#     print(f"Problem: {error}")
# print("After the handler")
# ANSWER:


# EXERCISE 5 — CHECK BOUNDARIES
# Which calls return a readiness message, and which raise ValueError?
# prepare_settings("exact", 0)
# prepare_settings("exact", 1)
# prepare_settings("exact", -0.1)
# prepare_settings("other", 0.5)
# ANSWER:


# EXERCISE 6 — WRITE YOUR OWN VALIDATION
# Define set_volume(level), assuming level is an ordinary number.
# Raise ValueError with a helpful message if level is outside 0 through 100.
# Otherwise return level. Handle the exception at the call site.
# Test 0, 50, 100, -1, and 101.
# Write your code below:


# OPTIONAL CHALLENGE — KEEP RAISING AND HANDLING SEPARATE
# Write a function that accepts a nonempty name string.
# Raise TypeError for a non-string and ValueError for an empty string.
# Return a greeting for valid input.
# At the call site, use separate handlers to display the two error messages.
# ANSWER:


# ============================================================
# SECTION 9 — FINAL REVIEW
# ============================================================
# 1. The __________ keyword explicitly triggers an exception.
# 2. Can raise accept an exception class as well as an instance?
# 3. How do you attach a descriptive message to a ValueError?
# 4. Must the function raising an exception also catch it?
# 5. What does error refer to in except ValueError as error?
# 6. Does execution continue with the next statement after raise?
# 7. Why does zero fail the positive-number requirement?
# 8. What is the benefit of validating inputs before the main calculation?
# ANSWER:
