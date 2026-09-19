# Shared References: Immutable vs. Mutable Objects — Study Summary
# Learning goals:
# 1. Explain why two names can reference the same object.
# 2. Compare shared references to immutable and mutable objects.
# 3. Distinguish reassignment from mutation.
# 4. Remember that assignment does not copy a list.


# --- 1. Variables reference objects, not other variables ---
a = 3
b = a

# a ──► 3 ◄── b
# Both names reference the same integer object.
# b does not follow a if a is later reassigned.


# --- 2. Shared references with immutable objects ---
# Integers, strings, booleans, and tuples are immutable.
# An immutable object's contents cannot be changed in place.
# A tuple can contain a mutable object; that inner object can still change.
a = 5

# a ──► 5
# b ──► 3
print(a)  # 5
print(b)  # 3

# Reassignment changes what a references; it does not modify the integer 3.
# The same idea applies to strings:
name = "Alex"
other_name = name
name = name.upper()
print(name)        # ALEX
print(other_name)  # Alex
# upper() returns a string; it does not mutate the original string.


# --- 3. Shared references with mutable objects ---
# Lists and dictionaries are mutable: their contents can change in place.
a = [1, 2, 3]
b = a

# a ──► [1, 2, 3] ◄── b
# Assignment binds another name to the list; it does not copy the list.
a.append(4)

# a ──► [1, 2, 3, 4] ◄── b
print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]


# --- 4. Mutation can happen through either reference ---
b.append(5)

# a ──► [1, 2, 3, 4, 5] ◄── b
print(a)  # [1, 2, 3, 4, 5]
print(b)  # [1, 2, 3, 4, 5]
# There is still only one list, accessible through two names.


# --- 5. Reassignment vs. mutation ---
a = [1, 2, 3]
b = a

# Reassignment: bind a to a different list.
a = [4, 5, 6]

# a ──► [4, 5, 6]
# b ──► [1, 2, 3]
print(a)  # [4, 5, 6]
print(b)  # [1, 2, 3]

# Mutation: change the existing list referenced by b.
b.append(4)
print(a)  # [4, 5, 6]
print(b)  # [1, 2, 3, 4]

# Patterns to recognize:
# b = a          -> binds b to the object a currently references
# a = [4, 5, 6]  -> reassigns a to a new list
# a.append(7)    -> mutates the list referenced by a
# a[0] = 99      -> mutates an item in the list referenced by a


# --- 6. Practice: predict, explain, then run ---
# Work on one exercise at a time. Write predictions before uncommenting code.
# For each exercise, track which object each name references.

# Exercise 1 — Immutable integers
# Predict both outputs. Does score = 20 change the original integer object?
score = 10
saved_score = score
score = 20
print(score)
print(saved_score)

# Exercise 2 — Shared list mutation
# Predict both outputs. How many list objects are created?
band = ["Alex Lifeson", "Geddy Lee"]
rush = band
rush.append("Neil Peart")
print(band)
print(rush)

# Exercise 3 — Reassign one name
# Predict both outputs. Does backup follow the reassignment of songs?
songs = ["Tom Sawyer", "Limelight"]
backup = songs
songs = ["Subdivisions"]
print(songs)
print(backup)

# Exercise 4 — Changing an item vs. reassigning a name
# Predict all three outputs. What object does replacement reference?
names = ["Alex", "Geddy"]
shared_names = names
replacement = names[0] = "Bob"
print(names)
print(shared_names)
print(replacement)
# Hint: this assignment puts the same string into names[0] and replacement.

# Exercise 5 — Track three references
# Draw arrows after each assignment or mutation, then predict the outputs.
first = [1, 2]
second = first
third = second
second = [9]
third.append(3)
print(first)  # [1, 2]
print(second) # [1, 2]
print(third)  # [1, 2, 3]

# Exercise 6 — Write your own example
# 1. Create a list of two hobbies and bind a second name to that list.
# 2. Append a hobby through the second name; print through the first name.
# 3. Reassign the second name to a new list of different hobbies.
# 4. Append another hobby through the first name, then print both lists.
# 5. Explain which lines mutate a list and which reassign a name.

hobbies = ['Classical Guitar', 'Python programming']
second_name = hobbies
second_name.append('Wood working')
second_name = ['Photography', 'Hiking']
print(hobbies)
print(second_name)

# Optional challenge — Equal contents vs. the same object
# == compares values; is checks whether references point to the same object.
# Predict each output. Use is for identity checks, not general value checks.
# left = [1, 2]
# right = [1, 2]
# alias = left
# print(left == right)
# print(left is right)
# print(left is alias)
