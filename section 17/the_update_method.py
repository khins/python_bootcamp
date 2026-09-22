# Dictionary update — Study Summary
# Instructor summary:
# - target.update(source) merges source entries into target.
# - The dictionary BEFORE the dot is the target being changed.
# - The dictionary INSIDE the parentheses supplies the incoming entries.
# - Missing keys are added; matching keys receive the incoming values.
# - Keys found only in the target stay unchanged.
# - update() changes the target in place and returns None.
# - With separate target and source dictionaries, the source entries stay unchanged.
# - Replacing a value does not create a duplicate key.
# - Direction and order matter: the incoming value wins for matching keys.


# --- 1. Add new entries and replace existing values ---
# Fictional salary data from the lesson.
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
print(len(employee_salaries))  # 4
# Guido already existed: its value was replaced, not its key duplicated.
# Yukihiro was missing: one new entry was added.
# James and Brandon had no incoming replacements: their values stayed the same.


# --- 2. Identify the target and source ---
print(extra_employee_salaries)
# Expected: {'Yukihiro': 1000000, 'Guido': 333333}
print(len(extra_employee_salaries))  # 2
# employee_salaries is before the dot: it changed.
# extra_employee_salaries is the argument: it supplied entries and stayed unchanged.
# update() does not remove the entries from the source.


# --- 3. Reverse direction with fresh starting dictionaries ---
# Reset both dictionaries so the previous update does not affect this example.
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
print(employee_salaries)
# Expected: {'Guido': 100000, 'James': 500000, 'Brandon': 900000}
# This time employee_salaries supplies the winning Guido value: 100000.
# The variable names do not decide the direction; their positions in the call do.


# --- 4. The return value is None ---
settings = {"volume": 5}
changes = {"volume": 9, "subtitles": True}
result = settings.update(changes)
print(result)    # None
print(settings)  # {'volume': 9, 'subtitles': True}
print(changes)   # {'volume': 9, 'subtitles': True}
# Avoid settings = settings.update(changes).
# That would update the dictionary, then assign the returned None to settings.
# Use settings.update(changes) by itself to keep using settings as a dictionary.


# --- 5. An empty update does not clear the target ---
menu = {"tea": 3}
menu.update({})
print(menu)  # {'tea': 3} — no incoming entries means no changes

menu.update({"Tea": 4})
print(menu)       # {'tea': 3, 'Tea': 4}
print(len(menu))  # 2 — string keys are case-sensitive
# menu.clear() would remove all entries; menu.update({}) leaves them alone.


# --- 6. Compare update() with setdefault() ---
profile = {"nickname": None}
print(profile.setdefault("nickname", "Guest"))  # None
# setdefault() preserves an existing value, even None.

profile.update({"nickname": "Kev", "city": "Chicago"})
print(profile)  # {'nickname': 'Kev', 'city': 'Chicago'}
# update() replaces the value for nickname and adds the missing city key.

# Compare with earlier lessons:
# data[key] = value             -> adds or replaces one entry
# data.setdefault(key, value)   -> adds only if the key is missing
# data.update(other)            -> adds/replaces entries supplied by other
# data.clear()                  -> removes all entries


# --- 7. Practice: predict, explain, then run ---
# Write predictions beside each print before uncommenting the exercise.
# Include the requested explanations: identify the target and incoming source.

# Exercise 1 — Add and replace
# Predict all three outputs. Which key is added and which value is replaced?
menu = {"tea": 3, "cake": 5}
changes = {"tea": 4, "coffee": 6}
menu.update(changes)
print(menu) # {"tea": 3, "cake": 5, "coffee": 6}
print(len(menu)) # 3
print(changes) # {"tea": 4, "coffee": 6}
# Explanation:
#   key tea: 4 is added and 3 is replaced


# Exercise 2 — Direction matters
# Predict both outputs. Identify the target and source in this call.
original = {"Kevin": 7, "Alex": 10}
incoming = {"Kevin": 12, "Sam": 8}
incoming.update(original)
print(incoming) # {"Kevin": 7, "Sam": 8, "Alex": 10}
print(original) # {"Kevin": 7, "Alex": 10}
# Explain why Kevin has that final value in incoming:
#   # Kevin becomes 7 because original supplies the incoming values.
#    update() replaces the target's existing value when the same key appears.


# Exercise 3 — Return value vs. updated dictionary
# Predict both outputs. What does result hold?
settings = {"volume": 5}
result = settings.update({"volume": 9, "subtitles": True})
print(result) # None
print(settings) # {'volume': 9, 'subtitles': True}

# Explain what settings would hold after settings = settings.update({"volume": 2}):
#   For the explanation question, settings = settings.update({"volume": 2}) would also
#  leave settings holding None: the dictionary is updated first, then the returned None
#  is assigned to settings.

# Exercise 4 — Empty sources and capitalization
# Predict all four outputs. Does the first update remove any entries?
settings = {"volume": 5}
settings.update({})
print(settings) # {"volume": 5}
settings.update({"Volume": 8})
print(settings) # {'volume': 5, 'Volume': 8}
print(len(settings)) # 2
print("VOLUME" in settings) # False
# Explain why volume and Volume are separate keys:
#   they are uniquely different because of case sensitivity


# Exercise 5 — Existing None values
# Predict all four outputs.
profile = {"nickname": None}
print(profile.setdefault("nickname", "Guest")) # None
profile.update({"nickname": "Kev", "city": "Chicago"})
print(profile["nickname"]) # Kev
print(profile) # {"nickname": "Kev", "city": "Chicago"}
print(len(profile)) # 2
# Explain why setdefault() preserves None but update() replaces it:
#   setdefault adds only if the key is missing and returns None 
#   update() replaces the value


# Exercise 6 — Write your own merge
# 1. Create song_artists with three song titles mapped to their artists.
# 2. Create artist_changes with two entries: one existing title with a changed
#    artist value (such as "Rush (live)"), and one new title with its artist.
# 3. Update song_artists using artist_changes.
# 4. Print song_artists and its length.
# 5. Print artist_changes to show that its entries remain unchanged.
# 6. Explain which entry was added, which value was replaced, and why there
#    are four keys in the target rather than five.
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



# Optional challenge — Combine settings while preserving the defaults
# Work through this one together when you are ready.
defaults = {"volume": 5, "subtitles": True, "difficulty": "medium"}
preferences = {"volume": 9, "difficulty": "hard"}
final_settings = {}
# Build a separate dictionary named final_settings, starting with {}.
# Use two update() calls so the preferences win for matching keys.
final_settings.update(defaults)
final_settings.update(preferences)
print(final_settings)
print(defaults)
print(preferences)

# Keep defaults and preferences unchanged.
# Predict and print all three dictionaries.
# Explain which source must be applied first and why subtitles remains present.
# Identify the dictionary before the dot in each update call.
#   Add a brief comment explaining that defaults are applied first so preferences win, 
# and subtitles remains because preferences doesn’t replace it.
