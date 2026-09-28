# Returned Values from Decorated Functions — Study Summary
# Instructor summary:
# - A decorated name calls the wrapper, so the caller receives the WRAPPER'S
#   return value, not automatically the original function's return value.
# - Calling fn(*args, **kwargs) without returning its result discards that result.
# - A wrapper that reaches its end without return implicitly returns None.
# - Returning immediately from fn(...) skips ordinary statements that follow it.
# - To preserve both after-call behavior and the original result:
#   1. Save result = fn(*args, **kwargs).
#   2. Perform the wrapper's remaining actions.
#   3. Return result to the caller.
# - The decorator itself returns a function; the wrapper returns a call's result.
#
# Clarifications and connections:
# - print(result) displays a value but does not return it to the caller.
# - result is an ordinary local name, created separately for each wrapper call.
# - Saving the result does not call the original function a second time.
# - The result can be any object, including None, a list, or a dictionary.
# - return fn(...) is appropriate if no ordinary after-call work is needed.
# - If fn raises an exception, the assignment does not complete and ordinary
#   after-call statements do not run. Cleanup on exceptions needs a separate
#   pattern, such as try/finally; this lesson assumes normal returns.
# - These examples forward *args and **kwargs as covered in the previous lesson.


# --- 1. See how a wrapper can lose the return value ---
def lose_result(fn):
    def wrapper(*args, **kwargs):
        print("Before")
        fn(*args, **kwargs)
        print("After")

    return wrapper


@lose_result
def sum_without_forwarded_result(a, b):
    return a + b


print(sum_without_forwarded_result(3, 5))
# Expected:
# Before
# After
# None
# The original function returns 8, but wrapper does nothing with that value.
# The outer print displays wrapper's implicit return value, None.


# --- 2. Returning immediately skips ordinary after-call statements ---
def return_too_soon(fn):
    def wrapper(*args, **kwargs):
        print("Before")
        return fn(*args, **kwargs)
        # A print("After") placed here would be unreachable.

    return wrapper


@return_too_soon
def sum_with_early_return(a, b):
    return a + b


print(sum_with_early_return(3, 5))
# Expected:
# Before
# 8
# The number reaches the caller, but this wrapper performs no after-call action.


# --- 3. Save the result, finish the wrapper, then return ---
def be_nice(fn):
    def inner(*args, **kwargs):
        print("Nice to meet you. I am honored to execute your function for you.")
        result = fn(*args, **kwargs)
        print("It was my pleasure executing your function. Have a nice day.")
        return result

    return inner


@be_nice
def complex_business_sum(a, b):
    return a + b


print(complex_business_sum(a=3, b=5))
# Expected:
# Nice to meet you. I am honored to execute your function for you.
# It was my pleasure executing your function. Have a nice day.
# 8
# The original sum does not print. It returns 8 to inner, which stores it,
# prints the final message, and returns 8 to the outer print call.


# --- 4. Store and use the returned value ---
saved_sum = complex_business_sum(10, b=4)
# The two courtesy messages print during the call above.
# Assignment alone does not print the saved numeric result.
print(saved_sum)  # 14
print(saved_sum * 2)  # 28
# The caller can calculate with the returned value because inner preserved it.


# --- 5. Separate the decorator's return from the wrapper's return ---
# In be_nice:
# - return inner runs when a function is decorated and supplies a callable.
# - return result runs when that callable is invoked and supplies its result.
#
# Manual equivalent for a separate example:
# def original_sum(a, b):
#     return a + b
# decorated_sum = be_nice(original_sum)
# answer = decorated_sum(3, 5)
#
# decorated_sum holds a function. answer holds the integer 8.
# The wrapper retains access to original_sum through its enclosing fn binding.


# --- 6. Forward other kinds of returned values ---
@be_nice
def album_record(title, artist, year):
    return {"title": title, "artist": artist, "year": year}


album = album_record("Hemispheres", "Rush", 1978)
# The same two courtesy messages print, then the dictionary is assigned to album.
print(album["title"])  # Hemispheres
print(album["year"])  # 1978
# The decorator does not need to know which type of object the original returns.


@be_nice
def no_result():
    pass


# Uncomment to see two courtesy messages followed by None:
# print(no_result())
# Here None is the ORIGINAL function's result and is correctly forwarded.
# Seeing None alone is not proof that the wrapper lost a meaningful value.


# --- 7. Preserve the result without repeating the original call ---
# This is the intended pattern:
# result = fn(*args, **kwargs)
# print("After")
# return result
#
# Do not replace the last line with return fn(*args, **kwargs): that would call
# the original function twice. Repeated calls could repeat side effects or return
# different values. Return the result already saved by the first call.


# --- 8. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Distinguish printed messages from returned values and when each occurs.

# Exercise 1 — Identify the lost result
# Predict all three output lines and explain where the value 7 is discarded.
# print(sum_without_forwarded_result(3, 4))
# ANSWER:


# Exercise 2 — Follow the corrected wrapper
# Predict every output line in order.
# print(complex_business_sum(6, b=7))
# Explain which function returns the final number to print().
# ANSWER:


# Exercise 3 — Assignment is not printing
# Predict the output from the call, then state the value stored in total.
# total = complex_business_sum(2, 9)
# Does the assignment print 11 by itself? Explain.
# ANSWER:


# Exercise 4 — Printing a result does not return it
# Explain what the caller receives and correct the wrapper to preserve fn's result.
# def print_only(fn):
#     def wrapper(*args, **kwargs):
#         result = fn(*args, **kwargs)
#         print(result)
#     return wrapper
# Keep the existing print behavior when correcting it.
# ANSWER:


# Exercise 5 — Avoid a duplicate call
# How many times does this wrapper invoke fn per wrapper call?
# Rewrite its final line to return the already-computed result.
# def duplicate_call(fn):
#     def wrapper(*args, **kwargs):
#         result = fn(*args, **kwargs)
#         print("Finished")
#         return fn(*args, **kwargs)
#     return wrapper
# Why could the original version be a problem for a function that appends to a list?
# ANSWER:


# Exercise 6 — Write your own result-preserving decorator
# 1. Define announce_completion(fn) with a wrapper taking *args and **kwargs.
# 2. Call fn exactly once, save its result, then print "Calculation complete".
# 3. Return the saved result from the wrapper and the wrapper from the decorator.
# 4. Decorate multiply(a, b), which returns a * b.
# 5. Save multiply(6, b=7) in answer, then print answer + 1.
# 6. Predict all output lines and explain the roles of the two return statements.
# Write your code below:


# Optional challenge — Report how many labels were produced
# Work through this one together when you are ready.
# Define report_count(fn). Its wrapper must accept and forward *args and **kwargs,
# call fn exactly once, and assume fn returns a list.
# Save that list, print "Produced N labels" with N replaced by len(result),
# then return the SAME list object without rebuilding or copying it.
# Decorate build_labels(albums), which creates and returns a NEW list of strings
# such as "Hemispheres by Rush (1978)" from album dictionaries.
# Preserve input order and leave the original dictionaries unchanged.
# Call build_labels with three albums, save its returned list, then print that list.
# Also call it with an empty list: expect "Produced 0 labels" and a returned [].
# Explain why returning the saved result avoids a second build_labels execution
# and why the decorator's count message appears before the caller prints the list.
# Write your code below:
