# Introduction to sets — Study Summary
# Instructor summary:
# - A set is a mutable collection of unique, hashable elements.
# - Use {value, value, ...} for a nonempty set; use set() for an empty set.
# - Duplicate elements contribute only one entry to a set.
# - Sets do not guarantee insertion order or support positional indexing.
# - len() counts elements; in and not in check membership.
# - A for loop visits each element, but its order is not guaranteed.
# - Set comprehensions use {expression for item in iterable}.
# - sorted(a_set) returns a new ordered LIST without changing the set.
#
# Corrections to the transcript:
# - Elements must be HASHABLE, not merely immutable. A tuple containing a
#   list is not hashable, even though the tuple itself is immutable.
# - Strings, numbers, and tuples of hashable elements work in these examples.
#   Lists, dictionaries, and ordinary sets cannot be set elements.
# - Unordered does not mean randomly shuffled on every iteration. It means
#   you must not rely on a particular order or on insertion order.
# - A duplicate does not remove the existing element; it adds no extra entry.
# - {} creates an empty dictionary, not an empty set.


# --- 1. Create sets and observe uniqueness ---
# These symbols are sample strings, not current financial information.
stocks = {"MSFT", "FB", "IBM", "FB"}
print(stocks)
# Contains 'MSFT', 'FB', and 'IBM' once each; display order may vary.
print(type(stocks))  # <class 'set'>
print(len(stocks))   # 3

prices = {1, 2, 3, 4, 5, 3, 4, 2}
print(sorted(prices))  # [1, 2, 3, 4, 5]
print(len(prices))     # 5
# Sorting is only for a predictable display; prices remains a set.


# --- 2. Distinguish sets, dictionaries, and empty collections ---
artists = {"Rush", "Yes"}
song_artists = {"YYZ": "Rush", "Roundabout": "Yes"}
empty_set = set()
empty_dictionary = {}
print(type(artists))           # <class 'set'>
print(type(song_artists))      # <class 'dict'>
print(empty_set)               # set()
print(type(empty_dictionary))  # <class 'dict'>
print(len(empty_set))          # 0
# A set contains elements; a dictionary associates keys with values.


# --- 3. Check membership ---
print("MSFT" in stocks)      # True
print("IBM" in stocks)       # True
print("GOOG" in stocks)      # False
print("MSFT" not in stocks)  # False
print("GOOG" not in stocks)  # True
# Membership does not change the set. String matching is case-sensitive.
print("msft" in stocks)      # False


# --- 4. Store hashable tuples ---
lottery_numbers = {(1, 2, 3), (4, 5, 6), (1, 2, 3)}
print(len(lottery_numbers))          # 2 — two tuples, not six integers
print(sorted(lottery_numbers))       # [(1, 2, 3), (4, 5, 6)]
print((1, 2, 3) in lottery_numbers)   # True
# Each tuple is one set element. Its integer contents are hashable.
# Leave these intentional errors commented out:
# invalid = {[1, 2, 3]}              # TypeError: a list is unhashable
# invalid = {{"song": "YYZ"}}        # TypeError: a dictionary is unhashable
# invalid = {("Rush", ["YYZ"])}      # TypeError: the tuple contains a list


# --- 5. Iterate without assuming order ---
for price in prices:
    print(price)
# Prints 1, 2, 3, 4, and 5 once each, in an unspecified order.

for numbers in lottery_numbers:
    for number in numbers:
        print(number)
# Each tuple retains its own order: 1, 2, 3 or 4, 5, 6.
# Either tuple may be visited first; the outer set has no guaranteed order.

# Use sorted() when a predictable traversal order is required:
for artist in sorted(artists):
    print(artist)
# Expected:
# Rush
# Yes

# Leave this intentional error commented out:
# print(stocks[0])  # TypeError: a set does not support indexing
# Converting to a list alone does not establish a sorted order.


# --- 6. Compare list and set comprehensions ---
numbers = [-5, -4, -3, 3, 4, 5]
square_list = [number ** 2 for number in numbers]
square_set = {number ** 2 for number in numbers}
print(square_list)         # [25, 16, 9, 9, 16, 25]
print(sorted(square_set))  # [9, 16, 25]
print(len(square_set))     # 3
print(numbers)            # [-5, -4, -3, 3, 4, 5]
# Opposite numbers have equal squares, so the set stores each result once.
# Both comprehensions create new collections and leave numbers unchanged.

positive_squares = {number ** 2 for number in numbers if number > 0}
print(sorted(positive_squares))  # [9, 16, 25]
# A condition can filter inputs, just as in a list comprehension.


# --- 7. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# For a raw set, give its contents without claiming a particular order.
# For sorted() output, give the exact list order.
# Keep intentional-error examples commented out.

# Exercise 1 — Count unique elements
# Predict all three outputs. Explain why the length differs from the number
# of strings written inside the braces.
# artists = {"Rush", "Yes", "Rush", "Genesis", "Yes"}
# print(len(artists))
# print(sorted(artists))
# print(type(artists))
# ANSWER:


# Exercise 2 — Empty set or dictionary?
# Predict all four outputs. Explain how to create an empty set.
# first = {}
# second = set()
# print(type(first))
# print(type(second))
# print(len(first))
# print(len(second))
# ANSWER:


# Exercise 3 — Membership and case
# Predict all four outputs. Explain whether these checks change the set.
# songs = {"YYZ", "Limelight", "YYZ"}
# print("YYZ" in songs)
# print("yyz" in songs)
# print("Roundabout" not in songs)
# print(len(songs))
# ANSWER:


# Exercise 4 — Tuples and ordering
# Predict the first two outputs. State the error the last line would raise.
# Explain why the set has two elements and why its tuples cannot be
# retrieved by a set index, even though each tuple supports indexing.
# groups = {(1, 2), (3, 4), (1, 2)}
# print(len(groups))
# print(sorted(groups))
# print(groups[0])  # Intentional error: keep commented out.
# ANSWER:


# Exercise 5 — Comprehension results
# Predict all four outputs. Explain why the two new collections have
# different lengths and whether the original list changes.
# numbers = [-2, -1, 1, 2]
# squares_list = [number ** 2 for number in numbers]
# squares_set = {number ** 2 for number in numbers}
# print(squares_list)
# print(sorted(squares_set))
# print(len(squares_set))
# print(numbers)
# ANSWER:


# Exercise 6 — Write your own unique artist summary
# 1. Create an artist set literal containing at least five strings, with
#    at least two repeated entries and at least three distinct artist names.
# 2. Print the set's type and its number of unique artists.
# 3. Check whether a chosen artist is present using in.
# 4. Loop directly over the set and print each artist.
# 5. Print a sorted list of the artists for a predictable alphabetical display.
# 6. Explain why the direct loop's order is not guaranteed and why sorted()
#    does not turn your original set into a list.
# Write your code below:


# Optional challenge — Unique positive squares
# Work through this one together when you are ready.
# Define unique_positive_squares(numbers) for a list of integers.
# Return a NEW SET of squares of only the positive input numbers.
# Use a set comprehension with a condition. Leave numbers unchanged.
# Return an empty set if the input is empty or no positive numbers qualify.
# unique_positive_squares([-3, 0, 2, 2, 3]) => {4, 9} (order unspecified)
# unique_positive_squares([-2, 0]) => set()
# unique_positive_squares([]) => set()
# Explain why repeated positive inputs contribute only one copy of a square.
# Write your code below:
