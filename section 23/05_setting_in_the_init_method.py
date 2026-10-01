# Setting attributes in the __init__ method — Study Summary
# Instructor summary:
# - Set expected instance attributes inside __init__ for consistent setup.
# - self refers to the instance currently being initialized.
# - self.wood = value assigns a wood attribute to that instance.
# - A constant value gives each instance the same initial attribute value.
# - Parameters after self let callers customize each instance's initial state.
# - In def __init__(self, wood), Python supplies self during Guitar(wood).
# - The caller supplies wood; self.wood = wood stores it on the instance.
# - Omitting a required argument raises TypeError.
# - Separate instances can have matching attribute values and still be distinct.
#
# Clarifications to the transcript:
# - self is a conventional parameter name, not a Python keyword.
# - __init__ initializes an instance that has already been created.
# - wood is a local parameter; self.wood is an attribute on the instance.
#   Matching names are conventional, but they are not required.
# - Assigning wood does not enforce a string type. Validation requires more code.
# - Setting attributes in __init__ provides consistent initial setup; it does
#   not prevent later reassignment or deletion of ordinary instance attributes.
# - Use is to check identity, rather than comparing printed memory addresses.
# - Matching attributes do not automatically make custom instances equal with ==.
#   The basic Guitar class below inherits identity-based equality from object.
# - __init__ implicitly returns None; the normal class call returns the instance.


# --- 1. Initialize an attribute with a constant value ---
class DefaultGuitar:
    def __init__(self):
        self.wood = "mahogany"


first_default = DefaultGuitar()
second_default = DefaultGuitar()
print(first_default.wood)   # => mahogany
print(second_default.wood)  # => mahogany
print(first_default is second_default)  # => False
# Each initialization assigns wood to its own instance.
# No manual first_default.wood assignment is needed after construction.
# DefaultGuitar is a separate demonstration class so Guitar below can show
# configurable initialization without redefining the same class name.


# --- 2. Customize initial state with a parameter ---
class Guitar:
    def __init__(self, wood):
        self.wood = wood


acoustic = Guitar("alder")
electric = Guitar("mahogany")
print(acoustic.wood)  # => alder
print(electric.wood)  # => mahogany
# In the first call, self refers to the new acoustic instance and wood is alder.
# In the second call, self refers to the new electric instance and wood is mahogany.
# Both instances have wood, but their initial values differ.


# --- 3. Distinguish the parameter from the attribute ---
# In self.wood = wood:
# - The right-hand wood reads the argument held by the local parameter.
# - The left-hand self.wood stores that value on the current instance.
# The attribute remains available after the initializer finishes.

class Instrument:
    def __init__(self, material):
        self.wood = material


instrument = Instrument("maple")
print(instrument.wood)  # => maple
# Different names also work: the parameter is material, the attribute is wood.
# print(instrument.material)  # AttributeError: no material attribute was set.
# Writing only wood = material inside the method would create a local variable,
# not an instance attribute. Use self.wood to store data on the instance.


# --- 4. Supply required arguments, but do not supply self ---
baritone = Guitar("alder")
custom = Guitar(wood="maple")
print(baritone.wood)  # => alder
print(custom.wood)    # => maple
# wood can be supplied positionally or by keyword with this definition.
# Guitar takes one explicit argument here, even though __init__ has two parameters.
# Keep these intentional errors commented out:
# missing = Guitar()                 # TypeError: required wood argument missing.
# extra = Guitar("alder", "maple")   # TypeError: too many positional arguments.
# Python supplies the new instance as self during the normal class call.


# --- 5. Matching state does not mean shared identity ---
print(acoustic.wood == baritone.wood)  # => True
print(acoustic is baritone)           # => False
print(acoustic == baritone)           # => False
# This basic class has no custom equality method. Python does not automatically
# compare its wood attributes when == is used on the instances themselves.

first_list = [1, 2, 3]
second_list = [1, 2, 3]
print(first_list == second_list)  # => True
print(first_list is second_list)  # => False
# Lists implement equality by comparing their contents; Guitar above does not.


# --- 6. Initial values can change after initialization ---
acoustic.wood = "cedar"
print(acoustic.wood)  # => cedar
print(baritone.wood)  # => alder
# Changing one instance's attribute does not reassign another's attribute.

backup = acoustic
backup.wood = "spruce"
print(backup is acoustic)  # => True
print(acoustic.wood)       # => spruce
# Assignment makes an alias; it does not call Guitar or rerun __init__.
# self.wood = wood stores the supplied value; it does not make a copy of it.
# These examples use immutable strings. Mutable argument values need care
# because multiple instances can hold references to the same mutable object.


# --- 7. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Keep intentional-error lines commented out.

# Exercise 1 — A consistent initial value
# Predict all three outputs. How often does __init__ run?
# class Player:
#     def __init__(self):
#         self.volume = 5
#
# first = Player()
# second = Player()
# print(first.volume)
# print(second.volume)
# print(first is second)
# ANSWER:


# Exercise 2 — Customize each instance
# Predict both outputs. Explain which value self refers to in each call
# and why each Album call needs only one explicit argument.
# class Album:
#     def __init__(self, title):
#         self.title = title
#
# first = Album("Moving Pictures")
# second = Album("Paranoid")
# print(first.title)
# print(second.title)
# ANSWER:


# Exercise 3 — A parameter is not automatically an attribute
# The final line is an intentional error; keep it commented out.
# Explain why title = name does not store a title attribute on the instance.
# Write the corrected assignment inside __init__.
# class Song:
#     def __init__(self, name):
#         title = name
#
# song = Song("YYZ")
# print(song.title)  # AttributeError
# ANSWER:


# Exercise 4 — Required arguments and self
# Consider each proposed call separately using this class:
# class Guitar:
#     def __init__(self, wood):
#         self.wood = wood
#
# A. Guitar()
# B. Guitar("alder")
# C. Guitar(wood="maple")
# D. Guitar("alder", "mahogany")
# Which calls succeed? Explain each failure and who supplies self.
# Keep the invalid calls commented out.
# ANSWER:


# Exercise 5 — Equal attribute values and aliases
# Predict all five outputs. How many Guitar instances are created?
# class Guitar:
#     def __init__(self, wood):
#         self.wood = wood
#
# first = Guitar("alder")
# second = Guitar("alder")
# alias = first
# print(first.wood == second.wood)
# print(first is second)
# print(first == second)
# alias.wood = "maple"
# print(first.wood)
# print(second.wood)
# ANSWER:


# Exercise 6 — Write your own initializer with an attribute
# 1. Define a class named MusicPlayer.
# 2. Define __init__ with self and brand parameters.
# 3. Store brand in an instance attribute named brand.
# 4. Create two instances with different brands and print both brand attributes.
# 5. Create a third instance with the same brand as the first.
# 6. Print whether the first and third have equal brand values, then whether
#    they are the same object. Explain the difference.
# Write your code below:

# ANSWER:


# Optional challenge — Initialize several attributes
# Work through this one together when you are ready.
# Define a class named CustomGuitar.
# Its __init__ should accept wood, strings, and year after self.
# Store all three values as attributes with the same names on the instance.
# Define a regular function make_guitar_pair(wood, strings, year) that returns
# a list of two NEW CustomGuitar instances initialized with those values.
# Use the initializer for attribute setup, rather than assigning attributes
# manually after each instance is created.
# Write your code below:


# Uncomment these checks after defining your class and function:
# pair = make_guitar_pair("mahogany", 6, 1990)
# print(len(pair))              # => 2
# print(pair[0].wood)           # => mahogany
# print(pair[0].strings)        # => 6
# print(pair[0].year)           # => 1990
# print(pair[1].year)           # => 1990
# print(pair[0] is pair[1])     # => False
# pair[0].year = 2005
# print(pair[1].year)           # => 1990
# Explain why __init__ has four parameters but each CustomGuitar call needs
# only three explicit arguments. Why would creating one guitar and putting
# it into the list twice fail this challenge?
