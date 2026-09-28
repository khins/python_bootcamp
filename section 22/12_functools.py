# functools.wraps and Decorator Metadata — Study Summary
# Instructor summary:
# - A docstring is a string literal that appears as the first statement in
#   a function body and documents what the function does.
# - help(function) displays documentation without calling that function.
# - A decorator replaces a function's name with a reference to its wrapper.
# - Without extra care, the wrapper exposes its own name and docstring instead
#   of the original function's metadata.
# - Import functools and place @functools.wraps(fn) above the nested wrapper.
# - wraps copies useful metadata from the original function onto the wrapper,
#   including its name and docstring.
# - Continue forwarding arguments and returning results as in earlier lessons.
#
# Clarifications and corrections:
# - help() displays documentation and returns None; it does not return a
#   documentation string. Use function.__doc__ to read the docstring directly.
# - The original function's documentation is not erased by decoration. Without
#   wraps, the replacement wrapper simply does not automatically expose it.
# - Triple-quoted strings are conventional for docstrings, though an ordinary
#   string literal can also serve as a one-line docstring.
# - wraps preserves metadata; it does not copy the original function's body
#   into the wrapper or make the wrapper and original the same object.
# - wraps adds __wrapped__, a reference to the original wrapped function.
# - wraps does not forward arguments or return values for you. Your wrapper's
#   code still has to do both.

import functools


# --- 1. Add documentation to an ordinary function ---
def plain_sum(a, b):
    """Add two numbers together."""
    return a + b


print(plain_sum.__name__)  # plain_sum
print(plain_sum.__doc__)  # Add two numbers together.
print(plain_sum(3, 5))  # 8
# Uncomment to view the function's documentation:
# help(plain_sum)
# help(len)
# Pass the function itself, not plain_sum(3, 5), which would supply the result 8.
# help() output formatting may vary by Python version and terminal.


# --- 2. Observe the metadata without wraps ---
def decorate_without_wraps(fn):
    def inner(*args, **kwargs):
        return fn(*args, **kwargs)

    return inner


unlabelled_sum = decorate_without_wraps(plain_sum)
print(unlabelled_sum(3, 5))  # 8
print(unlabelled_sum.__name__)  # inner
print(unlabelled_sum.__doc__)  # None
print(plain_sum.__doc__)  # Add two numbers together.
# The original still has its documentation. The replacement is a different
# function whose own definition has no docstring.
# help(unlabelled_sum) would describe inner rather than the original plain_sum.


# --- 3. Preserve metadata with functools.wraps ---
def be_nice(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        print("Nice to meet you. I am honored to execute your function for you.")
        result = fn(*args, **kwargs)
        print("It was my pleasure executing your function. Have a nice day.")
        return result

    return inner


@be_nice
def complex_business_sum(a, b):
    """Add two numbers together."""
    return a + b


print(complex_business_sum.__name__)  # complex_business_sum
print(complex_business_sum.__doc__)  # Add two numbers together.
print(complex_business_sum(a=3, b=5))
# Expected from the final print call:
# Nice to meet you. I am honored to execute your function for you.
# It was my pleasure executing your function. Have a nice day.
# 8
# Uncomment to inspect the preserved documentation:
# help(complex_business_sum)
# Inspecting this function with help does not execute its courtesy messages.


# --- 4. Place wraps on the wrapper, not on the original definition ---
# Read the pattern in order:
# 1. @be_nice passes the original complex_business_sum function into be_nice.
# 2. fn refers to that original function.
# 3. @functools.wraps(fn) updates inner's metadata using fn.
# 4. be_nice returns inner, which becomes the decorated name's new value.
# 5. Calling that name still runs inner's body, including its extra behavior.
#
# The fn argument to wraps is a function object, not fn().
# The parentheses in wraps(fn) configure the metadata-preserving decorator;
# they do not execute the original business function.


# --- 5. The wrapper remains distinct from the original ---
print(complex_business_sum is complex_business_sum.__wrapped__)  # False
print(complex_business_sum.__wrapped__(3, 5))  # 8
# The second line explicitly calls the original function and bypasses the
# courtesy messages. Ordinary complex_business_sum(...) calls still use the wrapper.
# Matching __name__ values do not imply that two references point to the same object.


# --- 6. Metadata preservation does not replace return forwarding ---
def loses_result(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        fn(*args, **kwargs)

    return wrapper


metadata_only_sum = loses_result(plain_sum)
print(metadata_only_sum.__name__)  # plain_sum
print(metadata_only_sum.__doc__)  # Add two numbers together.
print(metadata_only_sum(3, 5))  # None
# wraps works, but wrapper discards the original return value.
# To fix this wrapper, use return fn(*args, **kwargs), or save the result and
# return it after any additional actions that must run on normal completion.


# --- 7. An equivalent import style ---
# In a separate script, this direct import is also valid:
# from functools import wraps
#
# def decorator(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         return fn(*args, **kwargs)
#     return wrapper
#
# Use @functools.wraps(fn) with import functools, or @wraps(fn) with the direct
# import. Both refer to the same standard-library helper.


# --- 8. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Distinguish metadata inspection from executing a decorated function.

# Exercise 1 — Read the docstring
# Predict both outputs. Does either line call plain_sum's body?
# print(plain_sum.__name__)
# print(plain_sum.__doc__)
# ANSWER:


# Exercise 2 — Compare wrappers
# Predict all four outputs and explain why the metadata differs.
# print(unlabelled_sum.__name__)
# print(unlabelled_sum.__doc__)
# print(complex_business_sum.__name__)
# print(complex_business_sum.__doc__)
# ANSWER:


# Exercise 3 — Inspect without calling
# Explain the difference between these expressions:
# help(complex_business_sum)
# complex_business_sum(2, 4)
# Which displays documentation, and which executes the wrapper's messages?
# What does help() return?
# ANSWER:


# Exercise 4 — Metadata is not behavior
# Predict the result and explain why the correct docstring does not guarantee
# that a wrapper correctly forwards the original return value.
# print(metadata_only_sum(10, 4))
# Correct the relevant line in the loses_result wrapper on paper or below.
# ANSWER:


# Exercise 5 — Access the original
# Predict the output and state whether either courtesy message appears.
# print(complex_business_sum.__wrapped__(10, 4))
# Explain how this differs from an ordinary complex_business_sum(10, 4) call.
# ANSWER:


# Exercise 6 — Write a documented decorated function
# 1. Define announce_completion(fn) with a nested wrapper.
# 2. Apply @functools.wraps(fn) to that wrapper.
# 3. Forward *args and **kwargs to fn exactly once and save its result.
# 4. Print "Finished", then return the saved result.
# 5. Decorate multiply(a, b), with docstring "Return the product of two numbers."
# 6. Print multiply.__name__, multiply.__doc__, and multiply(6, b=7).
# 7. Predict all output lines and explain why the name is not wrapper.
# Write your code below:


# Optional challenge — Preserve an album formatter's documentation
# Work through this one together when you are ready.
# Define count_calls(fn), retaining count = 0 in its enclosing scope.
# Its nested wrapper must use @functools.wraps(fn), accept *args and **kwargs,
# increment count with nonlocal, print "Call N", and return fn's result.
# Decorate album_label(title, artist, year), which returns a string such as
# "Hemispheres by Rush (1978)". Give album_label a descriptive docstring.
# Print the decorated function's __name__ and __doc__ without calling its body.
# Then call it twice, once positionally and once using an unpacked album dictionary.
# Print each returned label and predict the output order, including call counts.
# Explain separately how wraps preserves metadata, the closure retains count,
# and the wrapper forwards arguments and the returned string.
# Write your code below:
