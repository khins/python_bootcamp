# Dictionary Membership Operators — Study Summary
# Instructor summary:
# - in and not in test membership and return True or False.
# - In a string, they check for a substring.
# - In a list, they check for an element.
# - In a dictionary, they check for a KEY, not a value or a nested item.
# - String keys are case-sensitive: "Fire" and "fire" are different.
# - not in gives the opposite result of in for the same membership check.
# - Use a membership check in an if statement before looking up a key
#   when you want separate behavior for an existing or missing key.
#
# Precision note: dictionary keys must be hashable, not simply immutable.
# Strings and integers work; lists and tuples containing lists do not.


# --- 1. Review: membership in strings ---
print("erm" in "watermelon")    # True — a matching substring
print("Z" in "watermelon")      # False
print("Z" not in "watermelon")  # True


# --- 2. Review: membership in lists ---
numbers = [10, 20, 25]
print(10 in numbers)      # True
print(30 in numbers)      # False
print(30 not in numbers)  # True


# --- 3. Dictionary membership searches keys ---
# Each category key maps to a list of Pokemon names.
pokemon = {
    "Fire": ["Charmander", "Charmeleon", "Charizard"],
    "Water": ["Squirtle", "Wartortle", "Blastoise"],
    "Grass": ["Bulbasaur", "Venusaur", "Ivysaur"],
}
print("Fire" in pokemon)      # True
print("Grass" in pokemon)     # True
print("Electric" in pokemon)  # False
print("fire" in pokemon)      # False — lowercase f does not match Fire

# The dictionary check does not search inside its list values.
print("Charmander" in pokemon)          # False — not a key
print("Charmander" in pokemon["Fire"])  # True — searches the retrieved list
# First retrieve the Fire list; then test membership in that list.


# --- 4. not in checks whether a key is absent ---
print("Electric" not in pokemon)  # True
print("fire" not in pokemon)      # True — this lowercase key is absent
print("Zombie" not in pokemon)    # True
print("Water" not in pokemon)     # False — Water IS a key

# Read the whole statement aloud:
# "Water is not a key in pokemon" is a false statement.


# --- 5. Check a key before accessing its value ---
# This lookup would raise KeyError, so leave it commented out:
# print(pokemon["Zombie"])

category = "Zombie"
if category in pokemon:
    print(pokemon[category])
else:
    print(f"The category {category} does not exist.")
# Expected: The category Zombie does not exist.
# The bracket lookup runs only when the membership check returns True.

category = "Water"
if category in pokemon:
    print(pokemon[category])
else:
    print(f"The category {category} does not exist.")
# Expected: ['Squirtle', 'Wartortle', 'Blastoise']

# Compare with your previous lesson:
# category in pokemon -> returns a boolean about whether the key exists
# pokemon[category]   -> returns the value, or raises KeyError if missing
# pokemon.get(category) -> returns the value, or None if missing


# --- 6. Membership also works with integer keys ---
packages = {29: "basic", 49: "standard", 79: "premium"}
print(49 in packages)         # True
print("49" in packages)       # False — a string differs from an integer
print("standard" in packages) # False — a value, not a key


# --- 7. Practice: predict, explain, then run ---
# Write predictions beside each print before uncommenting the exercise.
# Identify what is being searched: a string, a list, or dictionary keys.
print("1" * 60)
# Exercise 1 — Review strings and lists
# Predict all four outputs. Explain how string and list membership differ.
print("tar" in "guitar")                        # True
print("guitar" in ["guitar", "bass", "drums"])  # True
print("tar" in ["guitar", "bass", "drums"])     # False
print("piano" not in ["guitar", "bass", "drums"]) # True

print("2" * 60)
# Exercise 2 — Keys, not values
# Predict all four outputs. Why does the second check differ from the first?
instruments = {"Alex": "guitar", "Geddy": "bass", "Neil": "drums"}
print("Alex" in instruments)    # True
print("guitar" in instruments)  # False
print("Neil" not in instruments) # False
print("Peter" not in instruments) # True

# Exercise 3 — Case and key types
# Predict all four outputs and explain the mismatches.
entries = {"Fire": "category", 49: "membership"}
print("Fire" in entries) # True
print("fire" in entries) # False
print(49 in entries)     # True
print("49" not in entries) #False

print("4" * 60)
# Exercise 4 — Dictionary vs. its nested list
# Predict all four outputs. What does bands["Rush"] return?
bands = {"Rush": ["Alex", "Geddy", "Neil"]}
print("Rush" in bands) # True
print("Alex" in bands) # False
print("Alex" in bands["Rush"]) # True
print("Peter" not in bands["Rush"]) # True

# Exercise 5 — Trace an if/else
# Predict the printed message. Does the bracket lookup run?
menu = {"tea": 3, "cake": 5}
selected_item = "tea" # changing to tea from coffee
if selected_item in menu:
    print(menu[selected_item]) 
else:
    print("Item not listed")
# Then change selected_item to "tea" and predict the new output.
# new output is 3

# Exercise 6 — Write your own membership checks
# 1. Create a dictionary mapping three song titles to their artists.
# 2. Use in to check an existing title and a missing title.
# 3. Use not in to check a missing title.
# 4. Store a song title in a variable named selected_song.
# 5. Write an if/else: if the key exists, print its artist; otherwise,
#    print "Song not listed".
# 6. Try an existing title and a missing title. Explain which branch runs.
# 7. Explain why checking an artist's name with in does not search the values.
# 1
songs_titles = {
    "Tom Sawyer": "Rush",
    "Hotel California": "Eagles",
    "Owner of a Lonely Heart": "Yes",
}
# 2
print("Hotel California" in songs_titles)
print("Heat Hotel" in songs_titles)
# 3
print("You shook me all night long" not in songs_titles)
#4 
selected_song = songs_titles["Tom Sawyer"] # Rush
# 5
if selected_song in menu:
    print(menu[selected_song]) 
else:
    print("Song not listed")

# 6
# if an existing tile is found in the if then it returns that value otherwise the default

# 7
#   with a dictionary the key is used to search and it returns the value 

# Optional challenge — A present key whose value is None
# Predict all three outputs. Does a None value mean the key is missing?
profile = {"nickname": None}
print("nickname" in profile) # Yes—the key exists! But "nickname" in profile returns True, not None.
print("city" in profile) # Correct! "city" isn’t a key in profile, so it returns False.
print("nickname" not in profile) # Correct! "nickname" exists, so saying it is not in profile is False.
# Explain how a membership check differs from profile.get("nickname").
#   The key distinction: in checks whether a key exists; .get() retrieves its value. A value of None doesn’t mean the key is missing.