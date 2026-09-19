# Python Equality vs. Identity — Study Summary
# Learning goals:
# 1. Use == to compare values or contents.
# 2. Use is to check whether two names reference the same object.
# 3. Explain why equal lists can be separate objects.
# 4. Predict how mutation and reassignment affect comparisons.


# --- 1. Two comparison questions ---
# == asks: "Do these objects have equal values?"
# is asks: "Are these references pointing to the exact same object?"
# != checks for unequal values; is not checks for different objects.


# --- 2. Equal contents, shared and separate lists ---
students = ["Bob", "Sally", "Sue"]
athletes = students
nerds = ["Bob", "Sally", "Sue"]

# students ──┐
#            ├──► List 1: ["Bob", "Sally", "Sue"]
# athletes ──┘
# nerds ────────► List 2: ["Bob", "Sally", "Sue"]

# There are two list objects. Assignment did not copy the first list.
# The second list has matching contents, but its own identity.


# --- 3. Equality: compare list contents with == ---
# Lists compare equal when corresponding elements compare equal
# and appear in the same order, with the same list length.
print(students == athletes)  # True
print(students == nerds)     # True
print(students != nerds)     # False


# --- 4. Identity: compare references with is ---
print(students is athletes)  # True — two names, one object
print(students is nerds)     # False — two separate objects
print(students is not nerds) # True

# For these ordinary lists, sharing an object also means equal contents.
# Equal contents alone do NOT mean the lists are the same object.
# "Same object always means equal" is not a universal Python rule:
# special values and custom equality behavior can be exceptions.


# --- 5. Mutation changes contents, not identity ---
athletes.append("Jane")
print(students)  # ['Bob', 'Sally', 'Sue', 'Jane']
print(nerds)     # ['Bob', 'Sally', 'Sue']
print(students == nerds)     # False — the contents now differ
print(students is athletes)  # True — the shared reference remains


# --- 6. Reassignment changes what a name references ---
athletes = ["Bob", "Sally", "Sue", "Jane"]
print(students == athletes)  # True — matching contents again
print(students is athletes)  # False — athletes now references a new list


# --- 7. Choosing the right operator ---
# Use == for value comparisons, including numbers and strings.
# Do not use is to compare their values: Python may reuse some objects,
# so identity is not a reliable way to ask whether values match.
answer = "yes"
print(answer == "yes")  # True

# A common use of is: checking for the singleton object None.
result = None
print(result is None)      # True
print(result is not None)  # False


# --- 8. Practice: predict, explain, then run ---
# Uncomment one exercise at a time after writing your predictions.
# Explain each answer using either "contents" or "same object".

# Exercise 1 — Equal lists or the same list?
# Predict all three outputs. How many list objects are created? 2 list objects created 
print('-' * 50)
first = [10, 20]
second = [10, 20]
print(first == second) # True
print(first is second) # False
print(first is not second) # True
print('-' * 50)

# Exercise 2 — Add a shared reference
# Predict each output. Draw arrows from each name to its list.
print('!' * 50)
band = ["Alex", "Geddy"]
alias = band
separate = ["Alex", "Geddy"]
print(band == alias) # True
print(band is alias) # True
print(alias == separate) # True matching contents
print(alias is separate) # False
print('-' * 50)

# Exercise 3 — Mutate through an alias
# Predict both lists and both comparisons after append().
print('?' * 50)
hobbies = ["guitar", "programming"]
shared = hobbies
other = ["guitar", "programming"]
shared.append("woodworking")
print(hobbies) # ["guitar", "programming", "woodworking"]
print(other) # ["guitar", "programming"]
print(hobbies == other) # False
print(hobbies is shared) # True
print('?' * 50)

print('=' * 50)
# Exercise 4 — Reassign to an equal list
# Predict each comparison before and after reassignment.
original = [1, 2, 3]
backup = original
print(original is backup) # True
backup = [1, 2, 3]
print(original == backup) # True
print(original is backup) # False
# Explain why reassignment changes one comparison but not the other.
print('=' * 50)

print('5' * 50)
# Exercise 5 — Same elements, different order
# Predict both comparisons. Does order matter for list equality?
left = [1, 2, 3]
right = [3, 2, 1]
print(left == right) # False 
print(left is right) # False
print('5' * 50)

print('6' * 50)
# Exercise 6 — Write your own example
# 1. Create a list of two favorite songs.
# 2. Bind a second name to that same list.
# 3. Create a separate list containing the same songs in the same order.
# 4. Use == and is to compare the first list with each of the other two.
# 5. Append a song through the second name, then repeat the comparisons.
# 6. Explain which comparison results changed and why.
fav_songs = ["Hotel California", "Comforably Numb"]
separates = fav_songs
third = ["Hotel California", "Comforably Numb"]
separates.append("Limelight")

print(separates ==  fav_songs)
print(fav_songs is separates)
print(third == fav_songs)
print(fav_songs is third)



# Optional challenge — Choose the operator
# Replace each ___ with ==, !=, is, or is not to express the question.
# username = "Kevin"
# pending = None
# print(username == "Kevin")  # Does username have the value "Kevin"?
# print(pending is None)      # Is pending the None object?
# print(pending is not None)      # Is pending something other than None?
