# Dictionary setdefault — Study Summary
# Instructor summary:
# - dictionary.setdefault(key, default) checks whether a key exists.
# - If the key exists, it returns the existing value without replacing it.
# - If the key is missing, it adds the key with the default and returns it.
# - If you omit the default, a missing key is added with the value None.
# - get() can return a fallback, but it does not add an entry.
# - Bracket assignment can replace an existing value; setdefault() does not.
# - A key with a value of None still exists, so setdefault() leaves it alone.
#
# Read the name as: "Set a default value only if this key is missing."


# --- 1. Review: get() returns a value without adding an entry ---
film_directors = {
    "The Godfather": "Francis Ford Coppola",
    "The Rock": "Michael Bay",
    "Goodfellas": "Martin Scorsese",
}

print(film_directors.get("Goodfellas"))             # Martin Scorsese
print(film_directors.get("Bad Boys"))               # None
print(film_directors.get("Bad Boys", "Michael Bay")) # Michael Bay
print("Bad Boys" in film_directors)                 # False
print(len(film_directors))                          # 3
# Returning a fallback is not the same as storing it in the dictionary.


# --- 2. setdefault() adds a missing key and returns its value ---
director = film_directors.setdefault("Bad Boys", "Michael Bay")
print(director)                       # Michael Bay
print(film_directors["Bad Boys"])     # Michael Bay
print("Bad Boys" in film_directors)   # True
print(len(film_directors))            # 4
# The method both adds this missing entry and returns the stored value.


# --- 3. An existing key keeps its current value ---
director = film_directors.setdefault("Bad Boys", "Another director")
print(director)                    # Michael Bay
print(film_directors["Bad Boys"])  # Michael Bay
print(len(film_directors))         # 4 — no extra entry was added
# "Another director" is only a proposed default for a missing key.
# Since "Bad Boys" already exists, its original value wins.


# --- 4. Omitting the default inserts None for a missing key ---
watchlist = {}
print(watchlist.setdefault("Next movie"))  # None
print(watchlist)                           # {'Next movie': None}
print("Next movie" in watchlist)           # True

print(watchlist.setdefault("Next movie", "The Godfather"))  # None
print(watchlist)                           # {'Next movie': None}
# None is a value, not evidence that the key is missing.
# The second call returns the existing None and leaves the entry unchanged.


# --- 5. Use assignment when you want to replace a value ---
watchlist["Next movie"] = "The Godfather"
print(watchlist)  # {'Next movie': 'The Godfather'}

# Compare these operations:
# data.get(key, default)        -> returns existing value or fallback; no insert
# data.setdefault(key, default) -> returns existing value or inserts/returns default
# data[key] = value             -> adds a missing key or replaces an existing value
# key in data                  -> returns True or False about key existence


# --- 6. The key can come from a variable ---
song_artists = {"Tom Sawyer": "Rush"}
selected_song = "Longer"
artist = song_artists.setdefault(selected_song, "Dan Fogelberg")
print(artist)                  # Dan Fogelberg
print(song_artists)
# Expected: {'Tom Sawyer': 'Rush', 'Longer': 'Dan Fogelberg'}
# selected_song supplies the key "Longer".
# "selected_song" in quotes would be a different, literal key.

# For this example, the same missing-key behavior can be written explicitly:
selected_song = "Tom Sawyer"
if selected_song not in song_artists:
    song_artists[selected_song] = "Unknown"
print(song_artists[selected_song])  # Rush — its existing value was preserved


# --- 7. Practice: predict, explain, then run ---
# Write predictions beside each print before uncommenting the exercise.
# Track both the returned value and any change to the dictionary.
print("1" * 60)
# Exercise 1 — get() does not insert
# Predict all three outputs. Does returning 4 add "coffee" to menu?
menu = {"tea": 3}
print(menu.get("coffee", 4)) # 4
print(menu)                  # {"tea": 3}
print("coffee" in menu)      # False
# Explanation:
#   no returning 4 does not add to the dict it is merely using fallback value

print("2" * 60)
# Exercise 2 — Add a missing key
# Predict all four outputs. What does result store?
menu = {"tea": 3}
result = menu.setdefault("coffee", 4)
print(result)           # 4
print(menu)             # {"tea": 3, "coffee": 4}
print("coffee" in menu) # True
print(len(menu))        # 2
# Explanation:
#   result stores the value of the new dict insert of coffee

print("3" * 60)
# Exercise 3 — Preserve an existing value
# Predict all three outputs. Why doesn't the value become 10?
scores = {"Kevin": 7}
print(scores.setdefault("Kevin", 10)) # 7
print(scores["Kevin"])                # 7
print(len(scores))                    # 1
# Explanation:
#   since the key already has a value the default will be ignored

print("4" * 60)
# Exercise 4 — A present key with None
# Predict all five outputs. Explain why the second call doesn't store "Kev".
profile = {}
print(profile.setdefault("nickname"))       # None
print("nickname" in profile)                # True
print(profile.setdefault("nickname", "Kev"))  # None  
print(profile.get("nickname", "Guest"))       # None
print(profile)
# Explanation:
#   no new value is stored because value is already present

print("5" * 60)
# Exercise 5 — setdefault() vs. assignment
# Predict all four outputs and track the stored volume after each operation.
settings = {"volume": 5}
print(settings.setdefault("volume", 8))     # 5
settings["volume"] = 8
print(settings.setdefault("volume", 10))    # 8
print(settings.setdefault("Volume", 3))     # 3
print(settings)                             # {'volume': 8, 'Volume': 3}
# Explain why "Volume" and "volume" produce separate entries:
#   because they are different keys due to case sensitivity

print("6" * 60)
# Exercise 6 — Write your own defaults
# 1. Create song_artists with "Tom Sawyer" mapped to "Rush".
# 2. Store "Longer" in a variable named selected_song.
# 3. Use that variable with setdefault() to add "Dan Fogelberg" as its artist.
#    Store the method's return value in artist, then print artist.
# 4. Call setdefault() for "Tom Sawyer" with the default "Unknown".
#    Print the return value and explain why the artist stays the same.
# 5. Use bracket assignment to change the value for "Tom Sawyer" to "Rush (live)".
# 6. Print the final dictionary and its length. Explain which steps added keys.
# Write your code below:
song_artists = {"Tom Sawyer": "Rush"}
selected_song = "Longer"
song_artists.setdefault(selected_song, "Dan Fogelberg")
print(song_artists)
print(song_artists.setdefault("Tom Sawyer", "Unknown")) 
song_artists["Tom Sawyer"] = "Rush (live)"
print(song_artists)
print(len(song_artists))

# Optional challenge — Use setdefault() in a word counter
# Work through this one together when you are ready.
# Write count_words_with_defaults(words), starting with an empty counts dictionary.
# For each word:
# 1. Use setdefault() to give an unseen word an initial count of 0.
# 2. Increase that word's stored count by 1 using bracket access and +=.
# Return counts after the loop. You do not need an if/else here.
# Predict the results for ["rock", "jazz", "rock"] and for [].
# Explain why the default should be 0 rather than 1 when you increment afterward.
#   Correct! More precisely, it keeps 1 because the key already exists. Then counts[word] += 1 raises the count to 2.
def count_words_with_defaults(words):
    counts = {}

    for word in words:
        counts.setdefault(word, 0)
        counts[word] += 1

    return counts

print(count_words_with_defaults(["rock", "jazz", "rock"]))
print(count_words_with_defaults([]))