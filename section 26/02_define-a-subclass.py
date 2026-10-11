# ============================================================
# FILE: define-a-subclass.py
# TOPIC: Defining Your First Subclass
# ============================================================
# LESSON OBJECTIVES
# 1. Define a superclass and subclass.
# 2. Inherit an __init__ method and an instance method.
# 3. Understand class references versus class instances.
# 4. Trace where Python finds inherited attributes and methods.
# 5. Practice a multi-level inheritance hierarchy.
#
# Run this file in VS Code. Uncomment each test only after predicting
# its output. Complete the TODO exercises yourself.


# ============================================================
# SECTION 1 — THE SUPERCLASS: Store
# ============================================================
# A superclass (also called parent or base class) provides behavior
# that more specific classes can reuse.

class Store:
    def __init__(self):
        self.owner = "Boris"

    def exclaim(self):
        return "Lots of stuff to buy. Come inside."


# EXERCISE 1 — PREDICT BEFORE RUNNING
# shop = Store()
# print(shop.owner)
# print(shop.exclaim())
#
# ANSWER:
# 1. ______________________________________________
# 2. ______________________________________________


# ============================================================
# SECTION 2 — THE SUBCLASS: CoffeeShop
# ============================================================
# A coffee shop IS A type of store.
# Store is the superclass; CoffeeShop is the subclass.
# In class CoffeeShop(Store), Store is the CLASS itself,
# not a Store() instance.
# 'pass' means the subclass has no new body yet.

class CoffeeShop(Store):
    pass


# EXERCISE 2 — INHERITED MEMBERS
# starbucks = CoffeeShop()
# print(starbucks.owner)
# print(starbucks.exclaim())
#
# PREDICT:
# 1. ______________________________________________
# 2. ______________________________________________
#
# QUESTION: CoffeeShop does not define __init__. Why does
# starbucks still have an owner attribute?
# ANSWER:
# ___________________________________________________
# ___________________________________________________


# ============================================================
# SECTION 3 — CLASS REFERENCE VS. INSTANCE
# ============================================================
# Compare:
# Store                 -> the class
# Store()               -> an instance of the class
# class CoffeeShop(Store):  -> inherit from the class Store
#
# QUESTION: Why would class CoffeeShop(Store()) be the wrong
# approach for the ordinary inheritance shown in this lesson?
# ANSWER:
# ___________________________________________________


# ============================================================
# SECTION 4 — ATTRIBUTE LOOKUP
# ============================================================
# For these examples, Python looks on the instance, then
# the class, then along the superclass hierarchy.
#
# starbucks.owner:
#   The inherited Store.__init__ assigned owner on the instance.
#
# starbucks.exclaim():
#   Not defined in CoffeeShop, so Python finds Store.exclaim.
#
# EXERCISE 3 — TRACE THE LOOKUP
# Write where each item comes from:
#
# starbucks.owner   -> ______________________________
# starbucks.exclaim -> ______________________________
#
# What does Python do when a method is absent from CoffeeShop?
# ANSWER:
# ___________________________________________________


# ============================================================
# SECTION 5 — ADDING SUBCLASS-ONLY FUNCTIONALITY
# ============================================================
# CHALLENGE 1:
# Create a subclass BookStore(Store).
# Give it a method named genre() returning "Fiction".
# Do NOT duplicate __init__ or exclaim.
#
# After implementing, test:
# books = BookStore()
# print(books.owner)
# print(books.exclaim())
# print(books.genre())
#
# Write your class below:

# class BookStore(Store):
#     # TODO: define genre(self)
#     pass


# ============================================================
# SECTION 6 — MULTI-LEVEL INHERITANCE
# ============================================================
# The lesson describes a chain: A -> B -> C.
# We can represent it with Store -> CoffeeShop -> SpecialtyCoffeeShop.
#
# CHALLENGE 2:
# Define SpecialtyCoffeeShop inheriting from CoffeeShop.
# Use 'pass' as its body.
# Instantiate it, then print owner and exclaim().
# Predict whether both inherited members still work.

# TODO: Write SpecialtyCoffeeShop here.

# PREDICTION:
# ___________________________________________________
# ___________________________________________________


# ============================================================
# SECTION 7 — TEST YOUR UNDERSTANDING
# ============================================================
# EXERCISE 4 — TRUE OR FALSE
#
# 1. A subclass can use methods from its superclass.  ______
# 2. Inheritance requires making a Store() object inside
#    the CoffeeShop class definition.                 ______
# 3. An inherited __init__ can initialize a subclass
#    instance.                                        ______
# 4. A subclass must copy every superclass method.   ______
# 5. Inheritance can extend across multiple levels.  ______
#
# EXERCISE 5 — FILL IN THE BLANKS
#
# 1. Store is the __________ class.
# 2. CoffeeShop is the __________ class.
# 3. The keyword for an empty class body is __________.
# 4. The method that initializes owner is __________.
# 5. The relationship 'CoffeeShop is a Store' is an
#    example of an __________ relationship.


# ============================================================
# SECTION 8 — BUILD YOUR OWN INHERITANCE PAIR
# ============================================================
# CHALLENGE 3:
# 1. Create a parent class Vehicle.
# 2. Define a method move(self) returning "Moving".
# 3. Create a child class Train(Vehicle) with 'pass'.
# 4. Instantiate Train and call move().
# 5. Explain why it works even though Train has no move().
#
# YOUR CODE:
#
#
# EXPLANATION:
# ___________________________________________________
# ___________________________________________________


# ============================================================
# SECTION 9 — KEY TAKEAWAYS
# ============================================================
# SUPERCLASS / PARENT / BASE CLASS:
# The general class whose behavior is reused.
#
# SUBCLASS / CHILD / DERIVED CLASS:
# A more specific class that inherits from a superclass.
#
# class CoffeeShop(Store):
# Means CoffeeShop inherits from Store.
#
# INHERITED __init__:
# When a CoffeeShop is created, Store.__init__ can run
# and initialize that CoffeeShop instance.
#
# LOOKUP:
# Python searches for a requested member along the
# instance/class/inheritance chain.
#
# BIG IDEA:
# Inheritance reduces duplicated code and models an
# 'is-a' relationship between related types.
# ============================================================
# END OF LESSON
# ============================================================
