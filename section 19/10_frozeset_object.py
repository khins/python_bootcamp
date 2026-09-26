# The frozenset Object — Study Summary
# Instructor summary:
# - A frozenset is an immutable set: its elements cannot be added or removed.
# - Create one with frozenset(iterable), using one lowercase word.
# - Duplicate values in the iterable become a single element.
# - Mutating methods such as add(), update(), remove(), and discard() are absent.
# - A frozenset can serve as a dictionary key; a regular set cannot.
#
# Clarifications and connections:
# - frozenset() with no argument creates an empty frozen set.
# - Like a set, a frozenset contains distinct, hashable elements and has no
#   guaranteed iteration order. It does not support indexing.
# - Dictionary keys must be HASHABLE, not merely described as immutable.
#   A frozenset is hashable; a regular set is mutable and unhashable.
# - Immutability alone is not a universal test: a tuple containing a list
#   is immutable as a container, but is still unhashable.
# - Membership tests, iteration, comparisons, and non-mutating set operations
#   are available on frozen sets.
# - Immutability prevents changing the object, not reassigning its variable.


# --- 1. Create a frozen set and remove duplicates ---
mr_freeze = frozenset([1, 2, 3, 2])
print(sorted(mr_freeze))  # [1, 2, 3]
print(type(mr_freeze))  # <class 'frozenset'>
print(len(mr_freeze))  # 3
print(2 in mr_freeze)  # True
print(4 in mr_freeze)  # False
print(frozenset())  # frozenset()
# sorted() returns a list for predictable display; it does not change mr_freeze.


# --- 2. Mutating methods are unavailable ---
# Leave these intentional errors commented out. Each raises AttributeError:
# mr_freeze.add(4)
# mr_freeze.update([4, 5])
# mr_freeze.remove(1)
# mr_freeze.discard(1)
# mr_freeze.clear()
# The methods do not exist on frozenset objects.

source = [1, 2, 3]
frozen = frozenset(source)
source.append(4)
print(source)  # [1, 2, 3, 4]
print(sorted(frozen))  # [1, 2, 3]
# Changing the source collection does not add elements to the frozen set.


# --- 3. Use a frozen set as a dictionary key ---
regular_set = {1, 2, 3}
# Leave this intentional error commented out:
# invalid_lookup = {regular_set: "some value"}  # TypeError: unhashable type: 'set'

lookup = {mr_freeze: "some value"}
print(lookup[mr_freeze])  # some value
print(lookup[frozenset([3, 2, 1, 2])])  # some value
# Equal frozen sets identify the same dictionary key, regardless of input order
# or duplicates. The key represents a collection of members, not a sequence.

# Elements of a frozen set must also be hashable:
# frozenset([[1, 2], [3, 4]])  # TypeError: unhashable type: 'list'
pairs = frozenset([(1, 2), (3, 4)])
print(sorted(pairs))  # [(1, 2), (3, 4)]


# --- 4. Perform non-mutating set operations ---
first = frozenset([1, 2, 3])
second = frozenset([3, 4])
print(sorted(first & second))  # [3]
print(sorted(first | second))  # [1, 2, 3, 4]
print(sorted(first - second))  # [1, 2]
print(sorted(first ^ second))  # [1, 2, 4]
print(first.issubset({1, 2, 3, 4}))  # True
print(first.issuperset({1, 2}))  # True
combined = first.union(second)
print(type(combined))  # <class 'frozenset'>
print(sorted(first))  # [1, 2, 3] — unchanged
print(sorted(second))  # [3, 4] — unchanged
# These operations compute results without modifying either input.


# --- 5. Reassign a variable or create a mutable copy ---
original = frozenset([1, 2, 3])
expanded = original | frozenset([4])
print(sorted(expanded))  # [1, 2, 3, 4]
print(sorted(original))  # [1, 2, 3]
# A variable can refer to a new result without changing the original object.
expanded = expanded | frozenset([5])
print(sorted(expanded))  # [1, 2, 3, 4, 5]

editable = set(original)
editable.add(4)
print(sorted(editable))  # [1, 2, 3, 4]
print(sorted(original))  # [1, 2, 3]
# set() creates a separate mutable collection from the frozen set's elements.


# --- 6. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Give exact list order for sorted() outputs; raw set order is unspecified.
# Keep intentional-error examples commented out.

# Exercise 1 — Distinct elements
# Predict all three outputs.
# artists = frozenset(["Rush", "Yes", "Rush"])
# print(sorted(artists))
# print(len(artists))
# print("Genesis" in artists)
# ANSWER:


# Exercise 2 — Diagnose a mutation
# Explain the error and write code that stores a new frozen set containing
# the original elements plus "Genesis" in a variable called expanded.
# artists = frozenset(["Rush", "Yes"])
# artists.add("Genesis")  # Intentional AttributeError; keep commented out.
# ANSWER:


# Exercise 3 — Dictionary lookup
# Predict the output. Explain why the second frozen set finds the same key.
# groups = {frozenset(["Rush", "Yes"]): "progressive rock"}
# print(groups[frozenset(["Yes", "Rush", "Yes"])])
# ANSWER:


# Exercise 4 — A separate mutable collection
# Predict both outputs. Explain why frozen does not lose an element.
# frozen = frozenset([1, 2, 3])
# editable = set(frozen)
# editable.remove(2)
# print(sorted(editable))
# print(sorted(frozen))
# ANSWER:


# Exercise 5 — Write your own frozen playlist
# 1. Create a frozenset from a list of song titles containing a duplicate.
# 2. Print its sorted titles, its length, and a membership test.
# 3. Create a second frozenset with one shared title and one new title.
# 4. Print their intersection and union using sorted().
# 5. Use the first frozenset as a dictionary key with a playlist name as its value.
# 6. Retrieve the name using an equal frozenset built from a different title order.
# Write your code below:
