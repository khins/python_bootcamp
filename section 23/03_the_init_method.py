# The __init__ method — Study Summary
# Instructor summary:
# - __init__ is a special method used to initialize an instance's state.
# - "Dunder" means double underscore: __init__ has two on each side.
# - Define a method with def inside the indented class body.
# - For the basic classes here, calling the class automatically runs __init__.
# - The first parameter, conventionally named self, receives the instance.
# - Python supplies self automatically; do not pass it in Guitar().
# - Each new instance gets its own initialization call.
# - Assigning an existing instance to another variable does not run __init__.
# - __init__ must return None, which happens implicitly without a return statement.
# - This lesson observes initialization; setting attributes comes later.
#
# Clarifications to the transcript:
# - __init__ initializes an instance that has already been created. Object
#   creation itself is handled by __new__, which is beyond this lesson.
# - Dunder methods are special methods, not private methods. Their names
#   participate in Python's defined protocols; do not invent dunder names.
# - self is a naming convention, not a Python keyword. Use it consistently.
# - Empty parentheses in a CLASS DEFINITION are optional: class Guitar: works.
#   Method definitions still need parentheses: def __init__(self):.
# - Putting __init__ first is a common layout choice, not a language requirement.
# - Executing a class definition creates the class and executes its body;
#   it does not run the body of __init__ merely because that method is defined.
# - Calling __init__ directly is possible, but does not create a new instance.
#   Use the normal class call for the instantiation examples in this lesson.


# --- 1. Define an initializer inside a class ---
class Guitar:
    def __init__(self):
        print("A guitar is being initialized.")
        print(f"This object is {self}")


# def is indented inside the class; the two prints are inside the method.
# The exact name __init__ is required for this initialization hook.
# No Guitar instance has been created yet, so those prints have not run.


# --- 2. Instantiate an object and observe automatic initialization ---
acoustic = Guitar()
# Prints two lines automatically, with a default representation like:
# A guitar is being initialized.
# This object is <__main__.Guitar object at 0x...>
# Python supplies the new instance as self; Guitar() takes no explicit
# arguments in this example because __init__ has only the self parameter.
# After initialization finishes, acoustic refers to that same instance.

print(acoustic)
# Shows the same object's default representation seen inside __init__.
# The hexadecimal text varies between runs; do not memorize it.
# The module prefix can differ when this file is imported.


# --- 3. Another instance gets another initialization call ---
electric = Guitar()
# Prints the two initialization lines again, this time for electric.
print(electric)
print(type(acoustic) is Guitar)  # => True
print(type(electric) is Guitar)  # => True
print(acoustic is electric)     # => False
# During the first call, self refers to the acoustic instance.
# During the second call, self refers to the electric instance.
# self is a parameter local to each method call, not one shared global object.


# --- 4. Assignment and printing do not initialize again ---
backup = acoustic
print(backup is acoustic)  # => True
print(backup)
# No new initialization message: assignment adds another reference to acoustic.
# Printing this basic object displays it; it does not call __init__ again.
# There are still only two Guitar instances in these examples.


# --- 5. Trace execution order with predictable output ---
class Ticket:
    def __init__(self):
        print("Initializing ticket")


print("Before")
ticket = Ticket()
print("After")
# Expected output from these three statements:
# Before
# Initializing ticket
# After
# Initialization runs during Ticket(), before assignment to ticket completes.
# The class call returns the instance even though __init__ returns None.
# Do not write return self inside __init__.


# --- 6. An initializer can have an empty placeholder body ---
class Album:
    def __init__(self):
        pass


album = Album()
print(type(album) is Album)  # => True
# pass performs no action. The method implicitly returns None.
# No custom initializer is needed if there is no custom setup to perform;
# this one exists only to demonstrate the syntax.
# Returning a string, number, or the instance from __init__ would raise TypeError
# during ordinary instantiation. Explicit return None is allowed but unnecessary.


# --- 7. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# For object representations, describe their shape rather than an exact address.
# Keep intentional-error examples commented out.

# Exercise 1 — When does the method run?
# Predict the exact output order. Does defining Player print "Ready"?
class Player:
    def __init__(self):
        print("Ready")

print("Before player")
player = Player()
print("After player")
# ANSWER:
# Before player
# Ready
# After player

# Exercise 2 — Count initialization calls
# How many times is "New song" printed? Predict the final two outputs too.
# Explain which statements create instances and which only assign references.
class Song:
    def __init__(self):
        print("New song")

first = Song() # create instances
second = first # only assign references
third = Song() # create instances
print(first is second)
print(first is third)
# ANSWER:
# True
# False

# Constructor parameters
class Song:
    def __init__(self, title):
        self.title = title
        print(f"Created: {self.title}")


first = Song("YYZ")
second = Song("Limelight")
third = first

print(third.title)
print(first is third)
# Created: YYZ
# Created: Limelight
# YYZ
# True

# Changing an instance attribute
class Song:
    def __init__(self, title):
        self.title = title


first = Song("YYZ")
second = Song("Limelight")
third = first

third.title = "Tom Sawyer"

print(first.title)
print(second.title)
print(third.title)
print(first is third)
# Tom Sawyer
# Limelight
# Tom Sawyer
# True

# Independent instance state
class Song:
    def __init__(self, title, plays=0):
        self.title = title
        self.plays = plays


first = Song("YYZ")
second = Song("Limelight", 5)

first.plays += 1
second.plays += 2

print(first.plays)
print(second.plays)
print(first.title)
print(second.title)
# True
# 1
# 7
# YYZ
# Limelight

print("-" * 65)

# Exercise 3 — What does self refer to?
class Book:
    def __init__(self):
        print(self)

book = Book()
print(book)
# Do the two displays describe the same object or different objects?
# Explain who supplies self and why Book() needs no explicit argument here.
# ANSWER:
# <__main__.Book object at 0x0000028D14F63DA0>
# <__main__.Book object at 0x0000028D14F63DA0>
# self is a reference to the instance being initialized, not the mechanism that creates it.
# this instance of Book does take any parameters hence no additional parms after self

# Using self to store data
class Book:
    def __init__(self, title):
        self.title = title
        # title is a parameter that receives the value passed to the constructor.
        # self.title is an instance attribute that stores that value on the object.


first = Book("Dune")
second = Book("Foundation")

print(first.title)
print(second.title)
print(first is second)
# Dune
# Foundation
# False


# Exercise 4 — Diagnose a missing parameter
# This is intentional-error code. Keep it commented out.
class Broken:
    def __init__():
        print("Starting")

# broken = Broken()
# Explain why instantiation raises TypeError before "Starting" can print.
# What parameter should be added to the method definition?
# ANSWER:
# missing self
# Python automatically supplies the instance as the first argument to an instance method. By convention, we name that parameter self.

# Exercise 5 — Diagnose an invalid return
# This is intentional-error code. Keep it commented out.
class Concert:
    def __init__(self):
        print("Ready")

concert = Concert()
# Why does this raise TypeError? How would you display "Ready" during
# initialization without returning a string from __init__?
# ANSWER:
# should return None, not 'str'

class Guitar:
    def __init__(self, brand):
        self.brand = brand
        print("Guitar initialized")

guitar = Guitar("Yamaha")
print(guitar.brand)
# Guitar initialized
# Yamaha

# Exercise 6 — Write your own initializer
# 1. Define a class named MusicPlayer.
# 2. Define __init__ with self as its only parameter.
# 3. Have the method print "Music player ready" and then print self.
# 4. Create two instances stored in different variables.
# 5. Print whether they are the same object.
# 6. Explain how many times the initializer runs and what self refers to each time.
# Do not add custom attributes yet.
# Write your code below:

# ANSWER:
class MusicPlayer:
    def __init__(self):
        print("Music player ready")
        print(self)

player1 = MusicPlayer()
player2 = MusicPlayer()
print(player1 is player2)
# the initializer runs for each instance of music player that is created, self refers to the instance like a this statement 

# Understanding self
class MusicPlayer:
    def __init__(self):
        print(self)

player1 = MusicPlayer()
player2 = MusicPlayer()

print(player1 is player2)
print(type(player1) is type(player2))
# <__main__.MusicPlayer object at 0x0000021F04DC06E0>
# <__main__.MusicPlayer object at 0x0000021F04DC2180>
# False
# True

print("-" * 65)

# Optional challenge — Trace a function that creates instances
# Work through this one together when you are ready.
# Define a class named Drum whose __init__ prints "Drum ready".
# Define a regular function make_drums() that returns a list of two NEW
# Drum instances. The function should not print the messages itself.
# Before running the checks, predict when and how often __init__ runs.
# Write your code below:
class Drum:
    def __init__(self):
        print("Drum ready")

def make_drums() -> list:
    new_list = []

    drum1 = Drum()
    drum2 = Drum()

    new_list.append(drum1)
    new_list.append(drum2)

    return new_list


# Uncomment these checks after defining your class and function:
print(len(make_drums())) # => Prints "Drum ready" twice, then 2 on its own line.
drums = make_drums() # Prints "Drum ready" twice.
print(type(drums[0]) is Drum) # => True
print(type(drums[1]) is Drum) # => True
print(drums[0] is drums[1]) # => False
same_drums = drums
print(same_drums is drums) # => True
# Explain why same_drums = drums does not print another initialization message.
