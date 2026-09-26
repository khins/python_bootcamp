# Set remove() and discard() — Study Summary
# Instructor summary:
# - remove(element) removes an existing element from a set.
# - remove(element) raises KeyError if the element is absent.
# - discard(element) removes an existing element and does nothing if absent.
# - Both methods mutate the existing set rather than create a new one.
# - Both return None when they complete normally, not the removed element.
# - Each call targets one element, not a position or a sequence of elements.
# - Sets contain unique elements, so there are no duplicate copies to remove.
#
# Clarifications to the transcript:
# - discard() tolerates missing elements; it does not suppress every possible
#   error. An invalid argument such as a list can still raise TypeError.
# - An unhandled KeyError stops normal execution; later statements do not run.
# - Set display order is unspecified. Examples use sorted() for clear output.
# - remove() is useful when absence should signal a problem; discard() is
#   useful when you simply want an element to be absent afterward.


# --- 1. Remove an existing element ---
agents = {"Mulder", "Scully", "Doggett", "Reyes"}
result = agents.remove("Doggett")
print(sorted(agents))  # ['Mulder', 'Reyes', 'Scully']
print(len(agents))     # 3
print(result)          # None
print("Doggett" in agents)  # False
# The method changes agents; result does not hold the removed name.


# --- 2. A missing element raises KeyError with remove() ---
agents = {"Mulder", "Scully", "Reyes"}
# Leave this intentional error commented out:
# agents.remove("Skinner")  # KeyError: 'Skinner'
print(sorted(agents))       # ['Mulder', 'Reyes', 'Scully']
# If the error line were uncommented and unhandled, this print would not run.
# The failed removal itself would not change the set's contents.


# --- 3. Discard existing and missing elements ---
agents = {"Mulder", "Scully", "Doggett", "Reyes"}
result = agents.discard("Doggett")
print(sorted(agents))  # ['Mulder', 'Reyes', 'Scully']
print(result)          # None

result = agents.discard("Skinner")
print(sorted(agents))  # ['Mulder', 'Reyes', 'Scully']
print(result)          # None
# Skinner was absent, so discard() made no change and execution continued.


# --- 4. Repeated calls and an empty set ---
songs = {"YYZ", "Limelight"}
songs.discard("YYZ")
songs.discard("YYZ")
print(sorted(songs))  # ['Limelight']
# Calling discard() again is harmless when the element is already absent.
songs.remove("Limelight")
print(songs)         # set()
# songs.remove("Limelight")  # KeyError: now that element is absent

empty = set()
print(empty.discard("YYZ"))  # None
print(len(empty))            # 0
# empty.remove("YYZ")        # KeyError


# --- 5. Aliases see mutations; copies remain separate ---
artists = {"Rush", "Yes", "Genesis"}
shared = artists
independent = set(artists)
artists.discard("Yes")
print(sorted(artists))      # ['Genesis', 'Rush']
print(sorted(shared))       # ['Genesis', 'Rush']
print(sorted(independent))  # ['Genesis', 'Rush', 'Yes']
print(shared is artists)    # True
# shared refers to the same set. set(artists) created a separate set earlier.
# Do not assign artists = artists.discard("Rush"): that would bind artists
# to None after mutating the set.


# --- 6. Target a whole element, not an index ---
groups = {(1, 2), (3, 4)}
groups.remove((1, 2))
print(sorted(groups))  # [(3, 4)]
# The tuple is one complete element.

numbers = {10, 20, 30}
numbers.discard(0)
print(sorted(numbers))  # [10, 20, 30]
# 0 means the value zero; it does not mean the first position.
# Leave these intentional errors commented out:
# numbers.remove(0)       # KeyError: zero is absent
# numbers.discard([10])   # TypeError: a list is unhashable
# numbers.remove(10, 20)  # TypeError: pass one element per call


# --- 7. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Predict the whole snippet, including all mutations and return values.
# Keep intentional-error calls commented out unless testing them separately.
# For raw sets, give contents without claiming a particular order.

# Exercise 1 — Remove a present element
# Predict all three outputs. Explain whether result contains the removed name.
# artists = {"Rush", "Yes", "Genesis"}
# result = artists.remove("Yes")
# print(sorted(artists))
# print(len(artists))
# print(result)
# ANSWER:


# Exercise 2 — Discard twice
# Predict all three outputs. Explain why the second discard() does not fail.
# songs = {"YYZ", "Limelight"}
# songs.discard("YYZ")
# result = songs.discard("YYZ")
# print(sorted(songs))
# print("YYZ" in songs)
# print(result)
# ANSWER:


# Exercise 3 — Trace an error
# If this complete snippet ran, what would print before the error?
# Name the error, identify its line, and explain whether "Finished" prints.
# Keep the snippet commented out.
# agents = {"Mulder", "Scully"}
# agents.remove("Mulder")
# print(sorted(agents))
# agents.remove("Mulder")
# print("Finished")
# ANSWER:


# Exercise 4 — Shared or independent?
# Predict all four outputs. Explain why only one of the other variables
# sees the removal performed through original.
# original = {"Rush", "Yes"}
# alias = original
# copied = set(original)
# original.discard("Rush")
# print(sorted(original))
# print(sorted(alias))
# print(sorted(copied))
# print(alias is original)
# ANSWER:


# Exercise 5 — Diagnose the assignment
# Predict both outputs. Explain the mistake and rewrite the code so artists
# remains a set with "Yes" removed, even if "Yes" was already absent.
# artists = {"Rush", "Yes"}
# artists = artists.discard("Yes")
# print(artists)
# print(type(artists))
# ANSWER:


# Exercise 6 — Write your own guest list cleanup
# 1. Create a set with four distinct guest names.
# 2. Use remove() to remove one guest who is present.
# 3. Use discard() to remove a different guest who is present.
# 4. Use discard() again for that same guest, storing and printing its result.
# 5. Print the remaining guests with sorted() and print the set's length.
# 6. Explain what would happen if step 4 used remove() instead, and why.
# Write your code below:


# Optional challenge — Remove unwanted artists from a copy
# Work through this one together when you are ready.
# Define without_artists(original, unwanted).
# original is a set of artist strings; unwanted is a list of artist strings.
# Return a NEW SET with all unwanted artists absent. Use set() to copy the
# original, then a for loop and discard(). Leave both inputs unchanged.
# Repeated or missing names in unwanted must not cause an error.
# without_artists({'Rush', 'Yes'}, ['Yes', 'Yes', 'Genesis']) => {'Rush'}
# without_artists(set(), ['Rush']) => set()
# without_artists({'Rush'}, []) => {'Rush'} (a different set object)
# Explain why discard() is appropriate for this function.
# Write your code below:
