# Introduction to Decorators — Study Summary
# Instructor summary:
# - A decorator can accept a function and return a replacement function that
#   adds behavior before, after, or around the original function call.
# - Define a nested wrapper that calls the original function.
# - Return the wrapper itself, without calling it during decoration.
# - The wrapper retains access to the original function through a closure.
# - decorated = be_nice(original) creates a wrapper; decorated() executes it.
# - @be_nice above a function definition applies the decorator and binds that
#   function's name to the returned replacement.
# - A decorator lets several functions share additional behavior without
#   repeating that behavior in each original function body.
#
# Clarifications and corrections:
# - For the simple example here, @be_nice is equivalent to defining the function
#   and then assigning its name = be_nice(its_name).
# - Decoration happens when the definition executes, not anew on every call.
# - The returned wrapper runs each time the decorated name is called.
# - be_nice is the decorator; its nested inner function is the wrapper.
# - A decorator is more generally a callable that returns a replacement object;
#   it does not have to use exactly this nested-function structure.
# - This introductory wrapper accepts no arguments and discards fn's return value.
#   It is therefore suitable here for no-argument functions that print messages.
# - Code after fn() runs only if fn() returns normally. An exception skips it
#   unless exception-handling logic explicitly arranges otherwise.
# - Wrapping does not rewrite the original function's body or update other
#   references that already point to the original function.


# --- 1. Define a decorator and its wrapper ---
def be_nice(fn):
    def inner():
        print("Nice to meet you. I am honored to execute your function for you.")
        fn()
        print("It was my pleasure executing your function. Have a nice day.")

    return inner


# fn is a parameter of be_nice, available to inner through its enclosing scope.
# return inner returns a function object. It does not run the wrapper's prints.


# --- 2. Decorate manually, then call the result ---
def complex_business_logic():
    print("Something complex.")


result = be_nice(complex_business_logic)
# No messages print during the assignment above: inner has not been called yet.
result()
# Expected:
# Nice to meet you. I am honored to execute your function for you.
# Something complex.
# It was my pleasure executing your function. Have a nice day.

# complex_business_logic still refers to the original function in this example.
# result refers to the wrapper returned by be_nice.
print(result is complex_business_logic)  # False


# --- 3. Select the wrapper and call it in one expression ---
# This produces the same three messages as result():
# be_nice(complex_business_logic)()
#
# The first call supplies the original function and receives inner.
# The final parentheses call that returned inner function.
# Do not write be_nice(complex_business_logic()) to pass the original function:
# that would call it immediately and pass its return value, None, as fn.


# --- 4. Use decorator syntax ---
@be_nice
def another_fancy_function():
    print("Goo Goo Gaga.")


another_fancy_function()
# Expected:
# Nice to meet you. I am honored to execute your function for you.
# Goo Goo Gaga.
# It was my pleasure executing your function. Have a nice day.
#
# The definition above has the same effect as this separate alternative:
# def another_fancy_function():
#     print("Goo Goo Gaga.")
# another_fancy_function = be_nice(another_fancy_function)
#
# After decoration, another_fancy_function refers to the wrapper. The wrapper
# still holds a reference to the original function through fn.


# --- 5. Reuse the same decorator ---
@be_nice
def announce_album():
    print("Now playing Hemispheres.")


announce_album()
# Expected:
# Nice to meet you. I am honored to execute your function for you.
# Now playing Hemispheres.
# It was my pleasure executing your function. Have a nice day.
# Each application of be_nice creates a wrapper for the function it receives.


# --- 6. Distinguish printing from returning ---
def give_number():
    return 42


decorated_number = be_nice(give_number)
# Uncomment to see the wrapper's two messages followed by None:
# print(decorated_number())
#
# give_number returns 42, but be_nice's inner function does not return that result.
# To preserve a no-argument function's returned value, save and return it:


def announce_call(fn):
    def wrapper():
        print("Before")
        value = fn()
        print("After")
        return value

    return wrapper


preserved_number = announce_call(give_number)
print(preserved_number())
# Expected:
# Before
# After
# 42
# The outer return supplies the wrapper; the inner return supplies each call's result.


# --- 7. Recognize this introductory wrapper's limits ---
# Leave this intentional error commented out:
# another_fancy_function("Hello")  # TypeError: inner accepts no arguments
#
# A wrapper accepting and forwarding *args and **kwargs can support functions
# with arguments. That is an extension of this introductory pattern.
#
# The wrapper also has its own name:
print(another_fancy_function.__name__)  # inner
# functools.wraps is commonly used to preserve the original function's name,
# docstring, and related metadata. It is another refinement for later practice.
#
# If fn() raises an exception, a simple statement after fn() is not guaranteed
# to run. The introductory examples assume normal completion.


# --- 8. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Distinguish decoration time, wrapper execution, and the original function call.
# Keep intentional-error examples commented out.

# Exercise 1 — Creating is not calling
# Predict which line first produces output and all the messages it produces.
# def say_hello():
#     print("Hello")
# wrapped = be_nice(say_hello)
# wrapped()
# ANSWER:


# Exercise 2 — Follow the order
# Predict every output line, including the outer print's output.
# @announce_call
# def answer():
#     print("Calculating")
#     return 7
# print(answer())
# ANSWER:


# Exercise 3 — Translate the syntax
# Rewrite this example without @ syntax while keeping the same decorated behavior.
# @be_nice
# def show_song():
#     print("YYZ")
# show_song()
# ANSWER:


# Exercise 4 — Original versus wrapped
# Predict the messages from each call. Does creating decorated replace original?
# def original():
#     print("Original body")
# decorated = announce_call(original)
# original()
# decorated()
# ANSWER:


# Exercise 5 — Find the missing return
# Explain why calling decorate_wrong(say_hello) returns None.
# Correct the outer function without calling wrapper prematurely.
# def decorate_wrong(fn):
#     def wrapper():
#         fn()
#
# Assume say_hello is a defined no-argument function.
# What error would occur if you stored the returned None and tried to call it?
# ANSWER:


# Exercise 6 — Write your own decorator
# 1. Define show_steps(fn) with a nested wrapper accepting no arguments.
# 2. Have the wrapper print "Starting", call fn(), then print "Finished".
# 3. Preserve and return the original function's result from the wrapper.
# 4. Return the wrapper from show_steps without calling it.
# 5. Decorate a no-argument function favorite_artist() that returns "Rush".
# 6. Print favorite_artist() and predict every output line in order.
# Write your code below:


# Optional challenge — Count calls with a decorator and a closure
# Work through this one together when you are ready.
# Define count_calls(fn). Inside it, initialize count = 0 and define wrapper().
# Use nonlocal count inside wrapper to increment the count and print a message
# such as "Call 1" before calling fn. Preserve and return fn's result.
# Return wrapper itself from count_calls.
# Apply @count_calls to two separate no-argument functions that return different
# album titles. Call the first function twice and the second once, printing results.
# Expect the first wrapper's counts to be 1, 2 and the second wrapper's count to be 1.
# Explain why the count initialization belongs outside wrapper, why nonlocal is
# needed for the increment, and why the two decorated functions have separate counts.
# Assume the original functions return normally. Do not use global state.
# Write your code below:
