# Accessing Dictionary Values — Study Summary
# Instructor summary:
# - Access a dictionary value using its KEY, not its position.
# - dictionary[key] returns the value or raises KeyError if the key is missing.
# - String keys are case-sensitive: "Chicago" and "chicago" are different.
# - Keys can have different hashable types; 49 and "49" are different keys.
# - dictionary.get(key, default) returns the value when the key exists,
#   or the default when the key is missing.
# - The default argument is optional; without it, a missing key returns None.
# - Choose brackets when the key is required; use get() when a missing key
#   has an acceptable fallback. Neither approach is always better.
#
# Clarifications:
# - Modern dictionaries preserve insertion order, but lookup still uses keys.
# - Keys must be hashable. A tuple containing a list cannot be a key.
# - get() does not insert a missing key or copy the value it returns.
# - get() avoids KeyError for missing keys; an unhashable key such as a list
#   still raises TypeError.


# --- 1. Accessing values with square brackets ---
# These flight prices are example data for this lesson.
flight_prices = {
    "Chicago": 199,
    "San Francisco": 499,
    "Denver": 295,
}
print(flight_prices["Chicago"])  # 199
print(flight_prices["Denver"])   # 295

# You can also use a variable containing the key.
destination = "San Francisco"
print(flight_prices[destination])  # 499


# --- 2. Missing keys and case sensitivity ---
# Leave these commented out so the rest of the lesson can run.
# print(flight_prices["Seattle"])  # KeyError: 'Seattle'
# print(flight_prices["chicago"])  # KeyError: 'chicago'
# print(flight_prices[0])          # KeyError: 0 — not "the first item"


# --- 3. Integer keys and list values ---
gym_membership_packages = {
    29: ["machines"],
    49: ["machines", "vitamin supplements"],
    79: ["machines", "vitamin supplements", "sauna"],
}
print(gym_membership_packages[49])  # ['machines', 'vitamin supplements']
print(gym_membership_packages[79])  # ['machines', 'vitamin supplements', 'sauna']

# 49 is an integer key, not a list index.
# "49" is a string and is not a key in this dictionary.
# print(gym_membership_packages["49"])  # KeyError: '49'

# After retrieving a list, you can index that list.
print(gym_membership_packages[79][2])  # sauna
# First [79]: dictionary lookup. Then [2]: list index.


# --- 4. Using get() with a fallback ---
print(gym_membership_packages.get(29, ["basic dumbbells"]))
# ['machines'] — the key exists, so the fallback is not returned

print(gym_membership_packages.get(100, ["basic dumbbells"]))
# ['basic dumbbells'] — the key is missing

print(len(gym_membership_packages))  # 3 — get() did not add key 100


# --- 5. Omitting the fallback ---
print(flight_prices.get("Chicago"))  # 199
print(flight_prices.get("Seattle"))  # None
print(flight_prices.get("Seattle", "No flight listed"))  # No flight listed

# None is a Python object, not the string "None".
# Use is None when you want to check whether a result is None.
price = flight_prices.get("Seattle")
print(price is None)  # True


# --- 6. A fallback applies only when the key is missing ---
# An existing value of 0, False, or None is still returned as stored.
settings = {
    "volume": 0,
    "notifications": False,
    "nickname": None,
}
print(settings.get("volume", 50))          # 0
print(settings.get("notifications", True)) # False
print(settings.get("nickname", "Guest"))  # None
print(settings.get("theme", "light"))     # light


# --- 7. Practice: predict, explain, then run ---
# Write predictions beside each print before uncommenting the code.
# If you predict KeyError, leave that line commented out or run it separately:
# an unhandled error stops execution before later lines can run.
print("1" * 60)
# Exercise 1 — Lookup by name
# Predict all three outputs. What does the variable instrument_name contain?
#    prediction is below
instruments = {"Alex": "guitar", "Geddy": "bass", "Neil": "drums"}
instrument_name = "Geddy"
print(instruments["Alex"])           # guitar
print(instruments[instrument_name])  # bass
print(len(instruments))              # 3

print("2" * 60)
# Exercise 2 — Exact keys matter
# Predict the result or error for each lookup. Explain the differences.
prices = {"Chicago": 199, 49: "gym membership"}
print(prices["Chicago"])  # 199
# print(prices["chicago"])  # error since the key does not match case sensitive
print(prices[49])         # gym membership
# print(prices["49"])       # key error again

print("3" * 60)
# Exercise 3 — Existing key vs. missing key
# Predict all four outputs. When is the fallback used?
menu = {"tea": 3, "cake": 5}
print(menu.get("tea", 0))     # 3
print(menu.get("coffee", 0))  # 0
print(menu.get("coffee"))     # None
print(len(menu))              # 2

# Exercise 4 — Existing values that look empty
# Predict each output. Does get() use the fallback for an existing None value?
print("4" * 60)
profile = {"name": "Kevin", "nickname": None, "points": 0}
# dictionary.get(key, fallback)
# Key exists: returns its stored value, even if that value is None, 0, or False.
# Key is missing: returns the fallback. If you omit the fallback, it returns None.
print(profile.get("nickname", "Guest"))  # None
print(profile.get("points", 100))        # 0
print(profile.get("city", "Unknown"))    # Unknown
# Explain why the last lookup behaves differently from the first two.

# Exercise 5 — Retrieve a list, then an item
# Predict all three outputs. Explain what each pair of brackets does.
print("5" * 60)
hobbies = {"Kevin": ["guitar", "programming", "woodworking"]}
print(hobbies["Kevin"])  # Kevin
print(hobbies["Kevin"][1]) # ["guitar", "programming", "woodworking"]
print(hobbies.get("Alex", ["no hobbies listed"]))  # ["no hobbies listed"]

print("6" * 60)
# Exercise 6 — Write your own lookups
# 1. Create a dictionary mapping three song titles to their artists.
# 2. Use brackets to look up one existing song.
# 3. Store another existing title in a variable and look it up using that name.
# 4. Use get() to look up a missing song with "Unknown artist" as the fallback.
# 5. Look up the same missing song with get() but without a fallback.
# 6. Print the dictionary's length and explain whether the lookups changed it.
# 7. Write a comment explaining when you would choose brackets vs. get().
#       I would choose get() when I am unsure of knowing what the dictionary holds
song_titles = {
    "Roundabout": "Fragile",
    "Owner of a Lonely Heart": "90125",
    "Close to the Edge": "Close to the Edge",
}
#2 
print(song_titles["Roundabout"])
#3
song_titles["Owner of a Lonely Heart"] = "90126"
print(song_titles["Owner of a Lonely Heart"])

#4 
print(song_titles.get("Subway Walls", "Unknown"))
#5
print(song_titles.get("Subway Walls"))
#6
print(len(song_titles)) # lookups did not change the dictionary

# Optional challenge — Connect lookup to shared references
# Predict both outputs. Does get() return a copy of the stored list?
musicians = {"Rush": ["Alex", "Geddy"]}
members = musicians.get("Rush")
members.append("Neil")
print(musicians["Rush"]) # "Rush": ["Alex", "Geddy", "Neil"]
print(members is musicians["Rush"]) # True
