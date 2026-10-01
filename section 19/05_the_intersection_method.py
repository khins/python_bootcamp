# Set intersection() — Study Summary
# Intersection = "What is in ALL of these sets?"
# Instructor summary:
# - An intersection contains only elements shared by all participating sets.
# - first.intersection(second) returns a NEW set and leaves both inputs unchanged.
# - first & second is the operator form when both operands are sets.
# - Elements present in only one input are excluded.
# - Sets with no shared elements produce an empty set, displayed as set().
# - Reversing two set operands produces equal intersection results.
# - Result order is unspecified; sorted() provides a predictable list display.
#
# Corrections to the transcript:
# - An element must occur in BOTH sets, not merely either one, to be included.
# - intersection() accepts iterable arguments, including lists and tuples,
#   and can accept multiple iterables in one call.
# - The & operator requires set operands (set or frozenset), not a plain list.
# - Equal integers and floats can match, such as 3 == 3.0.
# - Python does NOT promote intersection elements to the "more complex" type.
#   Do not depend on whether an equal int or float is retained in the result.
# - Equal set results need not contain the same object representatives.


# --- 1. Find shared favorites ---
candy_bars = {"Milky Way", "Snickers", "100 Grand"}
sweet_things = {"Sour Patch Kids", "Reese's Pieces", "Snickers"}
shared = candy_bars.intersection(sweet_things) # Return a new set with elements common to the set and all others.
print(sorted(shared))  # ['Snickers']
print(len(shared))     # 1
print(type(shared))    # <class 'set'>
# Snickers occurs in both inputs; every other name occurs in only one.
print(sorted(candy_bars))   # ['100 Grand', 'Milky Way', 'Snickers']
print(sorted(sweet_things)) # ["Reese's Pieces", 'Snickers', 'Sour Patch Kids']
# Neither source set changed.


# --- 2. Use the & operator ---
first = {"Rush", "Yes", "Genesis"}
second = {"Yes", "Genesis", "Kansas"}
print(sorted(first & second))  # ['Genesis', 'Yes']
print(first.intersection(second) == (first & second))  # True
print((first & second) == (second & first))            # True
# & means intersection here. The keyword and is a different operation:
print((first and second) is second)  # True — both sets are nonempty
# Boolean and returns an operand; it does not calculate shared elements.


# --- 3. No overlap, empty input, and a new result ---
print({1, 2}.intersection({3, 4}))  # set()
print({1, 2}.intersection(set()))  # set()
print(set() & {1, 2})             # set()

original = {"Rush", "Yes"}
common = original.intersection(original)
print(common == original)  # True — same contents
print(common is original)  # False — separate set objects
common.add("Genesis")
print(sorted(common))     # ['Genesis', 'Rush', 'Yes']
print(sorted(original))   # ['Rush', 'Yes']
# Changing the result's membership does not change the input set.


# --- 4. Pass iterables to the method ---
artists = {"Rush", "Yes", "Genesis"}
requests = ["Yes", "Yes", "Kansas"]
print(sorted(artists.intersection(requests)))  # ['Yes']
print(requests)  # ['Yes', 'Yes', 'Kansas']
# Repeated matches still appear only once in the result.
print(sorted(artists.intersection(("Rush", "Kansas"))))  # ['Rush']
# Leave this intentional error commented out:
# artists & requests  # TypeError: the right operand is a list
# You can explicitly convert the list for the operator form:
print(sorted(artists & set(requests)))  # ['Yes']

# Strings supply characters, and dictionaries supply keys:
print(sorted({"a", "b", "c"}.intersection("banana")))  # ['a', 'b']
print(sorted({"tea", "juice"}.intersection({"tea": 3, "cake": 5})))  # ['tea']


# --- 5. Find elements shared by three sets ---
alex = {"Rush", "Yes", "Genesis"}
kevin = {"Rush", "Yes", "Kansas"}
sam = {"Rush", "Genesis"}
print(sorted(alex.intersection(kevin, sam)))  # ['Rush']
print(sorted(alex & kevin & sam))            # ['Rush']
# Yes is shared by Alex and Kevin, but not Sam, so it is excluded.


# --- 6. Numeric equality, not type promotion ---
values = {3.0, 4.0, 5.0}
more_values = {3, 4, 5, 6}
common = values.intersection(more_values)
print(3 == 3.0)                   # True
print(common == {3, 4, 5})        # True
print(common == {3.0, 4.0, 5.0})  # True
print(len(common))               # 3
print(6 in common)               # False
print(common == more_values.intersection(values))  # True
# Equal numeric values match across these types. Test the contents by
# equality; do not predict a guaranteed int-versus-float representation.


# --- 7. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Give exact list order for sorted() output; raw set order is unspecified.
# Keep intentional-error examples commented out.

# Exercise 1 — Shared songs
# Predict all three outputs. Explain why only those titles are included.
first = {"YYZ", "Limelight", "Tom Sawyer"}
second = {"Roundabout", "YYZ", "Limelight"}
print(sorted(first.intersection(second)))
print(len(first & second))
print("Roundabout" in (first & second))
# ANSWER:
# outputs
# {"Limelight", "Roundabout", "Tom Sawyer", "YYZ"}
# 3
# False


# Exercise 2 — Inputs and result
# Predict all four outputs. Explain why adding to common does not change first.
first = {1, 2, 3}
second = {2, 3, 4}
common = first & second
common.add(9)
print(sorted(common))
print(sorted(first))
print(sorted(second))
print(common is first)
# ANSWER:
# outputs
# [2, 3, 9]
# [1, 2, 3]
# [2, 3, 4]
# False
# Explain why adding to common does not change first:
# common is a new set object created by the intersection.
# It does not reference the same set object as first.
# first  ──────────► {1, 2, 3}

# second ──────────► {2, 3, 4}

# first & second
#       │
#       ▼
#     {2, 3}
#       ▲
#       │
#     common
# mutates only that new set:

# first  ──────────► {1, 2, 3}

# second ──────────► {2, 3, 4}

# common ──────────► {2, 3, 9}
# first ───┐
#          ├────► {1, 2, 3}
# common ──┘


# Exercise 3 — Empty intersections
# Predict all three outputs. Explain why the first two results are empty.
print({"Rush"}.intersection({"Yes"}))
print({"Rush"} & set())
print(type({"Rush"} & set()))
# ANSWER:
# outputs
# set()
# set()
# <class 'set'>
# 1. Why does the first one produce set()?
# {"Rush"}.intersection({"Yes"})
# SET 1           SET 2

# {"Rush"}        {"Yes"}
#     │              │
#     └──── ??? ─────┘

# Nothing matches.
# The & operator is another way of doing an intersection:
# set1 & set2
# {"Rush"}       set()
#    │             │
#    │             │
#  "Rush"       NOTHING

#        ↓

# What exists in BOTH?

#        ↓

#     NOTHING
# Explain why the first two results are empty:
# There are no elements shared by both sets.

# Exercise 4 — Method versus operator
# Predict the first output. Name the error the final expression would raise
# and explain the difference in accepted inputs. Write a corrected operator
# expression using set(). Keep the error line commented out.
numbers = {1, 2, 3}
incoming = [2, 2, 4]
print(sorted(numbers.intersection(incoming)))
print(numbers.intersection({2, 2, 4}))
# print(numbers & incoming)  # Intentional error
# ANSWER:
# [2]
# TypeError: unsupported operand type(s) for &: 'set' and 'list'
#  Name the error the final expression would raise
# and explain the difference in accepted inputs. Write a corrected operator
# expression using set():
# intersection() can accept an iterable such as a list.
# The & operator requires set operands, so incoming must first
# be converted to a set with set(incoming).


# Exercise 5 — Shared by everyone
# Predict all three outputs. Explain why matching two groups is not enough
# to appear in the three-way intersection.
first = {"Rush", "Yes", "Genesis"}
second = {"Rush", "Yes"}
third = {"Rush", "Kansas"}
print(sorted(first & second))
print(sorted(first.intersection(second, third)))
print((first & second) == (second & first))
# ANSWER:
# outputs
# ['Rush', 'Yes']
# ['Rush']
# True
# ARTIST       first     second     third
# -----------------------------------------
# Rush           ✓         ✓          ✓
# Yes            ✓         ✓          ✗
# Genesis        ✓         ✗          ✗
# Kansas         ✗         ✗          ✓
# keep an artist only if there is a ✓ in every set being compared.

# Exercise 6 — Write your own shared favorites report
# 1. Create two sets of artist names with at least three names each.
#    Include two shared names and at least one name unique to each set.
# 2. Store their intersection using intersection().
# 3. Print the shared names with sorted() and print their count.
# 4. Calculate the intersection with & and print whether both results are equal.
# 5. Print both original sets with sorted() to show they remain unchanged.
# 6. Explain why a name found in only one set is excluded, and why reversing
#    the operands produces an equal result.
# Write your code below:
set_a = {"Geddy Lee", "Alex Lifeson", "Neil Peart"}
set_b = {"Geddy Lee", "Alex Lifeson", "Steve Howe"}

# Store the intersection using intersection()
shared = set_a.intersection(set_b)

# Print shared names and their count
print(sorted(shared))
print(len(shared))

# Calculate intersection using &
shared_operator = set_a & set_b

# Check whether both intersection results are equal
print(shared == shared_operator)

# Show that the original sets remain unchanged
print(sorted(set_a))
print(sorted(set_b))
# outputs
# ['Alex Lifeson', 'Geddy Lee']
# ['Alex Lifeson', 'Geddy Lee']
# {'Alex Lifeson', 'Geddy Lee', 'Neil Peart'}
# {'Alex Lifeson', 'Geddy Lee', 'Steve Howe'}
# Explain why a name found in only one set is excluded, and why reversing
# #    the operands produces an equal result.

# Optional challenge — Shared artists across three playlists
# Work through this one together when you are ready.
# Define shared_artists(first, second, third), accepting three lists of strings.
# Return a NEW alphabetically sorted LIST of artists appearing in all three.
# Use set(), intersection(), and sorted(). Leave all input lists unchanged.
# Repeated names count once. Matching is case-sensitive.
# Return [] if any list is empty or no artist appears in all three.
# shared_artists(['Rush', 'Yes', 'Rush'], ['Rush', 'Genesis'], ['Rush', 'Yes'])
# => ['Rush']
#  => []
# Explain why the result excludes artists found in only two playlists.
# Write your code below:

# Define.. accepting three lists of strings.
def shared_artists(first, second, third) -> list:
    # Return a NEW alphabetically sorted LIST of artists appearing in all three.
    # Use set(), intersection(), and sorted(). Leave all input lists unchanged.
    new_set = set(first)

    new_set = new_set.intersection(second)

    new_set = new_set.intersection(third)
    return sorted(new_set)

print(shared_artists(['Rush'], ['rush'], ['Rush'])) # => []
print(shared_artists([], ['Rush'], ['Rush'])) # => []
# Explain why the result excludes artists found in only two playlists:
# Artists found in only two playlists are excluded because an
# intersection across three collections only includes artists
# that appear in ALL THREE playlists.
# first
#   │
#   ▼
# {"Rush", "Yes"}
#   │
#   │ intersection(second)
#   ▼
# {"Rush"}
#   │
#   │ intersection(third)
#   ▼
# {"Rush"}
#   │
#   │ sorted()
#   ▼
# ["Rush"]