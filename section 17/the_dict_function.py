# The dict function — Study Summary
# Instructor summary:
# - dict() creates a new dictionary; with no arguments, it creates {}.
# - {} is the usual, shorter way to write an empty dictionary.
# - dict() can build a dictionary from a sequence of key-value pairs.
# - Each pair must contain exactly two elements: the key, then its value.
# - The pairs can be lists or tuples.
# - Repeated keys receive the last value supplied for that key.
# - Creating a dictionary from a list of pairs does not change that list.
# - Keys must be hashable: strings and numbers work; lists do not.


# --- 1. Review: functions that create or convert objects ---
print(list("ABC"))  # ['A', 'B', 'C']
print(str(9))       # 9 — the returned value is the string "9"
print(type(str(9)))  # <class 'str'>
# print() displays a string without surrounding quotation marks.


# --- 2. Create an empty dictionary ---
employees = dict()
print(employees)        # {}
print(len(employees))  # 0
print(type(employees))  # <class 'dict'>

# The dictionary literal produces an empty dictionary too.
employees = {}
print(employees)  # {}
# Use {} for a simple empty dictionary; use dict() when conversion is useful.


# --- 3. Convert a list of lists into a dictionary ---
employee_titles = [
    ["Mary", "Senior Manager"],
    ["Brian", "Vice President"],
    ["Julie", "Assistant Vice President"],
]
titles = dict(employee_titles)
print(titles)
# Expected: {'Mary': 'Senior Manager', 'Brian': 'Vice President', 'Julie': 'Assistant Vice President'}
print(titles["Mary"])  # Senior Manager
print(len(titles))     # 3
# In each inner list, the first element becomes a key.
# The second element becomes that key's value.

print(employee_titles)
# Expected: [['Mary', 'Senior Manager'], ['Brian', 'Vice President'], ['Julie', 'Assistant Vice President']]
# dict() returns a new dictionary; the original list stays a list.


# --- 4. Tuples can supply the pairs too ---
menu_pairs = [("tea", 3), ("cake", 5)]
menu = dict(menu_pairs)
print(menu)         # {'tea': 3, 'cake': 5}
print(menu["tea"])  # 3
# Both ["tea", 3] and ("tea", 3) can supply one key-value pair.
# The values keep their types: the prices here are integers.


# --- 5. Repeated keys use the last supplied value ---
score_pairs = [["Kevin", 7], ["Alex", 10], ["Kevin", 12]]
scores = dict(score_pairs)
print(scores)       # {'Kevin': 12, 'Alex': 10}
print(len(scores))  # 2
# Three input pairs produce two keys because "Kevin" appears twice.
# Like update(), a later value replaces an earlier value for the same key.


# --- 6. Each pair needs exactly two elements and a valid key ---
# Leave these intentional errors commented out:
# dict([["Mary"]])                    # ValueError — only one element in the pair
# dict([["Mary", "Manager", 2026]])   # ValueError — three elements in the pair
# dict([[["Mary"], "Manager"]])       # TypeError — a list cannot be a key

# A list CAN be a value. The key here is a string:
teams = dict([["support", ["Mary", "Brian"]]])
print(teams)  # {'support': ['Mary', 'Brian']}
# The outer pair has two elements, even though its value contains another list.

# Compare with the previous lesson:
# dict(pairs)         -> creates and returns a new dictionary from pairs
# target.update(data) -> changes an existing dictionary and returns None


# --- 7. Practice: predict, explain, then run ---
# Write predictions beside each print before uncommenting that exercise.
# Include the requested explanations. Keep intentional-error lines commented.

# Exercise 1 — Empty dictionary
# Predict all three outputs. How else could you create this empty dictionary?
settings = dict()
print(settings) # {}
print(len(settings)) # 0
print(type(settings)) #<class 'dict'>
# Explanation:
#   settings = {}


# Exercise 2 — Lists of pairs
# Predict all three outputs. Identify the key and value in each inner list.
menu_pairs = [["tea", 3], ["cake", 5], ["coffee", 4]]
menu = dict(menu_pairs)
print(menu) # {'tea': 3, 'cake': 5, 'coffee': 4}
print(menu["cake"]) # 5
print(len(menu)) # 3
# Explanation:
#   tea 3, cake 5, coffee 4


# Exercise 3 — The original input
# Predict all three outputs. Does creating titles change employee_pairs?
employee_pairs = [["Mary", "Manager"], ["Brian", "Developer"]]
titles = dict(employee_pairs)
print(titles) # { "Mary": "Manager", "Brian": "Developer" }
print(employee_pairs) # [["Mary", "Manager"], ["Brian", "Developer"]]
print(type(employee_pairs)) # <class 'dict'>
# Explanation:
#   employee_pairs does not change by creating a new dict


# Exercise 4 — Repeated keys
# Predict all three outputs. Why does the number of keys differ from the
# number of input pairs?
pairs = [("volume", 5), ("subtitles", True), ("volume", 9)]
settings = dict(pairs)
print(settings) # { "volume": 9, "subtitles": True }
print(len(settings)) # 2
print(settings["volume"]) # 9
# Explanation:
#   because volume 9 wins due to the duplicate keys


# Exercise 5 — Valid and invalid pairs
# Decide whether each call works or raises an error. For valid calls,
# predict the dictionary. For invalid calls, explain what is wrong.
# Uncomment only the valid calls when running the whole file.
print(dict([["nickname", None]])) # {'nickname': None}
# print(dict([["tea", 3, 4]])) # Invalid
# print(dict([["tea"]])) # ValueError
# print(dict([[["tea"], 3]])) # TypeError
print(dict([["artists", ["Rush", "Yes"]]])) # {'artists': ['Rush', 'Yes']}
# Explanation:


# Exercise 6 — Build your own song dictionary
# 1. Create song_pairs as a list containing three inner lists.
#    Each inner list should contain a song title and its artist.
# 2. Use dict(song_pairs) to create song_artists.
# 3. Print song_artists and its length.
# 4. Use a song title as a key to print one artist.
# 5. Print song_pairs to show that the input remains a list of lists.
# 6. Explain which part of each pair becomes the key and which becomes the value.
# Write your code below:
song_pairs = [
    ["Go Your Own Way", "Fleetwood Mac"],
    ["Dreams", "Fleetwood Mac"],
    ["The Chain", "Fleetwood Mac"],
]
song_artists = dict(song_pairs)
print(song_artists)
print(len(song_artists))
print(song_pairs)
print(song_artists["Go Your Own Way"]) # Fleetwood Mac



# Optional challenge — Create, then update
# Work through this one together when you are ready.
# Start with:
default_pairs = [["volume", 5], ["subtitles", True], ["difficulty", "medium"]]
preferences = {"volume": 9, "difficulty": "hard"}
final_settings = dict(default_pairs)
final_settings.update(preferences)
print(final_settings)

# Create final_settings from default_pairs using dict().
# Then apply preferences using update().
# Predict and print final_settings, default_pairs, and preferences.
# Explain why subtitles remains and why the two sources stay unchanged.
# Which call returns a dictionary, and which call returns None?
