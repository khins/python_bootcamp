# Python Objects and References — Study Summary
# Learning goals:
# 1. Distinguish a variable name from the object it references.
# 2. Explain why objects have types and names can be reassigned.
# 3. Compare changing an object with reassigning a variable.
# 4. Understand when an object can become eligible for cleanup.


# --- 1. Variables are names that reference objects ---
# Objects contain the actual data. A variable is a name bound to an object.
# Read the assignment below as:
# "scores references a list object containing 1, 2, and 3."
scores = [1, 2, 3]
print(scores)  # [1, 2, 3]


# --- 2. Objects have types ---
# type() tells us the type of the object a variable currently references.
value = 10
print(type(value))  # <class 'int'>

# Reassignment binds the same name to a different object.
# It does not transform the original integer object into a string.
value = "hello"
print(type(value))  # <class 'str'>

# Python allows this, but use names consistently when changing types
# would make the code harder to understand.


# --- 3. Two names can reference the same object ---
original = [10, 20]
shared = original

# Assignment does not automatically copy the list.
print(shared is original)  # True — both names reference the same object

# Lists are mutable: their contents can change.
shared.append(30)
print(original)  # [10, 20, 30]
print(shared)    # [10, 20, 30]


# --- 4. Reassignment is different from changing an object ---
# This assignment makes shared reference a NEW list.
shared = [99]
print(shared)    # [99]
print(original)  # [10, 20, 30] — the earlier list still exists
print(shared is original)  # False

# Useful distinction:
# shared.append(30) -> changes the list that shared references
# shared = [99]    -> changes which object the name shared references


# --- 5. Unreachable objects and memory cleanup ---
# Python manages object memory automatically. When an object is no longer
# reachable, its memory can be reclaimed. Do not rely on exact cleanup timing.
first = ["temporary"]
second = first

first = None
# The list is still reachable through second.
print(second)  # ['temporary']

second = None
# Neither name now references that list. With no other references in this
# example, the list is eligible for cleanup.
# Assigning None rebinds a name; it does not explicitly delete an object.


# --- 6. Practice: predict, explain, then run ---
# Work on one exercise at a time. Write your prediction before uncommenting
# its code, then compare the output with your explanation.

# Exercise 1 — Track the object type
# Predict both printed types. Does the first object change its type? No prints the int type
# item = 42
# print(type(item))
item = [42]
print(type(item)) # <class 'list'>

# Exercise 2 — Follow shared references
# Predict both lists. How many list objects are created here?
colors = ["red", "blue"]
other_colors = colors
other_colors.append("green")
print(colors) # ['red', 'blue', 'green']
print(other_colors) # ['red', 'blue', 'green']

# Exercise 3 — Spot reassignment
# Predict both lists. Which line creates a second list object?
tasks = ["read", "practice"]
remaining = tasks
remaining = ["review"]
print(tasks) # ["read", "practice"]
print(remaining) # ["review"]

# Exercise 4 — Combine mutation and reassignment
# Predict each output and draw arrows from names to lists after each line.
a = [1, 2]
b = a
b.append(3)
a = [4, 5]
a.append(6)
print(a)
print(b)

# Exercise 5 — Reason about reachability
# After first_name is rebound, what still references the list? Nothing references the list second_name still references it:
# After second_name is rebound, is that list still reachable in this example? No
# The key idea: reassigning one name does not change what another name references.
first_name = [100, 200]
second_name = first_name
first_name = None
second_name = None
print(first_name)
print(second_name)

# Exercise 6 — Write your own example
# Create a list and bind two names to it.
# Change the list through one name and print it through the other.
# Reassign one name to a new list, then print both lists.
# Explain why the last two outputs differ.
aged_rockers = ['Alex Lifeson', 'Geddy Lee']
rush = aged_rockers
rush.append('Neil Peart')
print(aged_rockers)
# ['Alex Lifeson', 'Geddy Lee', 'Neil Peart'] because the variable rush is the list and then
# we appened Neil Peart to that list