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
# Think of a subset as asking:
# "Are ALL the elements on the left also contained in the set on the right?"
# Is every item in empty also in artists?
# There are no items to check.
# * The empty set is a subset of EVERY set.
# The < operator means proper subset.
# 1. Everything in LEFT exists in RIGHT.
#              AND
# 2. LEFT and RIGHT are NOT equal.
# <=  subset, equality allowed
# <   proper subset, must be smaller
# >= means superset.
empty = set()
artists = {"Rush", "Yes"}
print(empty <= artists)  # True — an empty set is a subset of every set
print(empty < artists)  # True — artists is nonempty
print(artists >= empty)  # True — every set is a superset of the empty set
print(artists <= empty)  # False
print(empty <= set())  # True
print(empty < set())  # False — the two empty sets are equal

# {}  <=  {"Rush", "Yes"}
#  ↑          ↑
# subset    superset

# {"Rush", "Yes"}  >=  {}
#        ↑              ↑
#    superset         subset

# <= means:
# "subset OR equal"

# {} is equal to {}

# → True

# < means PROPER subset

# LEFT must be a subset of RIGHT
# AND
# LEFT must NOT equal RIGHT.

# ! IMPORTANT - The main operators to remember
# * SET RELATIONSHIP OPERATORS

# <=  SUBSET
# Every element on the LEFT exists on the RIGHT.
# Equality is allowed.

# <   PROPER SUBSET
# Every element on the LEFT exists on the RIGHT,
# AND the two sets cannot be equal.

# >=  SUPERSET
# The LEFT contains every element from the RIGHT.
# Equality is allowed.

# >   PROPER SUPERSET
# The LEFT contains every element from the RIGHT,
# AND the two sets cannot be equal.

# The mental shortcut:
# <=   "Does RIGHT contain everything from LEFT?"

# <    "Does RIGHT contain everything from LEFT,
#       AND have something extra?"



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
# Predict all four outputs. 
favorites = {"Rush", "Yes"}
library = {"Rush", "Yes", "Genesis"}
print(favorites.issubset(library))
print(library.issuperset(favorites)) # Asks: "Is everything in favorites also in library?" Yes.
print(library <= favorites) # This asks whether everything in library exists in favorites.
print(favorites >= library) # This asks whether favorites is a superset of library—whether favorites contains everything from library
# ANSWER:
# output
# True
# True
# False
# False
# Explain which set contains all of the other:
# favorites all in library ;
# Every element in favorites is contained in library.
# Therefore, favorites is a subset of library,
# and library is a superset of favorites.
# relationship visually:
# favorites = {"Rush", "Yes"}
#                  ↓    ↓
# library   = {"Rush", "Yes", "Genesis"}
#                                ↑
#                          extra element
# SUBSET
# A <= B
# # "Does B contain everything from A?"

# # SUPERSET
# A >= B
# # "Does A contain everything from B?"

# ! IMPORTANT
# SUBset   → smaller/equal collection fits inside the other
# SUPERset → larger/equal collection contains the other


# Exercise 2 — Equal sets
# Predict all four outputs. 
first = {2, 4, 6}
second = {6, 4, 2}
print(first <= second)
print(first < second) # Is every element of first in second AND does second have something extra?
print(first >= second)
print(first > second) # "Does one set have something extra?"
# ANSWER:
# outputs
# True
# False
# True
# False

# Explain why the strict comparisons differ:
# The reason < and > are False is that they are strict comparisons—proper subset and proper superset.

# The sets contain exactly the same elements, so they are equal.
# <= and >= allow equal sets, so they return True.
# < and > require a proper subset or proper superset, meaning one set
# must contain additional elements, so they return False.

# Exercise 3 — Size versus containment
# Predict all three outputs. 
first = {1, 7}
second = {1, 2, 3, 4}
print(len(first) < len(second))
# 1 → Is 1 in second?  YES ✓
# 7 → Is 7 in second?  NO  ✗
print(first.issubset(second))
print(second.issuperset(first))
# ANSWER:
# outputs
# True
# False
# False
# Identify the element that prevents containment:
# first prevents containment because of value 7 ;
# The value 7 prevents first from being a subset of second
# because 7 does not exist in second.

# * SIZE DOES NOT DETERMINE SUBSET/SUPERSET

# len(A) < len(B)
# only tells us A has fewer elements.

# A.issubset(B)
# asks whether EVERY element of A exists in B.

# len()       → "HOW MANY?"
# subset      → "ARE THEY ALL IN THERE?"
# superset    → "DO I CONTAIN THEM ALL?"


# Exercise 4 — Empty inputs
# Predict all four outputs 
print(set() <= {"YYZ"})
print(set() < {"YYZ"})
print(set() <= set())
print(set() < set())
# ANSWER:
# outputs
# True
# True
# True
# False

# explain the difference between <= and <:
# <= asks does left have everything from right, < asks the same but adds does it have extras

# <= asks: Does the RIGHT contain everything from the LEFT?
#     Equality is allowed.
#
# <  asks: Does the RIGHT contain everything from the LEFT,
#     AND does the RIGHT have something extra?

# Exercise 5 — Write your own permissions check
# 1. Create a set of required permissions and a set of granted permissions.
# Write your code below:
required_permissions = {
    "read_data",
    "write_data",
    "delete_data",
    "execute_job",
}

granted_permissions = {
    "read_data",
    "write_data",
    "view_logs",
}

# 2. Use issubset() to check whether all required permissions are granted.
print(required_permissions.issubset(granted_permissions)) # => False

# 3. Repeat the check using <=, then reverse the inputs and use issuperset().
print(required_permissions <= granted_permissions) # => False

# 4. Add an unrelated permission to granted. Check whether the result changes.
granted_permissions.add("grant execute")

print(required_permissions <= granted_permissions) # => False

# 5. Remove one required permission from granted and repeat the check.
granted_permissions.remove("read data")
print(required_permissions <= granted_permissions)

# 6. Explain why having more permissions is not enough if a required one is absent:
# having more permissions is not enough if they dont equal to at required ;
# Having more permissions is not enough because every required
# permission must exist in granted_permissions. Extra unrelated
# permissions do not make up for a missing required permission.

# required_permissions     granted_permissions

# read_data          ✓     read_data
# write_data         ✓     write_data
# delete_data        ✗
# execute_job        ✗
#                          view_logs  ← unrelated extra

# SUBSET/SUPERSET IS NOT:

# "Which set has MORE?"


# SUBSET/SUPERSET IS:

# "Are ALL the required elements THERE?"

