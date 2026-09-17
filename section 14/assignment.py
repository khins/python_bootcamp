# section 14 built in functions
help("hello")
help("len")

# map function
numbers = [2, 8, 5, 7, 9, 11]
cubes = [numb ** 3 for numb in numbers]
print(cubes)

def cube(number):
    return number ** 3

print(list(map(cube, numbers)))

animals = ['dog', 'cat', 'elephant', 'lion', 'tiger']
print([len(animal) for animal in animals])

long_words = [animal for animal in animals if len(animal) > 5]
print(long_words)

def is_long_animal(animal):
    return len(animal) >= 5

# Think of filter() as a gatekeeper: it checks each item and keeps the ones that pass a condition.
# is_long_animal is the function that checks each item.
# animals is the list supplying the items.
# An animal is kept when the function returns True and skipped when it returns False.
# Why no parentheses after is_long_animal?
# You’re passing the function itself to filter(). That lets filter() call it with each animal,
# effectively doing is_long_animal('dog'), then is_long_animal('cat'), and so on.
print(list(filter(is_long_animal, animals)))

# This also connects to your earlier map() example: map() transforms items;
#  filter() selects items. Your map(cube, numbers) produces cubes,
#  while filter(is_long_animal, animals) keeps the original animal strings that pass the check.

# Lambda functions
# a function without a name
metals = ["gold", "silver", "platinum", "palladium"]
print(list(filter(lambda metal: len(metal) > 5, metals)))
print(list(map(lambda word: word.count("l"), metals)))
print(list(map(lambda val: val.replace("s", "$"), metals)))

# Declare a right_words function that accepts a list of words and a number.
# Return a new list with the words that have a length equal to the number.
# Do NOT use list comprehension.
#
def right_words(words, number):
    return list(filter(lambda word: len(word) == number, words))
   

# EXAMPLES:
print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3))  # => ['cat', 'dog', 'ace']
print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5))  # => ['heart']
print(right_words([], 4))                                      # => []


# Declare an only_odds function.
# It should accept a list of whole numbers.
# It should return a list with only the odd numbers from the original list.
# Do NOT use list comprehension.
#
def only_odds(numbers):
    return list(filter(lambda number: number % 2 == 1, numbers))

# EXAMPLES:
print(only_odds([1, 3, 5, 6, 7, 8]))  # => [1, 3, 5, 7]
print(only_odds([2, 4, 6, 8]))        # => []


# # Declare a count_of_a function that accepts a list of strings.
# # It should return a list with counts of how many "a" characters appear per string.
# # Do NOT use list comprehension.
def count_of_a(words):
    return list(map(lambda word: word.count("a"), words))


# # EXAMPLES:
print(count_of_a(["alligator", "aardvark", "albatross"]))  # => [2, 3, 2]
print(count_of_a(["plywood"]))                             # => [0]
print(count_of_a([]))                                      # => []

# The all and any functions 
print(all([True]))
print(any([0, 1]))
print(max([3, 5, 7]))
print(max(["a", "g", "p"]))
print(sum([2, 3, 4]))
print(sum([-1.4, 4.6, 7.8]))

# Declare a greater_sum function that accepts two lists of numbers.
# It should return the list with the greatest sum.
# You can assume the lists will always have different sums.

def greater_sum(list1, list2):
    if sum(list1) > sum(list2):
        return list1
    return list2


# EXAMPLES
print(greater_sum([1, 2, 3], [1, 2, 4]))  # => [1, 2, 4]
print(greater_sum([4, 5], [2, 3, 6]))     # => [2, 3, 6]
print(greater_sum([1], []))                # => [1]


# Declare a sum_difference function that accepts two lists of numbers.
# It should return the difference between the sum of values in the first list
# and the second list

def sum_difference(list1, list2):
    total = 0
    total += sum(list1) - sum(list2)
    return total

# EXAMPLES
print(sum_difference([1, 2, 3], [1, 2, 4]))  # => 6 - 7 => -1
print(sum_difference([4, 5], [2, 3, 6]))     # => 9 - 11 => -2
print(sum_difference([1], []))                # => 1

# dir function
# print(dir("pasta"))
print("pasta".__len__())
print("pasta".__contains__("st"))

# format function
number = 0.123456789
print(format(number, ".2f")) # 2 floating point
print(format(number, ".3f")) # 3 flotaing point
print(format(8675309, ","))

def words_containing(animals, text):
    return list(filter(lambda animal: text.lower() in animal.lower(), animals))

print(words_containing(["Tiger", "bird", "tigerfish"], "TI"))
# => ["Tiger", "tigerfish"]

print(words_containing([], "a"))
# => []

def format_prices(numbers):
   return list(map(lambda number: f'${format(number, ",.2f")}', numbers))


print(format_prices([3, 12.5, 0.99]))
# => ["$3.00", "$12.50", "$0.99"]

# Return whether every number is greater than zero.
# Hint: Use all() with map(). The empty-list result is intentional: there are
# no items that fail the condition.
def all_positive(my_list):
    return all(map(lambda number: number > 0, my_list))

print(all_positive([2, 7, 1]))  # => True
print(all_positive([2, 0, 1])) # => False
print(all_positive([]))       # => True

# Return whether at least one word is longer than limit.
# Hint: Use any(). Think about why its empty-list result differs from all().
def has_long_word(elements, number):
    return any(map(lambda element: len(element) > number, elements))   


print(has_long_word(["cat", "elephant"], 5)) # => True
print(has_long_word(["cat", "dog"], 3))      # => False
print(has_long_word([], 5))                  # => False

# Select the even numbers, square them, and return their sum.
# Hint: Combine filter(), map(), and sum(). Start with separate 
# variables for each step.
def sum_even_squares(numbers):
    evens = filter(lambda numb: numb % 2 == 0, numbers)
    squares = map(lambda numb: numb ** 2, evens)
    return sum(squares)

print(sum_even_squares([1, 2, 3, 4])) # => 20
print(sum_even_squares([1, 3, 5]))   # => 0
print(sum_even_squares([-2, 0, 6]))   # => 40

# Return the longest word. If lengths tie, return the first one. For an
# empty list, return ""
# Stretch hint: Explore the key and default arguments of max() using help(max).
# help(max)

def longest_word(words):
    return max(words, key=len, default="")

print(longest_word(["cat", "elephant", "tiger"])) # => "elephant"
print(longest_word(["dog", "cat"]))              # => "dog"
print(longest_word([]))                          # => ""