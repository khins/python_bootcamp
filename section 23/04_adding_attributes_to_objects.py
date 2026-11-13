# Adding attributes to objects — Study Summary
# Instructor summary:
# - An attribute is data stored on an object: part of its state.
# - Use object.attribute = value to assign an attribute.
# - Use object.attribute to read its current value.
# - Attribute names follow variable naming rules; snake_case is conventional.
# - Ordinary instance attributes are publicly accessible through dot syntax.
# - Separate instances can hold different values for the same attribute name.
# - Adding an attribute to one instance does not add it to another instance.
# - Reading a missing attribute raises AttributeError for the basic class here.
# - Establish expected instance attributes in __init__ for consistent setup.
#
# Clarifications to the transcript:
# - The simple user-defined class here allows new attributes after creation.
#   Not every Python object allows this; for example, a plain list does not.
# - Assigning attributes later is legal and sometimes useful. The design concern
#   here is inconsistent setup, not a rule that later assignment is always bad.
# - Instances of the same class are not required to have identical attributes,
#   but reliably providing expected attributes makes them easier to use.
# - Consistent attributes can have different values on different instances.
# - An attribute does not create a standalone variable with the same name.
# - __init__ initializes an already-created instance; it does not create it.
# - Moving attribute setup into __init__ is the focus of the next lesson.


# --- 1. Create two guitar instances ---
class Guitar:
    def __init__(self):
        print("A guitar is being initialized.")


acoustic = Guitar()
electric = Guitar()
# Prints the initialization message twice: once for each new instance.
print(type(acoustic) is type(electric))  # => True
print(acoustic is electric)             # => False
# The initializer does not assign any custom attributes yet.


# --- 2. Add attributes using dot syntax ---
acoustic.wood = "mahogany"
acoustic.strings = 6
acoustic.year = 1990

electric.nickname = "Sound Viking 3000"
# These assignments happen after instantiation.
# wood, strings, and year belong to acoustic; nickname belongs to electric.
# An attribute can hold a string, integer, or another Python object.
# For a multiword attribute name, use snake_case, such as wood_type.


# --- 3. Read attributes from their instance ---
print(acoustic.wood)      # => mahogany
print(acoustic.strings)   # => 6
print(acoustic.year)      # => 1990
print(electric.nickname) # => Sound Viking 3000
# Assignment writes a value; an attribute expression reads a value.
# Keep this intentional error commented out:
# print(wood)  # NameError: no standalone variable named wood was defined.

wood = "maple"
print(wood)           # => maple
print(acoustic.wood)  # => mahogany
# The standalone variable and the instance attribute are separate bindings.


# --- 4. Missing attributes belong to neither the other instance nor the class ---
# Keep these intentional errors commented out:
# print(electric.year)      # AttributeError: electric has no year attribute.
# print(acoustic.nickname)  # AttributeError: acoustic has no nickname attribute.
# print(Guitar.wood)        # AttributeError: wood was assigned to acoustic only.
# Having the same class does not automatically copy instance attributes.

electric.year = 2005
print(acoustic.year)  # => 1990
print(electric.year)  # => 2005
# Both instances now have year, with independent values.


# --- 5. Change an attribute and observe aliases ---
acoustic.strings = 12
print(acoustic.strings)  # => 12
# Assigning an existing attribute replaces its value.

backup = acoustic
backup.year = 1992
print(backup is acoustic)  # => True
print(acoustic.year)       # => 1992
print(electric.year)       # => 2005
# backup is another reference to acoustic, not a separate guitar.
# Updating through backup changes the object acoustic also refers to.


# --- 6. Why consistent initialization matters ---
third_guitar = Guitar()
# Prints the initialization message once more.
# third_guitar has none of the custom attributes assigned above.
# print(third_guitar.year)  # AttributeError: keep commented out.
# Repeating manual setup for every instance makes it easy to forget a field.
# The next lesson moves expected attribute assignments into __init__, using
# self.attribute = value so each instance receives its own initial state.
# Different guitars can still have different years, woods, and nicknames.


# --- 7. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Keep intentional-error lines commented out.

# Exercise 1 — Assign and read attributes
# Predict both outputs. Identify the instance and its two attribute names.
class Album:
    pass

album = Album() # the instance
album.title = "Moving Pictures" # attribute names
album.year = 1981 # attribute names
print(album.title)
print(album.year)
# ANSWER:
# Moving Pictures
# 1981
# Python allows you to dynamically add attributes to instances of ordinary classes

class Album:
    pass

first = Album()
second = Album()

first.title = "Moving Pictures"
second.title = "Fragile"

first.year = 1981
second.year = 1971

print(first.title)
print(second.year)
print(first is second)


# Exercise 2 — Same attribute name, different instances
# Predict all three outputs. Explain why changing first does not change second.
class Guitar:
    pass

first = Guitar()
second = Guitar()
first.strings = 6
second.strings = 12
first.strings = 7
print(first.strings)
print(second.strings)
print(first is second)
# ANSWER:
# 7
# 12
# False
# first does not change second because they are different instances of Guitar
# Key OOP concept: Two objects can belong to the same class and have attributes with identical names while storing different values.



# Exercise 3 — Attribute or standalone variable?
# Predict both outputs. Explain why assigning nickname does not change
# player.nickname, even though they use the same name.
class Player:
    pass

player = Player()
player.nickname = "Roadrunner"
nickname = "Viking"
print(nickname)
print(player.nickname)
# ANSWER:
# Viking
# Roadrunner
# assigning nickname does not change player.nickname because nickname is not part of the Player instances because of the dot notation

# Attribute reassignment
class Player:
    pass

player = Player()
player.nickname = "Roadrunner"

nickname = player.nickname
nickname = "Viking"

print(nickname)
print(player.nickname)
# Viking
# Roadrunner

# Exercise 4 — Diagnose a missing attribute
# Explain why the final line would raise AttributeError.
# Write an assignment that would let second.year be read successfully.
# Does assigning first.year also create an attribute on the class itself?
class Guitar:
    pass

first = Guitar()
second = Guitar()
first.year = 1990
print(first.year)
# print(second.year)  # Intentional error: keep this line commented out.
# ANSWER:
# second.year has not been created yet hence you cannot print a value that does not exist

# The key concept here is instance attribute shadowing:
class Guitar:
    year = 1990

first = Guitar()
second = Guitar()

first.year = 2005

print(first.year)
print(second.year)
print(Guitar.year)
# 2005
# 1990
# 1990

print("-" * 65)
# Changing a class attribute:
class Guitar:
    year = 1990

first = Guitar()
second = Guitar()

first.year = 2005
Guitar.year = 2020

print(first.year)
print(second.year)
print(Guitar.year)
# 2005
# 2020
# 2020

class Guitar:
    strings = 6

first = Guitar()
second = Guitar()

second.strings = 10
Guitar.strings = 7

print(first.strings)
print(second.strings)
print(Guitar.strings)

# Removing an instance attribute:
class Guitar:
    strings = 6

first = Guitar()
second = Guitar()

first.strings = 12

del first.strings

print(first.strings)
print(second.strings)
print(Guitar.strings)

# Exercise 5 — Two names for one instance
# Predict all three outputs. How many Song instances are created?
# Explain why the title read through song changes.
class Song:
    pass

song = Song()
song.title = "YYZ"
favorite = song
favorite.title = "Limelight"
print(song.title)
print(favorite.title)
print(song is favorite)
# ANSWER:
# Limelight
# Limelight
# True
# How many Song instances are created? One
# Explain why the title read through song changes: 
# It does not create a new Song instance. Instead, both variables reference the same object.
# The title read through song changes because favorite and song reference the same Song instance. Changing
#  the title through either variable modifies the same object's attribute.

# Reassignment versus modification
class Song:
    pass

song = Song()
song.title = "YYZ"

favorite = song
favorite = Song()
favorite.title = "Limelight"

print(song.title)
print(favorite.title)
print(song is favorite)
# YYZ
# Limelight
# False

class Song:
    pass

first = Song()
first.title = "YYZ"

second = first
second.title = "Limelight"

third = Song()
third.title = "Tom Sawyer"

print(first.title)
print(second.title)
print(third.title)
print(first is second)

# Exercise 6 — Describe your own objects
# 1. Define an empty class named MusicPlayer using pass.
# 2. Create two separate instances.
# 3. Give BOTH instances brand and volume attributes using dot assignments.
# 4. Use different brands and integer volume values for the two instances.
# 5. Change the first instance's volume, then print both volumes.
# 6. Explain why the second volume stays unchanged and why setting expected
#    attributes in __init__ would be more reliable than repeated manual setup.
# Keep the assignments outside the class for this lesson.
# Write your code below:

# ANSWER:
class MusicPlayer:
    pass

my_music_player = MusicPlayer()
my_music_player.brand = "Sony"
my_music_player.volume = 10

second = MusicPlayer() # creating two separate instances
second.volume = 8
second.brand = "Yamaha"

print(f'Volume 1: {my_music_player.volume}')
print(f'Volume 2: {second.volume}')
print(my_music_player.brand)
# Volume 1: 10
# Volume 2: 8
# Sony

first = MusicPlayer()
second = MusicPlayer()
third = first

first.volume = 10
second.volume = 20
third.volume = 5

print(first.volume)
print(second.volume)
print(third.volume)

# — Initializing attributes with __init__()
class MusicPlayer:
    def __init__(self, brand, volume):
        self.brand = brand
        self.volume = volume


first = MusicPlayer("Sony", 10)
second = MusicPlayer("Yamaha", 20)

first.volume = 15

print(first.brand)
print(first.volume)
print(second.volume)
# Sony
# 15
# 20
# The statement self.volume = volume takes the value received through the volume parameter and stores it as an instance attribute.

# Optional challenge — Build an object in a function
# Work through this one together when you are ready.
# Define an empty class named Guitar using pass.
# Define a regular function make_guitar(wood, strings, year).
# Inside the function, create a NEW Guitar instance, assign its wood, strings,
# and year attributes from the parameters, and return that instance.
# Keep the class empty; the next lesson will move setup into __init__.
# Each function call must return a separate guitar.
# Write your code below:
class Guitar:
    pass

def make_guitar(wood, strings, year) -> Guitar:
    new_guitar = Guitar()
    new_guitar.wood = wood
    new_guitar.strings = strings
    new_guitar.year = year

    return new_guitar


# Uncomment these checks after defining your class and function:
first = make_guitar("mahogany", 6, 1990)
second = make_guitar("maple", 12, 2005)
print(type(first) is Guitar)  # => True
print(first.wood)            # => mahogany
print(first.strings)         # => 6
print(first.year)            # => 1990
print(second.wood)           # => maple
print(first is second)       # => False
first.year = 1992
print(second.year)           # => 2005
# Explain why returning the instance is different from printing it.
# Would calling Guitar() directly guarantee these three attributes exist
# with your empty class? Explain how this motivates using __init__ next.

print("-" * 65)
# — Move initialization into the class
class Guitar:
    def __init__(self, wood, strings, year): # constructor parameters.
        # Assign the three instance attributes here
        self.wood = wood
        self.strings = strings # instance attributes.
        self.year = year


first = Guitar("mahogany", 6, 1990)
second = Guitar("maple", 12, 2005)

print(first.wood)
print(second.strings)
print(first is second)
# mahogany
# 12
# False

# — Default constructor parameters
class Guitar:
    def __init__(self, wood, year, strings=6):
        self.wood = wood
        self.year = year
        self.strings = strings


first = Guitar("mahogany", 1990)
second = Guitar("maple", 2005, 12)

print(first.strings)
print(second.strings)
print(first.year)
# 6
# 12
# 1990