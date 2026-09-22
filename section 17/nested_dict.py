# Nested dictionaries — Study Summary
# Instructor summary:
# - A dictionary value can be another dictionary, a list, or another object.
# - Nested structures can model relationships such as shows -> seasons -> episodes.
# - Read chained square brackets from left to right, one level at a time.
# - For a dictionary, use a key; for a list or string, use an index.
# - List indexes start at 0, so the second item has index 1.
# - Each lookup returns an object that determines what the next lookup needs.
# - len() and membership checks apply only to the object you give them.
# - Indentation and trailing commas make nested data easier to read and edit.


# --- 1. Build a nested structure ---
# These are lesson sample details with fictional episode titles and simplified genres.
tv_shows = {
    "The X-Files": {
        "Season 1": {
            "episodes": ["Scary Monster", "Scary Alien"],
            "genre": "Science Fiction",
            "year": 1993,
        },
        "Season 2": {
            "episodes": ["Scary Conspiracy"],
            "genre": "Horror",
            "year": 1994,
        },
    },
    "Lost": {
        "Season 1": {
            "episodes": ["What the heck is happening on this island?"],
            "genre": "Science Fiction",
            "year": 2004,
        },
    },
}
# Each opening brace has a matching closing brace.
# Commas separate entries at each dictionary level.
# A comma after the final entry is allowed and useful when adding entries later.
# Editor folding can hide or reveal a block without deleting its contents.


# --- 2. Navigate one level at a time ---
x_files = tv_shows["The X-Files"]
print(type(x_files))  # <class 'dict'>
print(len(x_files))   # 2 — two seasons

season_one = x_files["Season 1"]
print(season_one)
# Expected: {'episodes': ['Scary Monster', 'Scary Alien'], 'genre': 'Science Fiction', 'year': 1993}

episodes = season_one["episodes"]
print(episodes)        # ['Scary Monster', 'Scary Alien']
print(type(episodes))  # <class 'list'>
print(episodes[1])     # Scary Alien
# The first three lookups used dictionary keys; the final lookup used a list index.


# --- 3. Chain the same lookups in one expression ---
print(tv_shows["The X-Files"]["Season 1"]["episodes"][1])  # Scary Alien
# tv_shows                 -> dictionary of shows
# ["The X-Files"]          -> dictionary of seasons
# ["Season 1"]             -> dictionary of season details
# ["episodes"]             -> list of episode titles
# [1]                      -> second title, a string

print(tv_shows["The X-Files"]["Season 2"]["year"])  # 1994
print(tv_shows["Lost"]["Season 1"]["genre"])       # Science Fiction
# Stop indexing when you have reached the value you want.


# --- 4. Count and check keys at the correct level ---
print(len(tv_shows))                                   # 2 — shows
print(len(tv_shows["The X-Files"]))                    # 2 — seasons
print(len(tv_shows["The X-Files"]["Season 1"]))        # 3 — detail keys
print(len(tv_shows["The X-Files"]["Season 1"]["episodes"]))  # 2 — episodes

print("year" in tv_shows)                              # False
print("year" in tv_shows["Lost"]["Season 1"])         # True
# Dictionary membership checks keys at the current level, not inside every value.


# --- 5. Match the lookup to the object ---
# Leave these intentional errors commented out:
# print(tv_shows["Season 1"])                 # KeyError — not a top-level key
# print(tv_shows["Lost"]["Season 2"])         # KeyError — this season is absent
# print(tv_shows["Lost"]["Season 1"]["episodes"][1])  # IndexError — only index 0 exists
# print(tv_shows["Lost"]["Season 1"]["episodes"]["year"])  # TypeError — a list needs an integer index here
# These dictionaries use string keys. An integer lookup would be a dictionary
# key lookup, not a request for the first or second dictionary entry.

# A string can also be indexed after you reach it:
print(tv_shows["The X-Files"]["Season 1"]["episodes"][1][0])  # S
# [1] selects the second episode title; [0] selects its first character.


# --- 6. Another valid design: a list of season dictionaries ---
# Choose structures to suit the data and how you want to access it.
seasons = [
    {"year": 1993, "episodes": ["Scary Monster", "Scary Alien"]},
    {"year": 1994, "episodes": ["Scary Conspiracy"]},
]
print(seasons[1]["year"])  # 1994
# Here seasons is a list, so [1] selects the second season.
# That item is a dictionary, so ["year"] selects its year.


# --- 7. Practice: predict, explain, then run ---
# Use tv_shows from section 1 for exercises 1–5.
# Write predictions beside each print before uncommenting that exercise.
# Keep intentional-error lines commented out.

# Exercise 1 — Follow the keys
# Predict all three outputs. Explain what each key selects.
print(tv_shows["The X-Files"]["Season 1"]["year"]) # 1993
print(tv_shows["The X-Files"]["Season 2"]["genre"]) # Horror
print(tv_shows["Lost"]["Season 1"]["year"]) # 2004
# Explanation:
#   each key selects the element within a nested structure 


# Exercise 2 — Dictionary keys, then a list index
# Predict both outputs. Why does the second episode use index 1?
print(tv_shows["The X-Files"]["Season 1"]["episodes"][0]) # Scary Monster
print(tv_shows["The X-Files"]["Season 1"]["episodes"][1]) # Scary Alien
# Explanation:
#   because the episodes are a list and thus are 0 based index, so item 
#   2 in the list is really a [1] index


# Exercise 3 — Know the current type
# Predict all four outputs.
print(type(tv_shows["Lost"])) # <class 'dict'>
print(type(tv_shows["Lost"]["Season 1"])) # <class 'dict'>
print(type(tv_shows["Lost"]["Season 1"]["episodes"])) # <class 'list'>
print(type(tv_shows["Lost"]["Season 1"]["episodes"][0])) # <class 'str'>
# Explain why the last lookup uses an index instead of a dictionary key:
#   because it is a list and is 0 based index


# Exercise 4 — Count and search at one level
# Predict all four outputs. Explain why the two membership checks differ.
print(len(tv_shows["Lost"])) # 1
print(len(tv_shows["Lost"]["Season 1"])) # 3
print("episodes" in tv_shows["Lost"]) # False
print("episodes" in tv_shows["Lost"]["Season 1"]) # True
# Explanation:


# Exercise 5 — Diagnose the path
# Identify the error each line would raise and explain why.
# Then write a corrected expression for each requested value.
# Leave the failing lines commented out.
# A. Get Lost's season-one year:
# print(tv_shows["Lost"]["year"]) # KeyError
# B. Get Lost's first episode title:
# print(tv_shows["Lost"]["Season 1"]["episodes"][1]) # IndexError
# C. Get The X-Files season-one first episode title:
# print(tv_shows["The X-Files"]["Season 1"]["episodes"]["first"]) #TypeError
# Explanations and corrected code:
print(tv_shows["Lost"]["Season 1"]["year"])
print(tv_shows["Lost"]["Season 1"]["episodes"][0]) 
print(tv_shows["The X-Files"]["Season 1"]["episodes"][1])

# Exercise 6 — Build your own music library
# 1. Create music_library with two artist-name keys.
# 2. Each artist's value should be a dictionary with one album-title key.
# 3. Each album's value should be a dictionary containing "year" and "songs".
#    Use an integer year and a list of at least two song titles.
#    You may use fictional sample data.
# 4. Print one album's year using chained dictionary lookups.
# 5. Print the second song from that album using a final list index.
# 6. Print the number of artists and the number of songs on that album.
# Explain which brackets use dictionary keys and which use a list index.
# Write your code below:
music_library = {
    "Tom Petty and the Heartbreakers": {
        "Tom Petty and the Heartbreakers": {
            "year": 1976,
            "songs": ["Breakdown", "American Girl"],
        }
    },
    "Tom Petty": {
        "Full Moon Fever": {
            "year": 1989,
            "songs": ["Free Fallin'", "I Won't Back Down"],
        }
    },
}

print(music_library["Tom Petty"]["Full Moon Fever"]["year"])
print(len(music_library["Tom Petty"]["Full Moon Fever"]["songs"]))
print(len(music_library))
#   songs uses a list index because songs are stored as a list



# Optional challenge — Update one nested dictionary
# Work through this one together when you are ready.
# Start with this independent sample:
library = {
    "Sample Artist": {
        "First Album": {
            "year": 2000,
            "songs": ["Opening Track", "Closing Track"],
        },
    },
}
changes = {"year": 2001, "genre": "Rock"}
library["Sample Artist"]["First Album"].update(changes)
print(len(library["Sample Artist"]["First Album"]))
# Use update() on the dictionary belonging to "First Album" to apply changes.
# Predict and print that album's dictionary and its number of keys.
# Print changes to show that it remains unchanged.
# Explain which value was replaced, which key was added, and why songs remains.
# Hint: first navigate to the dictionary you want to change.
#   Add a comment explaining that year was replaced, genre was added, and songs remains because no replacement was supplied.
