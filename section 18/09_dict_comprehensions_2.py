# Dictionary comprehensions from dictionaries — Study Summary
# Instructor summary:
# - Use source.items() to iterate over an existing dictionary's key-value pairs.
# - Unpack each pair into two descriptive variables in the comprehension.
# - The expressions before for determine the NEW dictionary's keys and values.
# - Inversion swaps roles: original values become keys, and original keys become values.
# - Pattern: {value: key for key, value in source.items()}
# - Add an if condition at the end to include only matching source entries.
# - These comprehensions create a new dictionary without changing the source.
# - Inversion preserves every association only when the original values are
#   distinct and hashable, so they can serve as separate dictionary keys.
# - Repeated output keys keep the last value supplied for that key.
# - Empty input or a filter with no matches produces {}.


# --- 1. Start with a dictionary of states and capitals ---
capitals = {
    "New York": "Albany",
    "California": "Sacramento",
    "Texas": "Austin",
}
print(capitals["Texas"])  # Austin
# Original direction: state -> capital.
# The following examples build a reverse lookup: capital -> state.


# --- 2. Invert using a regular loop ---
inverted_by_loop = {}
for state, capital in capitals.items():
    inverted_by_loop[capital] = state
print(inverted_by_loop)
# Expected: {'Albany': 'New York', 'Sacramento': 'California', 'Austin': 'Texas'}
# On the first iteration, state is 'New York' and capital is 'Albany'.
# The assignment makes 'Albany' the new key and 'New York' its value.


# --- 3. Invert using a dictionary comprehension ---
inverted = {capital: state for state, capital in capitals.items()}
print(inverted)
# Expected: {'Albany': 'New York', 'Sacramento': 'California', 'Austin': 'Texas'}
print(inverted["Austin"])  # Texas
print(capitals)
# Expected: {'New York': 'Albany', 'California': 'Sacramento', 'Texas': 'Austin'}
print(inverted is capitals)  # False — these are separate dictionaries
# for state, capital ... -> receive the original key and value, in that order
# capital: state         -> choose the new key and value, in that order
# Changing variable names alone does not reverse a mapping; the output
# expressions determine which object becomes the key.


# --- 4. Filter the original pairs before creating entries ---
filtered_inverted = {
    capital: state
    for state, capital in capitals.items()
    if len(state) != len(capital)
}
print(filtered_inverted)  # {'Albany': 'New York', 'Austin': 'Texas'}
# New York: 8 characters (including its space); Albany: 6 -> included
# California: 10; Sacramento: 10 -> excluded
# Texas: 5; Austin: 6 -> included
# Excluding an entry from the result does not delete it from capitals.
print(len(capitals))           # 3
print(len(filtered_inverted))  # 2


# --- 5. Repeated values become conflicting keys ---
song_artists = {"YYZ": "Rush", "Roundabout": "Yes", "Limelight": "Rush"}
artist_song = {artist: title for title, artist in song_artists.items()}
print(artist_song)       # {'Rush': 'Limelight', 'Yes': 'Roundabout'}
print(len(artist_song))  # 2
# Rush is produced twice as a key. The later title, Limelight, replaces YYZ.
# This does not preserve a list of all songs by each artist.
# The source still contains all three songs:
print(len(song_artists))  # 3
# Replacing Rush's value does not move its original insertion position.


# --- 6. Values must be valid keys before you invert ---
# A dictionary value can be a list, but a dictionary key cannot be a list.
teams = {"support": ["Mary", "Brian"]}
# Leave this intentional error commented out:
# inverted_teams = {members: team for team, members in teams.items()}
# TypeError — the new key would be an unhashable list.
# String values in the capitals example are valid dictionary keys.

# A comprehension can also keep keys and transform values instead of inverting:
menu = {"tea": 3, "cake": 5}
raised_prices = {item: price + 1 for item, price in menu.items()}
print(raised_prices)  # {'tea': 4, 'cake': 6}
print(menu)           # {'tea': 3, 'cake': 5}

empty = {}
print({value: key for key, value in empty.items()})  # {}


# --- 7. Practice: predict, explain, then run ---
# Write predictions in the ANSWER comments before uncommenting each exercise.
# Identify the original key/value and the new key/value separately.
# Keep intentional-error examples commented out.

# Exercise 1 — Reverse the mapping
# Predict both outputs. What becomes the key in reversed_codes?
# codes = {"Illinois": "IL", "Texas": "TX", "Ohio": "OH"}
# reversed_codes = {code: state for state, code in codes.items()}
# print(reversed_codes)
# print(reversed_codes["IL"])
# ANSWER:


# Exercise 2 — Filter while inverting
# Predict both outputs. Explain which pair is excluded and why.
# words = {"cat": "feline", "dog": "pup", "bird": "avian"}
# selected = {
#     description: animal
#     for animal, description in words.items()
#     if len(animal) != len(description)
# }
# print(selected)
# print(words)
# ANSWER:


# Exercise 3 — Duplicate output keys
# Predict both outputs. Why does one original name disappear from the result?
# scores = {"Kevin": 10, "Alex": 8, "Sam": 10}
# names_by_score = {score: name for name, score in scores.items()}
# print(names_by_score)
# print(len(names_by_score))
# ANSWER:


# Exercise 4 — Names vs. positions
# Predict both outputs. Does the second comprehension actually invert codes?
# codes = {"Illinois": "IL", "Texas": "TX"}
# first = {value: key for key, value in codes.items()}
# second = {value: key for value, key in codes.items()}
# print(first)
# print(second)
# Explain what value and key receive in the SECOND comprehension.
# ANSWER:


# Exercise 5 — Diagnose an invalid inversion
# Identify the error and explain why it occurs, even though the source
# dictionary itself is valid. Is the problem with the new keys or values?
# albums = {"Rush": ["Moving Pictures", "Permanent Waves"]}
# inverted = {titles: artist for artist, titles in albums.items()}
# ANSWER:


# Exercise 6 — Build your own reverse lookup
# 1. Create a dictionary named song_codes containing three song titles as keys
#    and three DISTINCT string codes as values, such as "YYZ": "R01".
# 2. Use a dictionary comprehension to create titles_by_code.
# 3. Print the new dictionary and use one code to look up its title.
# 4. Create a second inverted dictionary including only titles longer than
#    five characters. Use a trailing if condition in the comprehension.
# 5. Print the filtered result and the original song_codes dictionary.
# 6. Explain why your codes must be distinct to preserve all three associations.
# Write your code below:


# Optional challenge — Reverse only qualifying entries
# Work through this one together when you are ready.
# Define invert_long_values(data, minimum).
# Assume data maps strings to DISTINCT string values, and minimum is nonnegative.
# Return a NEW inverted dictionary containing only entries whose ORIGINAL
# values have lengths greater than or equal to minimum.
# Use a dictionary comprehension with items() and an if condition.
# Leave data unchanged.
# invert_long_values({"a": "Rush", "b": "Yes", "c": "Genesis"}, 4)
# => {'Rush': 'a', 'Genesis': 'c'}
# invert_long_values({"a": "Rush"}, 10) => {}
# invert_long_values({}, 0) => {}
# Explain whether your filter checks the original keys or the original values.
# Write your code below:
