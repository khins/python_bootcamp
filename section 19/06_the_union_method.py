# Set union() — Study Summary
# Original learning content — no instructor transcript was provided.
#
# - A union contains every distinct element found in any of its inputs.
# - first.union(second) returns a NEW set and leaves both inputs unchanged.
# - first | second is the operator form for set operands.
# - Shared elements appear once, just like all other elements in a set.
# - union() accepts iterable arguments, including lists and tuples.
# - union() can combine multiple iterables in one call.
# - The | operator requires set operands (set or frozenset) for set union.
# - Sets have no guaranteed display or insertion order; use sorted() to
#   create a predictable list for display.
#
# Connection to earlier lessons:
# - Intersection (&): keep only elements shared by all inputs.
# - Union (|): keep elements found in at least one input.
# - update(): add elements to the existing set and return None.
# - union(): return a separate combined set without changing either input.
# - Union does not retain duplicate counts or preserve playlist order.


# --- 1. Combine two sets of favorites ---
first = {"Rush", "Yes", "Genesis"}
second = {"Yes", "Kansas", "Rush"}
combined = first.union(second)
print(sorted(combined))  # ['Genesis', 'Kansas', 'Rush', 'Yes']
print(len(combined))     # 4
print(type(combined))    # <class 'set'>
# Rush and Yes occur in both inputs but appear only once in the result.
# Genesis and Kansas are included even though each occurs in only one input.
print(sorted(first))     # ['Genesis', 'Rush', 'Yes']
print(sorted(second))    # ['Kansas', 'Rush', 'Yes']
# Both original sets remain unchanged.


# --- 2. Use the | operator and compare intersection ---
print(sorted(first | second))  # ['Genesis', 'Kansas', 'Rush', 'Yes']
print(first.union(second) == (first | second))  # True
print((first | second) == (second | first))     # True
print(sorted(first & second))  # ['Rush', 'Yes']
# Union includes every distinct artist; intersection includes shared artists.

# | and the keyword or are different operations:
print((first or second) is first)  # True — first is nonempty
# Boolean or returns an operand based on truthiness. It does not combine sets.


# --- 3. Empty inputs, identical inputs, and independent results ---
artists = {"Rush", "Yes"}
print(sorted(artists.union(set())))  # ['Rush', 'Yes']
print(set().union(set()))            # set()
print(sorted(artists | artists))     # ['Rush', 'Yes']

combined = artists.union(set())
print(combined == artists)  # True — equal contents
print(combined is artists) # False — different set objects
combined.add("Genesis")
print(sorted(combined))    # ['Genesis', 'Rush', 'Yes']
print(sorted(artists))     # ['Rush', 'Yes']
# The result is a separate set even when the other input adds nothing.


# --- 4. Supply iterables to union() ---
artists = {"Rush"}
requests = ["Yes", "Rush", "Yes"]
combined = artists.union(requests)
print(sorted(combined))  # ['Rush', 'Yes']
print(requests)          # ['Yes', 'Rush', 'Yes']
print(sorted(artists))   # ['Rush']
# The list is unchanged, and its repeated names appear once in the result.

print(sorted(artists.union(("Genesis", "Yes"))))  # ['Genesis', 'Rush', 'Yes']
# Leave this intentional error commented out:
# artists | requests  # TypeError: a list is not a set operand
print(sorted(artists | set(requests)))  # ['Rush', 'Yes']

# Strings supply characters, not a whole name:
print(sorted({"R"}.union("Rush")))  # ['R', 'h', 's', 'u']
print(sorted({"Rush"}.union(["Yes"])))  # ['Rush', 'Yes']
# A dictionary supplies its keys unless you choose a different view:
songs = {"YYZ": "Rush", "Roundabout": "Yes"}
print(sorted({"Limelight"}.union(songs)))  # ['Limelight', 'Roundabout', 'YYZ']
print(sorted({"Genesis"}.union(songs.values())))  # ['Genesis', 'Rush', 'Yes']
# Elements supplied by the iterable must be hashable.
# {1}.union([[2, 3]])  # TypeError: a supplied element is a list


# --- 5. Combine more than two collections ---
alex = {"Rush", "Yes"}
kevin = {"Genesis", "Rush"}
sam = {"Kansas", "Yes"}
print(sorted(alex.union(kevin, sam)))  # ['Genesis', 'Kansas', 'Rush', 'Yes']
print(sorted(alex | kevin | sam))     # ['Genesis', 'Kansas', 'Rush', 'Yes']
# Appearing in any one collection is enough to be included.
print(sorted(alex.intersection(kevin, sam)))  # []
# There is no artist shared by all three, but their union is not empty.


# --- 6. Compare union() with update() ---
original = {"Rush"}
shared = original
combined = original.union({"Yes"})
print(sorted(original))  # ['Rush']
print(sorted(shared))    # ['Rush']
print(sorted(combined))  # ['Rush', 'Yes']

result = original.update({"Genesis"})
print(sorted(original))  # ['Genesis', 'Rush']
print(sorted(shared))    # ['Genesis', 'Rush']
print(sorted(combined))  # ['Rush', 'Yes']
print(result)            # None
# union() built a new set; update() changed the set shared refers to.
# Calling original.union(...) without saving or using its result does not
# update original. Assign the result if you want to keep the new set.


# --- 7. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Predict the whole snippet, including any mutations.
# Give exact list order for sorted() outputs; raw set order is unspecified.
# Keep intentional-error examples commented out.

# Exercise 1 — Combine unique elements
# Predict all three outputs. Explain why the result has fewer elements than
# the sum of the two input lengths.
# first = {"Rush", "Yes", "Genesis"}
# second = {"Rush", "Kansas", "Yes"}
# combined = first.union(second)
# print(sorted(combined))
# print(len(combined))
# print("Kansas" in combined)
# ANSWER:


# Exercise 2 — Union versus intersection
# Predict all three outputs. Explain which operation includes elements
# found in only one input.
# first = {1, 2, 3}
# second = {3, 4, 5}
# print(sorted(first | second))
# print(sorted(first & second))
# print((first | second) == (second | first))
# ANSWER:


# Exercise 3 — A separate result
# Predict all four outputs. Explain why removing from combined does not
# remove anything from artists.
# artists = {"Rush", "Yes"}
# combined = artists.union(set())
# print(combined == artists)
# print(combined is artists)
# combined.remove("Rush")
# print(sorted(combined))
# print(sorted(artists))
# ANSWER:


# Exercise 4 — Method inputs and operator inputs
# Predict the first two outputs. Name the error the final expression would
# raise and rewrite it using | with a converted set. Keep the error commented.
# numbers = {1, 2}
# additions = [2, 3, 3]
# print(sorted(numbers.union(additions)))
# print(additions)
# print(numbers | additions)  # Intentional error
# ANSWER:


# Exercise 5 — Diagnose an unused return value
# Predict both outputs. Explain why the first call does not change artists.
# Then write a correction that saves a new combined set in a separate variable
# while leaving artists unchanged. Start with a fresh {"Rush"}.
# artists = {"Rush"}
# artists.union({"Yes"})
# print(sorted(artists))
# result = artists.update({"Genesis"})
# print(result)
# ANSWER:


# Exercise 6 — Write your own combined favorites report
# 1. Create two sets of artist names with at least three names each.
#    Include at least one shared artist and one artist unique to each set.
# 2. Use union() to store their combined artists in a new variable.
# 3. Print a sorted list of the combined artists and their count.
# 4. Use | and print whether its result equals your union() result.
# 5. Print the intersection too, followed by both unchanged original sets.
#    Use sorted() for each display.
# 6. Explain why the union includes more artists than the intersection for
#    your inputs, and how union() differs from update().
# Write your code below:


# Optional challenge — Combine three artist lists
# Work through this one together when you are ready.
# Define combined_artists(first, second, third), accepting three lists of
# artist strings. Return a NEW alphabetically sorted LIST containing every
# distinct artist found in any of the inputs.
# Use set(), union(), and sorted(). Leave all input lists unchanged.
# Matching is case-sensitive; repeated names appear once.
# combined_artists(['Rush', 'Yes'], ['Rush', 'Genesis'], ['Kansas'])
# => ['Genesis', 'Kansas', 'Rush', 'Yes']
# combined_artists([], ['Rush', 'Rush'], []) => ['Rush']
# combined_artists([], [], []) => []
# Explain why an empty input list does not force an empty union result.
# Write your code below:
