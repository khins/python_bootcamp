# ============================================================
# FILE: polymorphism-and-duck-typing.py
# TOPIC: Polymorphism, Duck Typing, and __len__
# ============================================================
# LESSON OBJECTIVES
# 1. Explain polymorphism: different objects respond to the same operation.
# 2. Explain duck typing: focus on supported behavior, not exact type.
# 3. See how len() works with strings, lists, tuples, and dictionaries.
# 4. Implement __len__ in a custom class.
# 5. Predict output and complete coding challenges independently.


# ============================================================
# SECTION 1 — KEY IDEAS
# ============================================================
# POLYMORPHISM:
# Different kinds of objects can respond to the same method or operation.
#
# DUCK TYPING:
# If an object supports the behavior our code needs, we can often use it
# without checking its exact type or requiring a shared superclass.
#
# The lesson's example uses the built-in len() function, which relies on
# an object's __len__ special method.
#
# Think: "Can this object tell me its length?" rather than
# "Is this object a string, list, tuple, or dictionary?"


# ============================================================
# SECTION 2 — BUILT-IN POLYMORPHISM WITH len()
# ============================================================
values = [
    "Boris",
    [1, 2, 3],
    (4, 5, 6, 7),
    {"A": 1, "B": 2},
]

# EXERCISE 1 — PREDICT BEFORE RUNNING
# Predict what each call to len(value) returns.
#
# ANSWERS:
# "Boris"                 -> __________
# [1, 2, 3]              -> __________
# (4, 5, 6, 7)           -> __________
# {"A": 1, "B": 2}       -> __________

# Uncomment to check:
# for value in values:
#     print(len(value))

# QUESTION:
# What is len() counting in a dictionary?
# ANSWER: ___________________________________________________


# ============================================================
# SECTION 3 — CREATE A PERSON CLASS
# ============================================================
# The instructor defines a Person with a name and height, then decides
# that the person's "length" should be their height.
#
# In this exercise, heights are nonnegative integers, as required by len().

class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    # CODING CHALLENGE 1:
    # Implement __len__(self) so len(person) returns self.height.
    # Replace pass with your method.
    pass


# TEST AFTER YOU COMPLETE THE METHOD:
# boris = Person("Boris", 71)
# print(len(boris))  # Predict: __________
#
# QUESTION:
# Does Person need to inherit from list or str for len() to work?
# ANSWER: ___________________________________________________


# ============================================================
# SECTION 4 — MIXED OBJECTS, SAME OPERATION
# ============================================================
# Once Person.__len__ is implemented, uncomment this experiment.
#
# mixed_values = [
#     "Boris",
#     [1, 2, 3],
#     (4, 5, 6, 7),
#     {"A": 1, "B": 2},
#     Person("Boris", 71),
# ]
#
# for value in mixed_values:
#     print(len(value))
#
# EXERCISE 2 — PREDICT ALL FIVE OUTPUT LINES
# 1. __________
# 2. __________
# 3. __________
# 4. __________
# 5. __________
#
# EXPLAIN:
# Why does the loop not need a separate if statement for each type?
# ANSWER: ___________________________________________________
# ___________________________________________________________


# ============================================================
# SECTION 5 — DUCK TYPING IN YOUR OWN WORDS
# ============================================================
# The lesson's analogy:
# "If it walks like a duck and quacks like a duck..."
#
# In Python, behavior matters more than the object's specific class.
#
# EXERCISE 3 — COMPLETE THE SENTENCES
# 1. Polymorphism lets different __________ respond to the same operation.
# 2. Duck typing emphasizes an object's __________, not just its type.
# 3. len(obj) relies on the special method __________.
# 4. A custom class can support len() by defining __________.


# ============================================================
# SECTION 6 — SECOND CUSTOM CLASS
# ============================================================
# CODING CHALLENGE 2 — ALBUM COLLECTION
# Create a class called AlbumCollection.
# Requirements:
# - __init__ receives a list of album titles.
# - Store that list on the instance.
# - Implement __len__ to return the number of albums.
#
# Example target behavior:
# albums = AlbumCollection(["Hemispheres", "Moving Pictures"])
# print(len(albums))  # 2

class AlbumCollection:
    # Write your methods here.
    pass


# ============================================================
# SECTION 7 — WRITE A POLYMORPHIC FUNCTION
# ============================================================
# CODING CHALLENGE 3
# Define report_lengths(items) that:
# - accepts a list of objects that support len()
# - uses a for loop
# - prints len(item) for each item
# - does NOT check whether an item is a string, list, or custom class
#
# Test it with a string, a list, and your AlbumCollection object.

def report_lengths(items):
    # Write your code here.
    pass


# ============================================================
# SECTION 8 — WHEN len() IS NOT SUPPORTED
# ============================================================
# EXERCISE 4 — PREDICT THE RESULT
# Uncomment one line at a time.
#
# print(len(42))
# print(len(None))
#
# QUESTION:
# What exception occurs when the object does not support len()?
# ANSWER: ___________________________________________________
#
# Extra technical note:
# __len__ should return a nonnegative integer. Returning a float or
# negative integer causes an error. A normal method named length() does
# not automatically make the built-in len() work.


# ============================================================
# SECTION 9 — POLYMORPHISM THROUGH METHOD OVERRIDING
# ============================================================
# Another example from the lesson's discussion: related classes can
# implement the same method differently.

class Animal:
    def speak(self):
        return "Some animal sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# EXERCISE 5 — PREDICT BEFORE RUNNING
# animals = [Animal(), Dog(), Cat()]
# for animal in animals:
#     print(animal.speak())
#
# 1. __________
# 2. __________
# 3. __________
#
# QUESTION:
# Why can the same animal.speak() expression produce different results?
# ANSWER: ___________________________________________________


# ============================================================
# SECTION 10 — FINAL REVIEW
# ============================================================
# 1. Define polymorphism in one sentence:
#    ________________________________________________________
#
# 2. Define duck typing in one sentence:
#    ________________________________________________________
#
# 3. Which special method does len() use?
#    ________________________________________________________
#
# 4. Why does len({"A": 1, "B": 2}) work?
#    ________________________________________________________
#
# 5. What must your Person class implement to support len()?
#    ________________________________________________________
#
# 6. How does polymorphism reduce type-specific conditional code?
#    ________________________________________________________
#
# KEY TAKEAWAY:
# Design code around supported behavior whenever appropriate.
# Objects of different types can respond to the same operation.
# ============================================================
# END OF LESSON
# ============================================================
