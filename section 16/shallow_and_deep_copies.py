# Shallow and Deep Copies — Study Summary
# Instructor summary:
# - Assignment (b = a) gives another name to the same object; it makes no copy.
# - A shallow copy creates a new outer list but keeps references to its items.
# - For a list of immutable values (numbers, strings, booleans), a shallow
#   copy lets you edit the new list without changing the original list.
# - Nested mutable objects remain shared in a shallow copy. Mutating a shared
#   inner list is visible through both outer lists.
# - A deep copy recursively copies nested lists so their mutations do not
#   affect the original lists.
# - Choose based on what must be independent: a nested list does not always
#   require a deep copy if sharing its inner objects is intentional.
# Precision note: deepcopy does not create a new object for everything;
# immutable values such as integers and strings may be reused.

import copy


# --- 1. Assignment is not copying ---
original = [1, 2, 3]
alias = original
print(original == alias)  # True — equal contents
print(original is alias)  # True — the same list


# --- 2. Three ways to make a shallow copy of a list ---
# copy is a standard-library module that provides copying functions.
# import copy makes those functions available through the name copy.
by_slice = original[:]
by_method = original.copy()
by_module = copy.copy(original)

print(original == by_slice)   # True
print(original is by_slice)   # False
print(original == by_method)  # True
print(original is by_method)  # False
print(original == by_module)  # True
print(original is by_module)  # False

# Each copy has its own outer list. Replacing an item changes only that list.
by_method[0] = 99
print(original)   # [1, 2, 3]
print(by_method)  # [99, 2, 3]
# This replaces a reference in by_method; it does not mutate the integer 1.


# --- 3. A shallow copy shares nested objects ---
numbers = [2, 3, 4]
a = [1, numbers, 5]
b = a.copy()

# a -> outer list A -> numbers
# b -> outer list B -> numbers (the SAME inner list)
print(a == b)        # True — matching contents
print(a is b)        # False — separate outer lists
print(a[1] is b[1])  # True — shared inner list

a[1].append(100)
print(a)  # [1, [2, 3, 4, 100], 5]
print(b)  # [1, [2, 3, 4, 100], 5]

# Adding an item to the outer list does not change the other outer list.
b.append(6)
print(a)  # [1, [2, 3, 4, 100], 5]
print(b)  # [1, [2, 3, 4, 100], 5, 6]


# --- 4. A deep copy also copies the nested lists ---
# Start fresh so this example is independent of the earlier mutations.
a = [1, [2, 3, 4], 5]
b = copy.deepcopy(a)

print(a == b)        # True — matching contents
print(a is b)        # False — separate outer lists
print(a[1] is b[1])  # False — separate inner lists

a[1].append(100)
b[1].append(200)
print(a)  # [1, [2, 3, 4, 100], 5]
print(b)  # [1, [2, 3, 4, 200], 5]


# --- 5. Replacing an inner list vs. mutating it ---
a = [[1, 2], [3, 4]]
b = a.copy()

# Replacing an item in b changes only b's outer list.
b[0] = [99]
print(a)  # [[1, 2], [3, 4]]
print(b)  # [[99], [3, 4]]

# The second inner list is still shared.
b[1].append(5)
print(a)  # [[1, 2], [3, 4, 5]]
print(b)  # [[99], [3, 4, 5]]

# Ask before each change: WHICH list am I changing — outer or inner?


# --- 6. Practice: predict, explain, then run ---
# Work on one exercise at a time. Write predictions beside each print before
# uncommenting the code. Explain shared references as well as the outputs.

# Exercise 1 — Assignment vs. a shallow copy
# Predict all four outputs. Which names share a list?
print("*" * 60)
songs = ["Limelight", "Tom Sawyer"]
alias = songs
cloned = songs.copy()
print(songs == cloned) # True
print(songs is cloned) # False 
print(songs is alias)  # True
cloned.append("Subdivisions")
print(songs) # ["Limelight", "Tom Sawyer"]

print("2" * 60)
# Exercise 2 — Copy a list of immutable values
# Predict both lists. Does replacing copied[0] change an integer object?
values = [10, 20, 30]
copied = values[:]
copied[0] = 99
copied.append(40)
print(values) # [10, 20, 30]
print(copied) # [99 ,20, 30, 40]

print("3" * 60)
# Exercise 3 — Find the shared inner list
# Predict all four outputs. Explain why the two identity checks differ.
# original → outer list A ──┐
#                          ├──→ ["guitar", "programming"]
# shallow  → outer list B ──┘
original = ["hobbies", ["guitar", "programming"]]
shallow = copy.copy(original)
print(original is shallow)        # False because of different outer lists
print(original[1] is shallow[1])  # True because the inner list is the same
shallow.append("woodworking")
print(original) # ["hobbies", ["guitar", "programming"]]
print(shallow)  # ["hobbies", ["guitar", "programming", "woodworking"]]

# Exercise 4 — Make the nested list independent
# Predict all four outputs, then compare your reasoning with Exercise 3.
# original = ["hobbies", ["guitar", "programming"]]
# deep = copy.deepcopy(original)
# print(original == deep)
# print(original[1] is deep[1])
# deep[1].append("photography")
# print(original)
# print(deep)

# Exercise 5 — Replacement vs. mutation
# Predict both lists and both identity checks after the changes.
# original = [[1, 2], [3, 4]]
# shallow = original.copy()
# shallow[0] = [100]
# shallow[1].append(5)
# print(original)
# print(shallow)
# print(original[0] is shallow[0])
# print(original[1] is shallow[1])
# Explain which change affects a shared inner list and which replaces a slot
# in the separate outer list.

# Exercise 6 — Write your own comparison
# 1. Create a list containing two inner lists: favorite songs and hobbies.
# 2. Make a shallow copy and a deep copy BEFORE changing any contents.
# 3. Append a song through the shallow copy's song list.
# 4. Print all three structures and explain which ones show the new song.
# 5. Append a hobby through the deep copy's hobby list.
# 6. Print all three again and explain which ones show the new hobby.
# 7. Use is to check outer-list and inner-list identities for both copies.

# Optional challenge — Choose a copy strategy
# Choose assignment, shallow copy, or deep copy for each goal. Explain why.
# A. Another name that should share all changes to the same list.
# B. A separate list of strings whose items you can replace independently.
# C. A nested list whose inner lists you need to mutate independently.
