# The __name__ Special Variable — Study Summary
# Instructor summary:
# - Python automatically supplies __name__ in a module's namespace.
# - "Dunder" means double underscore: __name__ has two on each side.
# - When a file runs as the program's entry point, __name__ is "__main__".
# - When normally imported, __name__ is the module's import name.
# - module.__name__ reads that attribute from a particular module object.
# - Bare __name__ reads the value in the current module's namespace.
# - if __name__ == "__main__": guards code intended to run as a script.
# - The guard lets one file provide reusable functions and a direct-run demo.
#
# Clarifications and connections:
# - __name__ is a string, not a function. Do not add parentheses to read it.
# - Dunder names are special conventions, not hidden or private attributes.
# - A normal import still executes top-level code, including the guard's check.
#   Only the indented body is skipped when the condition is False.
# - Functions outside the guard remain available to importing code.
# - A main() function is a convention; Python does not call it automatically.
# - Running a module with python -m also executes it as "__main__".
# - Package imports can have qualified names such as package.calculator.
# - Prefer separate import lines over comma-separated module imports.

import math


# --- 1. Define reusable functions outside the guard ---
def subtract(a, b):
    return a - b


def area(radius):
    return math.pi * radius ** 2


# --- 2. Collect the direct-run examples in main() ---
def main():
    print(math.__name__)  # math — the imported module's name
    print(__name__)  # __main__ — when this lesson runs as the entry point
    print(type(__name__))  # <class 'str'>
    print("This demo runs when the file is executed as a script.")
    print(subtract(3, 5))  # -2
    print(round(area(5), 2))  # 78.54


# --- 3. Call main() only when this file is the entry point ---
if __name__ == "__main__":
    main()

# Running this lesson directly prints the six lines from main().
# Importing it normally defines subtract(), area(), and main(), but does not
# call main(). The function definitions themselves do not print anything.
# Notice the distinction: __name__ is a variable; "__main__" is a string literal.


# --- 4. Compare direct execution with importing: a two-file example ---
# This lesson's numbered filename cannot be used in a normal import statement.
# To try the experiment, copy the following code into a separate name_demo.py:
#
# def subtract(a, b):
#     return a - b
#
# print(__name__)
#
# if __name__ == "__main__":
#     print("Running the demo directly")
#     print(subtract(3, 5))
#
# Running name_demo.py directly prints:
# __main__
# Running the demo directly
# -2
#
# Next, create playground.py in the same directory with this code:
#
# import name_demo
#
# print(name_demo.__name__)
# print(__name__)
# print(name_demo.subtract(10, 4))
#
# Running playground.py in a fresh Python process prints:
# name_demo
# name_demo
# __main__
# 6
#
# The first line comes from name_demo's unguarded print during import.
# The next two lines show the imported module's name and the script's name.
# The guarded demo in name_demo is skipped, but subtract() is still available.
# Remove the unguarded print from name_demo.py after observing the behavior.


# --- 5. Apply the guard to the earlier calculator module ---
# In a calculator.py file containing subtract() and area(), place any direct-run
# demonstrations under the guard:
#
# if __name__ == "__main__":
#     print("Calculator demo")
#     print(subtract(3, 5))
#
# In a separate playground.py file:
#
# import calculator
#
# print(calculator.__name__)  # calculator
# print(round(calculator.area(5), 2))  # 78.54
#
# With no unguarded prints in calculator.py, importing it produces no output.
# The two prints in playground.py still run. Guarding the demo does not prevent
# callers from using the calculator's functions.


# --- 6. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before trying each exercise.
# Use the separate files described above for import experiments.

# Exercise 1 — Identify the execution context
# What is __name__ inside name_demo.py in each situation?
# 1. You run name_demo.py directly.
# 2. You run playground.py, which imports name_demo.
# What is __name__ inside playground.py in the second situation?
# ANSWER:
# outputs
# __main__
# name_demo
# name_demo
# __main_
# The Python file you directly run gets __name__ == "__main__". An imported module gets its module name.

# Exercise 2 — Guarded versus unguarded output
# Suppose example.py contains the following code:
print("A")
if __name__ == "__main__":
    print("B")
print("C")
# Predict the output when example.py runs directly, then when another script
# first imports example. Explain which lines the guard controls.
# ANSWER:
# A
# B
# C
# Importing example from another script:
# A
# C

# The __name__ == "__main__" guard controls only print("B").
# A and C are outside the guard, so they execute whether the
# file is run directly or imported.

# Exercise 3 — Defining a function does not call it
# Suppose example.py contains only this code:
# def main():
#     print("Hello")
# Predict the output when the file runs directly. Add a guard that calls main().
# ANSWER:
# nothing happens when file runs directly
#  # Nothing happens when the file runs directly because defining
# main() does not call it.

# Exercise 4 — An explicit call after import
# Suppose example.py defines main() to print "Hello" and calls it under a guard.
# Predict the output from this separate script in a fresh Python process:
# import example
#
# print("Imported")
# example.main()
# Explain why main() can still be called explicitly after import.
# ANSWER:
# When example is imported, the guard prevents main() from being
# called automatically because __name__ is "example", not "__main__".
#
# However, importing example still defines main() in the example
# module's namespace. Therefore, we can explicitly call the function
# afterward using example.main().

# Exercise 5 — Write your own reusable module
# 1. Create greetings.py and define greet(name) to return a greeting string.
# 2. Define main() to print greet("Kevin") and the current __name__.
# 3. Call main() under an if __name__ == "__main__": guard.
# 4. Run greetings.py directly and inspect the output.
# 5. In a separate script, import greetings and print greetings.greet("Alex").
# 6. Explain why importing the module does not print the greeting for Kevin.
# Write your code in the two files described above:
