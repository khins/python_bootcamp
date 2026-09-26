# The sorted function — Study Summary
# Instructor summary:
# - sorted(iterable) returns a NEW list containing the input's elements in order.
# - The default is ascending order; reverse=True requests descending order.
# - sorted() does not rearrange or modify the original collection.
# - sorted(dictionary) sorts its KEYS, just like sorted(dictionary.keys()).
# - sorted(dictionary.values()) sorts its values, keeping duplicates.
# - sorted(dictionary.items()) sorts its (key, value) tuples.
# - Tuples compare from left to right, so item pairs with distinct comparable
#   keys are ordered by those keys by default.
# - sorted() returns a list, even when its input is a dictionary or a view.
# - list.sort() changes a list in place and returns None.
#
# Corrections to the transcript:
# - Python 3.7+ dictionaries preserve insertion order. They are not automatically
#   sorted by key, but their iteration order is guaranteed.
# - sorted() is useful when you want a different order, such as alphabetical
#   display. Using it with a dictionary is a normal, valid design choice.
# - String sorting is case-sensitive and based on Unicode character order;
#   it is not always the same as human alphabetical ordering.


# --- 1. Sort a list without changing it ---
numbers = [4, 7, 2, 9]
ordered_numbers = sorted(numbers)
print(ordered_numbers)  # [2, 4, 7, 9]
print(numbers)          # [4, 7, 2, 9]
print(ordered_numbers is numbers)  # False

print(sorted(numbers, reverse=True))  # [9, 7, 4, 2]
print(sorted("cab"))                  # ['a', 'b', 'c']
# A string input still produces a list, not a sorted string.


# --- 2. Compare sorted() with list.sort() ---
numbers = [4, 7, 2, 9]
result = numbers.sort()
print(numbers)  # [2, 4, 7, 9]
print(result)   # None
# Use sorted(numbers) when you want a new list.
# Use numbers.sort() when you want to change the existing list.
# A dictionary does not have a .sort() method.


# --- 3. Passing a dictionary sorts its keys ---
# Fictional pay amounts used only to illustrate the data structure.
salaries = {"Executive Assistant": 20, "CEO": 100}
print(sorted(salaries))         # ['CEO', 'Executive Assistant']
print(sorted(salaries.keys()))  # ['CEO', 'Executive Assistant']
print(salaries)                 # {'Executive Assistant': 20, 'CEO': 100}
# The original dictionary keeps its entries and insertion order.
# Neither sorted call sorts the salary amounts.


# --- 4. Choose the view that contains what you want to sort ---
# Sample wheel counts for these example vehicles.
wheel_count = {"truck": 6, "car": 4, "bicycle": 2}
print(sorted(wheel_count.keys()))
# Expected: ['bicycle', 'car', 'truck']
print(sorted(wheel_count.values()))
# Expected: [2, 4, 6]
print(sorted(wheel_count.items()))
# Expected: [('bicycle', 2), ('car', 4), ('truck', 6)]
# items() preserves each key's association with its value in a tuple.
# Sorting values alone does not include the keys they came from.

menu = {"tea": 3, "cake": 5, "juice": 3}
print(sorted(menu.values()))  # [3, 3, 5] — duplicates remain


# --- 5. Iterate over sorted key-value pairs ---
for vehicle, count in sorted(wheel_count.items()):
    print(f"The {vehicle} has {count} wheels.")
# Expected:
# The bicycle has 2 wheels.
# The car has 4 wheels.
# The truck has 6 wheels.
# First sorted() builds a list of pairs. Then the loop unpacks each pair.

print(list(wheel_count))  # ['truck', 'car', 'bicycle']
# The sorted display did not change the dictionary's insertion order.


# --- 6. Key order is different from value order ---
scores = {"Zoe": 2, "Alex": 9, "Sam": 5}
print(sorted(scores.items()))  # [('Alex', 9), ('Sam', 5), ('Zoe', 2)]
print(sorted(scores.values()))  # [2, 5, 9]
# The first result orders pairs by their keys, not by their numeric scores.

# Connection to key= and lambda from earlier lessons:
print(sorted(scores.items(), key=lambda pair: pair[1]))
# Expected: [('Zoe', 2), ('Sam', 5), ('Alex', 9)]
# pair[1] supplies the value used for sorting; the result still contains pairs.
# Equal sorting keys keep their original relative order (sorting is stable).

# Empty input produces an empty list:
print(sorted({}))  # []
# Values must support the requested ordering. Leave this error commented out:
# print(sorted({"tea": 3, 10: "ten"}))  # TypeError — str and int keys cannot be ordered together here


# --- 7. Practice: predict, explain, then run ---
# Write predictions in the ANSWER comments before uncommenting each exercise.
# Predict all lines, including whether the original collection changes.

# Exercise 1 — New list or changed list?
# Predict all three outputs. Explain why numbers keeps its original order.
numbers = [8, 2, 5]
ordered = sorted(numbers)
print(ordered) 
print(numbers)
print(ordered is numbers)
# ANSWER:
# [2, 5, 8]
# [8, 2, 5]
# False : ordered is numbers
# Explain why numbers keeps its original order: because the list is not modified by the 
# sorted function, hence keeping original order

# Exercise 2 — Sort dictionary keys
# Predict all three outputs. Does sorted(scores) sort names or scores?
scores = {"Zoe": 2, "Alex": 9, "Sam": 5}
print(sorted(scores))
print(sorted(scores, reverse=True))
print(list(scores))
# ANSWER:
# ["Alex", "Sam", "Zoe"]
# ['Zoe', 'Sam', 'Alex']
# ['Zoe', 'Alex', 'Sam']
# Does sorted(scores) sort names or scores?: sorted in this case would sort names which equal to 
# being a key in the dict

# Exercise 3 — Select a view
# Predict all three outputs. Explain which result preserves key-value pairs.
menu = {"tea": 3, "cake": 5, "juice": 3}
print(sorted(menu.keys()))
print(sorted(menu.values()))
print(sorted(menu.items()))
# ANSWER:
# [cake, juice, tea]
# [3, 3, 5]
# [('cake', 5), ('juice', 3), ('tea', 3)]

# Exercise 4 — Read the sorted loop
# Predict every output line. Is this loop sorting by title or by artist?
songs = {"YYZ": "Rush", "Roundabout": "Yes", "Dreams": "Fleetwood Mac"}
for title, artist in sorted(songs.items()):
    print(f"{title} by {artist}")
# ANSWER:
# Dreams by Fleetwood Mac
# Roundabout by Yes
# YYZ by Rush


# Exercise 5 — Diagnose the return value
# This code intends to save a sorted list in ordered.
# Predict both outputs, then write a correction using sorted() that also
# leaves the ORIGINAL numbers list unchanged. Start with a fresh [8, 2, 5].
numbers = [8, 2, 5]
ordered = numbers.sort()
print(ordered)
print(numbers)
# ANSWER:
# None because the sort method returns None when assigned to a variable
# [2, 5, 8]

# Exercise 6 — Write your own sorted menu
# 1. Create a menu dictionary with three lowercase item names and numeric prices.
#    Insert the names in an order that is not alphabetical.
# 2. Use sorted(menu.items()) in a loop with two descriptive variables.
# 3. Print each entry alphabetically by item name, in this format: tea: $3.00
# 4. Print list(menu) afterward to show its original key order is unchanged.
# 5. Print the prices from highest to lowest using values() and sorted().
# 6. Explain why the loop sorts pairs by name rather than price.
# Write your code below:
menu = {
    "oil filter": 8.99,
    "brake pads": 34.50,
    "spark plug": 4.25,
}
print(sorted(menu.items()))
for item, price in sorted(menu.items()):
    print(f'{item}: ${price:.2f}')

print(list(menu))

for price in sorted(menu.values()):
    print(f' ${price:.2f}')

# Explain why the loop sorts pairs by name rather than price: sorts by key when using .items()
# or rather: sorted() compares the tuples by their first element—the item name. .items() 
# supplies the pairs; it doesn’t sort them.


# Optional challenge — Sort songs by duration
# Work through this one together when you are ready.
# Define songs_by_duration(durations) to return a NEW list of (title, minutes)
# tuples, ordered from shortest to longest duration.
# Use items(), sorted(), and key= with a lambda. Leave durations unchanged.
# For equal durations, preserve the original insertion order of those entries.
# songs_by_duration({"Long Track": 8, "Short Track": 3, "Another Short": 3})
# => [('Short Track', 3), ('Another Short', 3), ('Long Track', 8)]
# songs_by_duration({}) => []
# Explain what pair[0] and pair[1] represent in your lambda's input.
# Write your code below:
