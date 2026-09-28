# Introduction to object-oriented programming — Study Summary
# Instructor summary:
# - Object-oriented programming (OOP) organizes code around interacting objects.
# - Objects can model physical things (balls, houses) or ideas (messages, games).
# - An object bundles data (state) with behavior.
# - Data attributes describe an object's state: its characteristics or details.
# - Methods provide behavior: actions associated with an object.
# - A method may read state, change state, or return a result.
# - A class defines an object type; think of it as a blueprint or recipe.
# - An instance is an object of a class. Creating one is called instantiation.
# - Instances of the same class share available behavior but can have different state.
# - Familiar Python lists and strings are already objects.
#
# Clarifications to the transcript:
# - Built-in objects can model many problems; custom classes are another tool.
# - Not every method changes an object. For example, str.upper() returns a new string.
# - Separate instances can share references to other objects; independence is not
#   an automatic guarantee that all their data has been copied.
# - A class is itself a Python object, even though we call it a blueprint.
# - A module organizes code and can contain classes and factory functions.
#   A module is not itself a class blueprint that you instantiate.
# - Technically, methods are attributes too. In this introduction, "attributes"
#   means data attributes when we contrast data with methods.
#
# This lesson focuses on concepts. Custom class syntax comes next.


# --- 1. Connect classes and instances to familiar objects ---
songs = ["YYZ", "Limelight"]
artists = ["Rush", "Yes", "Genesis"]
print(type(songs))    # => <class 'list'>
print(type(artists))  # => <class 'list'>
print(songs)          # => ['YYZ', 'Limelight']
print(artists)        # => ['Rush', 'Yes', 'Genesis']
# Both objects are instances of list, but they contain different data.
# A class describes the type; an instance is a particular object of that type.


# --- 2. Create an instance by calling a built-in class ---
playlist = list()
print(playlist)        # => []
print(type(playlist))  # => <class 'list'>
# list() creates an empty list instance. [] also creates an empty list.
# Instantiation means creating an instance, not merely naming a variable.


# --- 3. Methods provide behavior ---
playlist.append("Tom Sawyer")
print(playlist)  # => ['Tom Sawyer']
playlist.append("YYZ")
print(playlist)  # => ['Tom Sawyer', 'YYZ']
print(playlist.count("YYZ"))  # => 1
print(playlist)              # => ['Tom Sawyer', 'YYZ']
# object.method(arguments) calls a method on that object.
# append() changes the list's state. count() reads it without changing it.
# len(playlist) is a built-in function call, not a method-call expression.
print(len(playlist))  # => 2


# --- 4. Same behavior, separate state ---
first_playlist = ["YYZ"]
second_playlist = ["Roundabout"]
first_playlist.append("Limelight")
print(first_playlist)   # => ['YYZ', 'Limelight']
print(second_playlist)  # => ['Roundabout']
# Both lists support append(), but this call changes only first_playlist.
# These two list literals created two separate list objects.
# Assigning another name to an existing list does NOT create a new instance:
same_playlist = first_playlist
print(same_playlist is first_playlist)  # => True
# Both names now refer to the same object. "is" checks object identity.


# --- 5. A method does not have to change its object ---
artist = "Rush"
uppercase_artist = artist.upper()
print(uppercase_artist)  # => RUSH
print(artist)            # => Rush
# Strings are immutable. upper() returns a string result without changing artist.
# Behavior can produce a result without modifying the original state.


# --- 6. Plan a custom object before writing a class ---
# Conceptual class: SoccerBall
# Possible data attributes:
# - manufacturer: a string such as "Nike"
# - weight_grams: a number such as 430
# - colors: a list of strings such as ["yellow", "blue"]
# Possible methods:
# - describe(): return a description based on the ball's data
# - paint(color): update the ball's colors
# These names describe a possible design, not a built-in Python class.
#
# Conceptual class: House
# Possible data attributes: address, price, owner.
# Possible methods: describe(), change_owner(new_owner).
# Two House instances could have different addresses and owners while
# supporting the same methods. Choose data and behavior your program needs.
#
# Physical objects are not required:
# A ChatMessage could have text and sender data, plus an edit(new_text) method.
# The class is the blueprint; each particular message is an instance.


# --- 7. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# For conceptual questions, explain in your own words.
# You do not need to define a custom class in this lesson.

# Exercise 1 — Class or instance?
# A music app has a Playlist class and two playlists named "Road Trip"
# and "Study Time" created from it.
# Identify the class and the two instances.
# What is the act of creating an instance called?
# ANSWER:


# Exercise 2 — Data or behavior?
# A proposed Song object has title, artist, duration_seconds, play(),
# and describe().
# Which names describe data attributes, and which describe methods?
# Must describe() change the object's state? Explain.
# ANSWER:


# Exercise 3 — Same class, different state
# Predict all four outputs. Explain why only one list changes.
# first = ["Rush"]
# second = ["Yes"]
# first.append("Genesis")
# print(first)
# print(second)
# print(type(first))
# print(type(second))
# ANSWER:


# Exercise 4 — Does every method change state?
# Predict all three outputs. Identify the method call and explain whether
# it changes the original string.
# title = "Limelight"
# loud_title = title.upper()
# print(loud_title)
# print(title)
# print(len(title))
# ANSWER:


# Exercise 5 — Another name or another instance?
# Predict both outputs. Explain whether assigning backup creates a new list.
# songs = ["YYZ"]
# backup = songs
# backup.append("Limelight")
# print(songs)
# print(backup is songs)
# ANSWER:


# Exercise 6 — Design your own object
# Choose a Book, GameCharacter, or another object you would like to model.
# 1. Give your proposed class a name.
# 2. List three data attributes and an example value for each.
# 3. List two methods and explain what each would do.
# 4. Describe two instances with different attribute values.
# 5. Explain which method would change state and what data it would change.
# This is a design exercise: write comments, not a class definition yet.
# ANSWER:


# Optional challenge — Describe a playlist without changing it
# Work through this one together when you are ready.
# Define describe_playlist(titles), where titles is a list of song-title strings.
# Return a dictionary with two entries:
# - "song_count": the number of titles
# - "yyz_count": the number of exact "YYZ" strings (case-sensitive)
# Use len() and the list's count() method. Leave titles unchanged.
# Explain which operation is a function call and which is a method call.
# This is a regular function using an existing object, not a custom class.
# Write your code below:


# Uncomment these checks after defining your function:
# print(describe_playlist(["YYZ", "Limelight", "YYZ"])) # => {'song_count': 3, 'yyz_count': 2}
# print(describe_playlist(["yyz", "Roundabout"])) # => {'song_count': 2, 'yyz_count': 0}
# print(describe_playlist([])) # => {'song_count': 0, 'yyz_count': 0}
