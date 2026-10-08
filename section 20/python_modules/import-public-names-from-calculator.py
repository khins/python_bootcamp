# --- 2. Import public names from calculator.py ---
# This example requires calculator.py containing creator, add(), and subtract()
# from lesson 1. Copy its reusable definitions into calculator.py to try it.
# The numbered file 01_calculator.py cannot be named in a normal import statement.
# In a separate script alongside calculator.py:
#
from calculator import *
#
print(creator)  # Boris — with the original lesson's definition
print(add(3, 5))  # 8
print(subtract(10, 4))  # 6
#
# Without __all__, the imported names depend on all of calculator's current
# names that do not begin with an underscore. A reader must inspect that module
# to discover exactly which names this statement introduces.