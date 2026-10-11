# Named Tuples — Study Summary
# Instructor summary:
# - A tuple stores objects in a fixed sequence and is immutable.
# - A named tuple also lets us access values through descriptive field names.
# - collections.namedtuple() creates a new class that inherits from tuple.
# - Call the generated class to create individual objects.
# - Declare field names with a list of strings or a space-separated string.
# - Positional arguments follow the order of the declared fields.
# - Keyword arguments identify fields by name, so their order can vary.
# - Named tuples are useful for simple records, such as books or playing cards.
# - They reduce the setup code needed to create a class for storing data.
#
# Clarifications to the transcript:
# - collections is a standard-library module; no installation is required.
# - namedtuple is a factory function that returns a class, not an instance
#   of the record you want to store. Book(...) then creates a record.
# - Named tuples have methods, including inherited tuple methods and helpers
#   such as _replace() and _asdict(). We do not write custom methods here.
# - Access fields with book.title, not book["title"]. A named tuple is not
#   a dictionary, even though its fields have names.
# - Immutability prevents replacing, adding, or deleting tuple elements.
#   A mutable object stored inside a tuple can still be changed.
# - _replace() returns a new record; it does not modify the original.
# - Use valid, unique field names that are not keywords and do not begin
#   with an underscore, such as title and author.

import collections


# --- 1. Create the Book class ---
Book = collections.namedtuple("Book", ["title", "author"])

# Equivalent alternative (use one definition, not both):
# Book = collections.namedtuple("Book", "title author")
#
# "Book" supplies the generated class's name.
# ["title", "author"] supplies its fields and their order.
# Book stores the class returned by namedtuple().
# We do not need to write __init__ or assign each attribute ourselves.
print(issubclass(Book, tuple))  # => True


# --- 2. Instantiate records with positional arguments ---
animal_farm = Book("Animal Farm", "George Orwell")

# The argument order matches the field order:
# First argument  -> title
# Second argument -> author
print(animal_farm)
# => Book(title='Animal Farm', author='George Orwell')
print(isinstance(animal_farm, Book))   # => True
print(isinstance(animal_farm, tuple))  # => True


# --- 3. Instantiate records with keyword arguments ---
gatsby = Book(title="The Great Gatsby", author="F. Scott Fitzgerald")

# Keyword arguments can appear in a different order:
other_gatsby = Book(author="F. Scott Fitzgerald", title="The Great Gatsby")

print(gatsby)
# => Book(title='The Great Gatsby', author='F. Scott Fitzgerald')
print(gatsby == other_gatsby)  # => True
# These records contain the same values in the same field positions.


# --- 4. Access values by index ---
print(animal_farm[0])  # => Animal Farm
print(gatsby[1])       # => F. Scott Fitzgerald
print(animal_farm[-1]) # => George Orwell

# Like a regular tuple, a named tuple uses zero-based indexing.
# Position 0 stores title; position 1 stores author.


# --- 5. Access values by field name ---
print(animal_farm.title)  # => Animal Farm
print(gatsby.author)     # => F. Scott Fitzgerald

print(animal_farm.title == animal_farm[0])  # => True
print(gatsby.author == gatsby[1])          # => True
# Field names make the meaning of each value easier to understand.
# Both forms access the same stored values.
# Keep this intentional error commented out:
# print(animal_farm["title"])  # TypeError: tuple indices cannot be strings.


# --- 6. Use familiar tuple behavior ---
print(len(animal_farm))       # => 2
print("George Orwell" in animal_farm)  # => True

book_title, book_author = animal_farm
print(book_title)   # => Animal Farm
print(book_author)  # => George Orwell

# Iteration follows field order:
for value in gatsby:
    print(value)
# => The Great Gatsby
# => F. Scott Fitzgerald


# --- 7. Named tuple fields are immutable ---
# Keep these intentional errors commented out:
# animal_farm.title = "1984"  # AttributeError: the field cannot be reassigned.
# animal_farm[0] = "1984"     # TypeError: tuple items cannot be reassigned.
# del animal_farm.author     # AttributeError: the field cannot be deleted.
#
# Create a new record when you need different field values:
new_book = animal_farm._replace(title="1984")

print(new_book)
# => Book(title='1984', author='George Orwell')
print(animal_farm.title)  # => Animal Farm
# _replace() leaves the original record unchanged.
# Its leading underscore is part of this documented helper's name.


# --- 8. Inspect fields or create a dictionary ---
print(Book._fields)  # => ('title', 'author')

book_details = animal_farm._asdict()
print(book_details)
# => {'title': 'Animal Farm', 'author': 'George Orwell'}
print(book_details["title"])  # => Animal Farm
# _asdict() returns a dictionary, which DOES support string-key lookup.


# --- 9. Immutability does not freeze nested objects ---
ReadingList = collections.namedtuple("ReadingList", ["name", "titles"])
weekend = ReadingList("Weekend", ["Animal Farm"])

weekend.titles.append("The Great Gatsby")
print(weekend.titles)  # => ['Animal Farm', 'The Great Gatsby']
# The titles field still refers to the same list; we changed that list.
# Reassigning weekend.titles to a different list would raise AttributeError.
# Use immutable field values when you also need the contents to stay fixed.


# --- 10. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Keep intentional-error examples commented out.

# Exercise 1 — Class or instance?
# What does collections.namedtuple() return?
# Which name below refers to a class, and which refers to an instance?
# Card = collections.namedtuple("Card", ["suit", "rank"])
# ace = Card("hearts", "ace")
# ANSWER:


# Exercise 2 — Match positions and names
# Predict all four outputs.
# novel = Book("Dune", "Frank Herbert")
# print(novel[0])
# print(novel.author)
# print(novel[-1])
# print(len(novel))
# ANSWER:


# Exercise 3 — Keyword argument order
# Predict the result. Explain why the keyword order does not change
# the order of values stored in the record.
# first = Book("Dune", "Frank Herbert")
# second = Book(author="Frank Herbert", title="Dune")
# print(first == second)
# print(second[0])
# ANSWER:


# Exercise 4 — Identify invalid operations
# Which expressions work, and which raise errors? Explain each choice.
# animal_farm.title
# animal_farm["title"]
# animal_farm.author = "Another author"
# animal_farm._replace(author="Another author")
# ANSWER:


# Exercise 5 — Predict replacement behavior
# Predict both titles. Does _replace() modify original?
# original = Book("Animal Farm", "George Orwell")
# replacement = original._replace(title="1984")
# print(original.title)
# print(replacement.title)
# ANSWER:


# Exercise 6 — Create your own record
# Create a Movie named tuple class with title, director, and year fields.
# Instantiate one movie with positional arguments and another with keywords.
# Print a field by name, access a field by index, and unpack one movie
# into three variables.
# Write your code below:


# Optional challenge — Explain nested mutability
# A named tuple contains a list. Why can list.append() work even though
# assigning a new value to the named tuple's field does not?
# Create a small example and explain what changes and what stays the same.
# ANSWER:


# --- 11. Final review ---
# 1. Import namedtuple from the __________ module.
# 2. namedtuple() returns a new __________.
# 3. Every generated named tuple class inherits from __________.
# 4. Fields can be accessed by index or by __________ syntax.
# 5. Positional argument order follows the declared __________ order.
# 6. Named tuple fields are mutable or immutable?
# 7. The __________ helper creates a new record with selected changes.
# 8. Does a named tuple have no methods at all? Explain.
# ANSWER:
