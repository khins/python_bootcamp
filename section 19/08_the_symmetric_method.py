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
# Predict both outputs. Explain why "sam" is excluded.
# morning_users = {"alex", "sam", "lee"}
# evening_users = {"sam", "jo"}
# print(sorted(morning_users.symmetric_difference(evening_users)))
# print(sorted(evening_users ^ morning_users))
# ANSWER:


# Exercise 2 — Compare operations
# Predict all four outputs and describe what each operation keeps.
# first = {1, 2, 3}
# second = {2, 3, 4}
# print(sorted(first & second))
# print(sorted(first | second))
# print(sorted(first - second))
# print(sorted(first ^ second))
# ANSWER:


# Exercise 3 — Equal and empty inputs
# Predict all three outputs.
# songs = {"YYZ", "Limelight"}
# print(songs ^ songs)
# print(sorted(songs ^ set()))
# print(sorted(set() ^ songs))
# ANSWER:


# Exercise 4 — Diagnose an unused result
# Predict the output. Then save the symmetric difference in a new variable
# and print it, leaving artists unchanged.
# artists = {"Rush", "Yes"}
# artists.symmetric_difference({"Yes", "Genesis"})
# print(sorted(artists))
# ANSWER:


# Exercise 5 — Write your own playlist comparison
# 1. Create two sets of song titles with at least one shared title and at
#    least one title exclusive to each set.
# 2. Store their symmetric difference and print it using sorted().
# 3. Use ^ and check that it produces the same result as the method.
# 4. Reverse the inputs and check that the result is still equal.
# 5. Print both original sets to show that neither was changed.
# Write your code below:
