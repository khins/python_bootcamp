# The set function — Study Summary
# Instructor summary:
# - set() creates an empty set; {} creates an empty dictionary.
# - set(iterable) creates a new set from the elements supplied by an iterable.
# - Lists, tuples, strings, and dictionaries are common iterable inputs.
# - The elements supplied must be hashable; duplicate elements appear once.
# - A string supplies individual characters, including spaces and punctuation.
# - A dictionary supplies its keys unless you explicitly choose another view.
# - list(set(values)) creates a list of unique elements without preserving
#   the input's order. It does not modify the original list.
# - sorted(set(values)) creates a sorted list of unique comparable elements.
#
# Corrections to the transcript:
# - set() is the standard way to create an empty set, but not the only way:
#   set([]), for example, also produces an empty set.
# - Converting a string produces a SET of characters, not a tuple.
# - Set order is unspecified, not a promise of random ordering.
# - Reassigning a variable to list(set(...)) binds it to a new list; it does
#   not change the old list that another variable might still reference.
# - An iterable input alone is not enough: its elements must be hashable.


# --- 1. Create an empty set ---
empty = set()
print(empty)        # set()
print(type(empty))  # <class 'set'>
print(len(empty))   # 0
print(type({}))     # <class 'dict'>
print(set([]))      # set()
# No input, or an empty iterable, produces an empty set.


# --- 2. Convert lists and tuples ---
numbers = [1, 2, 3, 3, 2, 1]
unique_numbers = set(numbers)
print(sorted(unique_numbers))  # [1, 2, 3]
print(len(unique_numbers))     # 3
print(numbers)                # [1, 2, 3, 3, 2, 1]
# The new set does not remove entries from the original list.

coordinates = (1, 2, 1, 2)
print(sorted(set(coordinates)))  # [1, 2]
# set(coordinates) consumes the tuple's elements; it does not store the
# entire tuple as one element. To do that, use {coordinates}:
print(len({coordinates}))        # 1
print(coordinates in {coordinates})  # True


# --- 3. Convert strings into unique characters ---
print(sorted(set("abc")))     # ['a', 'b', 'c']
print(sorted(set("aabbcc")))  # ['a', 'b', 'c']
print(sorted(set("Aa a")))    # [' ', 'A', 'a']
# Uppercase and lowercase characters differ. Spaces are elements too.
print(set(""))               # set()

word = "banana"
print(sorted(set(word)))      # ['a', 'b', 'n']
print(sorted({word}))         # ['banana']
# set(word) iterates over characters; {word} stores the whole string.


# --- 4. Choose which dictionary elements to convert ---
song_artists = {"YYZ": "Rush", "Limelight": "Rush", "Roundabout": "Yes"}
print(sorted(set(song_artists)))           # ['Limelight', 'Roundabout', 'YYZ']
print(sorted(set(song_artists.keys())))    # ['Limelight', 'Roundabout', 'YYZ']
print(sorted(set(song_artists.values())))  # ['Rush', 'Yes']
print(len(song_artists))                   # 3 — original entries unchanged
# Direct dictionary iteration yields keys, which are already unique.
# values() can contain duplicates, so converting it can reduce the count.

pairs = set(song_artists.items())
print(sorted(pairs))
# Expected: [('Limelight', 'Rush'), ('Roundabout', 'Yes'), ('YYZ', 'Rush')]
# These (key, value) tuples are hashable because both parts are strings.
# An items() view with list values would not work as input to set().


# --- 5. Remove duplicates without changing the source ---
philosophers = ["Plato", "Socrates", "Aristotle", "Pythagoras", "Socrates", "Plato"]
philosopher_set = set(philosophers)
unique_philosophers = list(philosopher_set)
print(len(philosophers))         # 6
print(len(unique_philosophers))  # 4
print(unique_philosophers)
# Contains Plato, Socrates, Aristotle, and Pythagoras once each.
# Do not predict or depend on the list order produced from a set.
print(philosophers)
# Expected: ['Plato', 'Socrates', 'Aristotle', 'Pythagoras', 'Socrates', 'Plato']

# The same conversion can be written in one expression:
unique_philosophers = list(set(philosophers))
# For a predictable alphabetical result, use sorted() instead of list():
print(sorted(set(philosophers)))
# Expected: ['Aristotle', 'Plato', 'Pythagoras', 'Socrates']
# Alphabetical order is not the original insertion order.


# --- 6. Reassignment and invalid inputs ---
names = ["Rush", "Yes", "Rush"]
original_reference = names
names = list(set(names))
print(sorted(names))             # ['Rush', 'Yes']
print(original_reference)        # ['Rush', 'Yes', 'Rush']
print(names is original_reference)  # False
# The name now refers to a new list; the original list still exists.

# Leave these intentional errors commented out:
# set(123)          # TypeError: an integer is not iterable
# set([[1], [2]])   # TypeError: list elements are unhashable
# set((1, [2]))     # TypeError: one supplied element is an unhashable list
# set(1, 2, 3)      # TypeError: pass one iterable, not separate elements
# A list of hashable tuples is valid:
print(sorted(set([(1, 2), (1, 2), (3, 4)])))  # [(1, 2), (3, 4)]


# --- 7. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# For raw sets or lists made directly from sets, describe contents without
# claiming a guaranteed order. For sorted() output, give the exact list.
# Keep intentional-error examples commented out.

# Exercise 1 — Empty and duplicate inputs
# Predict all four outputs. Explain why the duplicate numbers count once.
# print(set())
# print(type({}))
# print(sorted(set([4, 2, 4, 1, 2])))
# print(len(set((7, 7, 7))))
# ANSWER:


# Exercise 2 — Characters or a whole string?
# Predict all three outputs. Explain how set(word) differs from {word}.
# word = "level"
# print(sorted(set(word)))
# print(len(set(word)))
# print(sorted({word}))
# ANSWER:


# Exercise 3 — Keys or values?
# Predict all three outputs. Explain why the first two lengths differ.
# songs = {"YYZ": "Rush", "Limelight": "Rush", "Roundabout": "Yes"}
# print(len(set(songs)))
# print(len(set(songs.values())))
# print(sorted(set(songs.values())))
# ANSWER:


# Exercise 4 — A new list
# Predict all four outputs. Explain whether source changes and whether
# unique itself is guaranteed to preserve the original order.
# source = [3, 1, 3, 2, 1]
# unique = list(set(source))
# print(sorted(unique))
# print(source)
# print(unique is source)
# print(type(unique))
# ANSWER:


# Exercise 5 — Diagnose the conversion
# Each line below is independent. State which succeeds and give its set
# contents; for each failing line, name the error and explain its cause.
# A. set(42)
# B. set([[1, 2], [1, 2]])
# C. set([(1, 2), (1, 2)])
# Keep the failing calls commented out.
# ANSWER A:
# ANSWER B:
# ANSWER C:


# Exercise 6 — Write your own unique artist report
# 1. Create a list containing at least five artist names with duplicates
#    and at least three distinct names.
# 2. Use set() to create a separate collection of unique artists.
# 3. Print the original list's length and the set's length.
# 4. Convert the set to a list and print it, then print a sorted version.
# 5. Print the original list to show its contents and order are unchanged.
# 6. Explain why list() alone does not remove duplicates, and why converting
#    a set back to a list does not restore the original order.
# Write your code below:


# Optional challenge — Unique artists from song entries
# Work through this one together when you are ready.
# Define unique_artists(song_artists), accepting a dictionary mapping song
# title strings to artist strings. Return a NEW alphabetically sorted LIST
# of distinct artists. Use values(), set(), and sorted().
# Leave the dictionary unchanged. Matching is case-sensitive.
# Return [] for an empty dictionary.
# unique_artists({"YYZ": "Rush", "Roundabout": "Yes", "Limelight": "Rush"})
# => ['Rush', 'Yes']
# unique_artists({"Track A": "rush", "Track B": "Rush"}) => ['Rush', 'rush']
# unique_artists({}) => []
# Explain the type of result produced by each step of your expression.
# Write your code below:
