# Dictionary clear — Study Summary
# Instructor summary:
# - dictionary.clear() removes ALL key-value pairs from a dictionary.
# - Call clear() with no arguments.
# - The same dictionary object remains, but it is empty: {}.
# - Its length becomes 0, and membership checks for former keys return False.
# - clear() changes the dictionary in place and returns None.
# - You can add new entries after clearing the dictionary.
# - del dictionary[key] removes one entry; del dictionary removes the variable name.
# - Reading a deleted variable name raises NameError unless it is defined again.
#
# Precision note: del removes a name binding; it does not necessarily destroy
# the object. Another variable may still refer to that same dictionary.


# --- 1. Review: clear() on a list ---
years = [1991, 1995, 2000, 2007]
years.clear()
print(years)       # []
print(len(years))  # 0
# The list still exists; all its elements have been removed.


# --- 2. Clear every entry from a dictionary ---
websites = {
    "Wikipedia": "https://www.wikipedia.org",
    "Google": "https://www.google.com",
    "Netflix": "https://www.netflix.com",
}
print(len(websites))  # 3

websites.clear()
print(websites)                 # {}
print(len(websites))            # 0
print("Wikipedia" in websites)  # False
# These URL strings are example values; the code does not visit the websites.
# The variable websites still refers to a dictionary, now with no entries.


# --- 3. clear() returns None, not the emptied dictionary ---
scores = {"Kevin": 7, "Alex": 10}
result = scores.clear()
print(result)  # None
print(scores)  # {}

# Avoid scores = scores.clear(): that would clear the dictionary and then
# assign None to scores. Call scores.clear() on its own to keep using the name
# for the dictionary.


# --- 4. Reuse an empty dictionary ---
websites["Wikipedia"] = "https://www.wikipedia.org"
print(websites)       # {'Wikipedia': 'https://www.wikipedia.org'}
print(len(websites))  # 1

websites.clear()
websites.clear()  # Clearing an already empty dictionary is fine.
print(websites)   # {}
# No KeyError: clear() does not look up an individual key.


# --- 5. Remove an entry vs. remove the variable name ---
song_artists = {"Tom Sawyer": "Rush", "Longer": "Dan Fogelberg"}
del song_artists["Longer"]
print(song_artists)  # {'Tom Sawyer': 'Rush'}

song_artists.clear()
print(song_artists)  # {} — the variable is still defined

del song_artists
# The following would raise NameError. Leave it commented out:
# print(song_artists)

# A deleted name can be assigned again.
song_artists = {"Echoes": "Pink Floyd"}
print(song_artists)  # {'Echoes': 'Pink Floyd'}

# Compare with the previous lesson:
# data.pop(key) -> removes one entry and returns its value
# del data[key] -> removes one entry without returning its value
# data.clear()  -> removes all entries and returns None; data stays defined
# del data     -> removes the name data; it does not clear the dictionary


# --- 6. Two names can refer to the same dictionary ---
playlist = {"Tom Sawyer": "Rush"}
shared_playlist = playlist
# This assignment does not copy the dictionary. Both names refer to one object.

playlist.clear()
print(playlist)         # {}
print(shared_playlist)  # {} — the same dictionary was cleared

shared_playlist["Longer"] = "Dan Fogelberg"
del playlist
print(shared_playlist)  # {'Longer': 'Dan Fogelberg'}
# Removing one name does not remove another name or empty their shared object.


# --- 7. Practice: predict, explain, then run ---
# Write predictions beside each print before uncommenting that exercise.
# Track the dictionary contents, return values, and whether names still exist.
# Keep intentional-error lines commented out when running the file.

# Exercise 1 — Clear all entries
# Predict all four outputs. Is menu still defined after clear()?
menu = {"tea": 3, "cake": 5, "coffee": 4}
print(len(menu)) # 3
menu.clear() 
print(menu) # {}
print(len(menu)) # 0 
print("tea" in menu) # False
# Explanation:


# Exercise 2 — The return value
# Predict both outputs. Which variable holds None, and which holds a dictionary?
scores = {"Kevin": 7}
result = scores.clear()
print(result) # None
print(scores) # {}
# Explain why scores = scores.clear() would be a mistake if you wanted
# to keep using scores as a dictionary:
#   because it returns None 


# Exercise 3 — Reuse after clearing
# Predict all three outputs. Explain why adding "volume" still works.
settings = {"volume": 5, "subtitles": True}
settings.clear()
settings["volume"] = 8
print(settings) # {"volume": 8}
print(len(settings)) # 1
print("subtitles" in settings) # False
# Explanation:
#   because volume is added back after the clear function call


# Exercise 4 — Clear an empty dictionary
# Predict all three outputs. Does the second clear() raise an error?
profile = {"nickname": None}
profile.clear()
print(profile.clear()) # None
print(profile) # {}
print("nickname" in profile) # False
# Explanation:
#   no error raised by the second clear


# Exercise 5 — del vs. clear
# Predict both printed dictionaries and identify the error in the final line.
songs = {"Tom Sawyer": "Rush", "Longer": "Dan Fogelberg"}
del songs["Longer"]
print(songs) # {"Tom Sawyer": "Rush"}
songs.clear()
print(songs) # {}
del songs
# print(songs)  # Intentional error: leave commented out.
# Explain how the three operations affect entries and the variable name:
#   


# Exercise 6 — Write your own reset
# 1. Create song_artists with three song titles mapped to their artists.
# 2. Use pop() to remove one existing song and save its artist in removed_artist.
# 3. Print removed_artist and the remaining dictionary.
# 4. Clear all remaining entries using clear().
# 5. Print the empty dictionary and its length.
# 6. Add a new song using bracket assignment, then print the dictionary.
# Explain why clear() does not prevent step 6 from working.
# Write your code below:
song_artists = {}
song_artists["Roundabout"] = "Yes"
song_artists["Tom Sawyer"] = "Rush"
song_artists["Hotel California"] = "Eagles"
removed_artist = song_artists.pop("Roundabout")
print(removed_artist)
song_artists.clear()
print(song_artists)
print(len(song_artists))
song_artists["Echoes"] = "Pink Floyd"
print(song_artists)


# Optional challenge — Clearing vs. assigning a new dictionary
# Work through this one together when you are ready.
# Predict both outputs in each case before uncommenting.
# Case A:
# playlist = {"Tom Sawyer": "Rush"}
# shared_playlist = playlist
# playlist.clear()
# print(playlist)
# print(shared_playlist)
#
# Case B (start fresh):
# playlist = {"Tom Sawyer": "Rush"}
# shared_playlist = playlist
# playlist = {}
# print(playlist)
# print(shared_playlist)
# Does assigning a new dictionary to playlist change the original dictionary
# that shared_playlist still refers to? Explain how this differs from clear().
