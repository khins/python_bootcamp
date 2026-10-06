# Import Specific Attributes — Study Summary
# Instructor summary:
# - Use from module_name import name to make an attribute available directly
#   in the current file's namespace.
# - Import multiple names by separating them with commas.
# - Imported names can refer to variables, constants, functions, or classes.
# - Call a directly imported function without a module prefix: sqrt(9).
# - Direct imports can cause name collisions when different modules provide
#   attributes with the same name.
# - Module prefixes help make the origin of generic names clear.
#
# Clarifications and connections:
# - from math import sqrt binds sqrt; it does not also bind math in this file.
# - A namespace organizes names; it is not a privacy or security boundary.
# - A name collision has a definite result: a later binding of the same local
#   name replaces the earlier binding. Python does not choose between them.
# - Explicit from imports are valid tools, not inherently incorrect style.
# - Use aliases or module prefixes when names would otherwise collide.
# - Importing one attribute still initializes the module on its first normal
#   import, including executing its unguarded top-level code.
# - Importing an attribute binds a reference to its object, not a copy of it.

from math import ceil, floor, sqrt
from math import pi as circle_pi


# --- 1. Import a function directly from the standard library ---
print(sqrt(9))  # 3.0
print(sqrt(64))  # 8.0
# sqrt is now a name available directly in this file.
# Leave this intentional error commented out:
# print(math.sqrt(9))  # NameError: the name math was not bound by these imports


# --- 2. Import multiple attributes ---
print(ceil(4.2))  # 5
print(floor(4.8))  # 4
# from math import ceil, floor, sqrt imports three attributes from one module.
# This differs from importing several modules on a single line.


# --- 3. Import selected calculator attributes ---
# This example requires calculator.py containing creator, add(), and subtract()
# from lesson 1. Copy those reusable definitions into calculator.py to try it.
# The numbered file 01_calculator.py cannot be named in a normal import statement.
# In a separate script alongside calculator.py, use:
#
# from calculator import creator, add, subtract
#
# print(creator)  # Boris — with the original lesson's definition
# print(add(3, 5))  # 8
# print(subtract(10, 4))  # 6
#
# These names are directly available in the importing script.
# The import does not bind the name calculator there.
# Names must match the module's attributes exactly, including capitalization.
# see section 20\python_modules\import-selected-calculator-attributes.py


# --- 4. Compare module imports and direct imports ---
# These are separate alternatives, each producing 8:
#
# import calculator
# print(calculator.add(3, 5))
#
# from calculator import add
# print(add(3, 5))
#
# A module import keeps the source visible through the calculator prefix.
# A direct import makes add available without that prefix.


# --- 5. Use an alias to make a name distinct ---
print(round(circle_pi, 5))  # 3.14159
radius = 2
print(round(circle_pi * radius ** 2, 2))  # 12.57
# from math import pi as circle_pi binds circle_pi, not pi.
# Aliasing an attribute changes its local name, not the original module attribute.


# --- 6. Understand name collisions ---
# Suppose calculator.py defines creator = "Boris", and another module named
# other_tools.py defines creator = "Alex". In a separate script:
#
# from calculator import creator
# from other_tools import creator
#
# print(creator)  # Alex — the second import replaces the first local binding
#
# To keep both names available, use aliases:
# from calculator import creator as calculator_creator
# from other_tools import creator as tools_creator
#
# print(calculator_creator)  # Boris
# print(tools_creator)  # Alex
#
# Or import the modules and retain their prefixes:
# import calculator
# import other_tools
#
# print(calculator.creator)  # Boris
# print(other_tools.creator)  # Alex


# --- 7. Local reassignment does not change the module attribute ---
# Try this in a separate script:
# import math
# from math import pi
#
# pi = 3
# print(pi)  # 3
# print(math.pi)  # 3.141592653589793
#
# pi = 3 rebinds the local name. It does not assign to math.pi.
# A directly imported name is not a live link to future attribute reassignments.


# --- 8. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Keep intentional-error lines commented out.
# Use fresh scripts where instructed so earlier imports do not hide errors.

# Exercise 1 — Direct function calls
# Predict all three outputs using the imports at the top of this lesson.
print(sqrt(25))
print(ceil(7.1))
print(floor(7.9))
# ANSWER:
# 5
# 8
# 7


# Exercise 2 — Which names are available?
# In a fresh script containing only from math import sqrt, 
from math import sqrt
# A: 
sqrt(16)
# B: 
# math.sqrt(16) # NameError: name 'math' is not defined. Did you forget to import 'math'
# ANSWER:
# identify which expression succeeds and which raises NameError. Explain why.
# math.sqrt raises a NameError because it was only importing a specific function in math
# A succeeds and returns 4.0.
# B raises a NameError.
#
# "from math import sqrt" imports sqrt directly into the
# script's namespace, but it does not bind the name "math"
# in the script. Therefore, sqrt() is available directly,
# but math.sqrt() is not.


# Exercise 3 — Alias a specific attribute
# Predict the successful call's output and explain why the other call fails
# in a fresh script.
#
from math import sqrt as root
#
# A: 
print(root(49)) # "Get sqrt from math, but in my program I want to call it root."
# B: 
print(sqrt(49))
# ANSWER:
# A succeeds and outputs 7.0.
# B raises a NameError.
#
# "from math import sqrt as root" imports the sqrt function
# but binds it to the alias "root" in this script.
# Therefore, root() is available, but sqrt() is not.
# from math import sqrt as root

# Our script's namespace:

# root ─────► math's sqrt function

# sqrt ─────► NOT DEFINED
# math ─────► NOT DEFINED

# Exercise 4 — Trace a name collision
# Assume calculator.creator is "Boris" and other_tools.creator is "Alex".
# Predict both outputs. Explain which import supplies each printed value.
# from calculator import creator
# print(creator)
# from other_tools import creator
# print(creator)
# Rewrite the imports with aliases so both values stay available afterward.
# ANSWER:


# Exercise 5 — Importing still executes module code
# Suppose greeting_tools.py contains:
# print("Loading greetings")
#
# def greet(name):
#     return f"Hello, {name}!"
#
# Predict the output order when this separate script runs in a fresh process:
# from greeting_tools import greet
#
# print(greet("Kevin"))
# Explain why importing only greet does not skip the top-level print.
# ANSWER:
# reference file section 20\python_modules\importing-still-executes-module-code.py
# Even though we are importing only greet, Python must execute the
# top-level code in greeting_tools.py when the module is first imported.
# Therefore, print("Loading greetings") runs during the import.
#
# After the import finishes, greet is available in this script and
# print(greet("Kevin")) executes.


# Exercise 6 — Write your own selected imports
# 1. In a separate script, import add and subtract from calculator.py.
# 2. Give subtract the alias difference in the import statement.
# 3. Import sqrt directly from math.
# 4. Print add(10, 4), difference(10, 4), and sqrt(81).
# 5. Predict all three outputs.
# 6. Explain which names your imports bind and why calculator.add(10, 4)
#    would fail unless you also bound the name calculator.
# Write your code in the separate script:


# Optional challenge — Build a square-root report
# Work through this one together when you are ready.
# Import sqrt as root, plus ceil and floor, from math.
# Define root_report(numbers), where numbers is a list of nonnegative integers.
# Return a NEW list of dictionaries, one per input, preserving input order.
# Each dictionary must contain "number", "root", "floor", and "ceil" keys.
# Store the original number, its square root, and the floor and ceiling of
# that square root. Use a loop and append(); leave numbers unchanged.
# root_report([9, 2]) returns:
# [{'number': 9, 'root': 3.0, 'floor': 3, 'ceil': 3},
#  {'number': 2, 'root': 1.4142135623730951, 'floor': 1, 'ceil': 2}]
# root_report([]) returns []
# Explain which imported names are functions and what each call returns.
# Write your code below:
