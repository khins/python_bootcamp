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
# candy_bars                         sweet_things
# ─────────────────                  ───────────────────
# Milky Way                          Sour Patch Kids
# Snickers          ← shared →       Snickers
# 100 Grand                          Reese's Pieces

#         candy_bars.difference(sweet_things)
#                        ↓
#              {"Milky Way", "100 Grand"}

# # UNION
# A | B == B | A             # True

# # INTERSECTION
# A & B == B & A             # True

# # DIFFERENCE
# A - B == B - A             # Usually False

# ! IMPORTANT
# * UNION         A | B  -> everything unique from A and B
# * INTERSECTION  A & B  -> elements in BOTH A and B
# * DIFFERENCE    A - B  -> elements in A but NOT in B

# ! Difference has direction: A - B is not generally the same as B - A.


# --- 2. Use - and reverse the direction ---
# Read A - B as "start with A, then exclude anything found in B."
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
# candy_bars - sweet_things

# START with candy_bars:
#     Milky Way       ✓
#     Snickers        ✗  also exists in sweet_things
#     100 Grand       ✓

# RESULT:
#     {'Milky Way', '100 Grand'}

# Reverse
# sweet_things - candy_bars

# START with sweet_things:
#     Sour Patch Kids   ✓
#     Reese's Pieces    ✓
#     Snickers          ✗  also exists in candy_bars

# RESULT:
#     {"Sour Patch Kids", "Reese's Pieces"}

# ! IMPORTANT
# * UNION
# A | B
# Direction doesn't matter.
# A | B == B | A

# * INTERSECTION
# A & B
# Direction doesn't matter.
# A & B == B & A

# ! DIFFERENCE
# A - B
# DIRECTION MATTERS.
# "Start with A; exclude anything also in B."
# A - B is generally NOT equal to B - A.


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
# Predict all three outputs. 
favorites = {"Rush", "Yes", "Genesis"}
excluded = {"Yes", "Kansas"}
remaining = favorites.difference(excluded)
print(sorted(remaining))
print(len(remaining))
print("Kansas" in remaining)
# ANSWER:
# outputs
# ["Genesis", "Rush"]
# 2
# False

# Explain why Kansas cannot appear in remaining:
# since by definition elements in A but NOT in B
# Kansas cannot appear in remaining because difference() only considers
# elements from favorites (the left-side set). Kansas is not in favorites,
# so it was never a candidate for the result.
# So difference() doesn't pull anything from the right-hand set


# Exercise 2 — Direction matters
# Predict all three outputs. 
first = {1, 2, 3}
second = {3, 4, 5}
print(sorted(first - second))
print(sorted(second - first))
print(sorted(first & second))
# ANSWER:
# outputs
# [1, 2]
# [4, 5]
#       BOTH?
# 1  → first only
# 2  → first only
# 3  → BOTH       ✓
# 4  → second only
# 5  → second only
# [3]

# Explain why the first two results differ:
# # Explain why the first two results differ:
# Difference is directional. first - second starts with first and removes
# anything also found in second, while second - first starts with second
# and removes anything also found in first.

# * |  UNION        → everything unique from BOTH sets combined
# * &  INTERSECTION → what's shared by BOTH sets
# * -  DIFFERENCE   → what's in the LEFT set but NOT the right

# Exercise 3 — Empty and equal inputs
# Predict all four outputs. 
artists = {"Rush", "Yes"}
print(sorted(artists - set()))
print(set() - artists)
print(artists - artists)
print(sorted(artists - {"Kansas"}))
# ANSWER:
# outputs
# ['Rush', 'Yes']
# set()
# set()
# ['Rush', 'Yes']

# Explain why subtracting an empty set differs from subtracting a set from itself:
# Subtracting an empty set removes nothing because none of the
# elements from the left set are found in the empty set.
#
# Subtracting a set from itself removes everything because every
# element in the left set is also found in the right set.
# A - empty
# ─────────
# Start with A.
# Right side contains nothing.
# → REMOVE NOTHING


# A - A
# ─────
# Start with A.
# Right side contains everything A contains.
# → REMOVE EVERYTHING

# ! IMPORTANT
# * A - set() = A
#   Nothing exists on the right to remove.

# * A - A = set()
#   Everything on the left also exists on the right.

# mental rule "what's in the LEFT but NOT the right"




# Exercise 4 — A new result
# Predict all four outputs. 
original = {"Rush", "Yes", "Genesis"}
remaining = original.difference({"Yes"})
remaining.remove("Rush")
print(sorted(remaining))
print(sorted(original))
print(remaining is original)
print("Yes" in original)
# ANSWER:
# outputs
# mental note: {"Rush", "Yes", "Genesis"} - {"Yes"} = ['Rush', 'Genesis']
# ['Genesis']
# ["Genesis", "Rush", "Yes"]
# False
# True

# Explain why removing from remaining does not remove anything from original:
# because they are separate objects ;

# difference() creates and returns a NEW set object.
# remaining and original therefore reference separate set objects.
# Removing an element from remaining does not modify original.

# original
#    │
#    └────► {"Rush", "Yes", "Genesis"}

#               difference({"Yes"})
#                        │
#                        ▼

# remaining
#    │
#    └────► {"Rush", "Genesis"}
#                        │
#                   remove("Rush")
#                        ▼
#                   {"Genesis"}

# * difference() → returns a NEW set
# ! remove()     → MUTATES the set it is called on
# some set methods produce a new object, while others modify the existing object.


# Exercise 5 — Diagnose an unused result
# Predict the output. 

artists = {"Rush", "Yes"}
artists.difference(["Yes"])
print(sorted(artists))
# ANSWER:

# Write a corrected version that saves the difference in a new variable
# called remaining and prints it, leaving artists unchanged.
artists = {"Rush", "Yes"}
remaining = artists.difference(["Yes"])
print(sorted(remaining))
print(artists)

# Explain why the excluded artist is still present: the excluded artist was still present because difference returns a NEW set
# but that was never assigned to anything ;
# The excluded artist is still present in artists because difference()
# returns a NEW set rather than modifying the original set.
# The first difference() result was never assigned to a variable.
# * difference() → returns a NEW set
#   Save the return value if you want to use it.
# * The - operator requires set operands.

# artists ─────► {"Rush", "Yes"}

#                difference(["Yes"])
#                        ↓
#                    {"Rush"}
#                        ↑
#                  not saved



# Exercise 6 — Write your own unplayed songs report
# 1. Create a set of at least four song titles and a separate set of played
#    titles. Include two titles from the first set and one outside it.
# Write your code below:
song_titles = {
    "Hotel California",
    "Desperado",
    "Take It Easy",
    "Life in the Fast Lane",
}

played_titles = {
    "Hotel California",
    "Desperado",
    "One of These Nights",
}

# 2. Use difference() to store the titles that have not been played.
not_played = song_titles.difference(played_titles)

# 3. Print those titles with sorted() and print their count.
print(sorted(not_played)) # => ['Life in the Fast Lane', 'Take It Easy']
print(len(not_played)) # => 2

# 4. Use - and print whether its result equals the method result.
print(sorted(song_titles - played_titles)) # => ['Life in the Fast Lane', 'Take It Easy']
print((song_titles - played_titles) == not_played)

# 5. Print the reversed difference and both unchanged input sets with sorted().
print(played_titles - song_titles) # => {'One of These Nights'}
print(sorted(song_titles)) # => {'Take It Easy', 'Hotel California', 'Life in the Fast Lane', 'Desperado'}
print(sorted(played_titles)) # => {'One of These Nights', 'Desperado', 'Hotel California'}

# 6. Explain what the reversed difference means and why a played title absent
#    from the original collection does not appear in the unplayed result:
# the reversed difference is just the played - the song titles instead therefore goes back to the rule
# "what's in the LEFT but NOT the right"; 
# The reversed difference starts with played_titles and keeps titles
# that are NOT in song_titles. Therefore, "One of These Nights" is
# returned because it exists in played_titles but not song_titles.
#
# "One of These Nights" does not appear in not_played because
# song_titles is the left-side set for that difference. Since
# "One of These Nights" was never in song_titles, it was never
# a candidate for the unplayed result.

# song_titles - played_titles

# Hotel California       → in played_titles → REMOVE
# Desperado              → in played_titles → REMOVE
# Take It Easy           → not in played    → KEEP
# Life in the Fast Lane  → not in played    → KEEP

# Result:
# {'Take It Easy', 'Life in the Fast Lane'}

# song_titles - played_titles
# ───────────────────────────
# "What songs in my collection have NOT been played?"

# → Take It Easy
# → Life in the Fast Lane


# played_titles - song_titles
# ───────────────────────────
# "What played songs are NOT in my original collection?"

# → One of These Nights


# Optional challenge — Available artists after two exclusions
# Work through this one together when you are ready.
# Write your code below:
# Define available_artists(candidates, unavailable, already_booked).
# Return a NEW alphabetically sorted LIST of distinct candidates that appear
def available_artists(candidates, unavailable, already_booked) -> list:
    # All three arguments are lists of artist strings in neither unavailable nor already_booked.
    # Use set(), difference(), and sorted(). Leave all inputs unchanged.
    # Matching is case-sensitive. Missing or repeated exclusions cause no error.
    new_list = set(candidates).difference(unavailable).difference(already_booked)
    return sorted(new_list)

print(available_artists(['Rush', 'Yes', 'Rush', 'Genesis'], ['Yes'], ['Genesis'])) # => ['Rush']
print(available_artists(['Rush'], ['rush'], [])) #  => ['Rush']
print(available_artists([], ['Yes'], [])) # => []

# Explain why an artist appearing in either exclusion list must be omitted.
# An artist appearing in either exclusion list must be omitted because
# each difference() removes artists found in that exclusion list.
# The first difference() removes unavailable artists, and the second
# difference() removes already-booked artists. Therefore, an artist
# must be absent from BOTH exclusion lists to remain available.

# Candidates:
# Rush, Yes, Genesis

# Unavailable:
# Yes              → REMOVE Yes

# Already booked:
# Genesis          → REMOVE Genesis

# Remaining:
# Rush

# The key phrase is:
# An artist must be in candidates AND not appear in either exclusion list.
# chained code works nicely