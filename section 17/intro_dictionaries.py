# Introduction to Dictionaries — Study Summary
# Instructor summary:
# - A dictionary is a mutable collection of key-value pairs.
# - Each key identifies an associated value, like a menu item and its price.
# - Keys are unique; different keys can have equal values.
# - Values can be any Python object, including lists and other dictionaries.
# - Use curly braces, a colon between each key and value, and commas
#   between pairs: {key: value, key: value}.
# - len(dictionary) counts pairs, not individual keys plus individual values.
# - Dictionaries organize mappings; lists organize sequences of items.
#
# Updates to the instructor's wording:
# - Dictionaries preserve insertion order in Python 3.7 and later.
#   They are not automatically sorted, and lookup uses keys, not positions.
# - Keys must be HASHABLE, not simply "immutable."
#   Strings and integers work. Lists and dictionaries do not.
#   A tuple works only if all its elements are also hashable.


# --- 1. Creating an empty dictionary ---
ice_cream_preferences = {}
print(type(ice_cream_preferences))  # <class 'dict'>
print(len(ice_cream_preferences))  # 0


# --- 2. Connecting keys with values ---
# Put one pair per line for readability.
# A trailing comma after the final pair is optional and convenient for edits.
ice_cream_preferences = {
    "Benjamin": "chocolate",
    "Sandy": "vanilla",
    "Marv": "cookies and cream",
    "Julia": "chocolate",
}

# In "Benjamin": "chocolate":
# - "Benjamin" is the key (the identifier).
# - "chocolate" is the value associated with that key.
# Benjamin and Julia have equal values, which is allowed.
print(len(ice_cream_preferences))  # 4 — four pairs, not eight strings


# --- 3. A first look at lookup by key ---
# Supply the key inside square brackets to retrieve its value.
print(ice_cream_preferences["Sandy"])  # vanilla
# This looks up the key "Sandy", not a numeric position.
# A key that is absent raises KeyError; we will study lookup options later.


# --- 4. Keys are unique; values can repeat ---
menu = {
    "water": 3,
    "tea": 3,
    "sandwich": 8,
}
print(len(menu))  # 3 — duplicate values do not remove entries

# Repeating a key in a literal keeps the last value for that key.
# This is a demonstration; avoid accidental duplicate keys in your own code.
preferences = {
    "Julia": "chocolate",
    "Julia": "strawberry",
}
print(preferences)       # {'Julia': 'strawberry'}
print(len(preferences))  # 1


# --- 5. Values can have different types ---
musician = {
    "name": "Alex",
    "instrument": "guitar",
    "years_playing": 10,
    "active": True,
    "favorite_songs": ["Limelight", "Tom Sawyer"],
}
print(len(musician))                # 5
print(musician["favorite_songs"])  # ['Limelight', 'Tom Sawyer']
# The entire list is ONE value in ONE key-value pair.


# --- 6. Valid keys ---
# Strings, integers, and tuples of hashable elements can be keys.
examples = {
    "name": "Kevin",
    7: "an integer key",
    (2, 3): "a tuple key",
}
print(examples[7])       # an integer key — 7 is a key, not position 7
print(examples[(2, 3)])  # a tuple key

# These would raise TypeError, so leave them commented out:
# invalid = {[1, 2]: "a list cannot be a key"}
# invalid = {("name", [1, 2]): "this tuple contains an unhashable list"}


# --- 7. Dictionaries are mutable and preserve insertion order ---
prices = {
    "tea": 3,
    "sandwich": 8,
}
prices["tea"] = 4      # Update the value for an existing key.
prices["cake"] = 5     # Add a new key-value pair at the end.
print(prices)          # {'tea': 4, 'sandwich': 8, 'cake': 5}
print(len(prices))     # 3
# Updating an existing key does not move it or add another entry.
# Insertion order is preserved; keys are not automatically sorted.


# --- 8. Practice: predict, explain, then run ---
# Uncomment one exercise at a time after writing your predictions.
# Keep your explanations as comments so this file remains valid Python.

