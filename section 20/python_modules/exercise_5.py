# Exercise 5 — Write your own aliased imports
# Write your code below, or in the separate script:
# 1. In a separate script, import math as maths and datetime as dt.
import math as maths
import datetime as dt
# 2. Use maths.sqrt() to calculate and print the square root of 81.
print(maths.sqrt(81))

# 3. Use dt.date() to create a date of your choice and print it.
print(dt.date(1969, 4, 14))
# 4. Print both modules' __name__ attributes.
print(dt.__name__)
print(maths.__name__)

# 5. Explain why the printed module names differ from your aliases:
# because my names were just an alias to the module ;
# ANSWER:
# maths and dt are only aliases that we created in our script.
# They are different names that reference the imported modules.
# The modules' own __name__ attributes remain "math" and "datetime".

# Our script's namespace:

# maths ─────────► math module
#                    __name__ = "math"

# dt ────────────► datetime module
#                    __name__ = "datetime"

# Import the math module, but bind it to the name maths in my program.
# maths is a name in your script that references the math module object; it isn't the module's actual name.
