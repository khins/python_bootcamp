# list iteration functions
# 
# Define a sum_of_lengths function that accepts a list of strings.
# The function should return the sum of the string lengths.
#
# EXAMPLES
# sum_of_lengths(["Hello", "Bob"])                    => 8
# sum_of_lengths(["Nonsense"])                        => 8
# sum_of_lengths(["Nonsense", "or", "Confidence"])   => 20
def sum_of_lengths(list):
    total = 0 
    for w in list:
        total += len(w)
    return total

print(sum_of_lengths(["Hello", "Bob"]))
print(sum_of_lengths(["Nonsense"]))
print(sum_of_lengths(["Nonsense", "or", "Confidence"]))

# Define a product function that accepts a list of numbers.
# The function should return the product of the numbers.
# The list will always have at least one value
#
def product(nums):
    total = 1
    for n in nums:
        total *= n
    return total

# EXAMPLES
print(product([1, 2, 3]))      # => 6
print(product([4, 5, 6, 7]))   # => 840
print(product([10]))          # => 10:

# Define a smallest_number function that accepts a list of numbers.
# It should return the smallest value in the list.
def smallest_number(numbers):
    smallest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n

    return smallest


# EXAMPLES
print(smallest_number([1, 2, 3]))     #=> 1
print(smallest_number([3, 2, 1]))     #=> 1
print(smallest_number([4, 5, 4]))     #=> 4
print(smallest_number([-3, -2, -1]))  #=> -3


# Define a concatenate function that accepts a list of strings.
#
# The function should return a concatenated string which consists of
# all list elements whose length is greater than 2 characters.

def concatenate(list):
    some_string = ""

    for string in list:
        if len(string) > 2:
            some_string += string
    return some_string


# EXAMPLES
print(concatenate(["abc", "def", "ghi"]))        #=> "abcdefghi"
print(concatenate(["abc", "de", "fgh", "i"]))    #=> "abcfgh"
print(concatenate(["ab", "cd", "ef", "gh"]))     #=> ""


# Define a super_sum function that accepts a list of strings.
# The function should sum the index positions of the first occurrence of the letter "s" in each
#
# Not every word is guaranteed to have an "s".
# Don't use "sum" as a variable name as it's a built-in keyword.
# Define a super_sum function that accepts a list of strings.
# The function should sum the index positions of the first occurrence of the letter "s" in each
#
# Not every word is guaranteed to have an "s".
# Don't use "sum" as a variable name as it's a built-in keyword.
#
def super_sum(list):
    list_sum = 0
    for word in list:
        if "s" in word:
            index = word.index("s")
            list_sum += index
    return list_sum

# EXAMPLES
print(super_sum([]))                                  # => 0
print(super_sum(["mustache"]))                        # => 2
print(super_sum(["mustache", "greatest"]))            # => 8
print(super_sum(["mustache", "pessimist"]))           # => 4
print(super_sum(["mustache", "greatest", "almost"]))  # => 12
#