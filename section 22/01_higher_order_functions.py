# Higher-Order Functions — Study Summary
# Instructor summary:
# - A higher-order function accepts a function as an argument, returns a
#   function, or does both.
# - Functions are objects: you can assign them to variables, store them in
#   collections, pass them as arguments, and return them from other functions.
# - A function name without parentheses refers to the function object.
# - Parentheses call the function: add refers to the function; add(3, 5)
#   executes it and produces its return value.
# - A parameter such as func can refer to the function supplied by the caller.
# - Inside calculate(func, a, b), func(a, b) calls the supplied function.
# - return func(a, b) passes that call's result back to calculate's caller.
# - These ideas form part of the foundation for understanding decorators.
#
# Clarifications and corrections:
# - Functions are first-class objects, but they do not support every operation
#   that numbers or strings support. For example, add + 1 raises TypeError.
# - func is an ordinary parameter name; it does not enforce a particular type.
# - calculate needs a callable that accepts its two supplied positional arguments.
#   Not every function has a compatible parameter list.
# - type(one) demonstrates inspecting a function object. type is itself a built-in
#   class; calculate below is the clearer example of a higher-order function.
# - Merely calling func(a, b) does not return its result from calculate.
#   Without an explicit return, calculate would return None.


# --- 1. Distinguish a function from its return value ---
def one():
    return 1


print(type(one))  # <class 'function'>
print(type(one()))  # <class 'int'>
print(one())  # 1
# type(one) receives the function object without running its body.
# type(one()) receives the integer returned after one() runs.


# --- 2. Define two ordinary functions ---
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


print(add(3, 5))  # 8
print(subtract(10, 4))  # 6


# --- 3. Accept and call a function ---
def calculate(func, a, b):
    return func(a, b)


print(calculate(add, 3, 5))  # 8
print(calculate(subtract, 10, 4))  # 6
# Trace calculate(add, 3, 5):
# 1. func refers to add, a holds 3, and b holds 5.
# 2. func(a, b) calls add(3, 5).
# 3. add returns 8 to calculate.
# 4. calculate returns that 8 to its caller, and print displays it.
# The same calculate code can use a different operation on its next call.


# --- 4. Store a function under another name ---
operation = add
print(operation is add)  # True
print(operation(8, 2))  # 10
operation = subtract
print(operation(8, 2))  # 6
# Assignment binds a name to the function object. It does not call or copy it.
# Reassigning operation does not change the definitions of add or subtract.


# --- 5. Store functions in a collection ---
operations = {"add": add, "subtract": subtract}
selected_operation = operations["subtract"]
print(calculate(selected_operation, 12, 5))  # 7
# The dictionary stores function objects as values, not the results of calls.
# Looking up "subtract" retrieves a function that can then be called.


# --- 6. Return a function for later use ---
def choose_operation(use_addition):
    if use_addition:
        return add
    return subtract


chosen = choose_operation(True)
print(chosen is add)  # True
print(chosen(4, 6))  # 10
chosen = choose_operation(False)
print(chosen(10, 3))  # 7
# choose_operation returns a function without calling it.
# The later chosen(...) call supplies the numbers and executes that function.
# Returning a function is the other way a function can be higher-order.


# --- 7. Separate calling from returning ---
def calculate_without_return(func, a, b):
    func(a, b)


print(calculate_without_return(add, 3, 5))  # None
# add still runs and returns 8, but calculate_without_return discards that value.
# Its caller receives None because it reaches the end without a return statement.

# Leave these intentional errors commented out:
# calculate(add(3, 5), 3, 5)  # TypeError: func receives 8, which is not callable
# calculate(one, 3, 5)  # TypeError: one() accepts no arguments, but receives two
# add + 1  # TypeError: a function object cannot be added to an integer
# The first example calls add too early; the second passes an incompatible function.


# --- 8. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Use the functions defined above. Keep intentional-error calls commented out.
# Distinguish a function object, a returned value, and printed output.

# Exercise 1 — Function or result?
# Predict all three outputs. Which expression calls one()?
# print(type(one))
# print(type(one()))
# print(one())
# ANSWER:


# Exercise 2 — Trace the supplied operation
# Predict both outputs. For each call, identify what func, a, and b hold
# inside calculate and name the function called by func(a, b).
# print(calculate(add, 7, 2))
# print(calculate(subtract, 7, 2))
# ANSWER:


# Exercise 3 — Rebind a function variable
# Predict all three outputs. Explain whether assigning selected changes add.
# selected = add
# print(selected is add)
# selected = subtract
# print(selected(9, 4))
# print(add(9, 4))
# ANSWER:


# Exercise 4 — Diagnose an early call
# Explain why this fails. What value would be assigned to func?
# Rewrite the call to pass the function itself.
# print(calculate(add(2, 3), 10, 4))  # Intentional TypeError
# ANSWER:


# Exercise 5 — Return a function, then call it
# Predict both outputs and identify which line selects the function and
# which line executes the selected function with numeric arguments.
# selected = choose_operation(False)
# print(selected is subtract)
# print(selected(20, 8))
# ANSWER:


# Exercise 6 — Add your own operation
# 1. Define multiply(a, b) to return the product of a and b.
# 2. Pass multiply to calculate with the numbers 6 and 7; print the result.
# 3. Store multiply in a variable called selected and use calculate again
#    with selected and two different numbers.
# 4. Predict both results and explain why multiply has no parentheses when
#    passed as the first argument to calculate.
# Write your code below:


# Optional challenge — Apply a function to each album
# Work through this one together when you are ready.
# Define transform_records(func, records).
# records is a list of album dictionaries, and func accepts one dictionary
# and returns a transformed value. Assume func does not mutate its argument.
# Use a loop and append() to return a NEW list of func(record) results in order.
# Do not print inside transform_records or modify the input records.
# Define a separate album_label(record) that returns a string like:
# "Hemispheres by Rush (1978)"
# Use the record's "title", "artist", and "year" keys.
# Pass album_label itself and a list of three album dictionaries to
# transform_records, then print the returned list outside the function.
# An empty records list must return [].
# Explain what func and record hold and where album_label is actually called.
# Write your code below:
