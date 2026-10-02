# Set symmetric_difference() — Study Summary
# Instructor summary:
# - first.symmetric_difference(second) returns a NEW set of elements found
#   in either input, but NOT in both.
# - first ^ second is the operator form for set operands.
# - In a Venn diagram, keep both outer regions and exclude the overlap.
# - Reversing the inputs produces the same result.
# - Neither input is changed by symmetric_difference() or the plain ^ operator.
# - The ^ symbol is called a caret (Shift + 6 on a US keyboard).
#
# Clarifications and connections:
# - symmetric_difference() accepts one iterable, such as a set, list, or tuple.
# - The ^ operator requires set operands (set or frozenset).
# - Intersection (&) keeps shared elements; union (|) keeps all elements;
#   difference (-) keeps only left-side elements absent from the right;
#   symmetric difference (^) keeps elements exclusive to either side.
# - Set order is unspecified; use sorted() for a predictable list display.


# --- 1. Find sweets that appear in exactly one set ---
candy_bars = {"Milky Way", "Snickers", "100 Grand"}
sweet_things = {"Sour Patch Kids", "Reese's Pieces", "Snickers"}
exclusive_sweets = candy_bars.symmetric_difference(sweet_things)
print(sorted(exclusive_sweets))
# Expected: ['100 Grand', 'Milky Way', "Reese's Pieces", 'Sour Patch Kids']
print(len(exclusive_sweets))  # 4
print(type(exclusive_sweets))  # <class 'set'>
print("Snickers" in exclusive_sweets)  # False
# Snickers appears in both inputs, so it is excluded.


# --- 2. Use ^ and reverse the inputs ---
print(sorted(candy_bars ^ sweet_things))
print(sorted(sweet_things.symmetric_difference(candy_bars)))
print(sorted(sweet_things ^ candy_bars))
# Each line prints the same sorted list as the first example.
print((candy_bars ^ sweet_things) == (sweet_things ^ candy_bars))  # True
print(sorted(candy_bars))  # ['100 Grand', 'Milky Way', 'Snickers']
print(sorted(sweet_things))  # ["Reese's Pieces", 'Snickers', 'Sour Patch Kids']
# Both original sets remain unchanged.


# --- 3. Compare the four operations ---
first = {1, 2, 3}
second = {3, 4, 5}
print(sorted(first & second))  # [3] — shared
print(sorted(first | second))  # [1, 2, 3, 4, 5] — combined
print(sorted(first - second))  # [1, 2] — only in first
print(sorted(second - first))  # [4, 5] — only in second
print(sorted(first ^ second))  # [1, 2, 4, 5] — exclusive to either input
print((first ^ second) == ((first | second) - (first & second)))  # True
print((first ^ second) == ((first - second) | (second - first)))  # True


# --- 4. Empty, equal, and non-overlapping inputs ---
artists = {"Rush", "Yes"}
print(sorted(artists ^ set()))  # ['Rush', 'Yes']
print(sorted(set() ^ artists))  # ['Rush', 'Yes']
print(artists ^ artists)  # set()
print(sorted(artists ^ {"Genesis"}))  # ['Genesis', 'Rush', 'Yes']
# Equal inputs have no exclusive elements. Non-overlapping inputs contribute
# every element, so their symmetric difference equals their union.

result = artists.symmetric_difference(set())
print(result == artists)  # True
print(result is artists)  # False
result.remove("Rush")
print(sorted(result))  # ['Yes']
print(sorted(artists))  # ['Rush', 'Yes']
# The result is a separate set, even when its contents equal an input.


# --- 5. Supply an iterable to the method ---
artists = {"Rush", "Yes"}
other_artists = ["Yes", "Genesis", "Genesis"]
print(sorted(artists.symmetric_difference(other_artists)))  # ['Genesis', 'Rush']
# Repeated values in the iterable count as a single distinct element.
# Leave this intentional error commented out:
# artists ^ other_artists  # TypeError: a list is not a set operand
print(sorted(artists ^ set(other_artists)))  # ['Genesis', 'Rush']


# --- 6. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Give exact list order for sorted() outputs; raw set order is unspecified.

# Exercise 1 — Exclusive users
# Predict both outputs. 
morning_users = {"alex", "sam", "lee"}
evening_users = {"sam", "jo"}
print(sorted(morning_users.symmetric_difference(evening_users)))
print(sorted(evening_users ^ morning_users))
# ANSWER:
# outputs
# ["alex", "jo", "lee"]
# ["alex", "jo", "lee"]
# Explain why "sam" is excluded:
# "sam" is excluded because symmetric difference includes elements
# that appear in either set, but NOT in both sets.
# Since "sam" appears in both sets, it is excluded.

# alex → morning only  → INCLUDE
# sam  → BOTH          → EXCLUDE
# lee  → morning only  → INCLUDE
# jo   → evening only  → INCLUDE

# * SYMMETRIC DIFFERENCE
# A.symmetric_difference(B)
# A ^ B
#
# Keep elements that are in ONE set, but NOT BOTH.

# A | B    UNION
#          Everything from either set

# A & B    INTERSECTION
#          What's in both

# A - B    DIFFERENCE
#          What's in A but not B
#          Direction matters

# A ^ B    SYMMETRIC DIFFERENCE
#          What's in either set, but NOT both

# direction doesn't matter for symmetric difference.



# Exercise 2 — Compare operations
# Predict all four outputs 
first = {1, 2, 3}
second = {2, 3, 4}
print(sorted(first & second))
print(sorted(first | second))
print(sorted(first - second))
print(sorted(first ^ second))
# ANSWER:
# describe what each operation keeps:
# [2, 3] - keeps what common between first and second
# [1, 2, 3, 4] - is union of both without duplicating
# [1] - in other words {1, 2, 3} - {2, 3, 4} = 1
# [1, 4] - the intersection of both

# ANSWER:
# describe what each operation keeps:

# [2, 3]
# & = INTERSECTION
# Keeps elements common to BOTH first and second.

# [1, 2, 3, 4]
# | = UNION
# Keeps all unique elements from BOTH sets without duplicates.

# [1]
# - = DIFFERENCE
# Keeps elements in first that are NOT in second.
# {1, 2, 3} - {2, 3, 4} = {1}

# [1, 4]
# ^ = SYMMETRIC DIFFERENCE
# Keeps elements found in EITHER set, but NOT in both.

# first  = {1, 2, 3}
# second = {2, 3, 4}

# 1 → first only   → KEEP
# 2 → both         → REMOVE
# 3 → both         → REMOVE
# 4 → second only  → KEEP

# first ^ second
#        ↓
#      {1, 4}

# ! IMPORTANT
# * &  INTERSECTION          → BOTH
# * |  UNION                 → EVERYTHING UNIQUE
# * -  DIFFERENCE            → LEFT but NOT RIGHT
# * ^  SYMMETRIC DIFFERENCE  → EITHER but NOT BOTH

# Exercise 3 — Equal and empty inputs
# Predict all three outputs.
songs = {"YYZ", "Limelight"}
print(songs ^ songs)
print(sorted(songs ^ set()))
print(sorted(set() ^ songs))
# ANSWER:
# set()
# ['Limelight', 'YYZ']
# ['Limelight', 'YYZ']

# songs ^ set()
#        ↓
# {"YYZ", "Limelight"}

# set() ^ songs
#        ↓
# {"YYZ", "Limelight"}



# Exercise 4 — Diagnose an unused result
# Predict the output. 
artists = {"Rush", "Yes"}
artists.symmetric_difference({"Yes", "Genesis"})
print(sorted(artists))
# ANSWER:
# Then save the symmetric difference in a new variable
# # and print it, leaving artists unchanged:
diff = artists.symmetric_difference({"Yes", "Genesis"})
print(sorted(diff))
# ['Rush', 'Yes']
# ['Genesis', 'Rush']
print(artists)
# {'Rush', 'Yes'}



# Exercise 5 — Write your own playlist comparison
# Write your code below:
# 1. Create two sets of song titles with at least one shared title and at
#    least one title exclusive to each set.
set_a = {
    "Peaceful Easy Feeling",
    "Tequila Sunrise",
    "Already Gone",
}

set_b = {
    "Tequila Sunrise",
    "Lyin' Eyes",
    "New Kid in Town",
}

# 2. Store their symmetric difference and print it using sorted().
difference = set_a.symmetric_difference(set_b)
print(sorted(difference)) # => ['Already Gone', "Lyin' Eyes", 'New Kid in Town', 'Peaceful Easy Feeling']

# 3. Use ^ and check that it produces the same result as the method.
print(set_a ^ set_b == difference) # => True

# 4. Reverse the inputs and check that the result is still equal.
print(set_b ^ set_a == set_a ^ set_b) # => True

# 5. Print both original sets to show that neither was changed.
print(sorted(set_a)) # => ['Already Gone', 'Peaceful Easy Feeling', 'Tequila Sunrise']
print(sorted(set_b)) # => ["Lyin' Eyes", 'New Kid in Town', 'Tequila Sunrise']

#                     set_a        set_b

# Peaceful Easy Feeling   ✓            ✗    → KEEP
# Tequila Sunrise         ✓            ✓    → EXCLUDE
# Already Gone            ✓            ✗    → KEEP
# Lyin' Eyes              ✗            ✓    → KEEP
# New Kid in Town         ✗            ✓    → KEEP

# symmetric_difference() and ^ return a NEW set containing elements
# found in either set, but NOT in both.
# "Tequila Sunrise" is excluded because it appears in both sets.
# Reversing the sets produces the same result because symmetric
# difference is not directional.

# &  intersection          -> BOTH
# |  union                 -> ALL UNIQUE
# -  difference            -> LEFT but NOT RIGHT
# ^  symmetric difference  -> EITHER but NOT BOTH

# - cares about direction; ^ does not.