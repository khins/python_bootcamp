# Exercise 6 — Replace a star import
# Rewrite this separate script with explicit imports for only the names it uses:
# from math import *
#
import math
print(math.sqrt(81))
print(math.ceil(2.2))
print(math.floor(2.8))

# Predict the three outputs. Then write an alternative using import math and
# module prefixes instead. 
# Write your code below:# 
from math import sqrt, ceil, floor
print(sqrt(81))
print(ceil(2.2))
print(floor(2.8))

# 9.0
# 3
# 2
# Explain how this clarify the names' origin.
# this makes it explicit in what is being imported