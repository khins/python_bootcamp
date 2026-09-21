# Adding or Modifying Dictionary Entries — Study Summary
# Instructor summary:
# - Dictionaries are mutable: their contents can change after creation.
# - Use dictionary[key] = value to add or replace an entry.
# - If the key is missing, assignment adds the key and its value.
# - If the key exists, assignment replaces its value.
# - Reading a missing key with dictionary[key] raises KeyError.
# - {} and dict() each create a new empty dictionary.
# - String keys are case-sensitive: "volume" and "Volume" are different.
# - A key can come from a variable, including a for-loop variable.
# - Combine membership checks and assignment to count repeated words.
#
# Precision note: keys must be hashable, not simply immutable.
# Assignment replaces the VALUE associated with a key, not the key itself.


# --- 1. Add a new key-value pair ---
# Historical lesson examples; these lists are not current team rosters.
sports_team_rosters = {
    "New England Patriots": ["Tom Brady", "Rob Gronkowski", "Julian Edelman"],
    "New York Giants": ["Eli Manning", "Odell Beckham"],
}

# Reading a missing key would raise KeyError. Leave this commented out:
# print(sports_team_rosters["Pittsburgh Steelers"])

# Assigning to that missing key adds an entry instead.
sports_team_rosters["Pittsburgh Steelers"] = ["Ben Roethlisberger", "Antonio Brown"]
print(sports_team_rosters["Pittsburgh Steelers"])
# Expected: ['Ben Roethlisberger', 'Antonio Brown']
print(len(sports_team_rosters))  # 3 — one new key was added


# --- 2. Replace the value for an existing key ---
sports_team_rosters["New York Giants"] = ["Eli Manning"]
print(sports_team_rosters["New York Giants"])  # ['Eli Manning']
print(len(sports_team_rosters))  # 3 — replacing a value adds no new key
# This assignment replaces the entire list associated with this key.
# It does not append a player to the old list.


# --- 3. Build a dictionary from scratch ---
video_game_options = {}
# Alternative: video_game_options = dict()
# Both forms create an empty dictionary; separate calls create separate objects.

video_game_options["subtitles"] = True
video_game_options["difficulty"] = "medium"
video_game_options["volume"] = 7
print(video_game_options)
# Expected: {'subtitles': True, 'difficulty': 'medium', 'volume': 7}
# Values can have different types: boolean, string, integer, list, etc.


# --- 4. Modify settings and watch case sensitivity ---
video_game_options["difficulty"] = "hard"
video_game_options["subtitles"] = False
print(video_game_options)
# Expected: {'subtitles': False, 'difficulty': 'hard', 'volume': 7}

video_game_options["Volume"] = 10
print(video_game_options["volume"])  # 7
print(video_game_options["Volume"])  # 10
print(len(video_game_options))      # 4 — "Volume" is a new key
# Capitalization changes which key you target.


# --- 5. Use a variable as the key ---
selected_option = "volume"
video_game_options[selected_option] = 9
print(video_game_options["volume"])  # 9
# selected_option holds the KEY to update, not its current value.
# Without quotes, Python uses the value stored in selected_option.
# video_game_options["selected_option"] would target a different, literal key.

# Compare with the previous lesson:
# selected_option in video_game_options -> checks whether the key exists
# video_game_options[selected_option] -> retrieves its value
# video_game_options[selected_option] = 9 -> assigns its value


# --- 6. Count words using dynamic keys ---
def count_words(words):
    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
            # Same as: counts[word] = counts[word] + 1
        else:
            counts[word] = 1

    return counts
    # Return after the loop so every word is processed.


words = ["danger", "beware", "danger"]
print(count_words(words))  # {'danger': 2, 'beware': 1}
print(count_words([]))     # {} — no words means no entries

# Trace the first call:
# Start:             {}
# First "danger":    {'danger': 1}                -> else: add a key
# First "beware":    {'danger': 1, 'beware': 1}   -> else: add a key
# Second "danger":   {'danger': 2, 'beware': 1}   -> if: update a value
# counts[word] += 1 reads the old value before assigning the new one.
# That is why a new word needs an initial count before it can be incremented.


# --- 7. Practice: predict, explain, then run ---
# Write predictions beside each print before uncommenting that exercise.
# For each assignment, identify whether it adds a key or replaces a value.
# Leave lines marked as intentional errors commented out when running the file.
print("1" * 60)
# Exercise 1 — Add vs. replace
# Predict all three outputs and explain each assignment.
menu = {"tea": 3, "cake": 5}
menu["coffee"] = 4
menu["tea"] = 6
print(menu)     # {'tea': 6, 'cake': 5, 'coffee': 4}
print(len(menu)) # 3
print(menu["tea"]) # 6

print("2" * 60)
# Exercise 2 — Reading vs. assigning
# Explain why the first operation would fail but the assignment works.
scores = {}
# print(scores["Kevin"])  # Intentional error: leave commented out.
scores["Kevin"] = 10
print(scores["Kevin"]) # 10
print("Kevin" in scores) # True

print("3" * 60)
# Exercise 3 — Case-sensitive keys
# Predict all four outputs. Did the second assignment replace the first value?
settings = {"volume": 5}
settings["Volume"] = 8
print(settings["volume"]) # 5
print(settings["Volume"]) # 8
print(len(settings)) # 2 
print("VOLUME" in settings) # False

print("4" * 60)
# Exercise 4 — A variable vs. a literal key
# Predict the final dictionary. Explain which key each assignment targets.
song_artists = {"Tom Sawyer": "Rush"}
selected_song = "Tom Sawyer"
song_artists[selected_song] = "Rush (live)"
song_artists[selected_song] = "Unknown"
print(song_artists)
# Explain why selected_song = song_artists["Tom Sawyer"] would instead
# store an artist value, making it unsuitable for targeting the song title.
#   perhaps because storing the artist value would suggest it is on a live cut album v.s. studio 

print("5" * 60)
# Exercise 5 — Trace the word counter
# Predict both outputs, then trace counts after each word in the first call.
print(count_words(["rock", "jazz", "rock", "rock", "jazz"])) # {'rock': 3, 'jazz': 2}
print(count_words([])) # {}
# Explain when the if branch runs and when the else branch runs.
#   the if branch checks for word in the counts else it adds to counts dict
# Why can't we use counts[word] += 1 for a word that has no entry yet?
#   because no words can be added to count dict


# Exercise 6 — Write your own assignments
# 1. Create an empty dictionary named song_artists.
# 2. Add three song titles as keys, with their artists as values,
#    using three separate bracket assignments.
# 3. Store one existing song TITLE in a variable named selected_song.
# 4. Use that variable as the key to replace its artist with a new value.
# 5. Add a fourth song, then print the dictionary and its length.
# 6. Explain why step 4 keeps the number of keys the same but step 5 adds one.
# Write your code below:
song_artists = {}
song_artists["Leader of the Band"] = "Dan Fogelberg"
song_artists["Longer"] = "Dan Fogelberg"
song_artists["Same Old Lang Syne"] = "Dan Fogelberg"
selected_song = "Same Old Lang Syne"
song_artists["selected_song"] = "Run for the roses"
song_artists["Heart Hotel"] = "Dan Fogelberg (live)"
print(song_artists)
print(len(song_artists))

# Optional challenge — Count words regardless of capitalization
# Work through this one together when you are ready.
# Write a function named count_words_ignore_case(words).
# Treat "Rock", "rock", and "ROCK" as the same word.
# Hint: use word.lower() to obtain a lowercase string before using it as a key.
# Try ["Rock", "jazz", "ROCK", "Jazz", "rock"], then an empty list.
# Predict each result before running your function.
def count_words_ignore_case(words):
    counts = {}

    for word in words:
        word = word.lower()
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


print(count_words_ignore_case(["Rock", "jazz", "ROCK", "Jazz", "rock"]))
# {'rock': 3, 'jazz': 2}

print(count_words_ignore_case([]))
# {}

