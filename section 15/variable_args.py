# Python *args — Variable Number of Positional Arguments
# Learning goals:
# 1. Collect positional arguments into a tuple.
# 2. Combine *args with other parameters.
# 3. Unpack a list or tuple when calling a function.


# --- 1. Collecting arguments: * in a function definition ---
# Python collects any number of positional arguments into a tuple.
# The name args is a convention; the asterisk * is what matters.
def accept_stuff(*args):
    print(type(args))
    print(args)


# Each call prints <class 'tuple'> first, then the tuple shown below.
accept_stuff(1)              # (1,) — the comma marks a one-item tuple
accept_stuff(1, 3, 5)        # (1, 3, 5)
accept_stuff(1, 2, 3, 4, 5)  # (1, 2, 3, 4, 5)
accept_stuff()               # () — no arguments means an empty tuple


# --- 2. Using the collected tuple ---
def my_max(*numbers):
    """Return the greatest number; requires at least one argument."""
    greatest = numbers[0]

    for number in numbers:
        if number > greatest:
            greatest = number

    return greatest


print(my_max(1))                       # 1
print(my_max(1, 3))                    # 3
print(my_max(1, 3, 9, 6, 7, 8, -14))  # 9
# my_max() would raise IndexError: an empty tuple has no numbers[0].
# Think: why start greatest at numbers[0] instead of 0?


# --- 3. A regular parameter BEFORE *args ---
# The first argument fills message; the remaining ones form numbers.
def message_first(message, *numbers):
    print(message)
    print(numbers)


message_first("Hello", 10, 20, 30)  # Prints Hello, then (10, 20, 30)


# --- 4. A parameter AFTER *args ---
# message is keyword-only: supply it by name with message="Hello".
def message_keyword(*numbers, message):
    print(numbers)
    print(message)


message_keyword(10, 20, 30, message="Hello")  # Prints (10, 20, 30), then Hello


# --- 5. Unpacking arguments: * in a function call ---
# In a call, * spreads a list or tuple into separate positional arguments.
def product(a, b):
    return a * b


print(product(3, 5))  # 15
numbers = (3, 5)
print(product(*numbers))  # 15 — equivalent to product(3, 5)

# Compare the two directions:
# Definition: def accept_stuff(*args):  -> COLLECT arguments into a tuple
# Call:       accept_stuff(*numbers)    -> UNPACK values into arguments


# --- 6. Guided practice: predict, write, then check ---
# Before running these, predict the tuple printed by each call:
#  
accept_stuff(numbers) # prints numbers
accept_stuff(*numbers)
# output
# <class 'tuple'>
# ((3, 5),)
# <class 'tuple'>
# (3, 5)


# Write sum_all(*numbers) below. It should:
# - accept any number of positional numbers;
# - use a loop to add them to a running total;
# - return the total (return 0 when no arguments are passed).
# First step: write the function header and initialize the total.

def sum_all(*numbers):
    total = 0
    for numb in numbers:
        total += numb
    return total

# Uncomment these calls when your function is ready:
print(sum_all(2, 4, 6))  # Expected: 12
print(sum_all(-3, 3))    # Expected: 0
print(sum_all())         # Expected: 0
values = (5, 10, 15)
print(sum_all(*values))  # Expected: 30
