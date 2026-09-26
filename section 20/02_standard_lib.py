# The Python Standard Library — Study Summary
# Instructor summary:
# - The standard library provides reusable tools distributed with Python.
# - Its modules cover tasks such as mathematics, text processing, dates,
#   statistics, randomness, and working with the operating system.
# - Import a standard-library module the same way as a custom module.
# - Access its constants and functions with module.attribute dot notation.
# - string provides useful character collections and text helpers.
# - math provides mathematical functions and constants.
# - import this displays The Zen of Python on its first normal import.
#
# Clarifications and connections:
# - Standard-library modules do not require a separate pip installation.
# - Some modules are written in Python; others use compiled implementations.
#   Not every module is a plain .py file or technically a built-in module.
# - Import resolution uses Python's import machinery and module search path.
#   Avoid naming your own files string.py or math.py: they can shadow the
#   standard-library modules you intended to import.
# - ASCII letters cover a-z and A-Z, not every letter in every language.
# - string.capwords() is similar to str.title(), but not identical.
# - ceil() and floor() round in opposite directions, not to the nearest integer.

import math
import string


# --- 1. Access character collections from string ---
print(string.ascii_letters)
# Expected: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)  # 0123456789
print(type(string.digits))  # <class 'str'>
# These attributes hold strings. digits is not a list of integers.
print(string.ascii_letters == string.ascii_lowercase + string.ascii_uppercase)
# Expected: True
print("G" in string.ascii_letters)  # True
print("7" in string.digits)  # True
print("é" in string.ascii_letters)  # False


# --- 2. Capitalize words with string.capwords() ---
print(string.capwords("hello there"))  # Hello There
print(string.capwords("hELLO THERE"))  # Hello There
print(string.capwords("  hello   there  "))  # Hello There
# By default, capwords() splits on whitespace, capitalizes each word, and
# joins the words with single spaces. Remaining letters become lowercase.

phrase = "they're here"
print(string.capwords(phrase))  # They're Here
print(phrase.title())  # They'Re Here
# title() treats the apostrophe as a word boundary; default capwords() does not.
print(phrase)  # they're here — the original string is unchanged


# --- 3. Round toward positive or negative infinity ---
print(math.ceil(4.5))  # 5 — smallest integer greater than or equal to 4.5
print(math.floor(4.8))  # 4 — largest integer less than or equal to 4.8
print(math.ceil(4.0))  # 4
print(math.floor(4.0))  # 4

print(math.ceil(-4.5))  # -4 — move toward positive infinity
print(math.floor(-4.5))  # -5 — move toward negative infinity
print(int(-4.5))  # -4 — int() truncates toward zero
# "Round up" and "round down" refer to position on the number line.
# floor() and int() differ for negative non-integers.


# --- 4. Calculate square roots and use pi ---
print(math.sqrt(9))  # 3.0
print(type(math.sqrt(9)))  # <class 'float'>
print(round(math.sqrt(32), 3))  # 5.657
print(math.sqrt(0))  # 0.0
# sqrt() returns a float even when the root is a whole number.
# Leave this intentional error commented out:
# math.sqrt(-1)  # ValueError: math domain error

print(math.pi)  # 3.141592653589793
radius = 2
circle_area = math.pi * radius ** 2
print(round(circle_area, 2))  # 12.57
# math.pi is a floating-point approximation, not an exact representation of pi.
# The attribute name is lowercase, even though pi is a mathematical constant.


# --- 5. Import a module that prints during import ---
# Uncomment the next line to display The Zen of Python:
# import this
#
# No print() call is needed here because the module prints during import.
# Repeating a normal import in the same interpreter reuses the cached module
# and does not print the text again. A fresh Python process imports it anew.
# This example connects to the previous lesson's top-level execution experiment.


# --- 6. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# The math and string imports at the top are available to these exercises.
# Keep intentional-error examples commented out.

# Exercise 1 — Character collections
# Predict all four outputs and explain why the digit is written as a string.
# print(len(string.ascii_lowercase))
# print(len(string.ascii_letters))
# print("5" in string.digits)
# print("z" in string.ascii_uppercase)
# ANSWER:


# Exercise 2 — Capitalization and whitespace
# Predict both outputs. Explain how capwords() handles extra whitespace.
# text = "  pYTHON   standard LIBRARY  "
# print(string.capwords(text))
# print(text)
# ANSWER:


# Exercise 3 — Negative numbers
# Predict all four outputs using positions on the number line.
# print(math.ceil(2.1))
# print(math.floor(2.9))
# print(math.ceil(-2.1))
# print(math.floor(-2.9))
# ANSWER:


# Exercise 4 — Access a module attribute
# Explain why the last line fails when sqrt has not been separately defined
# or imported. Rewrite it using dot notation.
# import math
# print(sqrt(16))  # Intentional NameError; keep commented out.
# ANSWER:


# Exercise 5 — Write your own circle report
# 1. Choose a positive radius and store it in a variable.
# 2. Use math.pi to calculate the circle's area and circumference.
#    Area = pi * radius ** 2; circumference = 2 * pi * radius.
# 3. Print both results rounded to two decimal places with round().
# 4. Print math.ceil() and math.floor() of the area.
# 5. Create a lowercase report title and print it using string.capwords().
# Write your code below:
