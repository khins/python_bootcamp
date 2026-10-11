# Length with __len__ — Study Summary
# Instructor summary:
# - __len__ gives a custom object a meaningful concept of length.
# - Python's built-in len() uses this special method to obtain a length.
# - Define __len__(self) in the class and return a nonnegative integer.
# - The class decides what its length represents.
# - A Library can define its length as the number of books it contains.
# - __len__ can delegate to len() on a stored collection, such as a tuple.
# - A parameter written as *books collects positional arguments into a tuple.
# - Named tuples provide convenient Book records for this example.
#
# Clarifications and connections:
# - The built-in function is spelled len(), with lowercase letters.
# - A length must be an integer greater than or equal to zero, not a float.
# - A negative result causes len() to raise ValueError; a float causes TypeError.
# - Define special methods on the class; implicit lookup uses the object's type.
# - Prefer len(object) over calling object.__len__() directly in ordinary code.
# - __len__ does not automatically make an object iterable or indexable.
# - Without __bool__, Python also uses __len__ to determine truthiness:
#   zero is falsy, and a positive length is truthy.
# - *books collects arguments in a definition; *collection unpacks them
#   in a call. Both uses appear below.

import collections


# --- 1. Explore length with a built-in string ---
word = "dynasty"

print(len(word))       # => 7
print(word.__len__())  # => 7
# The direct call illustrates the special method used for string length.
# Use len(word) in ordinary code.


# --- 2. Create simple Book records ---
Book = collections.namedtuple("Book", ["title", "author"])

animal_farm = Book("Animal Farm", "George Orwell")
gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald")

# Each book has two named fields. These are the records our library stores.
print(animal_farm.title)  # => Animal Farm
print(gatsby.author)     # => F. Scott Fitzgerald


# --- 3. Define what the length of a Library means ---
class Library:

    def __init__(self, *books):
        self.books = books
        self.librarians = []

    def __len__(self):
        return len(self.books)


# *books accepts zero or more positional arguments after self.
# Python collects those arguments into a tuple named books.
# Each Library stores that tuple and starts with its own empty librarian list.
#
# Our rule:
# Length of a library = number of books in self.books.
#
# We could model a different measure, but this class counts books.
# The number of librarians does not affect this rule.


# --- 4. Create libraries with different numbers of books ---
l1 = Library(animal_farm)
l2 = Library(animal_farm, gatsby)
empty_library = Library()

print(len(l1))             # => 1
print(len(l2))             # => 2
print(len(empty_library))  # => 0

print(type(l2.books))      # => <class 'tuple'>
print(empty_library.books) # => ()
# With no positional book arguments, *books collects an empty tuple.


# --- 5. Trace a length calculation ---
# For len(l2), Python uses Library.__len__ with l2 as self.
#
# Inside that method:
# return len(self.books)
#
# self.books contains (animal_farm, gatsby).
# len() on that tuple gives 2, so len(l2) gives 2.
print(len(l2.books))  # => 2
print(len(l2))        # => 2

# These are different objects with different meanings of length:
print(len(animal_farm))        # => 2 (fields in the named tuple)
print(len(animal_farm.title))  # => 11 (characters in the title)
print(len(l1))                 # => 1 (books in the library)
# Library.__len__ counts book records, not their fields or title characters.
# Do not return len(self) inside __len__: that would call it again repeatedly.


# --- 6. Librarians do not change the book count ---
l2.librarians.append("Alex")
l2.librarians.append("Sam")
l2.librarians.append("Jordan")

print(len(l2.librarians))  # => 3
print(len(l2))             # => 2
# The class has multiple collections, but __len__ uses only self.books.


# --- 7. Unpack a collection when passing multiple books ---
book_collection = [animal_farm, gatsby]

unpacked_library = Library(*book_collection)
print(len(unpacked_library))  # => 2
# The * in this call passes the list's elements as separate arguments.

nested_library = Library(book_collection)
print(len(nested_library))    # => 1
# Without *, the entire list is ONE positional argument.
# This simple class does not validate the types of its arguments.
# It stores a tuple containing that one list, so its length is 1.


# --- 8. Connect length to truthiness ---
print(bool(empty_library))  # => False
print(bool(l1))             # => True

if l2:
    print("This library has books.")
# => This library has books.

# Library does not define __bool__, so Python falls back to __len__.
# Defining __bool__ would give that method priority for truth testing.


# --- 9. Return a valid length ---
# Keep these intentional-error examples commented out:
#
# class NegativeLength:
#     def __len__(self):
#         return -1
#
# print(len(NegativeLength()))  # ValueError: __len__() should return >= 0
#
# class FractionalLength:
#     def __len__(self):
#         return 1.5
#
# print(len(FractionalLength()))  # TypeError: a float is not a valid length.
#
# Returning len(self.books) gives Library a valid nonnegative integer.


# --- 10. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Keep intentional-error examples commented out.

# Exercise 1 — Predict the lengths
# print(len(Library()))
# print(len(Library(gatsby)))
# print(len(Library(animal_farm, gatsby, animal_farm)))
# Does our class remove duplicate books before counting?
# ANSWER:


# Exercise 2 — Trace self and *books
# For this example, what does self refer to inside __len__?
# What type is self.books, and which objects does it contain?
# branch = Library(animal_farm, gatsby)
# print(len(branch))
# ANSWER:
# self refers to:
# Type of self.books:
# Contents of self.books:
# Returned length:


# Exercise 3 — Choose the collection
# Predict both outputs and explain why they differ.
# branch = Library(gatsby)
# branch.librarians.extend(["Casey", "Morgan"])
# print(len(branch.librarians))
# print(len(branch))
# ANSWER:


# Exercise 4 — Collecting versus unpacking
# Predict both outputs. Explain what * changes at the call site.
# books = [animal_farm, gatsby]
# print(len(Library(books)))
# print(len(Library(*books)))
# ANSWER:


# Exercise 5 — Truthiness from length
# Predict both outputs. Why does this work without Library.__bool__?
# print(bool(Library()))
# print(bool(Library(animal_farm)))
# ANSWER:


# Exercise 6 — Define your own length
# Create a Playlist class whose __init__ accepts *songs.
# Store the songs in an attribute and define __len__ to count them.
# Test an empty playlist and a playlist containing three song titles.
# Write your code below:


# Optional challenge — Model a different measure
# Create a separate StaffedLibrary class whose length counts librarians.
# Give it book and librarian collections, then demonstrate that adding
# a librarian changes its length while adding a book does not.
# Explain why a clearly documented length rule matters to users of a class.
# ANSWER:


# --- 11. Final review ---
# 1. The built-in len() function uses the __________ special method.
# 2. A valid length is an integer greater than or equal to __________.
# 3. A parameter written as *books collects arguments into a __________.
# 4. In this lesson, Library length counts __________, not librarians.
# 5. Calling Library(*books) __________ the collection into arguments.
# 6. Without __bool__, an object with length zero is truthy or falsy?
# 7. Does defining __len__ automatically allow library[0]?
# ANSWER:
