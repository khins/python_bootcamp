# ============================================================
# FILE: multiple-inheritance-I.py
# TOPIC: Multiple Inheritance and Method Resolution Order (MRO)
# ============================================================
# OBJECTIVES
# - Inherit from more than one superclass.
# - Understand methods shared across parent classes.
# - Predict which method Python chooses when names collide.
# - Inspect the method resolution order using ClassName.mro().
# - Practice changing superclass order and overriding methods.

# ============================================================
# SECTION 1 — TWO INDEPENDENT SUPERCLASSES
# ============================================================
class FrozenFood:
    def thaw(self, minutes):
        print(f"Thawing for {minutes} minutes")

    def store(self):
        print("Putting in the freezer")


class Dessert:
    def add_weight(self):
        print("Putting on the pounds")

    def store(self):
        print("Putting in the refrigerator")


# ============================================================
# SECTION 2 — A SUBCLASS WITH TWO PARENTS
# ============================================================
class IceCream(FrozenFood, Dessert):
    pass


# Predict the output before uncommenting.
# icy = IceCream()
# icy.add_weight()
# icy.thaw(5)
# icy.store()

# EXERCISE 1 — PREDICT THE OUTPUT
# 1. __________________________________________
# 2. __________________________________________
# 3. __________________________________________
# Why does IceCream have access to both thaw() and add_weight()?
# ANSWER: _____________________________________


# ============================================================
# SECTION 3 — WHEN TWO PARENTS DEFINE THE SAME METHOD
# ============================================================
# Both FrozenFood and Dessert define store().
# Python checks IceCream first, then follows the MRO.
# In this simple hierarchy, FrozenFood is checked before Dessert.
#
# EXERCISE 2
# Predict which store() method runs for IceCream(FrozenFood, Dessert).
# ANSWER: _____________________________________
# Why? ________________________________________


# ============================================================
# SECTION 4 — INSPECTING THE METHOD RESOLUTION ORDER
# ============================================================
# .mro() is called on a CLASS, not an instance.
# It returns a list of CLASS OBJECTS (not strings).
#
# print(IceCream.mro())
#
# EXERCISE 3 — WRITE THE ORDER
# 1. __________________
# 2. __________________
# 3. __________________
# 4. __________________
#
# Note: object is the final class in this hierarchy.


# ============================================================
# SECTION 5 — REVERSE THE PARENT ORDER
# ============================================================
class ReversedIceCream(Dessert, FrozenFood):
    pass


# Predict before uncommenting:
# reversed_icy = ReversedIceCream()
# reversed_icy.store()
# print(ReversedIceCream.mro())
#
# EXERCISE 4
# Which store() implementation wins now?
# ANSWER: _____________________________________
# How did the MRO change?
# ANSWER: _____________________________________


# ============================================================
# SECTION 6 — OVERRIDING IN THE CHILD CLASS
# ============================================================
class CustomIceCream(FrozenFood, Dessert):
    def store(self):
        print("Putting ice cream in a special freezer")


# Predict before uncommenting:
# custom = CustomIceCream()
# custom.store()
#
# EXERCISE 5
# Why does CustomIceCream.store() run instead of a parent's store()?
# ANSWER: _____________________________________


# ============================================================
# SECTION 7 — CODING CHALLENGE 1: YOUR OWN TWO PARENTS
# ============================================================
# Create a class Musician with a play() method that prints
# "Playing music".
# Create a class Teacher with a teach() method that prints
# "Teaching students".
# Create MusicInstructor that inherits from BOTH.
# Instantiate it and call both inherited methods.

# WRITE YOUR CODE BELOW:



# ============================================================
# SECTION 8 — CODING CHALLENGE 2: METHOD COLLISION
# ============================================================
# Add a describe() method to Musician and Teacher.
# Give each a different printed message.
# Call describe() on MusicInstructor.
# Predict which message appears, then check its MRO.
# Change the parent order and run the test again.
#
# PREDICTION BEFORE REVERSING: __________________________
# PREDICTION AFTER REVERSING:  __________________________

# WRITE YOUR CODE BELOW:



# ============================================================
# SECTION 9 — CODING CHALLENGE 3: CHILD OVERRIDE
# ============================================================
# Override describe() inside MusicInstructor.
# Confirm the child implementation runs instead of either parent.
# Does this change the MRO list? Predict before testing.
# ANSWER: _____________________________________

# WRITE YOUR CODE BELOW:



# ============================================================
# SECTION 10 — FINAL KNOWLEDGE REVIEW
# ============================================================
# 1. Multiple inheritance means a class inherits from ________.
# 2. Parent classes are separated by ________ in class syntax.
# 3. MRO stands for Method __________ Order.
# 4. You can inspect it by calling ClassName.________().
# 5. In this example, Python checks the ________ class first.
# 6. When parent methods share a name, Python follows the ________.
# 7. A method defined directly on the child can ________ a parent method.
# 8. The final class shown by mro() here is ________.
# 9. Does mro() return strings or class objects? __________.
# 10. Why might many parent classes make code harder to maintain?
#     _________________________________________________

# ============================================================
# KEY CONCEPTS
# ============================================================
# - IceCream(FrozenFood, Dessert) inherits from both parents.
# - Shared method names are resolved using the MRO.
# - The simple example checks parents in their listed order.
# - More complex multiple-inheritance hierarchies use Python's
#   C3 method resolution order; not every hierarchy is a simple
#   left-to-right search.
# - A child can override an inherited method.
# - ClassName.mro() shows the lookup order without an instance.
# ============================================================
