# --- 3. Import selected calculator attributes ---
# This example requires calculator.py containing creator, add(), and subtract()
# from lesson 1. Copy those reusable definitions into calculator.py to try it.
# The numbered file 01_calculator.py cannot be named in a normal import statement.
# In a separate script alongside calculator.py, use:
#
# from calculator import creator, add, subtract
# #
# print(creator)  # Boris — with the original lesson's definition
# print(add(3, 5))  # 8
# print(subtract(10, 4))  # 6
#
# These names are directly available in the importing script.
# The import does not bind the name calculator there.
# Names must match the module's attributes exactly, including capitalization.

# --- 4. Compare module imports and direct imports ---
# These are separate alternatives, each producing 8:
#
import calculator
print(calculator.add(3, 5))
# Your program
#     │
#     └── calculator ──► calculator module
#                            │
#                            ├── add()
#                            ├── subtract()
#                            ├── multiply()
#                            └── etc.

from calculator import add
# only importing the add 
# calculator module
#       │
#       └── add()
#            │
#            │ direct import
#            ▼
# Your program
#       │
#       └── add()
print(add(3, 5))
#
# A module import keeps the source visible through the calculator prefix.
# A direct import makes add available without that prefix.

# A module import keeps the source visible through the calculator prefix.

# --- 6. Understand name collisions ---
# Suppose calculator.py defines creator = "Boris", and another module named
# other_tools.py defines creator = "Alex". In a separate script:
#
from calculator import creator
from other_tools import creator
#
print(creator)  # Alex — the second import replaces the first local binding
#
# To keep both names available, use aliases:
from calculator import creator as calculator_creator
from other_tools import creator as tools_creator
#
print(calculator_creator)  # Boris
print(tools_creator)  # Alex
#
# Or import the modules and retain their prefixes:
import calculator
import other_tools

print(calculator.creator)  # Boris
print(other_tools.creator)  # Alex