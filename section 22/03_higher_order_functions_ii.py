# Higher-Order Functions II — Study Summary
# Instructor summary:
# - A higher-order function can return another function as its return value.
# - Define nested functions, then choose which function object to return.
# - return add returns the function; return add(a, b) calls it and returns its result.
# - Store a returned function in a variable and call it later with parentheses.
# - calculator("add")(10, 4) makes two calls: first select a function, then call it.
# - Lists and dictionaries can store function objects without calling them.
# - A loop can retrieve each function from a collection and invoke it.
#
# Clarifications and corrections:
# - A returned function is a return VALUE, not an argument to the outer function.
# - The nested function's local name is not globally available, but a returned
#   reference lets you call the function after the outer call has finished.
# - If no branch returns a value, Python returns None implicitly.
# - The calculator below preserves that behavior for unrecognized operation names.
# - Function objects support assignment, storage, passing, and returning, but
#   not all operations supported by numbers. A function cannot simply be added to 1.
# - Printing a function object shows its representation, not its calculation.
#   Its representation includes details that can vary between program runs.


# --- 1. Return a selected nested function ---
def calculator(operation):
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    if operation == "add":
        return add
    elif operation == "subtract":
        return subtract


# Neither branch calls its selected function. The numbers arrive in a later call.
# Both inner definitions execute during an outer call, creating function objects;
# their bodies execute only when those functions are called.


# --- 2. Store the returned function, then call it ---
addition = calculator("add")
print(type(addition))  # <class 'function'>
print(addition(10, 4))  # 14

subtraction = calculator("subtract")
print(type(subtraction))  # <class 'function'>
print(subtraction(7, 7))  # 0
# addition and subtraction refer to functions, not numeric results.
# calculator has already returned before these inner functions are called.
# The inner names add and subtract are not automatically bound at module level.


# --- 3. Combine selection and invocation ---
print(calculator("add")(10, 4))  # 14
print(calculator("subtract")(7, 7))  # 0
# Read calculator("add")(10, 4) in two stages:
# 1. calculator("add") returns its nested add function.
# 2. (10, 4) calls that returned function and produces 14.
# This is equivalent to storing the selected function before calling it.
# The first parentheses belong to calculator; the second belong to its result.


# --- 4. Recognize unsupported operation names ---
unknown = calculator("multiply")
print(unknown)  # None
print(calculator("ADD"))  # None — string comparisons are case-sensitive
# Neither branch matches, so the outer function reaches its end without return.
# Leave these intentional errors commented out:
# unknown(3, 4)  # TypeError: None is not callable
# calculator("add")()  # TypeError: the returned function still needs a and b
# print(add(3, 4))  # NameError: no module-level name add was defined here
# A larger application could explicitly raise ValueError for unsupported names;
# this example keeps the instructor's original implicit-None behavior visible.


# --- 5. Define functions to store in a list ---
def square(num):
    return num ** 2


def cube(num):
    return num ** 3


def times_ten(num):
    return num * 10


operations = [square, cube, times_ten]
for func in operations:
    print(func(5))
# Expected:
# 25
# 125
# 50
# Each func is a function object. Every function receives the SAME input, 5.
# The result of square is not passed into cube; this is not a chain of calculations.


# --- 6. Distinguish stored functions from stored results ---
functions = [square, cube, times_ten]
results = [square(5), cube(5), times_ten(5)]
print(type(functions[0]))  # <class 'function'>
print(functions[0](3))  # 9
print(results)  # [25, 125, 50]
# Building functions stores references without calling the functions.
# Building results executes the three calls immediately and stores their integers.
# results[0](3)  # Intentional TypeError: the integer 25 is not callable


# --- 7. Use dictionary keys to select functions ---
named_operations = {"square": square, "cube": cube, "times_ten": times_ten}
selected = named_operations["cube"]
print(selected(3))  # 27
print(named_operations["times_ten"](4))  # 40
# A dictionary lookup can return a callable, just as calculator() does.
# A missing key raises KeyError with [] lookup; it does not implicitly return None.


# --- 8. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Keep intentional-error examples commented out.
# Distinguish selecting a function from executing its body.

# Exercise 1 — Function or result?
# Predict all three outputs and identify what chosen holds.
# chosen = calculator("add")
# print(type(chosen))
# print(chosen(8, 2))
# print(chosen(1, 4))
# ANSWER:


# Exercise 2 — Read two calls
# Predict both outputs. Explain what each pair of parentheses does.
# print(calculator("subtract")(20, 6))
# print(calculator("add")(20, 6))
# ANSWER:


# Exercise 3 — No matching branch
# Predict the printed value and explain why the next line would fail.
# chosen = calculator("divide")
# print(chosen)
# chosen(8, 2)  # Intentional TypeError; keep commented out.
# ANSWER:


# Exercise 4 — Trace a list of functions
# Predict every output line. What does func hold on each iteration?
# for func in [times_ten, square, cube]:
#     print(func(2))
# Does each call receive 2, or does it receive the previous function's result?
# ANSWER:


# Exercise 5 — Diagnose stored results
# Explain what values this list contains and why the loop fails.
# Rewrite the list so the loop calls each function with 3.
# operations = [square(2), cube(2)]
# for func in operations:
#     print(func(3))  # Intentional TypeError; keep commented out.
# ANSWER:


# Exercise 6 — Write your own function selector
# 1. Define choose_transform(name).
# 2. Inside it, define double(number) and triple(number), each returning its result.
# 3. Return double for "double" and triple for "triple", without calling either.
# 4. Store choose_transform("double") in a variable and call it with 6.
# 5. Use choose_transform("triple")(6) to select and call in one expression.
# 6. Predict both results and explain what an unrecognized name returns if
#    you leave the function without a fallback return or exception.
# Write your code below:


# Optional challenge — Select an album formatter
# Work through this one together when you are ready.
# Define choose_formatter(style) with two nested functions:
# - title_only(album): returns the album's "title" value.
# - full_label(album): returns "Hemispheres by Rush (1978)" for a matching record.
# Return title_only for "short" and full_label for "full". For any other style,
# explicitly return None. Do not call either formatter inside choose_formatter.
# Create a list of three dictionaries containing "title", "artist", and "year".
# Select the "full" formatter once, before a loop, and store it in formatter.
# Loop over the albums and append formatter(album) to a NEW labels list.
# Print labels after the loop. Preserve the original records and their order.
# Repeat with the "short" formatter to compare the results.
# Explain what choose_formatter returns versus what formatter(album) returns.
# Write your code below:
