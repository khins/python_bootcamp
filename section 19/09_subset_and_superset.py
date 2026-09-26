# Set issubset() and issuperset() — Study Summary
# Instructor summary:
# - first.issubset(second) checks whether every element in first is in second.
# - first.issuperset(second) checks whether first contains every element in second.
# - Both methods return a Boolean: True or False. Neither changes the inputs.
# - Read comparisons from left to right: "Is first a subset/superset of second?"
# - If first is a subset of second, second is a superset of first.
#
# Clarifications and connections:
# - <= is the operator equivalent of issubset(); >= matches issuperset().
# - Equal sets are both subsets and supersets of each other.
# - < checks for a PROPER subset: all elements are included, but sets differ.
# - > checks for a PROPER superset: all elements are included, plus extras.
# - Containment matters, not just the number of elements or their numeric values.
# - The methods accept iterables such as lists and tuples. The comparison
#   operators require set operands (set or frozenset).
# - Superset and subset are converse relationships, not Boolean opposites.


# --- 1. Check whether a is a subset of b ---
a = {1, 2, 4}
b = {1, 2, 3, 4, 5}
print(a.issubset(b))  # True
print(a <= b)  # True
print(a < b)  # True — a is also a proper subset of b
print(b.issubset(a))  # False — a is missing 3 and 5
# Every element of a appears in b. The extra elements in b are allowed.
# All three forward checks agree here because the sets are unequal.


# --- 2. Check whether b is a superset of a ---
print(b.issuperset(a))  # True
print(b >= a)  # True
print(b > a)  # True — b is also a proper superset of a
print(a.issuperset(b))  # False
print(a.issubset(b) == b.issuperset(a))  # True
# Reversing the inputs and switching the relationship asks the same question.
print(sorted(a))  # [1, 2, 4]
print(sorted(b))  # [1, 2, 3, 4, 5]
# Neither input has changed. sorted() makes the display order predictable.


# --- 3. Equal sets distinguish ordinary and proper containment ---
first = {1, 2, 4}
second = {4, 2, 1}
print(first == second)  # True — sets ignore element order
print(first.issubset(second))  # True
print(first <= second)  # True
print(first < second)  # False — no extra elements in second
print(first.issuperset(second))  # True
print(first >= second)  # True
print(first > second)  # False — no extra elements in first
# A set is always a subset and superset of itself, but never a proper one.


# --- 4. A smaller set is not necessarily a subset ---
small = {1, 9}
large = {1, 2, 3, 4, 5}
print(len(small) < len(large))  # True
print(small <= large)  # False — 9 is missing from large
print(small >= large)  # False — small is missing several elements
print(large <= small)  # False
# Neither set contains the other. Subset and superset checks can both be False.
print({1} < {2})  # False — this does not compare 1 numerically with 2


# --- 5. Empty sets ---
empty = set()
artists = {"Rush", "Yes"}
print(empty <= artists)  # True — an empty set is a subset of every set
print(empty < artists)  # True — artists is nonempty
print(artists >= empty)  # True — every set is a superset of the empty set
print(artists <= empty)  # False
print(empty <= set())  # True
print(empty < set())  # False — the two empty sets are equal


# --- 6. Supply iterables to the methods ---
required = {"read", "write"}
granted = ["read", "write", "share", "read"]
print(required.issubset(granted))  # True
print({"read", "write", "share"}.issuperset(["read", "read"]))  # True
# Duplicate values do not change whether every required element is present.
# Leave this intentional error commented out:
# required <= granted  # TypeError: a list is not a set operand
print(required <= set(granted))  # True


# --- 7. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Keep intentional-error examples commented out.

# Exercise 1 — Read the direction
# Predict all four outputs. Explain which set contains all of the other.
# favorites = {"Rush", "Yes"}
# library = {"Rush", "Yes", "Genesis"}
# print(favorites.issubset(library))
# print(library.issuperset(favorites))
# print(library <= favorites)
# print(favorites >= library)
# ANSWER:


# Exercise 2 — Equal sets
# Predict all four outputs. Explain why the strict comparisons differ.
# first = {2, 4, 6}
# second = {6, 4, 2}
# print(first <= second)
# print(first < second)
# print(first >= second)
# print(first > second)
# ANSWER:


# Exercise 3 — Size versus containment
# Predict all three outputs. Identify the element that prevents containment.
# first = {1, 7}
# second = {1, 2, 3, 4}
# print(len(first) < len(second))
# print(first.issubset(second))
# print(second.issuperset(first))
# ANSWER:


# Exercise 4 — Empty inputs
# Predict all four outputs and explain the difference between <= and <.
# print(set() <= {"YYZ"})
# print(set() < {"YYZ"})
# print(set() <= set())
# print(set() < set())
# ANSWER:


# Exercise 5 — Write your own permissions check
# 1. Create a set of required permissions and a set of granted permissions.
# 2. Use issubset() to check whether all required permissions are granted.
# 3. Repeat the check using <=, then reverse the inputs and use issuperset().
# 4. Add an unrelated permission to granted. Check whether the result changes.
# 5. Remove one required permission from granted and repeat the check.
# 6. Explain why having more permissions is not enough if a required one is absent.
# Write your code below:
