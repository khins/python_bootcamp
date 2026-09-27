# Unpacking argument dictionaries — Study Summary
# Instructor summary:
# - In a function CALL, **data unpacks a dictionary into keyword arguments.
# - Each dictionary key supplies an argument name; its value supplies the argument.
# - For example, function(**{"feet": 5, "inches": 11}) passes feet=5, inches=11.
# - Arguments match parameters by name, not by dictionary insertion order.
# - Passing data without ** passes the entire dictionary as one argument.
# - Keys used with ** in a call must be strings.
# - Keyword names are case-sensitive and must be accepted by the function.
# - Required parameters must receive values; parameters with defaults may be omitted.
# - Extra keywords require a matching parameter or a **kwargs collector.
# - Supplying the same argument twice raises TypeError; later values do not win.
#
# Compare the two uses of **:
# Definition: def collect(**kwargs): -> COLLECT extra keywords into a dictionary
# Call:       collect(**data)        -> UNPACK a dictionary into keyword arguments
#
# Precision note: the dictionary does not always need exactly as many entries
# as the function has parameters. Defaults, other supplied arguments, and
# **kwargs affect which entries are needed and accepted.


# --- 1. Start with ordinary function calls ---
def height_to_meters(feet, inches):
    total_inches = feet * 12 + inches
    return total_inches * 0.0254


print(f"{height_to_meters(5, 11):.4f}")               # 1.8034
print(f"{height_to_meters(feet=5, inches=11):.4f}")   # 1.8034
# Both calls supply the same values. The formatting shows four decimal places.


# --- 2. Unpack a dictionary into keyword arguments ---
stats = {"feet": 5, "inches": 11}
print(f"{height_to_meters(**stats):.4f}")  # 1.8034
print(stats)  # {'feet': 5, 'inches': 11}
# height_to_meters(**stats) is equivalent to:
# height_to_meters(feet=5, inches=11)
# Unpacking does not remove entries from stats.

# Leave this intentional error commented out:
# height_to_meters(stats)  # TypeError — stats fills feet; inches is missing
# Python does not automatically unpack a dictionary passed as one argument.


# --- 3. Names determine the match, not insertion order ---
reordered_stats = {"inches": 11, "feet": 5}
print(f"{height_to_meters(**reordered_stats):.4f}")  # 1.8034
# Even though inches appears first, its value still fills the inches parameter.

# A regular argument can supply one parameter while ** supplies another:
remaining_stats = {"inches": 11}
print(f"{height_to_meters(5, **remaining_stats):.4f}")  # 1.8034


# --- 4. Defaults and extra keyword arguments ---
def describe_track(title, artist="Unknown"):
    return f"{title} by {artist}"


track = {"title": "YYZ"}
print(describe_track(**track))  # YYZ by Unknown
# artist has a default, so the dictionary does not need that key.


def show_track(title, **details):
    print(title)
    print(details)


track_details = {"title": "YYZ", "artist": "Rush", "year": 1981}
show_track(**track_details)
# Expected:
# YYZ
# {'artist': 'Rush', 'year': 1981}
# The call unpacks all three entries. The definition binds title separately
# and collects the two extra keywords into details.


# --- 5. Common unpacking errors ---
# Leave all intentional errors commented out:
# height_to_meters(**{"feets": 5, "inches": 11})
# TypeError — feets is not an accepted keyword; spelling must match.

# height_to_meters(**{"Feet": 5, "inches": 11})
# TypeError — Feet and feet are different names.

# height_to_meters(**{"feet": 5})
# TypeError — the required inches argument is missing.

# height_to_meters(**{"feet": 5, "inches": 11, "extra": True})
# TypeError — this function has no extra parameter or **kwargs collector.

# height_to_meters(feet=6, **stats)
# TypeError — feet was supplied twice; ** does not overwrite the earlier value.

# height_to_meters(**{1: 5, "inches": 11})
# TypeError — keyword names supplied through ** must be strings.


# --- 6. Compare * and ** in calls ---
def show_arguments(*args, **kwargs):
    print(args)
    print(kwargs)


settings = {"volume": 9, "subtitles": True}
show_arguments(settings)
# Expected:
# ({'volume': 9, 'subtitles': True},)
# {}
# No stars: one positional argument containing the whole dictionary.

show_arguments(*settings)
# Expected:
# ('volume', 'subtitles')
# {}
# One star: dictionary iteration supplies KEYS as positional arguments.

show_arguments(**settings)
# Expected:
# ()
# {'volume': 9, 'subtitles': True}
# Two stars: entries become keyword arguments.


# --- 7. Practice: predict, explain, then run ---
# Write predictions in the ANSWER comments before uncommenting each exercise.
# Keep intentional-error calls commented out.

# Exercise 1 — Match names to parameters
# Predict both outputs. Why do they match despite the dictionary's order?
def subtract(first, second):
    return first - second

numbers = {"second": 3, "first": 10}
print(subtract(**numbers))
print(subtract(first=10, second=3))
# ANSWER:
# Outputs:
# 7
# 7
# Arguments match parameters by name, not by dictionary insertion order.


# Exercise 2 — Use a default
# Predict both outputs. Explain which call uses the default artist.
print(describe_track(**{"title": "Roundabout"}))
print(describe_track(**{"artist": "Yes", "title": "Roundabout"}))
# ANSWER:
# Roundabout by Unknown, first call uses default artist
# Roundabout by Yes


# Exercise 3 — Unpack, then collect extras
# Predict both output lines. Why is title absent from details?
data = {"artist": "Rush", "title": "Limelight", "year": 1981}
show_track(**data)
# ANSWER:
# Limelight
# {'artist': 'Rush', 'year': 1981}


# Exercise 4 — One star vs. two stars
# Predict all four output lines using show_arguments from section 6.
# Explain which call supplies keys as positional arguments.
data = {"name": "Kevin", "city": "Chicago"}
show_arguments(*data)
show_arguments(**data)
# ANSWER:
# ()
# {'name': 'Kevin', 'city': 'Chicago'}
# Explain which call supplies keys as positional arguments: the second supplies
# kwargs as a dict


# Exercise 5 — Diagnose each call
# For each call, say whether it succeeds or raises TypeError, and explain why.
# For successful calls, state the values received by feet and inches.
# Leave failing calls commented out.
# A:
# height_to_meters(**{"feet": 5, "inches": 11})
# # B: 
# height_to_meters({"feet": 5, "inches": 11}) # TypeError missing 1 required positional argument: 'inches'
# # C: 
# height_to_meters(**{"feet": 5, "Inches": 11}) # TypeError  got an unexpected keyword argument 'Inches'
# # D: 
# height_to_meters(5, **{"inches": 11})
# # E: 
# height_to_meters(5, **{"feet": 6, "inches": 11}) # TypeError: height_to_meters() got multiple values for argument 'feet'
# ANSWER:


# Exercise 6 — Write your own unpacked call
# 1. Define album_label(title, artist, year) to return a string in this format:
#    Moving Pictures by Rush (1981)
# 2. Create an album dictionary with matching string keys and appropriate values.
#    Insert the keys in a different order from the function's parameters.
# 3. Call album_label using **album and print its returned string.
# 4. Print album afterward to show its entries remain unchanged.
# 5. Explain why passing album without ** would behave differently.
# Write your code below:
def album_label(title, artist, year):

    return f'{title} {artist} {year}'

labels = []
album = {
    "title": "Hemispheres",
    "artist": "Rush",
    "year": 1978
}
labels.append(album_label(**album))
print(labels)


# Optional challenge — Unpack each record in a list
# Work through this one together when you are ready.
# Using your album_label function, create a list of three album dictionaries.
# Each dictionary must contain title, artist, and year entries.
# Loop over the list and unpack each dictionary into an album_label call.
# Collect the returned strings in a NEW list, then print that list after the loop.
# Leave the original records unchanged.
# Explain what your loop variable contains and what ** does in each call.
# Write your code below:
labels = []
albums = [
    {"title": "Hemispheres", "artist": "Rush", "year": 1978},
    {"title": "Moving Pictures", "artist": "Rush", "year": 1981},
    {"title": "Tarkus", "artist": "Emerson, Lake & Palmer", "year": 1971},
]

for album in albums:
    labels.append(album_label(**album))

print(labels)
# album holds one dictionary from albums during each iteration.
# **album passes that dictionary's entries as keyword arguments,
# matching its keys to the function's parameter names.