# Exercise 1 — Identify keys and values
# List the keys and their corresponding values. Predict the output.
flavors = {
    "Alex": "vanilla",
    "Geddy": "chocolate",
    "Neil": "vanilla",
}
print(len(flavors)) # 3
# Explain why repeated "vanilla" values do not reduce the length.
#     because they have different keys values duplicated don't matter

# Exercise 2 — Count pairs, not objects inside values
# Predict both outputs. How many pairs does the dictionary contain?
profile = {
    "name": "Kevin",
    "hobbies": ["guitar", "programming", "woodworking"],
    "learning_python": True,
}
print(len(profile))  # 3
print(profile["hobbies"])  # ["guitar", "programming", "woodworking"]

# Exercise 3 — A repeated key
# Predict both outputs. Which value remains associated with "tea"?
drinks = {
    "tea": 3,
    "coffee": 4,
    "tea": 5,
}
print(len(drinks)) # 3
print(drinks["tea"])  # 5

# Exercise 4 — Choose valid keys
# For each candidate, say whether it can be a dictionary key and why:
# A. "guitar"  "invalid"
# B. 42         "valid"
# C. ("Alex", "Geddy") "valid" A tuple can be a dictionary key if every element inside it is hashable.
# D. ["Alex", "Geddy"] "Invalid" Lists are mutable and not hashable.
# E. ("band", ["Alex", "Geddy"]) # Invalid because the tuple contains an unhashable list. Being inside a tuple doesn’t make that list hashable.
# Can the invalid key candidates still be used as VALUES?
#    Yes because Dictionary values can be any Python object—they don’t need to be hashable.

print("5" * 60)
# Exercise 5 — Update vs. add
# Predict both outputs. Which assignment adds a pair?
menu = {"tea": 3, "cake": 5}
menu["tea"] = 4
menu["water"] = 2
print(len(menu))  # 3
print(menu)  # {'tea': 4, 'cake': 5, 'water': 2}
# Explain why updating "tea" does not create a second "tea" entry.
#   because "tea" already exists, assigning to it replaces its value instead of adding another entry.

# Exercise 6 — Write your own dictionary
# 1. Create a dictionary mapping three musicians' names to their instruments.
# 2. Give at least two musicians the same instrument value.
# 3. Print the dictionary's length and look up one musician's instrument.
# 4. Update one musician's instrument, then add a fourth musician.
# 5. Print the dictionary and its length again.
# 6. Explain which items are keys, which are values, and why values may repeat.
print("6" * 60)
musicians = {
    "Neil Peart": "Drums",
    "Jon Anderson": "Lead Vocals",
    "Peter Gabriel": "Lead Vocals",
}
print(len(musicians)) # 3
print(musicians["Neil Peart"]) # Drums
musicians["Peter Gabriel"] = "tambourine"
musicians["Bob Dylan"] = "guitar"
print(len(musicians)) # 4
print(musicians)
# the musicians names are the keys in this case and the values can repeat because the keys are unique


# Optional challenge — Dictionary or list?
# Choose a structure and explain your choice for each goal:
# A. Look up an instrument using a musician's name.
#     Correct—a dictionary fits. Each musician’s name is a unique key that lets you look up the associated instrument:
# B. Store a playlist where the same song may appear more than once.
#     List Correct! A list allows repeated songs and keeps them in playback order:
# C. Look up a menu item's price using its name.
#    Dictionary Correct! A dictionary maps each unique menu item name to its price:


# Create an empty dictionary and assign it to the variable empty.
empty = {}


# Create a dictionary with three key-value pairs.
# The keys should be strings and the values should be integer values.
# Assign the dictionary to a my_dict variable.
my_dict = {"water": 1,
            "soda": 2,
           "juice": 3}


# A dictionary's keys can be any immutable data structure.
# Create a dictionary with two key-value pairs and assign it to
# a winning_lottery_numbers variable.
# Both of the keys should be tuples.
# One of the values should be True, the other value should be False.
winning_lottery_numbers = {(1, 5, 9): True
                           , (17, 19, 3): False}