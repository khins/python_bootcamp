# section 15 Tuples
# Tuples and lists have many similarities in Python, but 
# the major difference is mutability: lists can be changed 
# after creation, while tuples cannot.
foods = ("sushi", "steak", "guacamole")
print(type(foods))

# Declare a months tuple with the last 4 months of the year
# (September, October, November, December) as strings.
# Make sure the first letter of each month is capitalized.

months = ("September", "October", "November", "December")
print(months)


# Create a faves variable with a list of your 3 three favorite movies as strings.
# Use the tuple function to convert the list to a tuple and
# save the result in a movies variable.
movies = ["Lord of the Rings", "Jack Reacher", "Mission Impossible"]
print(tuple(movies))


# Create a numbers_a, numbers_b, and numbers_c tuple.
# Each tuple should contain 3 integers.
# Declare an all_numbers tuple containing these three tuples.
numbers_a = (1, 4, 9)
numbers_b = (7, 6, 3)
numbers_c = (2, 5, 0)
all_numbers = (numbers_a, numbers_b, numbers_c)
print(all_numbers)

# Tuples are ordered, so every element has an index beginning at 0:
birthday = (4, 12, 1991)
print(birthday[0])  # 4
print(birthday[1])  # 12
print(birthday[2])  # 1991

# Trying to access an index that doesn't exist causes an IndexError.
# Negative indexing also works exactly like it does with lists.
# The major difference: tuples are immutable
# A tuple does not, Tuple objects do not support item assignment.
# A useful way to remember this is:
# List  → mutable   → can change
# Tuple → immutable → cannot change
# but a tuple can contain mutable objects, such as lists:
addresses = (
    ["Hudson Street", "New York", "New York"],
    ["Franklin Street", "San Francisco", "California"]
)

# Unlike lists, tuples don't have methods such as:
# append()
# pop()
# insert()

# Key takeaway

# Lists and tuples are both ordered collections, support len(), indexing, negative indexing, count() and index().

# The concept to remember above everything else is:

# A tuple is immutable, but an object stored inside a tuple can still be mutable.