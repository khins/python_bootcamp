# Exercise 6 — Write your own selected imports
# Write your code in the separate script:
# 1. In a separate script, import add and subtract from calculator.py.
# 2. Give subtract the alias difference in the import statement.
from calculator import add, subtract as difference
# from calculator import add, subtract as difference
#                        ↓              ↓
#                       add         difference

# from math import sqrt
#                  ↓
#                 sqrt
# 3. Import sqrt directly from math.
from math import sqrt
# 4. Print add(10, 4), difference(10, 4), and sqrt(81).
# print(calc.add(10, 4))
# print(calculator.add(10, 4)) # not defined
print(sqrt(81))
# 5. Predict all three outputs.
# calculator
# 14
# 9.0
# 6. Explain which names your imports bind and why calculator.add(10, 4)
#    would fail unless you also bound the name calculator.
# calculator.add(10, 4) comes up as an error because the import binding was set to an alias of calc
