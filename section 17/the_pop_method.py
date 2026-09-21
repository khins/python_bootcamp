# Dictionary pop — Study Summary
# Instructor summary:
# - dictionary.pop(key) removes a key-value pair and returns its VALUE.
# - A dictionary requires a key for pop(); a list can use pop() with no argument.
# - List pop uses an index; dictionary pop uses a key.
# - A missing key raises KeyError unless you supply a default return value.
# - dictionary.pop(key, default) returns the default if the key is missing.
# - That fallback is not inserted into the dictionary.
# - An existing key is removed even when you supply a default.
# - del dictionary[key] removes an entry without returning its value.
# - del also raises KeyError for a missing key.
#
# Remember: removing an entry changes the dictionary itself.


# --- 1. Review: pop() on a list ---
years = [1991, 1995, 2000, 2007]
last_year = years.pop()
print(last_year)  # 2007
print(years)      # [1991, 1995, 2000]

# Reset the list so this example starts with the original four elements.
years = [1991, 1995, 2000, 2007]
removed_year = years.pop(1)
print(removed_year)  # 1995 — the element at index 1
print(years)         # [1991, 2000, 2007]


# --- 2. Remove a dictionary entry and keep its value ---
release_dates = {"Python": 1991, "Ruby": 1995, "Java": 1995}
year = release_dates.pop("Java")
print(year)                  # 1995 — returns the value, not the key
print(release_dates)         # {'Python': 1991, 'Ruby': 1995}
print("Java" in release_dates)  # False
print(len(release_dates))    # 2
# The entire "Java": 1995 entry is removed.
# Ruby stays: sharing the same value does not make it the same key.

# Dictionary pop requires a key. Leave this intentional error commented out:
# release_dates.pop()  # TypeError — unlike list.pop(), a key is required


# --- 3. A missing key raises KeyError ---
# Java was already removed. Removing it again would fail:
# release_dates.pop("Java")  # KeyError — leave commented out

selected_language = "Rust"
if selected_language in release_dates:
    print(release_dates.pop(selected_language))
else:
    print("Language not listed")
# Expected: Language not listed
# Membership checks keys, so the pop call runs only if this key exists.


# --- 4. Supply a fallback for a missing key ---
year = release_dates.pop("Rust", "Not listed")
print(year)                         # Not listed
print("Rust" in release_dates)       # False
print(release_dates)                 # {'Python': 1991, 'Ruby': 1995}
# The fallback avoids KeyError; it does not create an entry.

# When the key exists, pop removes it and returns its actual value.
year = release_dates.pop("Ruby", "Not listed")
print(year)                         # 1995
print(release_dates)                 # {'Python': 1991}


# --- 5. A stored None is still a value ---
profile = {"nickname": None}
print(profile.pop("nickname", "Guest"))  # None — the key exists
print(profile)                           # {} — the entry was removed
print(profile.pop("nickname", "Guest"))  # Guest — now the key is missing

# Unlike get(), pop() does not automatically default to None.
# Pass None explicitly when you want it as the fallback:
print(profile.pop("city", None))  # None — no KeyError and no insertion


# --- 6. del removes an entry without returning a value ---
song_artists = {"Tom Sawyer": "Rush", "Longer": "Dan Fogelberg"}
del song_artists["Longer"]
print(song_artists)  # {'Tom Sawyer': 'Rush'}

# del is a statement, not a method that returns the removed value.
# Use it when you simply want to delete an entry.
# Use pop when you want the removed value or a fallback for a missing key.
# This missing-key deletion would raise KeyError; leave it commented out:
# del song_artists["Longer"]

# Compare with earlier lessons:
# data.get(key, default)        -> reads a value or fallback; no change
# data.setdefault(key, default) -> reads an existing value or adds a missing entry
# data.pop(key, default)        -> removes an existing entry or returns fallback
# del data[key]                -> removes an existing entry; no returned value
# None of these fallback arguments replaces an existing value.


# --- 7. Practice: predict, explain, then run ---
# Write predictions beside each print before uncommenting that exercise.
# Track both the returned value and the entries left in the dictionary.
# Keep intentional-error lines commented out when running the file.

# Exercise 1 — Remove and return
# Predict all four outputs. Does pop return the key or its value?
menu = {"tea": 3, "cake": 5, "coffee": 4}
removed_price = menu.pop("cake")
print(removed_price) # 5
print(menu)          # {"tea": 3, "coffee": 4}
print("cake" in menu) # False
print(len(menu))      # 2
# Explanation:
#   pop returns the value

# Exercise 2 — A missing key with a fallback
# Predict all three outputs. Is "juice" added to menu?
menu = {"tea": 3}
print(menu.pop("juice", "Not available")) # "Not available"
print(menu) # {"tea": 3}
print("juice" in menu) # False
# What would menu.pop("juice") do without the fallback?
#   without default it would be a KeyError
# Explanation:
#   juice is not added to menu the pop just returned the fallback value

# Exercise 3 — An existing value wins
# Predict all four outputs. Explain why the two pop calls return different values.
scores = {"Kevin": 7, "Alex": 10}
print(scores.pop("Kevin", 0)) # 7
print(scores) #"{Alex": 10}
print(scores.pop("Kevin", 0)) # 0
print(scores) # {Alex": 10}
# Explanation:
#   the first is the existing key value and the second is the default fallback value


# Exercise 4 — None and key existence
# Predict all five outputs. Does None stop the first call from removing the key?
profile = {"nickname": None}
print(profile.pop("nickname", "Guest")) # None
print("nickname" in profile) # False
print(profile.pop("nickname", "Guest")) # Guest
print(profile.pop("city", None)) # None
print(profile) # {}
# Explanation:
#   No


# Exercise 5 — Keys, indexes, and del
# Predict all four outputs. What does 1 mean in each pop call?
numbers = [10, 20, 30]
labels = {1: "one", 2: "two", 3: "three"}
print(numbers.pop(1)) # 20
print(labels.pop(1)) # one
del labels[2] # three
print(numbers) # [10, 30]
print(labels) # {3: "three"}
# del labels[2]  # Intentional error: leave commented out.
# Explain why repeating the deletion would raise KeyError:


# Exercise 6 — Write your own removals
# 1. Create song_artists with three song titles mapped to their artists.
# 2. Store one existing song TITLE in selected_song.
# 3. Use selected_song as the key in pop(), saving the return value in removed_artist.
# 4. Print removed_artist, the remaining dictionary, and its length.
# 5. Try popping the same song again with "Song not listed" as the fallback.
#    Print the result and explain why the fallback is returned this time.
# 6. Use del to remove another existing song, then print the final dictionary.
# Explain why neither the removed entries nor the fallback remain in the dictionary.
# Write your code below:
song_artists = {}
song_artists["Comfortably Numb"] = "Pink Floyd"
song_artists["Wish You Were Here"] = "Pink Floyd"
song_artists["Another Brick in the Wall"] = "Pink Floyd"
song_artists["Echoes"] = "Pink Floyd"
selected_song = "Wish You Were Here"
removed_artist = song_artists.pop(selected_song)
print(removed_artist) # Key Error
print(song_artists)
print(len(song_artists))

print(song_artists.pop(selected_song, "Song not listed"))
del song_artists["Another Brick in the Wall"]
print(song_artists)


# Optional challenge — Move a song between dictionaries
# Work through this one together when you are ready.
# Start with:
playlist = {"Tom Sawyer": "Rush", "Longer": "Dan Fogelberg"}
played = {}
selected_song = "Tom Sawyer"
# If selected_song exists in playlist, remove it with pop() and store its
# returned artist in played under that same song title.
# Otherwise, print "Song not in playlist".
# Predict both dictionaries after moving the song.
# Then try the same selection again. Which branch runs, and why?
# Hint: connect a membership check, pop's return value, and bracket assignment.
if selected_song in playlist:
    artist = playlist.pop(selected_song)
    played[selected_song] = artist
else:
    print("Song not in playlist")

# Declare a delete_keys function that accepts two arguments:
# a dictionary and a list of strings.
# For each string in the list, if the string exists as a dictionary key,
# delete the key-value pair from the dictionary.
#
# If the string does not exist as a dictionary key, avoid an error.
# The return value should be the modified dictionary object.
#
# EXAMPLE:
my_dict = {
    "A": 1,
    "B": 2,
    "C": 3
}

strings = ["A", "C"]

def delete_keys(my_dict, strings):
    for key in strings:
        del my_dict[key]
    return my_dict

print(delete_keys(my_dict, strings))  # => {'B': 2}