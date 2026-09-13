popular_rush_songs = [
    "Tom Sawyer",
    "The Spirit of Radio",
    "Limelight",
    "Closer to the Heart",
    "2112: Overture / The Temples of Syrinx",
    "Freewill",
    "Fly by Night",
    "Subdivisions",
    "Working Man",
    "YYZ",
    "Red Barchetta",
    "Time Stand Still",
]

print(popular_rush_songs)
popular_rush_songs[1] = "I think I'm going bald"
print(popular_rush_songs)
popular_rush_songs[-1] = "Roll the bones"
print(popular_rush_songs)


# All official members before the 1980 breakup (including early members)
coworkers = [
    "Don Henley",
    "Glenn Frey",
    "Bernie Leadon",
    "Randy Meisner",
    "Don Felder",
    "Joe Walsh",
    "Timothy B. Schmit",
]

coworkers[-3:-1] = ["Alex Liefson"]

print(coworkers)
print("-" * 45)

# Given the great_directors list below, overwrite the "Steven Spielberg"
# string with a string of "Michael Bay".
great_directors = ["Martin Scorsese", "Steven Spielberg", "Francis Ford Coppola"]
great_directors[1] = "Michael Bay"
print(great_directors)


# Given the transformers list below, overwrite "Bumblebee" with "Grimlock".
transformers = ["Optimus Prime", "Megatron", "Bumblebee", "Starscream"]
transformers[2] = "Grimlock"
print(transformers)


# Given the camping_trip_supplies list below, overwrite "Socks" with "Food".
camping_trip_supplies = ["Socks", "Flashlight", "Tent", "Blanket"]
camping_trip_supplies[0] = "Food"
print(camping_trip_supplies)


# Given the tech_companies list below, overwrite the Microsoft, Blackberry, and IBM strings
# with the strings "Facebook" and "Apple". Use list slicing syntax.
tech_companies = ["Google", "Microsoft", "Blackberry", "IBM", "Yahoo"]
tech_companies[1:4] = ["fb", "ap"]
print(tech_companies)
print("-" * 45)

# Declare a length_match function that accepts a list of strings and an integer.
# It should return a count of the number of strings whose length is equal to the number.
def length_match(list, str_len):
    count = 0 
    for word in list:
        if str_len == len(word):
            count += 1
    return count


print("-" * 45)
# EXAMPLES
print(length_match(["cat", "dog", "kangaroo", "mouse"], 3))  # => 2
print(length_match(["cat", "dog", "kangaroo", "mouse"], 5))  # => 1
print(length_match(["cat", "dog", "kangaroo", "mouse"], 4))  # => 0
print(length_match([], 5))                                   # => 0
print("-" * 45)

# Declare a sum_from function that accepts two numbers as arguments.
# The second number will always be greater than the first number.
# The function should return the sum of all numbers from the
# first number to the second number (inclusive).
def sum_from(num1, num2):
    total = 0
    count = 0
    for number in range(num1, num2 + 1):
        total += number

    return total


# EXAMPLES
print(sum_from(1, 2))   # 1 + 2                 => 3
print(sum_from(1, 5))   # 1 + 2 + 3 + 4 + 5     => 15
print(sum_from(3, 8))   # 3 + 4 + 5 + 6 + 7 + 8 => 33
print(sum_from(9, 12))  # 9 + 10 + 11 + 12      => 42
print("-" * 45)

# Declare a same_index_values function that accepts two lists.
# The function should return a list of the index positions in which the two lists have equal elements.
def same_index_values(list1, list2):
    results = []
    for index, value in enumerate(list1):
        if value == list2[index]:
            results.append(index)
    
    return results



# EXAMPLES
print(same_index_values([1, 2, 3], [3, 2, 1]))                  # => [1]
print(same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]))  # => [1, 3]

print("-" * 45)
# Define an only_evens function that accepts a list of numbers.
# It should return a new list consisting of only the even numbers from the original list.
def only_evens(numbers):
    new_list = []
    for num in numbers:
        if num % 2 == 0:
            new_list.append(num)
    return new_list


# EXAMPLES
print(only_evens([4, 8, 15, 16, 23, 42]))  # => [4, 8, 16, 42]
print(only_evens([1, 3, 5]))                # => []
print(only_evens([]))                       # => []

print("-" * 45)
# Define a long_strings function that accepts a list of strings.
# It should return a new list consisting of only the
# strings that have 5 characters or more.
def long_strings(list):
    new_list = []
    for w in list:
        if len(w) >= 5:
            new_list.append(w)

    return new_list

# EXAMPLES
print(long_strings(["Hello", "Goodbye", "Sam"]))  # => ["Hello", "Goodbye"]
print(long_strings(["Ace", "Cat", "Job"]))        # => []
print(long_strings([]))                           # => []

# The method is called extend(). It mutates an existing list by adding each item from
# another iterable to the end.
fruits = ["apple", "banana"]
fruits.extend(["cherry", "orange"])

print(fruits)
# ["apple", "banana", "cherry", "orange"]

# Also, extend() changes the list in place and returns None, so use:
fruits.extend(["grape"])
letters = ["a", "b"]

letters.extend("cat")    # Adds "c", "a", "t"
letters.append("cat")    # Adds "cat"
letters.extend(["cat"])  # Adds "cat" — the list contains one item
print(letters)

numbers = [1, 2]
numbers.extend([3, 4])
print(numbers)

# The key is that extend() changes the original list and returns None.
numbers = [1, 2]
result = numbers.extend([3, 4])

print(numbers)
print(result)

pets = ["dog"]
pets.extend(["cat", "bird"])
print(pets)

pets = ["dog"]
pets = pets.extend(["cat"])

print(pets)
print("-" * 45)

# Declare a length_match function that accepts a list of strings and an integer.
# It should return a count of the number of strings whose length is equal to the number.
def length_match(list, number):
    count = 0
    for word in list:
        if len(word) == number:
            count += 1

    return count


# EXAMPLES
print(length_match(["cat", "dog", "kangaroo", "mouse"], 3))  # => 2
print(length_match(["cat", "dog", "kangaroo", "mouse"], 5))  # => 1
print(length_match(["cat", "dog", "kangaroo", "mouse"], 4))  # => 0
print(length_match([], 5))                                   # => 0


# Write a factors function that accepts a positive whole number
# It should return a list of all of the number's factors in ascending order
# HINT: Could the range function be helpful here? Or maybe a while loop?
def factors(number):
    my_factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            my_factors.append(i)

    return my_factors


# EXAMPLES
print(factors(1))   # => [1]
print(factors(2))   # => [1, 2]
print(factors(10))  # => [1, 2, 5, 10]
print(factors(64))  # => [1, 2, 4, 8, 16, 32, 64]

# The Pop method
last_one = popular_rush_songs.pop()
last_one = popular_rush_songs.pop()
last_one = popular_rush_songs.pop(-2)
print(last_one)

del popular_rush_songs[1:3]
print(popular_rush_songs)

new_rush_list = popular_rush_songs
new_rush_list.remove("YYZ")

print(new_rush_list)

new_rush_list.clear()
print(new_rush_list)

# Declare a delete_all function that accepts a list of strings and a target string
# Remove all occurrences of the target string from the list and return it

def delete_all(numbers, target):
    while target in numbers:
        numbers.remove(target)    

    return numbers

# EXAMPLES
print(delete_all([1, 3, 5], 3))    # => [1, 5]
print(delete_all([5, 3, 5], 5))    # => [3]
print(delete_all([4, 4, 4], 4))    # => []
print(delete_all([4, 4, 4], 6))    # => [4, 4, 4]


# Declare a push_or_pop function that accepts a list of numbers
# Build up and return a new list by iterating over the list of numbers
# If a number is greater than 5, add it to the end of the new list
# If a number is less than or equal to 5, remove the last element added to the new list
# Assume the order of numbers in the argument will never require removing from an empty list
def push_or_pop(list):
    new_list = []
    for numb in list:
        if numb > 5:
            new_list.append(numb)
        else:            
            list.pop()

    return new_list

# EXAMPLES
print(push_or_pop([10]))             # => [10]
print(push_or_pop([10, 4]))          # => []
print(push_or_pop([10, 20, 30]))     # => [10, 20, 30]
print(push_or_pop([10, 20, 2, 30]))  # => [10, 30]

print("-" * 45)
# reverse method 
coworkers.reverse()
print(coworkers)

# sort method on a list
coworkers.sort()
print(coworkers)