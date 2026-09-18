# Python Tuple Unpacking — Study Summary

# Tuple unpacking allows you to take the ordered elements of a tuple and assign them to multiple variables in a single statement.
employee = ("Bob", "Johnson", "Manager", 50)

first_name, last_name, position, age = employee

# So the general pattern is:
# variable1, variable2, variable3 = tuple

# For basic unpacking, remember:
# Number of variables = Number of elements
# Conceptually, Python first evaluates the right side:
# b, a

# Key takeaway

# Tuple unpacking is essentially taking apart an ordered collection and assigning its elements to variables:
coordinates = (10, 20, 30)

x, y, z = coordinates
print(coordinates)

# The three main ideas from this lesson are: unpacking assigns elements in order,
#  basic unpacking requires the number of variables to match the number of elements, and 
#  unpacking provides a convenient Python technique for swapping variable values.