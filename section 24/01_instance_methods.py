# Instance methods — Study Summary
# Instructor summary:
# - Instance methods describe behavior available on instances of a class.
# - Define them with def inside the class, at the same indentation as __init__.
# - Use self as the first parameter to refer to the instance receiving the call.
# - Call a method using object.method(arguments).
# - Python supplies self automatically when calling a method through an instance.
# - Additional parameters follow self; callers supply their required arguments.
# - Methods can read attributes, change attributes, print, and return values.
# - Access instance state through self.attribute inside a method.
# - Assign the result of a calculation to an attribute to update its value.
# - Separate instances can respond to the same method using different state.
#
# Clarifications to the transcript:
# - self is a naming convention, not a Python keyword.
# - Ordinary functions defined in a class become bound methods when accessed
#   through an instance. Static methods and class methods are different topics.
# - Methods are also accessed as attributes; parentheses call the method.
#   pokemon.roar refers to a bound method; pokemon.roar() executes it.
# - A method without an explicit return value returns None, even if it prints.
# - Method names such as roar and take_damage are chosen by the programmer;
#   special names such as __init__ have a meaning defined by Python.
# - A bare name such as health does not automatically refer to self.health.
# - These examples store independent numeric health values. Objects can share
#   references to mutable data, so independence is not universal for all state.
# - The simple damage method has no validation: negative damage increases health,
#   and damage greater than current health can make health negative.


# --- 1. Define methods alongside the initializer ---
class Pokemon:
    def __init__(self, name, specialty, health=100):
        self.name = name
        self.specialty = specialty
        self.health = health

    def roar(self):
        print("Roar!")

    def describe(self):
        print(f"I am {self.name}. I am a {self.specialty} Pokemon!")

    def take_damage(self, amount):
        self.health -= amount


# Each def is inside the class; each method body is indented one level further.
# Defining the methods does not execute their bodies.
# take_damage uses self.health = self.health - amount in a shorter form.


# --- 2. Call a method on different instances ---
squirtle = Pokemon("Squirtle", "water")
charmander = Pokemon(name="Charmander", specialty="fire", health=110)

squirtle.roar()    # => Roar!
charmander.roar()  # => Roar!
# roar has one parameter, self, but these calls need no explicit arguments.
# The instance before the dot is supplied as self automatically.
# This method does not need to read or change state to be a valid instance method.


# --- 3. Read instance state inside a method ---
squirtle.describe()    # => I am Squirtle. I am a water Pokemon!
charmander.describe()  # => I am Charmander. I am a fire Pokemon!
# Both calls use the same method definition, but self refers to a different
# instance on each call. self.name and self.specialty read that instance's data.
# A method can also call another method on its instance using self.roar().


# --- 4. Accept an argument and change state ---
print(squirtle.health)  # => 100
squirtle.take_damage(20)
print(squirtle.health)  # => 80
print(charmander.health)  # => 110

squirtle.take_damage(amount=5)
print(squirtle.health)  # => 75
# Both positional and keyword arguments work for amount.
# self.health - amount alone would calculate a value without updating health.
# Changing squirtle's health does not change charmander's health.


# --- 5. Distinguish printed output, return values, and method references ---
result = squirtle.roar()  # => Roar!
print(result)            # => None

result = squirtle.take_damage(10)
print(result)           # => None
print(squirtle.health)  # => 65
# take_damage changes health but does not print or explicitly return a value.
# Do not write squirtle = squirtle.take_damage(10): squirtle would become None.

saved_roar = squirtle.roar
# No roar is printed yet: there are no call parentheses on the line above.
saved_roar()  # => Roar!
# The saved bound method still knows which instance to supply as self.


# --- 6. Direct assignments, aliases, and common mistakes ---
squirtle.health = 60
print(squirtle.health)  # => 60
# Direct assignment is allowed. A method gives the operation a descriptive name
# and a place to put shared behavior when that operation becomes more involved.

partner = squirtle
partner.take_damage(5)
print(partner is squirtle)  # => True
print(squirtle.health)      # => 55
print(charmander.health)    # => 110
# An alias refers to the same instance, so changes through it affect that instance.
# Keep these intentional errors commented out:
# squirtle.take_damage()       # TypeError: required amount argument missing.
# squirtle.take_damage(10, 20) # TypeError: too many positional arguments.
# squirtle.roar(10)           # TypeError: roar needs no explicit argument.
# A definition such as def roar(): omits the parameter that receives the instance
# and would raise TypeError when called normally through an instance.


# --- 7. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Exercises using Pokemon refer to the class defined in section 1 above.
# Keep intentional-error lines commented out.

# Exercise 1 — Read each instance's state
# Predict both output lines. Explain what self refers to in each call.
# first = Pokemon("Bulbasaur", "grass")
# second = Pokemon("Pikachu", "electric", 90)
# first.describe()
# second.describe()
# ANSWER:


# Exercise 2 — Trace repeated method calls
# Predict all three outputs. Explain why the second Pokemon stays unchanged.
# first = Pokemon("Squirtle", "water")
# second = Pokemon("Charmander", "fire", 110)
# first.take_damage(15)
# first.take_damage(amount=10)
# print(first.health)
# print(second.health)
# print(first is second)
# ANSWER:


# Exercise 3 — Print versus return
# Predict the entire output in order, including the line printed inside roar.
# Explain why neither result contains a Pokemon or its health.
# pokemon = Pokemon("Eevee", "normal", 80)
# roar_result = pokemon.roar()
# damage_result = pokemon.take_damage(5)
# print(roar_result)
# print(damage_result)
# print(pokemon.health)
# ANSWER:


# Exercise 4 — Diagnose a calculation that does not update state
# Predict the final output. Rewrite the method body so it reduces health.
# Explain why simply calculating self.health - amount is not enough.
# class Fighter:
#     def __init__(self, health=100):
#         self.health = health
#
#     def take_damage(self, amount):
#         self.health - amount
#
# fighter = Fighter()
# fighter.take_damage(20)
# print(fighter.health)
# ANSWER:


# Exercise 5 — A saved method and an alias
# Predict all three outputs. Does assigning attack call the method?
# Explain which instance the saved bound method will change.
# first = Pokemon("Squirtle", "water")
# alias = first
# attack = first.take_damage
# attack(25)
# print(first.health)
# print(alias.health)
# print(alias is first)
# ANSWER:


# Exercise 6 — Write your own instance methods
# 1. Define MusicPlayer with __init__(self, brand, volume=5).
# 2. Store brand and volume as instance attributes.
# 3. Define describe(self) to print the player's brand and current volume.
# 4. Define increase_volume(self, amount) to add amount to self.volume.
# 5. Create two separate players and increase only the first player's volume.
# 6. Call describe() on both players and explain why their volumes are independent.
# 7. Store and print the result of an increase_volume() call. Explain its value.
# No volume limits or input validation are required for this exercise.
# Write your code below:

# ANSWER:


# Optional challenge — Change state and return the new value
# Work through this one together when you are ready.
# Define a class named BattlePokemon with __init__(self, name, health=100).
# Store name and health as instance attributes.
# Define take_damage(self, amount) to subtract amount from health, keep health
# from falling below zero, and RETURN the resulting health.
# Assume starting health and damage amounts are nonnegative integers.
# Use an if statement or max() to keep health at zero when damage is too large.
# Create two instances and verify that damaging one leaves the other unchanged.
# Write your code below:


# Uncomment these checks after defining your class:
# first = BattlePokemon("Squirtle")
# second = BattlePokemon("Charmander", 110)
# print(first.take_damage(20))  # => 80
# print(first.health)           # => 80
# print(first.take_damage(200)) # => 0
# print(first.health)           # => 0
# print(first.take_damage(5))   # => 0
# print(second.health)          # => 110
# Explain how this method differs from the lesson's take_damage(), which
# returns None. Why must you update self.health as well as return a value?
