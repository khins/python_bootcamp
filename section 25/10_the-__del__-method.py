
# ============================================================
# FILE: the-__del__-method.py
# TOPIC: The __del__ Magic Method
# ============================================================

# LESSON OBJECTIVES
#
# 1. Understand the purpose of __del__.
# 2. Learn when Python may invoke __del__.
# 3. Understand how object references affect object lifetime.
# 4. Use time.sleep() to observe execution order.
# 5. Practice predicting output.
# 6. Write your own class using __del__.


# ============================================================
# SECTION 1 — WHAT IS __del__?
# ============================================================

# __del__ is a special method (also called a dunder method).
#
# Python may call __del__ when an object is being finalized.
#
# Syntax:
#
# def __del__(self):
#     ...
#
# Important:
# __del__ is not called simply because a variable is deleted.
# It is associated with the object's lifetime, not the name
# of the variable referencing it.
#
# In CPython, an object with no remaining references is often
# finalized immediately.
#
# However, the timing of __del__ is not guaranteed.


# ============================================================
# SECTION 2 — OUR FIRST __del__ EXAMPLE
# ============================================================

class Garbage:

    def __del__(self):
        print("This is my last breath")


# Create an instance of Garbage.
# Uncomment to experiment.

# g = Garbage()

# QUESTION 1:
#
# What do you predict will happen when this script finishes?
#
# ANSWER:
#
# _________________________________________________


# ============================================================
# SECTION 3 — REASSIGNING A VARIABLE
# ============================================================

# Consider the following:
#
# g = Garbage()
# g = [1, 2, 3]
#
# Initially:
#
# g ------> Garbage object
#
# After reassignment:
#
# g ------> [1, 2, 3]
#
# If no other references exist, the Garbage object
# becomes eligible for cleanup.


# EXERCISE 1 — PREDICT THE OUTPUT

def exercise_one():

    g = Garbage()

    print("Object created")

    g = [1, 2, 3]

    print("Variable reassigned")


# Uncomment to test your prediction.
# exercise_one()


# QUESTION 2:
#
# Predict the order of the printed messages.
#
# ANSWER:
#
# 1. ___________________________________
# 2. ___________________________________
# 3. ___________________________________
#
# Why might __del__ execute before the function finishes?
#
# _________________________________________________
# _________________________________________________


# ============================================================
# SECTION 4 — INTRODUCING THE TIME MODULE
# ============================================================

# Python's time module provides a sleep() function.
#
# sleep(seconds)
#
# This pauses the current thread for approximately
# the specified number of seconds.

import time


# EXAMPLE

def sleep_example():

    print("Starting")

    time.sleep(2)

    print("Finished")


# Uncomment to run:
# sleep_example()


# QUESTION 3:
#
# Approximately how long will Python wait between messages?
#
# ANSWER:
#
# _________________________________________________


# ============================================================
# SECTION 5 — OBSERVING __del__ WITH time.sleep()
# ============================================================

# This reproduces the main demonstration from the lesson.

def exercise_two():

    g = Garbage()

    g = [1, 2, 3]

    time.sleep(5)

    print("Program done")


# Uncomment to run:
# exercise_two()


# QUESTION 4:
#
# Predict the output order.
#
# ANSWER:
#
# 1. ___________________________________
# 2. ___________________________________
#
# Does __del__ necessarily have to wait until
# the entire program finishes?
#
# ANSWER:
#
# _________________________________________________
#
# Why is the sleep() function useful in this example?
#
# _________________________________________________


# ============================================================
# SECTION 6 — OBJECTS AND REFERENCES
# ============================================================

# Remember:
#
# Variables reference objects.
#
# Multiple variables can reference the same object.
#
# Reassigning one variable does not necessarily
# destroy the original object.


# EXERCISE 3 — MULTIPLE REFERENCES

def exercise_three():

    first = Garbage()

    second = first

    print("Two references exist")

    first = None

    print("First reference removed")

    second = None

    print("Second reference removed")


# Uncomment to run:
# exercise_three()


# QUESTION 5:
#
# After first = None, does the Garbage object
# still have a reference?
#
# ANSWER:
#
# _________________________________________________
#
# Which assignment removes the final reference?
#
# ANSWER:
#
# _________________________________________________
#
# Predict the order of all printed messages.
#
# ANSWER:
#
# 1. ___________________________________
# 2. ___________________________________
# 3. ___________________________________
# 4. ___________________________________


# ============================================================
# SECTION 7 — USING del ON A VARIABLE
# ============================================================

# Python also has a del statement.
#
# Example:
#
# del variable
#
# This removes the variable's binding.
#
# It does not necessarily destroy the object,
# because other variables may reference it.


# EXERCISE 4 — del AND OBJECT REFERENCES

def exercise_four():

    first = Garbage()

    second = first

    del first

    print("Deleted first name")

    del second

    print("Deleted second name")


# Uncomment to run:
# exercise_four()


# QUESTION 6:
#
# Does deleting first immediately finalize the object?
#
# ANSWER:
#
# _________________________________________________
#
# Why or why not?
#
# _________________________________________________
#
# At what point is the final reference removed?
#
# _________________________________________________


# ============================================================
# SECTION 8 — WRITE YOUR OWN CLASS
# ============================================================

# CODING CHALLENGE 1
#
# Create a class called MusicAlbum.
#
# Requirements:
#
# 1. Define __init__(self, title, artist).
# 2. Store title and artist as instance attributes.
# 3. Define __del__(self).
# 4. Print a message when the object is finalized.
#
# Example message:
#
# "Cleaning up album: Hemispheres"
#
# Do not hardcode the album title.
# Use the object's title attribute.


class MusicAlbum:

    # Write your code here.
    pass


# TEST CODE
#
# Uncomment after implementing MusicAlbum.
#
# album = MusicAlbum("Hemispheres", "Rush")
#
# album = None


# ============================================================
# SECTION 9 — CHALLENGE: TWO OBJECTS
# ============================================================

# CODING CHALLENGE 2
#
# Using your MusicAlbum class:
#
# 1. Create album1 for "Hemispheres" by "Rush".
# 2. Create album2 for "Fragile" by "Yes".
# 3. Reassign album1 to None.
# 4. Print "First album released".
# 5. Reassign album2 to None.
# 6. Print "Second album released".
#
# Before running:
#
# Predict the order of the cleanup messages.


def music_album_challenge():

    # Write your code here.
    pass


# Uncomment after implementing:
# music_album_challenge()


# YOUR PREDICTED OUTPUT:
#
# 1. ___________________________________
# 2. ___________________________________
# 3. ___________________________________
# 4. ___________________________________


# ============================================================
# SECTION 10 — CHALLENGE: SHARED REFERENCES
# ============================================================

# CODING CHALLENGE 3
#
# Create one MusicAlbum object.
#
# Assign it to two different variables.
#
# Remove the first reference.
#
# Print a message.
#
# Remove the second reference.
#
# Print another message.
#
# Determine when __del__ executes.


def shared_reference_challenge():

    # Write your code here.
    pass


# Uncomment after implementing:
# shared_reference_challenge()


# QUESTION 7:
#
# How many MusicAlbum objects did you create?
#
# ANSWER:
#
# _________________________________________________
#
# How many variables referenced that object?
#
# ANSWER:
#
# _________________________________________________
#
# How many times should __del__ normally execute
# for that one object?
#
# ANSWER:
#
# _________________________________________________


# ============================================================
# SECTION 11 — REAL-WORLD CLEANUP
# ============================================================

# The lesson mentions cleanup operations such as:
#
# - Closing database connections
# - Shutting down processes
# - Removing temporary files
#
# Although __del__ can participate in object finalization,
# it should not be the primary mechanism for important
# resource cleanup.
#
# Why?
#
# Its execution time is not guaranteed.
# It may run during interpreter shutdown.
# Objects involved in reference cycles can complicate timing.
#
# Better approaches for reliable cleanup include:
#
# - Explicit close() methods
# - try/finally
# - Context managers using with
#
# We can study context managers in a future lesson.


# ============================================================
# SECTION 12 — FINAL REVIEW
# ============================================================

# Fill in the blanks.
#
# 1. The special method for object finalization is ________.
#
# 2. Its first parameter is conventionally named ________.
#
# 3. Python uses the ________ module to provide sleep().
#
# 4. time.sleep(5) pauses execution for approximately
#    ________ seconds.
#
# 5. A variable is a name that ________ an object.
#
# 6. Reassigning a variable does not necessarily destroy
#    an object if other ________ still exist.
#
# 7. The del statement removes a name's ________.
#
# 8. In CPython, removing the last reference often causes
#    immediate object ________.
#
# 9. The exact timing of __del__ is not ________.
#
# 10. For reliable cleanup, a context ________ is often
#     preferable to relying on __del__.


# ============================================================
# SECTION 13 — KEY CONCEPTS
# ============================================================

# __init__
# Called during instance initialization.
#
# __del__
# Called when an object is being finalized.
#
# REFERENCE
# A variable name can reference an object.
#
# REASSIGNMENT
# Changes which object a name references.
#
# del
# Removes a binding or deletes a target, depending
# on the expression.
#
# GARBAGE COLLECTION
# Python's mechanism for reclaiming objects that
# are no longer needed.
#
# sys.modules
# Not involved in ordinary instance finalization;
# this is the module cache from our previous lessons.
#
# IMPORTANT TAKEAWAY:
#
# __del__ belongs to the object, not to a variable name.
#
# Removing one reference does not necessarily mean
# the object is ready to be finalized.
#
# ============================================================
# END OF LESSON
# ============================================================
