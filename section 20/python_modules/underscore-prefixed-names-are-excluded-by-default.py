# --- 3. Underscore-prefixed names are excluded by default ---
# Suppose calculator.py has no __all__ and contains this extra assignment:
_year = 2020
#
# In a fresh script:
from calculator import *
#
print(creator)  # Boris
# print(_year)  # Intentional NameError; keep this line commented out
# print(year)  # Intentional NameError; no year name was defined either
#
# The underscore is part of the name. Python does not rename _year to year.
# The default star-import rule simply skips _year.

# --- 4. An underscore does not make an attribute inaccessible ---
# With _year = 2020 defined in calculator.py, these alternatives still work:
#
import calculator
print(calculator._year)  # 2020

from calculator import _year
print(_year)  # 2020
#
# These are explicit accesses. The underscore convention signals that the name
# is intended for internal use, but Python does not enforce privacy here.