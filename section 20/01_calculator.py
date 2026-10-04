# Modules and Imports — Study Summary
# Instructor summary:
# - Split larger programs into modules to organize and reuse code.
# - A Python source file can serve as a module; no special declaration is needed.
# - A script is typically run directly, while a module is typically imported.
# - A module has its own namespace containing names such as variables,
#   constants, and functions. Those names are attributes of the module object.
# - import calculator binds the name calculator to that module object.
# - Use dot notation to access its attributes: calculator.creator,
#   calculator.PI, and calculator.add(3, 5).
# - Importing a module executes its top-level code on the first normal import.
# - Repeated normal imports reuse the cached module in the same interpreter.
#
# Clarifications and connections:
# - The same file can be run as a script or imported as a module.
# - A namespace organizes names; it is not a privacy or security boundary.
# - Function definitions create functions during import; their bodies run only
#   when called. A top-level print() runs during import.
# - Python searches for imports using its module search path (sys.path).
#   Files need not always share a directory, though that is convenient here.
# - Put imports near the top of a file, after any module docstring.
# - Uppercase constant names such as PI are a convention, not enforced immutability.
# - A fresh Python process imports modules again. The cache is not permanent.
#
# Filename note:
# - This numbered lesson is named 01_calculator.py. A normal import statement
#   cannot use a module name starting with a digit.
# - For the two-file examples below, copy the calculator definitions into
#   calculator.py and create my_program.py in the same directory.
# - Write import calculator, without the .py extension.


# --- 1. Define the reusable calculator contents ---
creator = "Boris"
PI = 3.14159


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def area(radius):
    return PI * radius * radius


# The definitions above are the contents to copy into calculator.py.
# area() reads PI from this module's global namespace when called.
# Defining these functions alone does not print anything.


# --- 2. Run examples directly ---
# This guard runs the examples when this file is executed directly, but skips
# them when it is imported. It keeps reusable code from printing unexpectedly.
if __name__ == "__main__":
    print(creator)  # Boris
    print(PI)  # 3.14159
    print(add(1, 3))  # 4
    print(add(3, 5))  # 8
    print(subtract(10, 4))  # 6
    print(area(2))  # 12.56636


# --- 3. Import the module from my_program.py ---
# After creating calculator.py as described above, place the following code
# in my_program.py and uncomment it THERE:
#
# import calculator
#
# print(calculator.creator)  # Boris
# print(calculator.PI)  # 3.14159
# print(calculator.add(3, 5))  # 8
# print(calculator.subtract(10, 4))  # 6
# print(calculator.area(2))  # 12.56636
#
# import calculator binds calculator in the importing file's namespace.
# It does not directly bind creator, PI, add, subtract, or area there.
# Leave this intentional error commented out in my_program.py:
# print(creator)  # NameError, unless my_program.py also defines/imports creator


# --- 4. Observe top-level execution during import ---
# To reproduce the instructor's experiment, temporarily add this UNGUARDED
# line at the bottom of calculator.py (outside any function or main guard):
# print(add(1, 3))
#
# Then run this code from my_program.py in a fresh Python process:
# import calculator
#
# print("This is coming from my_program")
#
# Expected output, in order:
# 4
# This is coming from my_program
#
# Python executes calculator's top-level code before continuing past the import
# in my_program.py. Remove the temporary print after the experiment, or put it
# under an if __name__ == "__main__": guard.
# Inside calculator.py, __name__ is "calculator" when imported normally and
# "__main__" when that file is executed directly.


# --- 5. Observe the import cache ---
# With the temporary unguarded print still present in calculator.py, run this
# separate experiment in my_program.py using a fresh Python process:
# import calculator
# import calculator
#
# print(calculator.add(2, 3))
#
# Expected output:
# 4
# 5
#
# The second normal import reuses the module cached under its name in sys.modules.
# It does not execute the calculator module's top-level code again.
# Repeated imports are unnecessary here; keep only one in the finished script.


# --- 6. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before trying each exercise.
# Run import exercises in my_program.py after creating calculator.py.
# Keep intentional-error examples commented out.

# Exercise 1 — Use the module's attributes
# Predict all three outputs.
# import calculator

# print(calculator.add(8, 2))
# print(calculator.subtract(8, 2))
# print(calculator.area(1))
# ANSWER:


# Exercise 2 — Diagnose a missing name
# Explain why the last line fails in a script that has not defined add.
# Rewrite that line using dot notation.
# import calculator
#
# print(add(3, 5))  # Intentional NameError; keep commented out.
# ANSWER:
# This is not referencing the calculator object correctly in the print statement hence error;
# The function exists as an attribute of the calculator module, so you access it with dot notation:


# Exercise 3 — Definitions versus calls
# Suppose calculator.py contains only creator, PI, and the three function
# definitions from section 1. What does running this script print?
# Explain why defining add() does not execute its body.
# import calculator
#
# print("Ready")
# ANSWER:
# simply prints the word Ready and even though it imports calculator if you dont call add()
# it doesn't do anything ;
# Importing calculator loads the module and defines add(), subtract(),
# and area(), but defining a function does not execute its body.
# The function body only runs when the function is called.


# Exercise 4 — Predict import timing
# Temporarily add print("Loading calculator") at the top level of calculator.py.
# Predict the output order below in a fresh Python process.
# Remove the temporary print when finished.
# import calculator
# import calculator
#
# print(calculator.add(1, 3))
# print("Finished")
# ANSWER:


# Exercise 5 — Extend the calculator
# 1. Add multiply(a, b) to calculator.py and return the product of its arguments.
# 2. Import calculator from my_program.py.
# 3. Print the result of calculator.multiply(6, 7).
# 4. Print the creator and the area of a circle with radius 3 using dot notation.
# 5. Explain which names belong to calculator's namespace and which module name
#    is bound in my_program.py.
# Write your code in the two files described above:
