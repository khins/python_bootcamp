# Set difference() — Study Summary
# Instructor summary:
# - first.difference(second) returns a NEW set containing elements in first
#   that are NOT in second.
# - first - second is the operator form for set operands.
# - Neither input is changed by difference() or by the plain - operator.
# - The left-hand set supplies the candidates; the right-hand set excludes matches.
# - Reversing the operands can change the result: direction matters.
# - Elements found only in the right-hand set are never added to the result.
# - Set order is unspecified; use sorted() for a predictable list display.
#
# Clarifications and connections:
# - Reversing the inputs does not ALWAYS produce different results. Equal
#   sets, for example, produce an empty difference in either direction.
# - difference() accepts iterable arguments such as lists and tuples, and
#   can accept multiple iterables in one call.
# - The - operator requires set operands (set or frozenset), not a plain list.
# - Intersection (&) keeps shared elements; union (|) combines all elements;
#   difference (-) keeps elements from the left input absent from the right.
# - This is element exclusion, not arithmetic subtraction of numeric members.


# --- 1. Find candy bars absent from the other set ---
candy_bars = {"Milky Way", "Snickers", "100 Grand"}
sweet_things = {"Sour Patch Kids", "Reese's Pieces", "Snickers"}
exclusive_bars = candy_bars.difference(sweet_things)
print(sorted(exclusive_bars))  # ['100 Grand', 'Milky Way']
print(len(exclusive_bars))     # 2
print(type(exclusive_bars))    # <class 'set'>
# Snickers is excluded because it appears in sweet_things too.
# Sour Patch Kids and Reese's Pieces were never candidates: they are not
# in candy_bars, the set on which difference() was called.


# --- 2. Use - and reverse the direction ---
print(sorted(candy_bars - sweet_things))  # ['100 Grand', 'Milky Way']
print(sorted(sweet_things.difference(candy_bars)))
# Expected: ["Reese's Pieces", 'Sour Patch Kids']
print(sorted(sweet_things - candy_bars))
# Expected: ["Reese's Pieces", 'Sour Patch Kids']
print((candy_bars - sweet_things) == (sweet_things - candy_bars))  # False
# Read A - B as "start with A, then exclude anything found in B."
print(sorted(candy_bars))   # ['100 Grand', 'Milky Way', 'Snickers']
print(sorted(sweet_things)) # ["Reese's Pieces", 'Snickers', 'Sour Patch Kids']
# Both original sets remain unchanged.


# --- 3. Compare the three operations ---
first = {1, 2, 3}
second = {3, 4}
print(sorted(first & second))  # [3] — shared
print(sorted(first | second))  # [1, 2, 3, 4] — combined
print(sorted(first - second))  # [1, 2] — only in first
print(sorted(second - first))  # [4] — only in second
# The result of first - second contains original elements 1 and 2.
# It does not calculate differences such as 1 - 3 or 2 - 4.


# --- 4. Empty, equal, and non-overlapping inputs ---
artists = {"Rush", "Yes"}
print(sorted(artists - set()))         # ['Rush', 'Yes']
print(set() - artists)                 # set()
print(artists - artists)              # set()
print(sorted(artists - {"Genesis"}))  # ['Rush', 'Yes']
# An empty exclusion set removes nothing. An empty starting set has no
# candidates. A set compared with itself has no exclusive elements.

result = artists.difference(set())
print(result == artists)  # True
print(result is artists)  # False
result.remove("Rush")
print(sorted(result))     # ['Yes']
print(sorted(artists))    # ['Rush', 'Yes']
# Even when all original elements survive, the result is a separate set.


# --- 5. Exclude elements supplied by iterables ---
artists = {"Rush", "Yes", "Genesis"}
unwanted = ["Yes", "Yes", "Kansas"]
print(sorted(artists.difference(unwanted)))  # ['Genesis', 'Rush']
print(unwanted)                             # ['Yes', 'Yes', 'Kansas']
# Repeated exclusions have no additional effect. Missing names cause no error.
# Leave this intentional error commented out:
# artists - unwanted  # TypeError: a list is not a set operand
print(sorted(artists - set(unwanted)))  # ['Genesis', 'Rush']

# Dictionaries supply keys unless you choose another view:
songs = {"YYZ", "Limelight", "Roundabout"}
played = {"YYZ": "Rush", "Roundabout": "Yes"}
print(sorted(songs.difference(played)))  # ['Limelight']
# Strings supply individual characters:
print(sorted({"a", "b", "c"}.difference("banana")))  # ['c']


# --- 6. Exclude elements from multiple collections ---
all_artists = {"Rush", "Yes", "Genesis", "Kansas"}
first_exclusions = {"Yes"}
second_exclusions = {"Genesis", "Yes"}
remaining = all_artists.difference(first_exclusions, second_exclusions)
print(sorted(remaining))  # ['Kansas', 'Rush']
print(sorted(all_artists - first_exclusions - second_exclusions))
# Expected: ['Kansas', 'Rush']
print(remaining == (all_artists - (first_exclusions | second_exclusions)))  # True
# An element is excluded if it occurs in ANY exclusion collection.
# This is different from excluding only their intersection.
print(sorted(all_artists))  # ['Genesis', 'Kansas', 'Rush', 'Yes']


# --- 7. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Give exact list order for sorted() outputs; raw set order is unspecified.
# Keep intentional-error examples commented out.

# Exercise 1 — Left-side candidates
# Predict all three outputs. Explain why Kansas cannot appear in remaining.
# favorites = {"Rush", "Yes", "Genesis"}
# excluded = {"Yes", "Kansas"}
# remaining = favorites.difference(excluded)
# print(sorted(remaining))
# print(len(remaining))
# print("Kansas" in remaining)
# ANSWER:


# Exercise 2 — Direction matters
# Predict all three outputs. Explain why the first two results differ.
# first = {1, 2, 3}
# second = {3, 4, 5}
# print(sorted(first - second))
# print(sorted(second - first))
# print(sorted(first & second))
# ANSWER:


# Exercise 3 — Empty and equal inputs
# Predict all four outputs. Explain why subtracting an empty set differs
# from subtracting a set from itself.
# artists = {"Rush", "Yes"}
# print(sorted(artists - set()))
# print(set() - artists)
# print(artists - artists)
# print(sorted(artists - {"Kansas"}))
# ANSWER:


# Exercise 4 — A new result
# Predict all four outputs. Explain why removing from remaining does not
# remove anything from original.
# original = {"Rush", "Yes", "Genesis"}
# remaining = original.difference({"Yes"})
# remaining.remove("Rush")
# print(sorted(remaining))
# print(sorted(original))
# print(remaining is original)
# print("Yes" in original)
# ANSWER:


# Exercise 5 — Diagnose an unused result
# Predict the output. Explain why the excluded artist is still present.
# Write a corrected version that saves the difference in a new variable
# called remaining and prints it, leaving artists unchanged.
# artists = {"Rush", "Yes"}
# artists.difference(["Yes"])
# print(sorted(artists))
# ANSWER:


# Exercise 6 — Write your own unplayed songs report
# 1. Create a set of at least four song titles and a separate set of played
#    titles. Include two titles from the first set and one outside it.
# 2. Use difference() to store the titles that have not been played.
# 3. Print those titles with sorted() and print their count.
# 4. Use - and print whether its result equals the method result.
# 5. Print the reversed difference and both unchanged input sets with sorted().
# 6. Explain what the reversed difference means and why a played title absent
#    from the original collection does not appear in the unplayed result.
# Write your code below:


# Optional challenge — Available artists after two exclusions
# Work through this one together when you are ready.
# Define available_artists(candidates, unavailable, already_booked).
# All three arguments are lists of artist strings.
# Return a NEW alphabetically sorted LIST of distinct candidates that appear
# in neither unavailable nor already_booked.
# Use set(), difference(), and sorted(). Leave all inputs unchanged.
# Matching is case-sensitive. Missing or repeated exclusions cause no error.
# available_artists(['Rush', 'Yes', 'Rush', 'Genesis'], ['Yes'], ['Genesis'])
# => ['Rush']
# available_artists(['Rush'], ['rush'], []) => ['Rush']
# available_artists([], ['Yes'], []) => []
# Explain why an artist appearing in either exclusion list must be omitted.
# Write your code below:
