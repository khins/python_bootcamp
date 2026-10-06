# Import sqrt as root, plus ceil and floor, from math.
# Define root_report(numbers), where numbers is a list of nonnegative integers.
# Return a NEW list of dictionaries, one per input, preserving input order.
# Each dictionary must contain "number", "root", "floor", and "ceil" keys.
# Store the original number, its square root, and the floor and ceiling of
# that square root. Use a loop and append(); leave numbers unchanged.
# root_report([9, 2]) returns:
# [{'number': 9, 'root': 3.0, 'floor': 3, 'ceil': 3},
#  {'number': 2, 'root': 1.4142135623730951, 'floor': 1, 'ceil': 2}]
# root_report([]) returns []
# Explain which imported names are functions and what each call returns.
from math import sqrt as root, ceil, floor

def root_report(numbers) -> list:
    # Create an empty list here
    report_list = []
    number_report = {}
    # loop through numbers here
    for number in numbers:
        square_root = root(number)
        number_report = {
                "number": number,
                "root": square_root,
                "floor": floor(square_root),
                "ceil": ceil(square_root)}

    report_list.append(number_report)
    return report_list

print(root_report([9, 2]))
# [{'number': 2, 'root': 1.4142135623730951, 'floor': 1, 'ceil': 2}]
print(type(root_report)) # <class 'function'>

number = 2

print(root(number))
print(type(root(number)))

number = 2
square_root = root(number)

print(floor(square_root))
print(type(floor(square_root)))

print(ceil(square_root))
print(type(ceil(square_root)))

# EXPLANATION:
# root, ceil, and floor are all functions imported from math.
#
# root is an alias for math.sqrt.
# root(2) returns 1.4142135623730951 as a float.
#
# floor(1.4142135623730951) returns 1 as an int.
# It rounds downward to the nearest integer.
#
# ceil(1.4142135623730951) returns 2 as an int.
# It rounds upward to the nearest integer.
