# my_program.py
# Exercise 1 — Use the module's attributes
print("Loading calculator")
import calculator
# import calculator

# print(calculator.add(1, 3))
# print("Finished")

# ANSWER:
# 10
# 6
# 100
print("Ready")
print(calculator.add(8, 2))
print(calculator.subtract(8, 2))
print(calculator.area)
# print(add(3, 5)) Error
print(calculator.multiply(6, 7))

# Print the creator and the area of a circle with radius 3 using dot notation.
print(calculator.creator)
print(calculator.area)
# ANSWER:
# creator, PI, add, subtract, area, and multiply belong to
# the calculator module's namespace.
#
# In my_program.py, the name calculator is bound to the
# imported calculator module. We use calculator.name to access
# names inside the calculator module.

# ANSWER:
# The names creator, PI, add, subtract, area, and multiply belong to
# calculator's namespace.
#
# 5. Explain which names belong to calculator's namespace and which module name
#    is bound in my_program.py:
# In my_program.py, the name calculator is bound to the imported
# calculator module. We use calculator.name to access names that
# belong to the calculator module.

import example

print("Imported")
example.main()