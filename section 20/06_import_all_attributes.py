# Import All Public Attributes — Study Summary
# Instructor summary:
# - from module_name import * brings the module's public names directly into
#   the current namespace. This is called a wildcard or star import.
# - Use the imported names without a module prefix, just like explicit imports.
# - Wildcard imports make it harder to identify where names came from.
# - They increase the chance of name collisions, especially across modules.
# - Prefer explicit imports or module prefixes in ordinary application code.
# - By default, names beginning with an underscore are excluded from star imports.
#
# Clarifications and connections:
# - If a module defines __all__, that list of strings determines which names
#   its star import exports, including underscore-prefixed names if listed.
# - Without __all__, all names not starting with an underscore are included.
#   Those can include names the module imported from elsewhere.
# - A leading underscore is a non-public naming convention, not access control.
#   Explicit imports and module.attribute access can still use such names.
# - A later import can replace an existing local name; Python does not report
#   an error simply because two imported names collide.
# - A star import does not also bind the module's own name in the importing file.
# - Star imports are allowed at module level, not inside function definitions.
# - The star here means importing public names, not multiplication or unpacking.


# --- 1. See the star-import syntax ---
# This intentional demonstration uses a star import to illustrate the lesson.
# In ordinary code, prefer: from math import pi, sqrt
from math import *

print(sqrt(9))  # 3.0
print(round(pi, 5))  # 3.14159
print(ceil(4.2))  # 5
# The names are available directly, without a math prefix.
# Leave this intentional error commented out:
# print(math.sqrt(9))  # NameError: the name math was not bound by the star import


# --- 2. Import public names from calculator.py ---
# This example requires calculator.py containing creator, add(), and subtract()
# from lesson 1. Copy its reusable definitions into calculator.py to try it.
# The numbered file 01_calculator.py cannot be named in a normal import statement.
# In a separate script alongside calculator.py:
#
# from calculator import *
#
# print(creator)  # Boris — with the original lesson's definition
# print(add(3, 5))  # 8
# print(subtract(10, 4))  # 6
#
# Without __all__, the imported names depend on all of calculator's current
# names that do not begin with an underscore. A reader must inspect that module
# to discover exactly which names this statement introduces.


# --- 3. Underscore-prefixed names are excluded by default ---
# Suppose calculator.py has no __all__ and contains this extra assignment:
# _year = 2020
#
# In a fresh script:
# from calculator import *
#
# print(creator)  # Boris
# print(_year)  # Intentional NameError; keep this line commented out
# print(year)  # Intentional NameError; no year name was defined either
#
# The underscore is part of the name. Python does not rename _year to year.
# The default star-import rule simply skips _year.


# --- 4. An underscore does not make an attribute inaccessible ---
# With _year = 2020 defined in calculator.py, these alternatives still work:
#
# import calculator
# print(calculator._year)  # 2020
#
# from calculator import _year
# print(_year)  # 2020
#
# These are explicit accesses. The underscore convention signals that the name
# is intended for internal use, but Python does not enforce privacy here.


# --- 5. __all__ controls a module's star exports ---
# To try this independently, create export_demo.py with these contents:
#
# __all__ = ["creator", "_year"]
# creator = "Boris"
# _year = 2020
# description = "Calculator tools"
#
# Then use a separate script:
# from export_demo import *
#
# print(creator)  # Boris
# print(_year)  # 2020 — explicitly listed in __all__
# print(description)  # Intentional NameError; keep commented out
#
# description still exists in export_demo. __all__ limits the star import;
# it does not delete attributes or prevent explicit access to them.
# An empty __all__ list exports no names through a star import.


# --- 6. Name collisions replace local bindings ---
# Suppose first_tools.py contains creator = "Boris", and second_tools.py
# contains creator = "Alex". Neither module defines __all__.
# In a separate script:
#
# from first_tools import *
# print(creator)  # Boris
# from second_tools import *
# print(creator)  # Alex — the later import replaces the local binding
#
# Module prefixes preserve clarity and allow access to both values:
# import first_tools
# import second_tools
#
# print(first_tools.creator)  # Boris
# print(second_tools.creator)  # Alex
#
# Explicit aliases are another option:
# from first_tools import creator as first_creator
# from second_tools import creator as second_creator


# --- 7. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before trying each exercise.
# Use fresh scripts for import experiments so existing names do not hide errors.
# Keep intentional-error lines commented out.

# Exercise 1 — Use directly imported names
# Predict both outputs using the star import at the top of this lesson.
# print(sqrt(64))
# print(floor(3.9))
# Rewrite the import to request only the two functions used here.
# ANSWER:


# Exercise 2 — Default public names
# Suppose settings_demo.py defines these names and does not define __all__:
# volume = 9
# subtitles = True
# _debug = False
#
# Which names become available after from settings_demo import * in a fresh
# script? Explain why _debug is treated differently.
# ANSWER:


# Exercise 3 — An explicit export list
# Suppose settings_demo.py instead includes:
# __all__ = ["volume", "_debug"]
#
# Which of volume, subtitles, and _debug become available through its star import?
# Does subtitles still exist as an attribute of settings_demo? Explain.
# ANSWER:


# Exercise 4 — Trace a collision
# Assume first_tools.creator is "Boris" and second_tools.creator is "Alex".
# Neither module defines __all__. Predict both printed values:
# from first_tools import *
# from second_tools import *
# print(creator)
# creator = "Kevin"
# print(creator)
# Does the final assignment change either original module's creator attribute?
# ANSWER:


# Exercise 5 — Explain the underscore
# A classmate says, "A name starting with an underscore cannot be imported."
# Explain what is incorrect about that statement. Show an explicit import of
# _year from calculator and a module-prefixed way to access the same attribute.
# Assume calculator.py defines _year = 2020.
# ANSWER:


# Exercise 6 — Replace a star import
# Rewrite this separate script with explicit imports for only the names it uses:
# from math import *
#
# print(sqrt(81))
# print(ceil(2.2))
# print(floor(2.8))
# Predict the three outputs. Then write an alternative using import math and
# module prefixes instead. Explain how both versions clarify the names' origin.
# Write your code below:


# Optional challenge — Design a small module's public exports
# Work through this one together when you are ready.
# 1. Create music_tools.py with creator = "Kevin", _year = 2026, and a function
#    album_label(title, artist) that returns a string like "Hemispheres by Rush".
# 2. Define __all__ so a star import exports only creator and album_label.
# 3. In a separate script, use a star import for this experiment and print creator
#    and the result of calling album_label with a title and artist of your choice.
# 4. Explain why the star import does not bind _year in that script.
# 5. Replace the star import with explicit imports of the same two names.
# 6. Explain whether __all__ would prevent someone explicitly importing _year.
# Keep intentional-error demonstrations commented out.
# Write your code in the two files described above:
