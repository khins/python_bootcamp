"""A module related to the joy of sushi.

No fishy code found here.
"""

# Docstrings — Study Summary
# Instructor summary:
# - A docstring is a string that documents a module, function, class, or method.
# - Place it as the first statement inside the object being documented.
# - Triple double quotes allow documentation to span multiple lines.
# - Describe the purpose, behavior, parameters, and return values as needed.
# - Python stores an object's docstring in its __doc__ attribute.
# - __doc__ is an attribute, not a method: do not add parentheses.
# - help() presents documentation in an organized, readable format.
# - Standard-library modules and built-in objects also provide documentation.
# - Documentation tools can use docstrings to generate reference pages.
#
# Clarifications to the transcript:
# - The spelling is docstring (one word).
# - A module docstring must be its first statement, before imports or code.
#   Comments and blank lines can appear before it.
# - Triple quotes are conventional; a one-line string can also be a docstring.
# - A string elsewhere in a body does not become that object's docstring.
# - __doc__ preserves the string's whitespace; help() formats documentation.
# - Some objects without documentation have __doc__ set to None.
# - Some __doc__ attributes can be reassigned, but normally you write the
#   docstring in the definition and let Python populate the attribute.
# - help() displays documentation and returns None; use help(object),
#   rather than print(help(object)).
#
# The transcript uses sushi.py and a separate docstrings.py file.
# Here, the examples live together so this lesson can run on its own.

import math


# --- 1. Document a module ---
# The triple-quoted string at the very top documents THIS module.
# At module level, __doc__ refers to the current module's docstring.
print(__doc__)
# => A module related to the joy of sushi.
# =>
# => No fishy code found here.
# The string ends with a newline, so print() adds an extra blank line.


# --- 2. Document a function ---
def fish():
    """Determine if fish is a good meal choice.

    Always return True because it always is.
    """
    return True


print(fish())       # => True
print(fish.__doc__)
# The second print displays the documentation, including its whitespace.
# Accessing fish.__doc__ does not call fish().
# fish() returns a Boolean; fish.__doc__ contains a string.


# --- 3. Document a class and its methods ---
class Salmon:
    """Blueprint for a salmon object.

    Each salmon starts with a tastiness value of 10.
    Baking increases its tastiness by 1.
    """

    def __init__(self):
        """Initialize the salmon with a tastiness value of 10."""
        self.tastiness = 10

    def bake(self):
        """Bake the fish in an oven, increasing tastiness by 1."""
        self.tastiness += 1


print(Salmon.__doc__)
print(Salmon.__init__.__doc__)
# => Initialize the salmon with a tastiness value of 10.
print(Salmon.bake.__doc__)
# => Bake the fish in an oven, increasing tastiness by 1.
# You do not need an instance to read a method's documentation.

salmon = Salmon()
print(salmon.tastiness)  # => 10
salmon.bake()
print(salmon.tastiness)  # => 11
# A docstring describes behavior; the method's code performs the work.


# --- 4. Read documentation from the standard library ---
print(math.__doc__)
# Displays the math module's description.
print(math.sqrt.__doc__)
# Describes returning the square root of x.
# Exact wording can vary between Python versions.
print(math.sqrt(25))  # => 5.0


# --- 5. Use help() for formatted documentation ---
help(fish)
help(Salmon.bake)
# help() uses docstrings along with information about the object.
# It can display names, signatures, methods, and other useful details.
# Uncomment these for longer documentation:
# help(Salmon)
# help(math)
# help(math.sqrt)
# Do not wrap help() in print(): that also prints its return value, None.


# --- 6. Connect this example to the transcript's two-file layout ---
# To follow the original layout, put the module docstring, fish function,
# and Salmon class into a file named sushi.py.
# In a second file in the same directory, use:
#
# import sushi
#
# print(sushi.__doc__)
# print(sushi.fish.__doc__)
# print(sushi.Salmon.__doc__)
# print(sushi.Salmon.bake.__doc__)
# help(sushi)
#
# help(sushi) groups the module's classes, functions, and documentation.
# These lines stay commented because no separate sushi.py is required here.


# --- 7. Docstrings must be the first statement ---
def undocumented_fish():
    meal = "sushi"
    "This string comes too late to be a docstring."
    return meal


print(undocumented_fish.__doc__)  # => None
print(undocumented_fish())       # => sushi
# A # comment is useful to readers of the source code, but it does not
# populate __doc__. The first-statement string has that special role.


# --- 8. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.

# Exercise 1 — Attribute or method?
# Which expression reads documentation, and which calls the function?
# What type of value does each expression produce?
# fish.__doc__
# fish()
# ANSWER:


# Exercise 2 — Find the docstring
# Which string becomes the function's documentation? Why?
# def choose_meal():
#     """Choose a meal for dinner."""
#     meal = "salmon"
#     "This is another string."
#     return meal
#
# print(choose_meal.__doc__)
# ANSWER:


# Exercise 3 — Access a method's documentation
# Write an expression that reads the bake method's docstring directly
# from Salmon, without creating a Salmon object.
# ANSWER:


# Exercise 4 — Documentation versus behavior
# Predict both outputs. Does reading the docstring bake the fish?
# dinner = Salmon()
# print(dinner.bake.__doc__)
# print(dinner.tastiness)
# ANSWER:


# Exercise 5 — Write your own docstring
# Define a function called favorite_meal that returns a food name.
# Give it a docstring explaining its purpose and return value.
# Display its documentation with both __doc__ and help().
# Write your code below:


# Exercise 6 — Explain help()
# Why does print(help(fish)) display an extra None after the help text?
# Which call would you normally use to view formatted documentation?
# ANSWER:


# Optional challenge — Document a class
# Create a Rice class with a servings attribute initialized to 2.
# Add a serve method that decreases servings by 1 when servings remain.
# Document the class, initializer, and method, including what happens
# when servings reaches zero. Inspect the result with help(Rice).
# ANSWER:


# --- 9. Final review ---
# 1. A docstring must be the __________ statement in its body.
# 2. Python stores documentation in the __________ attribute.
# 3. Triple quotes allow a string to span __________ lines.
# 4. The __________ function displays formatted documentation.
# 5. Reading Salmon.bake.__doc__ requires an instance: True or False?
# 6. Does changing a docstring change the function's return value?
# ANSWER:
