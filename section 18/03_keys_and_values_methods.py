# Dictionary keys() and values() — Study Summary
# Instructor summary:
# - dictionary.keys() returns an iterable view of the dictionary's keys.
# - dictionary.values() returns an iterable view of its values.
# - These views are not lists; their types are dict_keys and dict_values.
# - Both support iteration, membership checks with in, and len().
# - Direct dictionary iteration and keys() both supply keys.
# - Direct dictionary membership checks keys; values() checks stored values.
# - len(data), len(data.keys()), and len(data.values()) are equal.
# - Values may repeat; values() includes one value for every entry.
# - Views reflect later changes to their dictionary.
# - Use list(view) when you need a list, such as for positional indexing.
# - Python 3.7+ preserves dictionary insertion order in these views.
#
# Connection to the previous lesson:
# data          -> iterate over keys
# data.keys()   -> iterate over keys explicitly
# data.values() -> iterate over values
# data.items()  -> iterate over (key, value) pairs
# Direct iteration and keys() are both valid choices when you need keys.


# --- 1. Inspect the views and their types ---
# Fictional sample prices from the lesson, not current market prices.
cryptocurrency_prices = {
    "Bitcoin": 400_000,
    "Ethereum": 7_000,
    "Litecoin": 10,
}

print(cryptocurrency_prices.keys())
# Expected: dict_keys(['Bitcoin', 'Ethereum', 'Litecoin'])
print(type(cryptocurrency_prices.keys()))  # <class 'dict_keys'>

print(cryptocurrency_prices.values())
# Expected: dict_values([400000, 7000, 10])
print(type(cryptocurrency_prices.values()))  # <class 'dict_values'>
# The parentheses in keys() and values() call the methods.
# Despite their displayed contents, the returned views are not lists.


# --- 2. Iterate over keys ---
for currency in cryptocurrency_prices.keys():
    print(f"The next currency is {currency}.")
# Expected:
# The next currency is Bitcoin.
# The next currency is Ethereum.
# The next currency is Litecoin.

# Direct iteration supplies those same keys in the same order:
for currency in cryptocurrency_prices:
    print(currency)
# Expected:
# Bitcoin
# Ethereum
# Litecoin


# --- 3. Iterate over values ---
for price in cryptocurrency_prices.values():
    print(f"The next price is {price}.")
# Expected:
# The next price is 400000.
# The next price is 7000.
# The next price is 10.
# price receives a numeric value, not a currency name or a key-value tuple.
# If you need the currency and its price together, use items().


# --- 4. Check membership at the right place ---
print("Bitcoin" in cryptocurrency_prices)         # True
print("Bitcoin" in cryptocurrency_prices.keys())  # True
print("Ripple" in cryptocurrency_prices.keys())   # False

print(400_000 in cryptocurrency_prices.values())  # True
print(5_000 in cryptocurrency_prices.values())    # False
print(400_000 in cryptocurrency_prices)           # False
# The last check looks for an integer KEY of 400000, not a stored price.
# Membership tests return a Boolean; they do not modify the dictionary.


# --- 5. Count entries, including repeated values ---
print(len(cryptocurrency_prices))           # 3
print(len(cryptocurrency_prices.keys()))    # 3
print(len(cryptocurrency_prices.values()))  # 3

song_artists = {"YYZ": "Rush", "Limelight": "Rush", "Roundabout": "Yes"}
print(list(song_artists.values()))  # ['Rush', 'Rush', 'Yes']
print(len(song_artists.values()))   # 3
# Three different keys have three corresponding values, even though two values
# are equal. values() does not remove duplicates or count unique artists.


# --- 6. A live view vs. a list made from it ---
menu = {"tea": 3, "cake": 5}
key_view = menu.keys()
value_view = menu.values()
saved_prices = list(value_view)

menu["tea"] = 4
menu["coffee"] = 6
print(list(key_view))    # ['tea', 'cake', 'coffee']
print(list(value_view))  # [4, 5, 6]
print(saved_prices)      # [3, 5]
# The saved views reflect the updated dictionary.
# saved_prices is a separate list of the integer values collected earlier.
# list() does not deep-copy mutable objects that might be stored as values.

print(saved_prices[0])  # 3 — a list supports positional indexing
# Leave this intentional error commented out:
# print(value_view[0])  # TypeError — dict_values does not support indexing
# dict_keys does not support positional indexing either.
# A for loop does not require converting a view to a list.
# Avoid adding or deleting keys while iterating over a live dictionary view;
# changing the dictionary's size during iteration can raise RuntimeError.


# --- 7. Practice: predict, explain, then run ---
# Write predictions in the ANSWER comments before uncommenting each exercise.
# Keep intentional-error lines commented out.

# Exercise 1 — Keys and values are different views
# Predict all four outputs. Explain what each method supplies.
menu = {"tea": 3, "cake": 5}
print(list(menu.keys()))
print(list(menu.values()))
print(type(menu.keys()))
print(type(menu.values()))
# ANSWER:
# ['tea', 'cake']
# [3, 5]
# <class 'dict_keys'>
# <class 'dict_values'>


# Exercise 2 — Membership checks
# Predict all four outputs. Explain why the first two checks differ.
scores = {"Kevin": 7, "Alex": 10}
print(7 in scores)
print(7 in scores.values())
print("Kevin" in scores.keys())
print("Kevin" in scores.values())
# ANSWER:
# False 7 in scores returns as false because it defaults to keys so it wont be values
# True
# True
# False


# Exercise 3 — Repeated values still count
# Predict all three outputs. Why is the values length not the number of
# different artists?
songs = {"YYZ": "Rush", "Limelight": "Rush", "Roundabout": "Yes"}
print(len(songs))
print(len(songs.values()))
print(list(songs.values()))
# ANSWER:
# 3
# 3
# ["Rush", "Rush", "Yes"]

# Exercise 4 — Changes after saving a view
# Predict all three outputs. Explain which object reflects the new entry.
menu = {"tea": 3}
keys = menu.keys()
saved_keys = list(keys)
menu["coffee"] = 4
print(list(keys))
print(saved_keys)
print(len(keys))
# ANSWER:
# ["tea", "coffee"]
# ["tea"]
# 2
# Explain which object reflects the new entry: the new entry is in the menu dict because 
# coffee was added after the var saved_keys was copied as a list


# Exercise 5 — Choose the right iteration
# The goal is to print only the numeric prices, one per line.
# Explain what this loop actually prints, then write a corrected loop using
# values(). Explain why renaming the variable alone would not fix it.
menu = {"tea": 3, "cake": 5}
for price in menu.keys():
    print(price)

# correct loop for value
for price in menu.values():
    print(price)
# ANSWER:
# tea
# cake
# variable change won't fix it without also obtaining the values while looping over the dict

# Exercise 6 — Write your own price summary
# 1. Create a menu dictionary with three item names and numeric prices.
# 2. Use keys() in a loop to print each item name.
# 3. Use values() in a separate loop to calculate a running total of the prices.
# 4. Print that total and the number of values.
# 5. Check whether a chosen numeric price exists using in and values().
# 6. Explain why the number of keys equals the number of values, even if
#    two items share a price.
# Write your code below:
menu = {
    "Margherita Pizza": 14.50,
    "Fettuccine Alfredo": 18.99,
    "Tiramisu": 18.99,
}
total = 0
for item in menu.keys():
    print(item)
for price in menu.values():
    print(f'${price:.2f}')
    total += price
print(f'${total:.2f}')
print(len(menu.values())) # 3
print(18.99 in menu.values()) # True


# the values can be duplicate in the dict because the keys are unique
# counts match: every key has one associated value, and .values() includes duplicates.

# Optional challenge — Count prices within a budget
# Work through this one together when you are ready.
# Define count_affordable(menu, budget) to return the number of entries whose
# prices are less than or equal to budget.
# Use values(), a for loop, and a counter. Leave menu unchanged.
# Count equal prices separately when they belong to different entries.
# Return 0 for an empty menu or when no prices qualify.
# count_affordable({"tea": 3, "juice": 3, "cake": 5}, 3) => 2
# count_affordable({"tea": 3}, 2) => 0
# count_affordable({}, 10) => 0
# Write your code below:
 