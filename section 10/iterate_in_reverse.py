the_simpsons = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]

for character in the_simpsons[::-1]:
    print(f"{character} has a total of {len(character)} characters.")

print(reversed(the_simpsons))
print(type(reversed(the_simpsons)))

for character in reversed(the_simpsons):
    print(f'{character} has a total of {len(character)} characters.')

print(list(reversed(the_simpsons)))

# 1 Number the reversed names.
# Produce 1. Maggie, 2. Lisa, and so on.
# Hint: Combine enumerate() with reversed()
# enumerate warm up
for character in the_simpsons:
    print(character)
# with enumerate By default, numbering starts at 0 but can change start parameter
for index, character in enumerate(the_simpsons, start=5):
    print(f'{index}: {character} is a character in the simpsons family')

for number, character in enumerate(reversed(the_simpsons), start=1):
    if len(character) > 4:
        print(f'{number}: {character}')


# Next, practice reversing a string: modify your print statement to produce:
# 1: Maggie → eiggaM
# 4: Marge → egraM
# 5: Homer → remoH
for number, character in enumerate(reversed(the_simpsons), start=1):
    if len(character) > 4:
        print(f'{number}: {character[::-1]}')

print("-" * 20)

for index in range(len(the_simpsons) -1, -1, -1):
    print(f'{index}: {the_simpsons[index]}')

print("-" * 20)
# use that backward loop to build a new reversed list

# set the_simpsons to empty list for edge case detection
# the_simpsons = ["Homer"]
backward = []

for index in range(len(the_simpsons) - 1, -1, -1):
    # Add the character at this index to backward
    backward.append(the_simpsons[index])

print(backward)

characters = ["Homer", "Marge", "Bart"]
characters.reverse()
print(characters)

characters = ["Homer", "Marge", "Bart"]
backward = characters[::-1]

print(characters)
print(backward)

# Final challenge: given numbers = [10, 20, 30, 40], build a new list containing twice
# each number, in reverse order, while keeping numbers unchanged.
numbers = [10, 20, 30, 40]
twice = []
for n in reversed(numbers):
    twice.append(n * 2)

print(twice)

print("-" * 20)
# Filter while looping backward.
# Print only names with more than four letters, in reverse order.
# Expected names: Maggie, Marge, Homer.
for index, character in enumerate(reversed(the_simpsons)):
    if len(character) > 4:
        print(f'{index} {character}')

print("-" * 20)
# Reverse the names themselves.
# Loop through the list backward and also reverse each name. Your first line should be Maggie → eiggaM.
# Think about: How does reversing a list differ from reversing a string inside it?    
for index, character in enumerate(reversed(the_simpsons)):
    print(f'{index} {character[::-1]}')

print("-" * 20)
# Loop backward using indexes.
# Print each name alongside its original index, starting with 4: Maggie and ending with 0: Homer. Don’t use slicing or reversed().
# Hint: Use range(start, stop, step). What must stop be to include index 0?

for index in range(len(the_simpsons) - 1, -1, -1):
    print(f'{index}: {the_simpsons[index]}')

print("-" * 20)
print("Explore whether the original changes.", end="\n")
# 5 
# Compare slicing, reversed(), and the_simpsons.reverse(). For each, predict what
# happens, then print the original list afterward. Also investigate what .reverse() returns.
for index, character in enumerate(reversed(the_simpsons)):
    print(f'{index} {character}')

the_simpsons.reverse()
print(the_simpsons) # reverse is a method on the list so it just reverse the order - modfifes original list


print("-" * 20)
# 6 Challenge: build your own reversed list.
# Start with backward = [] and fill it using a loop. Don’t use slicing, reversed(), or .reverse().
# Confirm that the original list stays unchanged.
# Bonus: Does your approach work with an empty list or a one-item list?
yes_list = [
    "Believe Again",
    "The Game",
    "Step Beyond",
    "To Ascend",
    "In a World of Our Own",
    "Light of the Ages",
    "It Was All We Knew",
    "Subway Walls",
]

backward = [] 
for index in range(len(yes_list)- 1, -1, -1):
    backward.append(yes_list[index])

print(backward)
print(yes_list)

# Define an in_list function that accepts a list of strings and a separate string.
# Return the index where the string exists in the list.
# If the string does not exist, return -1.
# Do NOT use the find or index methods.
#
# EXAMPLES
strings = ["enchanted", "sparks fly", "long live"]

def in_list(list, stop_word):
    for index, word in enumerate(strings):
        if stop_word == word:
            return index
    return -1


print(in_list(strings, "enchanted"))    # => 0
print(in_list(strings, "sparks fly"))   # => 1
print(in_list(strings, "fifteen"))      # => -1
print(in_list(strings, "love story"))   # => -1


# Define a sum_of_values_and_indices function that accepts a list of numbers.
# It should return the sum of all of the elements along with their index values.
#
# EXAMPLES
def sum_of_values_and_indices(list):
    total = 0
    
    for index, number in enumerate(list):
        total += index + number

    return total

print(sum_of_values_and_indices([1, 2, 3]))    # => (1 + 0) + (2 + 1) + (3 + 2) => 9
print(sum_of_values_and_indices([0, 0, 0, 0])) # => 6
print(sum_of_values_and_indices([]))           # => 0