# Import Aliases — Study Summary
# Instructor summary:
# - An alias is an alternate name or nickname for an imported module.
# - Use import module_name as alias to bind the module to your chosen name.
# - Access its attributes through the alias: alias.attribute or alias.function().
# - Aliases can reduce typing and follow familiar naming conventions.
# - Choose clear names and use them consistently across your project.
#
# Clarifications and connections:
# - An alias changes the name bound in the importing namespace, not the module's
#   filename, contents, or __name__ attribute.
# - import math as maths binds maths; it does not also bind math in this file.
# - Aliasing does not create a separate copy of the module.
# - Different files can choose different aliases, but consistency helps readers.
# - dt is a recognizable alias for datetime, not a required or universal name.
# - Use valid Python identifiers for aliases and avoid overwriting other names.

import datetime as dt
import math as maths


# --- 1. Access a module through its alias ---
print(maths.sqrt(9))  # 3.0
print(maths.ceil(4.5))  # 5
print(round(maths.pi, 5))  # 3.14159
# Dot notation works exactly as before; only the local module name changes.
# Leave this intentional error commented out:
# print(math.sqrt(9))  # NameError: this file imported math only as maths


# --- 2. Inspect the original module name ---
print(maths.__name__)  # math
print(dt.__name__)  # datetime
# The alias is a local reference. It does not rename the actual module.


# --- 3. Use datetime with the alias dt ---
lesson_date = dt.date(2026, 9, 26)
print(lesson_date)  # 2026-09-26
print(lesson_date.year)  # 2026
print(lesson_date.month)  # 9
print(lesson_date.day)  # 26
# dt refers to the datetime module; date is a class provided by that module.
# Calling dt.date(year, month, day) creates a date object.
# A fixed date makes the example's output predictable whenever you run it.


# --- 4. Alias the custom calculator module ---
# This example requires calculator.py containing the functions from lesson 1.
# The numbered file 01_calculator.py cannot be named directly in a normal import
# statement. Copy its reusable definitions into calculator.py to try this.
# Place the following code in a separate script alongside calculator.py:
#
# import calculator as calc

# print(calc.add(3, 5))  # 8
# print(calc.subtract(10, 4))  # 6
# print(calc.creator)  # Boris — with the original lesson's definition
# print(calc.__name__)  # calculator
#
# calc is the name available in the importing script. The original module's
# functions and variables are accessed through that name.
# Leave this intentional error commented out in that script:
# print(calculator.add(3, 5))  # NameError, unless calculator is separately bound


# --- 5. Two aliases can refer to the same module ---
# Try this in a separate script:
# import math as first_name
# import math as second_name
#
# print(first_name is second_name)  # True
# print(first_name.sqrt(16))  # 4.0
# print(second_name.sqrt(16))  # 4.0
#
# Normal imports reuse the cached module, even when different aliases are used.
# One clear, consistent alias is enough in ordinary code.


# --- 6. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# The dt and maths imports at the top are available to these exercises.
# Keep intentional-error examples commented out.

# Exercise 1 — Use the alias
# Predict all three outputs.
print(maths.floor(8.9))
print(maths.sqrt(25))
print(maths.__name__)
# ANSWER:
# 8
# 5
# math

# Exercise 2 — Diagnose a missing name
# In a fresh script, explain why the last line fails and correct it.
# import datetime as dt
#
# print(datetime.date(2025, 1, 2))  # Intentional NameError; keep commented out.
# ANSWER:
#  see section 20\python_modules\exercise_2.py


# Exercise 3 — Alias versus attribute
# Predict both outputs. Identify the module alias and the class name used below.
birthday = dt.date(2000, 7, 15)
print(birthday.month)
print(dt.__name__)
# ANSWER:
# 7
# datetime
#  Identify the module alias and the class name: datetime the date class


# Exercise 4 — Choose a clear name
# Both imports below are valid alternatives. Explain why calc is usually easier
# to understand than c in code that uses several different modules.
# import calculator as c
# import calculator as calc
# ANSWER:
# an alias of just c has no direct meaning and will force the developer to have to look it up
# rather than just making a more meaningful name
# why aliases should still be descriptive.


# Exercise 5 — Write your own aliased imports
# 1. In a separate script, import math as maths and datetime as dt.
# 2. Use maths.sqrt() to calculate and print the square root of 81.
# 3. Use dt.date() to create a date of your choice and print it.
# 4. Print both modules' __name__ attributes.
# 5. Explain why the printed module names differ from your aliases.
# Write your code below, or in the separate script:
# see section 20\python_modules\exercise_5.py
