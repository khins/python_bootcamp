# Set add() and update() methods — Study Summary
# Instructor summary:
# - add(element) adds one hashable element to an existing set.
# - update(iterable) adds the elements supplied by an iterable.
# - Both methods mutate the existing set and return None.
# - Existing elements are not added again; duplicates do not increase length.
# - Sets do not guarantee insertion order. Adding is not appending to a position.
# - update() accepts lists, tuples, sets, strings, and other iterables.
# - All elements being added must be hashable.
#
# Corrections and clarifications:
# - Hashable is the precise requirement, rather than simply immutable.
#   A tuple containing a list cannot be added to a set.
# - Unspecified order does not mean the set randomly shuffles on every use.
# - update() can accept multiple iterables in one call.
# - add("Rush") adds one whole string; update("Rush") adds its characters.
# - A dictionary passed to update() supplies its keys, not its values.


# --- 1. Add one element ---
disney_characters = {"Mickey Mouse", "Minnie Mouse", "Elsa"}
result = disney_characters.add("Ariel")
print(sorted(disney_characters))
# Expected: ['Ariel', 'Elsa', 'Mickey Mouse', 'Minnie Mouse']
print(len(disney_characters))  # 4
print(result)                 # None
# sorted() gives a predictable display without changing the set's type.

disney_characters.add("Elsa")
print(len(disney_characters))  # 4 — Elsa was already present


# --- 2. Update from lists and tuples ---
disney_characters.update(["Donald Duck", "Goofy"])
print(sorted(disney_characters))
# Expected: ['Ariel', 'Donald Duck', 'Elsa', 'Goofy', 'Mickey Mouse', 'Minnie Mouse']

disney_characters.update(("Simba", "Pluto", "Mickey Mouse"))
print(sorted(disney_characters))
# Expected: ['Ariel', 'Donald Duck', 'Elsa', 'Goofy', 'Mickey Mouse', 'Minnie Mouse', 'Pluto', 'Simba']
print(len(disney_characters))  # 8
# Only Simba and Pluto were new in the second update.


# --- 3. One object versus its elements ---
whole_names = set()
whole_names.add("Rush")
print(sorted(whole_names))  # ['Rush']

letters = set()
letters.update("Rush")
print(sorted(letters))      # ['R', 'h', 's', 'u']
# Wrap a string in a list if update() should add it as one element:
whole_names.update(["Yes", "Rush"])
print(sorted(whole_names))  # ['Rush', 'Yes']

one_tuple = set()
one_tuple.add((1, 2))
print(sorted(one_tuple))    # [(1, 2)]
separate_numbers = set()
separate_numbers.update((1, 2))
print(sorted(separate_numbers))  # [1, 2]
# add() keeps the tuple whole; update() iterates over its elements.


# --- 4. Multiple iterables and dictionary inputs ---
artists = {"Rush"}
artists.update(["Yes", "Rush"], ("Genesis",), {"Kansas"})
print(sorted(artists))  # ['Genesis', 'Kansas', 'Rush', 'Yes']
artists.update([])
print(len(artists))     # 4 — an empty iterable adds nothing

songs = {"YYZ": "Rush", "Roundabout": "Yes"}
titles = set()
titles.update(songs)
print(sorted(titles))   # ['Roundabout', 'YYZ']
performers = set()
performers.update(songs.values())
print(sorted(performers))  # ['Rush', 'Yes']
# Choose the dictionary view that supplies the elements you need.


# --- 5. Mutation, aliases, and return values ---
favorites = {"Rush"}
shared = favorites
result = favorites.update(["Yes", "Rush"])
print(sorted(favorites))      # ['Rush', 'Yes']
print(sorted(shared))         # ['Rush', 'Yes']
print(shared is favorites)    # True
print(result)                 # None
# Both names refer to the same set, so both see the mutation.
# Do not write favorites = favorites.add("Genesis") or assign update()'s
# result back to favorites: that would rebind the name to None.


# --- 6. Valid inputs and common mistakes ---
numbers = {1}
numbers.update([2, 3, 3])
print(sorted(numbers))  # [1, 2, 3]
# The input list is iterable; its integer elements are hashable.
# Leave these intentional errors commented out:
# numbers.add([2, 3])       # TypeError: the list itself is unhashable
# numbers.update(4)         # TypeError: an integer is not iterable
# numbers.add(4, 5)         # TypeError: add() takes one element
# numbers.add((4, [5]))     # TypeError: the tuple contains an unhashable list
# numbers.update([[4, 5]])  # TypeError: the iterable supplies a list element
# To add one integer use add(4); to add several use update([4, 5]).


# --- 7. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Predict the entire snippet, including all mutations.
# sorted() outputs have a definite order; raw set order is unspecified.
# Keep intentional-error lines commented out.

# Exercise 1 — New and duplicate elements
# Predict all three outputs. Explain why the second add() does not grow the set.
# artists = {"Rush", "Yes"}
# artists.add("Genesis")
# artists.add("Rush")
# print(sorted(artists))
# print(len(artists))
# print("Genesis" in artists)
# ANSWER:


# Exercise 2 — Update from an iterable
# Predict all three outputs. Explain what update() does with each list element.
# numbers = {1, 3}
# incoming = [3, 4, 4, 5]
# numbers.update(incoming)
# print(sorted(numbers))
# print(len(numbers))
# print(incoming)
# ANSWER:


# Exercise 3 — A string is iterable
# Predict all three outputs. Explain why the two sets contain different elements.
# first = set()
# second = set()
# first.add("Yes")
# second.update("Yes")
# print(sorted(first))
# print(sorted(second))
# print(len(first), len(second))
# ANSWER:


# Exercise 4 — Shared set and returned value
# Predict all four outputs. Explain why shared changes and result is not a set.
# artists = {"Rush"}
# shared = artists
# result = artists.update(("Yes", "Rush"))
# print(sorted(artists))
# print(sorted(shared))
# print(shared is artists)
# print(result)
# ANSWER:


# Exercise 5 — Diagnose add() versus update()
# The goal is to add the individual integers 2 and 3 to numbers.
# Explain why the attempted call raises TypeError. Write a corrected call
# using update(), then predict sorted(numbers) after your correction.
# numbers = {1}
# numbers.add([2, 3])  # Intentional error: keep commented out.
# ANSWER:


# Exercise 6 — Write your own growing artist set
# 1. Create a set containing three distinct artist names.
# 2. Use add() to add one new artist, then add an existing artist again.
# 3. Use update() with a list containing two new artists and one existing artist.
# 4. Print a sorted list of the final artists and the final set length.
# 5. Store the return value of a separate add() call for an existing artist
#    in a variable, and print that variable.
# 6. Explain why duplicates do not increase the count and why the stored
#    return value differs from the set you changed.
# Write your code below:


# Optional challenge — Extend a copied collection
# Work through this one together when you are ready.
# Define expanded_artists(original, additions).
# original is a set of artist strings; additions is a list of artist strings.
# Return a NEW SET containing the original artists and all additions.
# Use set() to make a separate set, then update() to add the new artists.
# Leave both inputs unchanged; duplicates should appear only once.
# expanded_artists({'Rush'}, ['Yes', 'Rush']) => {'Rush', 'Yes'} (order unspecified)
# expanded_artists(set(), []) => set()
# expanded_artists({'Rush'}, []) => {'Rush'} (a different set object)
# Explain why returning the result of update() directly would be incorrect.
# Write your code below:
