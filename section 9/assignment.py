# Create an empty list and assign it to the variable "empty".


# Create a list with a single Boolean - True - and
# assign it to the variable "active".
active = [True]
print(active)

# Create a list with 5 integers of your choice and
# assign it to the variable "favorite_numbers".
favorite_numbers = [8, 6, 7, 5, 3]
print(favorite_numbers)

# Create a list with 3 strings - "red", "green", "blue"
# and assign it to the variable "colors".
colors = ["red", "green", "blue"]
print(colors)

# Declare an is_long function that accepts a single list as an argument
# It should return True if the list has more than 5 elements, and False otherwise
def is_long(numbers):
    test = len(numbers)
    return len(numbers) > 5

print(is_long([8, 6, 7, 5, 3, 0, 9]))


# Define a first_and_last function that accepts a list of strings.
# The function should return a concatenation of the first element and the last element.
# Assume the list will always have 1 or more elements.
#
# first_and_last(["a", "b", "c"])          => "ac"
# first_and_last(["bob", "tom", "rob"])    => "bobrob"
# first_and_last(["a"])                    => "aa"
def first_and_last(strings):
    return strings[0] + strings[-1]

print(first_and_last(["a", "b", "c"]))
print(first_and_last(["bob", "tom", "rob"]))
print(first_and_last(["a"]))


# Define a product_of_even_indices function that accepts a list of numbers.
# The list will always have 6 total elements.
# The function should return the product (multiplied total)
# of all numbers at an even index (0, 2, 4).
#
# product_of_even_indices([1, 2, 3, 4, 5, 6])    => 15
# product_of_even_indices([3, 4, 3, 5, 3, 6])    => 27
def product_of_even_indices(elements):
    return elements[0] * elements[2] * elements[4]

print(product_of_even_indices([1, 2, 3, 4, 5, 6]))
print(product_of_even_indices([3, 4, 3, 5, 3, 6]))

# Define a first_letter_of_last_string function that accepts a list of strings.
# It should return one character - the first letter of the last string in the list.
# Assume the list will always have at least one string.
#
# first_letter_of_last_string(["cat", "dog", "zebra"]) => "z"
# first_letter_of_last_string(["nonsense"])             => "n"
def first_letter_of_last_string(string):    
    return string[-1][0]

print(first_letter_of_last_string(["cat", "dog", "zebra"]))
print(first_letter_of_last_string(["nonsens"]))

# Define a split_in_two function that accepts a list and a number.
# If the number is even, return the list elements from the third element
# to the end of the list.
#
# If the number is odd, return the list elements from
# index 0 (inclusive) to 2 (exclusive)
#
# EXAMPLE:
values = ["a", "b", "c", "d", "e", "f"]
# split_in_two(values, 3)     => ["a", "b"]
# split_in_two(values, 4)     => ["c", "d", "e", "f"]
# split_in_two(values, 1)     => ["a", "b"]
# split_in_two(values, 10)    => ["c", "d", "e", "f"]
def split_in_two(mylist, number):
    if number % 2 == 0:
        return mylist[2:]
    else:
        return mylist[0:2]

print(split_in_two(values, 3))
print(split_in_two(values, 4))
print(split_in_two(values, 1))
print(split_in_two(values, 10))

# Define a first_and_last function that accepts a list of strings.
# The function should return a concatenation of the first element and the last element.
# Assume the list will always have 1 or more elements.
#
# first_and_last(["a", "b", "c"])       => "ac"
# first_and_last(["bob", "tom", "rob"]) => "bobrob"
# first_and_last(["a"])                 => "aa"
def first_and_last(mylist):
    return mylist[0] + mylist[-1]

print(first_and_last(["a", "b", "c"]))
print(first_and_last(["bob", "tom", "rob"]))
print(first_and_last(["a"]))


# Declare a nested_extraction function that accepts a list of lists and an index position.
#
# The function should use the index as the basis of finding both the nested list
# and the element from that list with the given index position
#
# You can assume the number of lists will always be equal to
# the number of elements within each of them.
#
def nested_extraction(numbers, index):    
    return numbers[index][index]

nl = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]
print(nested_extraction(nl, 0))  #=> # 3
print(nested_extraction(nl, 1))  #=> # 8
print(nested_extraction(nl, 2))  #=> # 12


# Declare a beginning_and_end function that accepts a list of elements.
#
# It should return True if the first and last elements in the list
# are equal and False if they are unequal.
#
# Assume the list will always have at least 1 element.
#
def beginning_and_end(list):
    if list[0] == list[-1]:
        return True
    return False


print(beginning_and_end([1, 2, 3, 1])) #     => True
print(beginning_and_end([1, 2, 3, 4, 5])) #  => False
print(beginning_and_end(["a", "b", "a"])) #  => True
print(beginning_and_end([15])) #             => True