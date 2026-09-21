# Dictionary update — Study Summary
# Instructor summary:
# - target.update(source) merges source entries into target.
# - Missing keys are added to target.
# - Existing keys receive the values from source: the incoming value wins.
# - Keys found only in target remain unchanged.
# - The method changes target in place and returns None.
# - When target and source are separate dictionaries, this call does not
#   change the entries in source.
# - Direction matters: a.update(b) and b.update(a) can give different results.
# - Updating an existing key does not create a duplicate key.
#
# Read target.update(source) as: "Update target using the entries in source."


# --- 1. Merge new entries and replace matching values ---
# These salaries are example data from the lesson.
employee_salaries = {
    "Guido": 100_000,
    "James": 500_000,
    "Brandon": 900_000,
}
extra_employee_salaries = {
    "Yukihiro": 1_000_000,
    "Guido": 333_333,
}

employee_salaries.update(extra_employee_salaries)
print(employee_salaries)
# Expected: {'Guido': 333333, 'James': 500000, 'Brandon': 900000, 'Yukihiro': 1000000}
print(len(employee_salaries))  # 4 — Guido remains one key
# Guido: already existed, so its value was replaced.
# Yukihiro: missing from the target, so a new entry was added.
# James and Brandon: absent from the source, so their values stayed the same.


# --- 2. The source dictionary keeps its entries ---
print(extra_employee_salaries)
# Expected: {'Yukihiro': 1000000, 'Guido': 333333}
print(len(extra_employee_salaries))  # 2
# update() does not remove entries from the source or move them out of it.


# --- 3. Reverse direction using fresh starting data ---
# Reset both dictionaries: the earlier example already changed employee_salaries.
employee_salaries = {
    "Guido": 100_000,
    "James": 500_000,
    "Brandon": 900_000,
}
extra_employee_salaries = {
    "Yukihiro": 1_000_000,
    "Guido": 333_333,
}

extra_employee_salaries.update(employee_salaries)
print(extra_employee_salaries)
# Expected: {'Yukihiro': 1000000, 'Guido': 100000, 'James': 500000, 'Brandon': 900000}
print(employee_salaries["Guido"])        # 100000 — source unchanged
print(extra_employee_salaries["Guido"])  # 100000 — incoming value wins
# The object before .update() is the target being changed.
# The argument inside the parentheses supplies the incoming entries.


# --- 4. update() returns None ---
settings = {"volume": 5, "subtitles": True}
changes = {"volume": 8, "difficulty": "hard"}
result = settings.update(changes)
print(result)    # None
print(settings)  # {'volume': 8, 'subtitles': True, 'difficulty': 'hard'}
# Avoid settings = settings.update(changes): it would assign None to settings.
# Call settings.update(changes) on its own to keep settings as the dictionary.


# --- 5. Empty sources and case-sensitive keys ---
menu = {"tea": 3}
menu.update({})
print(menu)  # {'tea': 3} — an empty source supplies no changes

menu.update({"Tea": 4})
print(menu)       # {'tea': 3, 'Tea': 4}
print(len(menu))  # 2 — capitalization makes these different keys

new_menu = {}
new_menu.update(menu)
print(new_menu)  # {'tea': 3, 'Tea': 4} — an empty target can receive entries


# --- 6. Compare update() with setdefault() and assignment ---
song_artists = {"Tom Sawyer": "Rush"}
print(song_artists.setdefault("Tom Sawyer", "Unknown"))  # Rush
# setdefault() preserves the value for an existing key.

song_artists.update({"Tom Sawyer": "Rush (live)", "Longer": "Dan Fogelberg"})
print(song_artists)
# Expected: {'Tom Sawyer': 'Rush (live)', 'Longer': 'Dan Fogelberg'}
# update() replaces existing values and adds missing entries.

song_artists["Tom Sawyer"] = "Rush"
print(song_artists["Tom Sawyer"])  # Rush
# Bracket assignment changes one entry; update() can apply several entries.


# --- 7. Practice: predict, explain, then run ---
# Write predictions beside each print before uncommenting that exercise.
# Identify the target, the source, and which values win for matching keys.

# Exercise 1 — Add and replace
# Predict all three outputs. Which key is added, and which value is replaced?
menu = {"tea": 3, "cake": 5}
changes = {"tea": 4, "coffee": 6}
menu.update(changes) 
print(menu) # {"tea": 4, "cake": 5, "coffee": 6}
print(len(menu)) # 3
print(changes) # {"tea": 4, "coffee": 6}
# Explanation:


# Exercise 2 — Direction matters
# Predict both dictionaries. Which dictionary is the target?
original = {"Kevin": 7, "Alex": 10}
incoming = {"Kevin": 12, "Sam": 8}
incoming.update(original)
print(incoming) # {'Kevin': 7, 'Sam': 8, 'Alex': 10}
print(original) # {"Kevin": 7, "Alex": 10}
# Explain why Kevin has that final value in incoming:
#   because the original key value was set


# Exercise 3 — The return value
# Predict both outputs. What does result hold?
settings = {"volume": 5}
result = settings.update({"volume": 9, "subtitles": True})
print(result) # None
print(settings) # {"volume": 9, "subtitles": True}
# Explain why settings = settings.update({"volume": 9}) would be a mistake
# if you wanted settings to keep referring to a dictionary:
#   it updates the original value of 5 


# Exercise 4 — Empty dictionaries and capitalization
# Predict all four outputs. Explain why two volume keys remain.
settings = {"volume": 5}
settings.update({})
print(settings) # {}
settings.update({"Volume": 8})
print(settings) # {"volume": 5,"Volume": 8}
print(len(settings)) # 2
print("VOLUME" in settings) # False
# Explanation:


# Exercise 5 — setdefault() vs. update()
# Predict all four outputs. Does an existing value of None prevent update()?
profile = {"nickname": None}
print(profile.setdefault("nickname", "Guest")) # None
profile.update({"nickname": "Kev", "city": "Chicago"})
print(profile["nickname"]) # Kev
print(profile) # {"nickname": "Kev", "city": "Chicago"}
print(len(profile)) # 2
# Explain why setdefault() preserves None but update() replaces it:


# Exercise 6 — Write your own merge
# 1. Create song_artists with three song titles mapped to their artists.
# 2. Create artist_changes with two entries: one existing title with a changed
#    artist value (such as "Rush (live)"), and one new title with its artist.
# 3. Update song_artists using artist_changes. Do not assign the return value
#    back to song_artists.
# 4. Print the updated song_artists and its length.
# 5. Print artist_changes to show that its entries remain unchanged.
# 6. Explain which entry was added, which was replaced, and why the target
#    now has four keys rather than five.
# Write your code below:
song_artists = {}
song_artists["Flirtin' with Disaster"] = "Molly Hatchet"
song_artists["Dreams I'll Never See"] = "Molly Hatchet"
song_artists["Whiskey Man"] = "Molly Hatchet"
artist_changes = {
    "Flirtin' with Disaster": "Molly Hatchet (live)",
    "Bounty Hunter": "Molly Hatchet",
}
song_artists.update(artist_changes)
print(song_artists)
print(len(song_artists))
print(artist_changes)


# Optional challenge — Combine settings while preserving the defaults
# Work through this one together when you are ready.
# Start with:
# defaults = {"volume": 5, "subtitles": True, "difficulty": "medium"}
# preferences = {"volume": 9, "difficulty": "hard"}
# Build a separate dictionary named final_settings using an empty dictionary
# and two update() calls. Keep defaults and preferences unchanged.
# Which source should you apply first so the user's preferences win?
# Predict and print all three dictionaries.
# Hint: later updates replace values supplied by earlier updates.
defaults = {"volume": 5, "subtitles": True, "difficulty": "medium"}
preferences = {"volume": 9, "difficulty": "hard"}
final_settings = {}

final_settings.update(defaults)
final_settings.update(preferences)

print(final_settings)
# {'volume': 9, 'subtitles': True, 'difficulty': 'hard'}

print(defaults)
# {'volume': 5, 'subtitles': True, 'difficulty': 'medium'}

print(preferences)
# {'volume': 9, 'difficulty': 'hard'}
