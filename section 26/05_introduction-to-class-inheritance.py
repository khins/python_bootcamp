# ============================================================
# FILE: introduction-to-class-inheritance.py
# TOPIC: Introduction to Python Class Inheritance
# ============================================================
# STUDY GUIDE + PRACTICE
# Complete the ANSWER blanks and TODO challenges before running.
# Uncomment individual exercises as you work through the file.

# ============================================================
# SECTION 1 — WHAT IS INHERITANCE?
# ============================================================
# Inheritance lets a class receive/reuse attributes and methods
# defined by another class.
#
# PARENT CLASS = superclass = base class
# CHILD CLASS  = subclass = derived class
#
# The parent describes a more general type.
# The child describes a more specific type.
#
# Think: "IS A" relationship.
#   A horse IS AN animal.
#   A train IS A vehicle.
#   A coffee shop IS A store.
#   An electric guitar IS A guitar.
#
# Why use inheritance?
# - Organize related classes.
# - Reduce duplicated code.
# - Allow subclasses to add specialized behavior.
#
# REVIEW 1:
# Which is the superclass in "A horse is an animal"?
# ANSWER: _______________________________________________
# Which is the subclass?
# ANSWER: _______________________________________________


# ============================================================
# SECTION 2 — BASIC SYNTAX: PARENT AND CHILD
# ============================================================
# The name in parentheses identifies the parent class.

class Animal:
    def breathe(self):
        return "Breathing"


class Horse(Animal):
    pass


# PREDICT BEFORE RUNNING:
# Does Horse need its own breathe() method?
# ANSWER: _______________________________________________
# What will this print?
# ANSWER: _______________________________________________

# horse = Horse()
# print(horse.breathe())


# ============================================================
# SECTION 3 — CHILD CLASSES ADD THEIR OWN METHODS
# ============================================================
class Guitar:
    def play(self):
        return "Playing guitar"

    def tune(self):
        return "Tuning guitar"


class ElectricGuitar(Guitar):
    def distortion(self):
        return "Distortion enabled"


# PREDICT THE THREE OUTPUTS:
# 1. _______________________________________________
# 2. _______________________________________________
# 3. _______________________________________________

# electric = ElectricGuitar()
# print(electric.play())
# print(electric.tune())
# print(electric.distortion())

# QUESTION:
# Which methods are inherited, and which is defined by the child?
# ANSWER: _______________________________________________


# ============================================================
# SECTION 4 — TRACE THE "IS A" RELATIONSHIP
# ============================================================
# Fill in PARENT or CHILD for each class:
#
# Store: __________       CoffeeShop: __________
# Vehicle: __________     Train: __________
# Guitar: __________      ElectricGuitar: __________
# Animal: __________      Horse: __________
#
# THINK:
# Every train is a vehicle, but is every vehicle a train?
# ANSWER: _______________________________________________


# ============================================================
# SECTION 5 — CODING CHALLENGE: VEHICLES
# ============================================================
# TODO:
# 1. Define a Vehicle class with a move(self) method.
# 2. Have move() return "Moving".
# 3. Define Train as a subclass of Vehicle.
# 4. Add a sound(self) method to Train that returns "Choo choo".
# 5. Uncomment the test calls.

# Write your classes here:


# train = Train()
# print(train.move())   # Expected: Moving
# print(train.sound())  # Expected: Choo choo

# QUESTION:
# Why can a Train instance call move()?
# ANSWER: _______________________________________________


# ============================================================
# SECTION 6 — CODING CHALLENGE: STORE AND COFFEE SHOP
# ============================================================
# TODO:
# 1. Define a Store class with an open(self) method.
#    Return "Store is open".
# 2. Define CoffeeShop as a subclass of Store.
# 3. Give CoffeeShop a serve_coffee(self) method.
#    Return "Serving coffee".
# 4. Create a CoffeeShop instance and test both methods.

# Write your code here:


# QUESTION:
# What behavior comes from Store, and what behavior is unique
# to CoffeeShop?
# ANSWER: _______________________________________________


# ============================================================
# SECTION 7 — PUBLIC, SINGLE UNDERSCORE, DOUBLE UNDERSCORE
# ============================================================
# The lesson introduces these naming patterns:
#
# name         Public attribute
# _name        Non-public/protected-by-convention attribute
# __name       Name-mangled attribute
#
# Python does not enforce Java/C#-style protected/private access.
# A single underscore is a convention, not an access restriction.
# Double underscores trigger name mangling; they do not make
# attributes absolutely inaccessible or remove them from inheritance.
#
# Special methods such as __str__ and __len__ can also be inherited.

class ExampleParent:
    public_name = "public"
    _internal_name = "internal"
    __mangled_name = "mangled"


class ExampleChild(ExampleParent):
    pass


# PREDICT:
# Which two lines below work as written?
# Which raises AttributeError?
# ANSWER: _______________________________________________

# example = ExampleChild()
# print(example.public_name)
# print(example._internal_name)
# print(example.__mangled_name)

# CHALLENGE:
# Research why the last line fails. What is "name mangling"?
# ANSWER: _______________________________________________


# ============================================================
# SECTION 8 — A CHILD CAN BE USED AS A PARENT TYPE
# ============================================================
# Python provides isinstance() to test type relationships.
# Predict the results before uncommenting.

# electric = ElectricGuitar()
# print(isinstance(electric, ElectricGuitar))
# print(isinstance(electric, Guitar))
# print(isinstance(Guitar(), ElectricGuitar))

# ANSWER 1: _____________________________________________
# ANSWER 2: _____________________________________________
# ANSWER 3: _____________________________________________
#
# Which results support the statement "An electric guitar is a guitar"?
# ANSWER: _______________________________________________


# ============================================================
# SECTION 9 — THINKING ABOUT DESIGN
# ============================================================
# Inheritance is one way to organize reusable behavior.
# It is not always the best design choice for every problem.
#
# QUESTION:
# Which relationship seems more appropriate for inheritance?
# A. A Horse is an Animal.
# B. A Horse has a Saddle.
#
# ANSWER: _______________________________________________
# Explain the difference between "IS A" and "HAS A".
# ANSWER: _______________________________________________


# ============================================================
# SECTION 10 — FINAL REVIEW
# ============================================================
# Fill in the blanks:
#
# 1. Inheritance helps reduce code ____________________.
# 2. A superclass is also called a __________ class.
# 3. A subclass is also called a __________ class.
# 4. The parent is generally the more __________ type.
# 5. The child is generally the more __________ type.
# 6. In class Horse(Animal), the parent is __________.
# 7. A child can reuse methods from its __________.
# 8. A child can also define its own __________.
# 9. A single leading underscore signals __________ use.
# 10. Double-leading-underscore attributes use name __________.
#
# FINAL CHALLENGE:
# Write a new parent/child example from a subject you enjoy.
# Include one inherited method and one child-only method.
#
# Your code:


# ============================================================
# KEY TAKEAWAY
# ============================================================
# A subclass represents a more specific kind of its superclass.
# It can reuse inherited behavior and add specialized behavior.
#
# NEXT LESSON: Defining and using subclasses in more detail.
# ============================================================
