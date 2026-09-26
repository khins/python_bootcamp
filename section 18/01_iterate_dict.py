# Iterating over dictionaries — Study Summary
# Instructor summary:
# - Iteration means visiting elements one at a time.
# - A for loop over a dictionary gives you its KEYS, one at a time.
# - Use dictionary[key] to retrieve the value for the current key.
# - The loop variable's name is your choice; a descriptive name helps.
# - Keys keep their types: an integer key stays an integer during iteration.
# - An empty dictionary produces zero loop iterations.
# - Python 3.7+ guarantees dictionary insertion order.
# - Insertion order is not the same as alphabetical or numerical sorting.
#
# Corrections to the transcript:
# - The claim that dictionary order is never guaranteed is outdated.
# - Looping over keys and looking up values is valid Python.
# - When both keys and values are needed, .items() is often clearer;
#   that approach belongs to the upcoming lessons.
# - The loop syntax uses the keyword in, not end.


# --- 1. Loop directly over a dictionary to get its keys ---
chinese_food = {
    "Sesame Chicken": 9.99,
    "Boneless Spare Ribs": 7.99,
    "Fried Rice": 1.99,
}

for food in chinese_food:
    print(food)
# Expected:
# Sesame Chicken
# Boneless Spare Ribs
# Fried Rice
# food receives each key, not its price or an entire key-value pair.


# --- 2. Look up the value using the current key ---
for food in chinese_food:
    price = chinese_food[food]
    print(f"The food is {food} and its price is ${price:.2f}.")
# Expected:
# The food is Sesame Chicken and its price is $9.99.
# The food is Boneless Spare Ribs and its price is $7.99.
# The food is Fried Rice and its price is $1.99.
# On the first iteration:
# food               -> "Sesame Chicken"
# chinese_food[food]  -> 9.99
# .2f displays the price with two digits after the decimal point.


# --- 3. Integer keys work too ---
pounds_to_kilograms = {
    5: 2.26796,
    10: 4.53592,
    25: 11.3398,
}

for weight_in_pounds in pounds_to_kilograms:
    weight_in_kilograms = pounds_to_kilograms[weight_in_pounds]
    print(f"{weight_in_pounds} pounds is equal to {weight_in_kilograms} kilograms.")
# Expected:
# 5 pounds is equal to 2.26796 kilograms.
# 10 pounds is equal to 4.53592 kilograms.
# 25 pounds is equal to 11.3398 kilograms.
# The numbers are sample rounded conversions from the lesson.
# The key 5 is an integer, not a list index and not the string "5".


# --- 4. Insertion order is different from sorted order ---
scores = {"Sam": 8, "Alex": 10, "Kevin": 7}
scores["Alex"] = 12
scores["Dana"] = 9

for name in scores:
    print(name)
# Expected:
# Sam
# Alex
# Kevin
# Dana
# Replacing Alex's value keeps that key in its existing position.
# Adding Dana inserts a new key at the end.
# Dictionary lookup still uses keys, even though insertion order is preserved.


# --- 5. Use values in calculations and conditions ---
menu = {"tea": 3, "cake": 5, "coffee": 4}
total = 0

for item in menu:
    total += menu[item]
print(total)  # 12 — the sum of one price for each menu item

for item in menu:
    if menu[item] <= 4:
        print(item)
# Expected:
# tea
# coffee
# The loop gives us the key; the lookup supplies the price to compare.


# --- 6. Empty dictionaries and common mistakes ---
empty_menu = {}
count = 0
for item in empty_menu:
    count += 1
print(count)  # 0 — the loop body never ran

# A variable name does not change what dictionary iteration yields:
for price in {"tea": 3}:
    print(price)  # tea — still a key, despite the misleading variable name

# Use the variable itself to look up its current key:
# menu[item]    -> value for whichever key item currently holds
# menu["item"] -> value for the literal key "item", which is absent here
# Do not add or delete dictionary keys while directly iterating over it;
# changing its size can raise RuntimeError. These examples only read entries.


# --- 7. Practice: predict, explain, then run ---
# Write predictions in the ANSWER comments before uncommenting each exercise.
# Predict the entire snippet, including each iteration of its loop.
# Use direct dictionary iteration and key lookups for this lesson.

# Exercise 1 — What does the loop receive?
# Predict all output lines. Does food hold a key, a value, or a pair?
menu = {"tea": 3, "cake": 5}
for food in menu:
    print(food)
# ANSWER:
#   tea
#   cake

# Exercise 2 — Keys and values together
# Predict all output lines. Explain what menu[item] retrieves each time.
menu = {"tea": 3, "coffee": 4}
for item in menu:
    print(f"{item}: ${menu[item]:.2f}")
# ANSWER:
#   tea: $3.00
#   coffee $4.00

# Exercise 3 — Integer keys
# Predict the four output lines, including the types.
# Explain why number is not a list index here.
labels = {10: "ten", 5: "five"}
for number in labels:
    print(type(number))
    print(labels[number])
# ANSWER:
#   int
#   ten
#   five


# Exercise 4 — Order and replacement
# Predict all output lines. Explain why replacing a value does not move its key.
scores = {"Kevin": 7, "Alex": 10}
scores["Kevin"] = 12
scores["Sam"] = 8
for name in scores:
    print(name, scores[name])
# ANSWER:
#   Kevin 12
#   Alex 10
#   Sam 8


# Exercise 5 — Diagnose the lookup
# The goal is to print each menu item's price.
# Identify the error raised by the first iteration and explain its cause.
# Write a corrected loop below. Keep the broken snippet commented out.
# menu = {"tea": 3, "cake": 5}
# for item in menu:
#     print(menu["item"])
# ANSWER:
#   KeyError


# Exercise 6 — Write your own song loop
# 1. Create song_artists with three song titles mapped to their artists.
# 2. Loop directly over song_artists using a descriptive variable name.
# 3. Print each entry in the format: Song Title by Artist
#    Retrieve the artist using the current song title as the dictionary key.
# 4. Use a counter to count the entries visited, then print it after the loop.
# 5. Explain what your loop variable contains during each iteration.
# Write your code below:
song_artists = {}
song_artists["Rikki Don't Lose That Number"] = "Steely Dan"
song_artists["Reelin' in the Years"] = "Steely Dan"
song_artists["Do It Again"] = "Steely Dan"
print(song_artists)
counter = 0
for song in song_artists:
    print(f'{song}: by Artist {song_artists[song]}')
    counter += 1 
print(counter)
# # song contains one song title (a dictionary key) during each iteration.


# Optional challenge — Find affordable menu items
# Work through this one together when you are ready.
# Define affordable_items(menu, budget) to return a NEW list of item names
# whose prices are less than or equal to budget.
# Use a for loop over the dictionary, key lookups, and append().
# Preserve the menu's insertion order and leave the menu unchanged.
# An empty menu or a menu with no affordable items should return [].
# affordable_items({"tea": 3, "cake": 5, "coffee": 4}, 4) => ["tea", "coffee"]
# affordable_items({"tea": 3}, 2) => []
# affordable_items({}, 10) => []
# Write your code below:
