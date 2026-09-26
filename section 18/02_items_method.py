# Dictionary items() — Study Summary
# Instructor summary:
# - dictionary.items() returns an iterable view of the dictionary's entries.
# - Iterating over that view supplies (key, value) tuples, one pair at a time.
# - Use for key, value in dictionary.items() to unpack each pair directly.
# - The first variable receives the key; the second receives its value.
# - Choose descriptive variable names, such as course and professor.
# - A single underscore (_) conventionally marks an unused variable.
# - The view reflects changes to the dictionary; it is not a saved copy.
# - Python 3.7+ guarantees dictionary insertion order, including items() iteration.
#
# Corrections to the transcript:
# - An items view is iterable, but is not itself an iterator.
# - class, for, and in are reserved keywords; print and len are built-in names.
#   Assigning to print or len is allowed but hides the built-in, so avoid it.
# - Use items() when you need both keys and values. Direct dictionary iteration
#   is appropriate for keys alone; values() is available for values alone.


# --- 1. Inspect the key-value pairs ---
college_courses = {
    "History": "Mr. Washington",
    "Math": "Mr. Newton",
    "Science": "Mr. Einstein",
}

print(college_courses.items())
# Expected: dict_items([('History', 'Mr. Washington'), ('Math', 'Mr. Newton'), ('Science', 'Mr. Einstein')])

for pair in college_courses.items():
    print(pair)
# Expected:
# ('History', 'Mr. Washington')
# ('Math', 'Mr. Newton')
# ('Science', 'Mr. Einstein')
# One loop variable receives the entire two-element tuple.


# --- 2. Unpack each pair in the loop header ---
for course, professor in college_courses.items():
    print(f"The course {course} is being taught by {professor}.")
# Expected:
# The course History is being taught by Mr. Washington.
# The course Math is being taught by Mr. Newton.
# The course Science is being taught by Mr. Einstein.
# On the first iteration, Python unpacks ('History', 'Mr. Washington'):
# course    -> 'History'
# professor -> 'Mr. Washington'


# --- 3. Compare direct iteration with items() ---
menu = {"tea": 3, "cake": 5}

for item in menu:
    print(item, menu[item])
# Expected:
# tea 3
# cake 5

for item, price in menu.items():
    print(item, price)
# Expected:
# tea 3
# cake 5
# Both loops work. items() gives both parts directly without another lookup.
# Variable names do not determine which part they receive; position does.


# --- 4. Mark an unused part with an underscore ---
for _, professor in college_courses.items():
    print(professor)
# Expected:
# Mr. Washington
# Mr. Newton
# Mr. Einstein
# _ still receives each key. It is an ordinary variable used by convention
# to communicate that this loop does not need that part of the pair.

# If only keys are needed, direct iteration is simpler:
for course in college_courses:
    print(course)
# Expected:
# History
# Math
# Science

# Preview: values() supplies just the values.
# for professor in college_courses.values():
#     print(professor)


# --- 5. Use keys and values in a condition ---
menu = {"tea": 3, "cake": 5, "coffee": 4}
affordable = []
for item, price in menu.items():
    if price <= 4:
        affordable.append(item)
print(affordable)  # ['tea', 'coffee']
# Compare the price, then keep the matching item's name.


# --- 6. The view reflects later dictionary changes ---
scores = {"Kevin": 7}
entries = scores.items()
print(list(entries))  # [('Kevin', 7)]

scores["Kevin"] = 12
scores["Alex"] = 10
print(list(entries))  # [('Kevin', 12), ('Alex', 10)]
# We did not call scores.items() again: the saved view reflects the changes.
# list(entries) creates a list of the pairs present at that moment.
# It does not deep-copy any mutable objects contained in the keys or values.
# Do not add or delete keys while iterating over the dictionary's live view;
# changing the dictionary's size during iteration can raise RuntimeError.

# An empty dictionary supplies no pairs, so its loop body runs zero times.
for key, value in {}.items():
    print(key, value)
# Expected: no output from this loop.


# --- 7. Practice: predict, explain, then run ---
# Write predictions in the ANSWER comments before uncommenting each exercise.
# Predict the whole snippet, including every iteration.
# Keep intentional-error examples commented out.

# Exercise 1 — One variable receives a pair
# Predict both output lines. What type of object does pair hold?
songs = {"YYZ": "Rush", "Roundabout": "Yes"}
for pair in songs.items():
    print(pair)
# ANSWER:
# ("YYZ", "Rush")
# ("Roundabout", "yes")

# Exercise 2 — Unpack keys and values
# Predict both output lines. Identify what title and artist receive.
songs = {"YYZ": "Rush", "Roundabout": "Yes"}
for title, artist in songs.items():
    print(f"{title} by {artist}")
# ANSWER:
# "YYZ by Rush"
# "Roundabout by Yes"

# Exercise 3 — Names do not control the order
# Predict both output lines. Explain why these variable names are misleading.
menu = {"tea": 3, "cake": 5}
for item, price in menu.items():
    print(item, price )
# Rewrite the loop with clearer names below.
# ANSWER:
# the original names were misleading because price received the item name and  
# item received the price. Variable names don’t change the order of the pair.

# Exercise 4 — Ignore one part
# Predict both output lines. What does _ receive during each iteration?
courses = {"History": "Ms. Lee", "Math": "Mr. Patel"}
for _, teacher in courses.items():
    print(teacher)
# Does using _ remove the keys from courses? Explain.
# ANSWER:
# Ms. Lee
#  Mr. Patel


# Exercise 5 — A live view
# Predict both outputs. Explain why entries reflects the updated score.
scores = {"Kevin": 7}
entries = scores.items()
scores["Kevin"] = 9
scores["Alex"] = 10
print(list(entries))
print(len(entries))
# ANSWER:
# [('Kevin', 9), ('Alex', 10)]
# 2


# Exercise 6 — Write your own menu loop
# 1. Create a menu dictionary with three item names and numeric prices.
# 2. Use items() and two descriptive loop variables to print each item and
#    its price in this format: tea: $3.00
# 3. Use a running total to add the prices during that same loop.
# 4. Print the total after the loop, formatted with two decimal places.
# 5. Explain which variable receives a key and which receives a value.
# Write your code below:
menu = {
    "Cheeseburger": 12.99,
    "French Fries": 4.50,
    "Milkshake": 5.99,
}
total = 0
for item, price in menu.items():
    print(item, f'${price:.2f}')
    total += price
print(f'${total:.2f}')
# Correct—item receives the key, and price receives its value.

# Optional challenge — Find songs by an artist
# Work through this one together when you are ready.
# Define songs_by_artist(song_artists, selected_artist).
# Use items(), a for loop, and append() to return a NEW list of titles whose
# artist exactly matches selected_artist. Matching is case-sensitive.
# Preserve insertion order and leave song_artists unchanged.
# Return [] when no artist matches or when the dictionary is empty.

# Write your code below:
def songs_by_artist(song_artists, selected_artist):
    titles = []
    for song, artist in song_artists.items():
        if artist == selected_artist:
            titles.append(song)
    return titles

print(songs_by_artist({"YYZ": "Rush", "Roundabout": "Yes", "Limelight": "Rush"}, "Rush")) #=> ['YYZ', 'Limelight']
print(songs_by_artist({"YYZ": "Rush"}, "rush")) #=> []
print(songs_by_artist({}, "Rush")) #=> []
# All three expected outputs in your comments are correct. No changes needed.