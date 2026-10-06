# Introduction to magic methods — Study Summary
# Instructor summary:
# - Magic methods are also called special methods or dunder methods.
# - Their names begin and end with double underscores, such as __len__.
# - "Dunder" is short for "double underscore".
# - Python calls special methods implicitly to support familiar operations.
# - These methods act as hooks: defined behavior Python uses at specific moments.
# - They let custom objects work with operators, built-in functions, and indexing.
# - Examples include addition, length, membership, and item access.
# - Other special methods support iteration, string representations, and equality.
# - Operator overloading gives familiar operators behavior for custom objects.
# - Consistent, meaningful behavior makes custom classes easier to use.
#
# Clarifications to the transcript:
# - Special methods are not secret or private; the underscores are part of their
#   documented names. Prefer ordinary syntax in everyday code.
# - Direct calls below illustrate the hooks; they are not a complete description
#   of how Python evaluates every operation.
# - Addition can involve __add__ and __radd__, depending on the operand types
#   and whether a method returns NotImplemented.
# - Membership can fall back to iteration when __contains__ is not defined.
# - Implicit special-method lookup generally happens on the object's type,
#   rather than through an attribute assigned to an individual instance.
# - The built-in function is spelled len(), with lowercase letters.
# - Floating-point arithmetic is approximate: 3.3 + 4.4 prints
#   7.7 on typical Python installations, but floats do not store exact decimals.
# - Implement only operations that make sense for your class; a custom object
#   does not need to support every operation that built-in objects support.
#
# This introduction explores built-in objects. Custom hooks come in later lessons.


# --- 1. Addition uses a special method ---
number = 3.3
print(number + 4.4)          # => 7.7
print(number.__add__(4.4))   # => 7.7
# For these float operands, both expressions produce the same result.
# __add__ receives the other operand as an explicit argument.
# Prefer number + 4.4 in ordinary code.


# --- 2. len() uses __len__ ---
numbers = [1, 2, 3]
print(len(numbers))         # => 3
print(numbers.__len__())    # => 3
# The list's length is its number of elements.
# The direct bound-method call takes no explicit arguments.
# Prefer len(numbers) in ordinary code.


# --- 3. Membership uses __contains__ for strings ---
greeting = "Hello"
print("H" in greeting)               # => True
print(greeting.__contains__("H"))    # => True
print("h" in greeting)               # => False
print(greeting.__contains__("h"))    # => False
# The container is on the RIGHT of in: greeting is the object being searched.
# The searched-for value becomes the argument to __contains__.
# String membership is case-sensitive and can also check a substring.
print("ell" in greeting)             # => True
# Prefer "H" in greeting in ordinary code.


# --- 4. Indexing uses __getitem__ ---
letters = ["A", "B", "C"]
print(letters[2])               # => C
print(letters.__getitem__(2))   # => C
# List positions start at zero, so index 2 selects the third element.
# The index in square brackets becomes the argument to __getitem__.
print(letters[-1])              # => C
print(letters.__getitem__(-1))  # => C
# Negative indexing is supported by lists; -1 selects the last element.
# Prefer letters[2] in ordinary code.
# Leave this intentional error commented out:
# print(letters[3])  # IndexError: list index out of range


# --- 5. Familiar operators can have type-specific behavior ---
print(2 + 3)                      # => 5
print("Hello" + " there")          # => Hello there
print([1, 2] + [3])                # => [1, 2, 3]
# Numeric addition, string concatenation, and list concatenation all use +.
# The operand types determine the supported behavior.
# Defining appropriate hooks lets our own classes support familiar syntax too.
# For example, a playlist could define __len__ to return its song count.
# A custom class defines __len__(self); len(instance) supplies no explicit self.
# Supporting familiar operations should preserve their expected meaning.


# --- 6. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Keep intentional-error examples commented out.

# Exercise 1 — Identify the hook
# Name the special method illustrated by each operation in this lesson.
# 1. 5.0 + 2.0
# 2. len(["red", "blue"])
# 3. "y" in "Python"
# 4. ["red", "blue"][0]
# ANSWER:


# Exercise 2 — Compare two ways to add
# Predict both outputs. Which expression would you use in ordinary code?
# value = 2.5
# print(value + 1.5)
# print(value.__add__(1.5))
# ANSWER:


# Exercise 3 — Length counts elements
# Predict both outputs. Explain why the lengths of the individual strings
# do not determine the result.
# colors = ["red", "blue", "green"]
# print(len(colors))
# print(colors.__len__())
# ANSWER:


# Exercise 4 — Identify the container
# Predict all three outputs. Which object supplies __contains__ here?
# language = "Python"
# print("P" in language)
# print(language.__contains__("p"))
# print("thon" in language)
# ANSWER:


# Exercise 5 — Match indexing to its hook
# Predict all three outputs, then rewrite the first two indexing expressions
# as direct __getitem__ calls for demonstration purposes.
# artists = ["Rush", "Yes", "Genesis"]
# print(artists[1])
# print(artists[-1])
# print(artists.__getitem__(0))
# ANSWER:


# Exercise 6 — Explain operator overloading
# Explain why 10 + 20 and "10" + "20" produce different results.
# How could special methods make a custom class easier for other developers
# to use? Does every custom class need an addition operation?
# ANSWER:


# Optional challenge — Plan a custom collection
# Work through this one together when you are ready.
# Imagine a Playlist class that stores song titles in order.
# Without implementing the class yet, describe the expected result of:
# - len(playlist)
# - "YYZ" in playlist
# - playlist[0]
# Name the special method you would define for each operation.
# What should indexing an empty playlist do if it behaves like a list?
# ANSWER:
