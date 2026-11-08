# Class definition and instantiation — Study Summary
# Instructor summary:
# - Use class to define a new object type (the blueprint).
# - Write a class name, a colon, and an indented body.
# - Use pass as a placeholder when you have no class body statements yet.
# - Class names conventionally use PascalCase: Person, DatabaseConnection.
# - Instance variable names conventionally use snake_case: database_connection.
# - Call the class with parentheses to create an instance: Person().
# - Assign the instance to a variable to refer to it later.
# - For the basic classes here, each call creates a separate instance.
# - Instances can have the same type without being the same object.
# - Printing a basic instance uses a default object representation.
#
# Clarifications to the transcript:
# - PascalCase and singular names are conventions, not syntax requirements.
#   Choose a name that accurately describes what one instance represents.
# - Class names follow Python identifier rules: they cannot start with a digit,
#   contain spaces or hyphens, or be reserved keywords.
# - Empty parentheses in a class definition are optional: class Person: works.
#   Parentheses in Person() are needed to CALL the class and create an instance.
# - class Person(object): is still valid Python 3, but object is redundant here.
# - A class namespace is not private or protected access. Class attributes
#   can be accessed through the class; ordinary if/for blocks do not create
#   their own scopes. Class and function scope rules are not identical.
# - pass adds no custom data or methods, but instances still inherit basic
#   behavior from object. They are not completely without attributes/methods.
# - The hexadecimal portion of the default representation is not a stable
#   output to memorize. In CPython it reflects a memory address; do not rely
#   on that as a portable Python guarantee. Use is to check identity.


# --- 1. Define a basic class ---
class Person:
    pass


# class introduces the definition; Person names the new class.
# The colon starts the body, and pass is indented inside that body.
# pass does nothing, but provides the statement an otherwise empty body needs.
# Defining this class does not create a Person instance yet.
# This equivalent spelling also allows an empty body:
# class Person():
#     pass


# --- 2. Define a class with a multiword name ---
class DatabaseConnection:
    pass


# Capitalize the first letter of each word in a conventional class name.
# This is just a placeholder type: its name does not connect to a database.
# Later lessons will add custom data and behavior to classes.


# --- 3. Instantiate objects by calling the class ---
boris = Person()
sally = Person()
database_connection = DatabaseConnection()
# These statements are outside the class bodies (not indented).
# Person is the class; Person() creates an instance of that class.
# boris and sally are variable names referring to two separate instances.
# Naming a variable boris does not automatically give its object a name attribute.

print(type(boris) is Person)  # => True
print(type(sally) is Person)  # => True
print(type(database_connection) is DatabaseConnection)  # => True
# type(instance) returns its class for these objects.


# --- 4. Inspect the default object representation ---
print(boris)
print(sally)
print(database_connection)
# When run directly, typical output has this shape:
# <__main__.Person object at 0x...>
# <__main__.Person object at 0x...>
# <__main__.DatabaseConnection object at 0x...>
# The dots stand for a varying hexadecimal value, not literal output.
# The module prefix may differ if this file is imported instead of run directly.
# Python uses this default because we have not customized string display.
# Do not predict or compare the exact hexadecimal text.


# --- 5. Same type does not mean same instance ---
print(type(boris) is type(sally))  # => True
print(boris is sally)             # => False
# Both came from Person, but each call created a separate object.

another_name = boris
print(another_name is boris)  # => True
print(another_name is sally)  # => False
# Assignment gives the existing object another name; it does not instantiate
# a new Person. There is no Person() call in another_name = boris.


# --- 6. Refer to a class without calling it ---
person_class = Person
print(person_class is Person)  # => True
new_person = person_class()
print(type(new_person) is Person)  # => True
print(new_person is boris)         # => False
# Classes are objects too, so a variable can refer to a class.
# Person refers to the blueprint; Person() calls it to make an instance.
# Prefer descriptive variable names and avoid overwriting the class name:
# Person = Person()  # Would replace the name's reference to the class.


# --- 7. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# For default instance displays, describe the shape; do not guess an address.
# Keep intentional syntax errors commented out.

# Exercise 1 — Define a class
# Write an empty class named Guitar using pass.
# Explain why pass is used and which line must be indented.
# Write your code below:

# ANSWER:
class Guitar:
    pass

my_guitar = Guitar()

print(type(my_guitar))
print(isinstance(my_guitar, Guitar))

print("-" * 65)
# Exercise 2 — Create two instances
# Predict all three outputs. Identify the class and the instance variables.
class Song:
    pass

first_song = Song() 
second_song = Song() 
print(type(first_song) is Song)
print(type(second_song) is Song)
print(first_song is second_song)
# ANSWER:
# True
# True
# False
# An instance attribute is different. It's data stored on a particular instance, such as first_song.title.

print("-" * 65)
# Exercise 3 — Class reference or instance?
# Predict both outputs. Which assignment actually creates an instance?
class Player:
    pass

player_type = Player
player = Player() # this creates an instance of Player
print(player_type is Player)
print(type(player) is Player)
# ANSWER:
# True
# True

print("-" * 65)
# Exercise 4 — Another name for an object
# Predict all three outputs. How many Ticket instances are created?
class Ticket:
    pass

first = Ticket()
second = first
third = Ticket()
print(first is second)
print(first is third)
print(type(second) is type(third))
# ANSWER:
# 2 Ticket instances are created
# True
# False
# True
# The important distinction is between object identity and object type.
# - is compares whether two references point to the same object.
# - type() identifies an object's class.

# Exercise 5 — Diagnose syntax and naming
# Consider these proposed definition headers separately:
# A. class music_player:
# B. class MusicPlayer:
# C. class 2Player:
# D. class MusicPlayer():
# Assume each header would be followed by a correctly indented pass.
# Which headers are valid Python? Which valid name misses the PascalCase
# convention? Are empty parentheses required in a class definition?
# Explain why MusicPlayer() has a different role outside a definition.
# ANSWER:
# A. class music_player: is not python proper syntax for class, snake case is for variables
    # valid Python syntax, but it doesn't follow the recommended naming convention.
# B. class MusicPlayer: is proper python naming syntax, it uses pascal conventions for class
    # PEP 8 style guide recommends
# C. class 2Player: invalid because it starts with a number value
# D. class MusicPlayer():  valid Python 3, The empty parentheses are optional

# Exercise 6 — Build your own simple type
# 1. Define an empty class representing one object of your choice.
# 2. Use a descriptive PascalCase name and pass in its body.
# 3. Create two instances and store them in snake_case variables.
# 4. Print both instances and describe the shape of their default displays.
# 5. Print whether they have the same type and whether they are the same object.
# 6. Explain why the class name alone does not instantiate an object.
# Write your code below:

# ANSWER:
class MuiscPlayer:
    pass

jazz_favorites = MuiscPlayer()
rock_classics = MuiscPlayer()
print(jazz_favorites)
print(rock_classics)
print(type(jazz_favorites) is type(rock_classics))
# the class name alone does not instantiate an object, it has to be called in order to create an instance


# Optional challenge — Create a pair of instances
# Work through this one together when you are ready.
# Define an empty class named Album.
# Define a regular function make_album_pair() that returns a list containing
# two NEW Album instances. Each function call should create two new objects.
# Do not add custom attributes or methods yet.
# Write your code below:
class Album:
    person_class

def make_album_pair() -> list:
    new_list = []

    album1 = Album()
    album2 = Album()

    # Add both album objects to new_list
    new_list.append(album1)
    new_list.append(album2)

    return new_list


album1 = Album()
album2 = Album()

albums = make_album_pair()
print(albums)

# Uncomment these checks after defining Album and make_album_pair:
print(len(make_album_pair())) # => 2
pair = make_album_pair()
print(type(pair[0]) is Album) # => True
print(type(pair[1]) is Album) # => True
print(pair[0] is pair[1]) # => False
another_pair = make_album_pair()
print(pair[0] is another_pair[0]) # => False
# Explain why making one Album and putting it into the list twice would
# fail the requirement for two separate instances.
# 2
# True
# True
# False
# False