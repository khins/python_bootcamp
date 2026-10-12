# ============================================================
# FILE: 10_multiple-inheritance-II.py
# TOPIC: Multiple Inheritance and Method Resolution Order (MRO)
# ============================================================
# OBJECTIVES
# - Trace method lookup through multiple levels of inheritance.
# - Predict which implementation runs when ancestors share a method name.
# - Inspect the actual order with ClassName.mro() and ClassName.__mro__.
# - Distinguish depth-first and breadth-first search from Python's C3 MRO.
# - Practice reversing base classes and overriding inherited behavior.
#
# STUDY SUMMARY
# - A subclass can inherit from multiple classes with their own ancestors.
# - Python follows the class's MRO to find an inherited method.
# - For the ordinary methods here, the first matching definition wins.
# - Base-class order influences the MRO, together with ancestor relationships.
# - .mro() returns a list of class objects, not strings.
# - __mro__ exposes the order as a tuple of class objects.
#
# CLARIFICATIONS TO THE TRANSCRIPT
# - Python uses C3 linearization, not a general depth-first search algorithm.
# - This lesson's first example resembles depth-first lookup, but that
#   description does not work for every multiple-inheritance hierarchy.
# - C3 respects local base-class order and preserves the relative order
#   established by parent MROs. Each class appears once in the final MRO.
# - If those ordering requirements conflict, class creation raises TypeError.
# - Inspect the MRO instead of assuming Python searches an entire branch
#   before considering another parent.


# ============================================================
# SECTION 1 — DEFINE THE RESTAURANT HIERARCHY
# ============================================================
class Restaurant:
    def make_reservation(self, party_size):
        print(f"Booked a table for {party_size}")


class Steakhouse(Restaurant):
    pass


class Bar:
    def make_reservation(self, party_size):
        print(f"Booked a lounge for {party_size}")


class BarAndGrill(Steakhouse, Bar):
    pass


# Direct bases:
# Restaurant  -> object
# Steakhouse  -> Restaurant
# Bar         -> object
# BarAndGrill -> Steakhouse, Bar
#
# Both Restaurant and Bar define make_reservation().
# Steakhouse and BarAndGrill inherit behavior without overriding it.
# Which definition will a BarAndGrill instance use?


# ============================================================
# SECTION 2 — CALL THE INHERITED METHOD
# ============================================================
bag = BarAndGrill()
bag.make_reservation(2)  # => Booked a table for 2

# The lookup follows this MRO:
# BarAndGrill -> Steakhouse -> Restaurant -> Bar -> object
#
# 1. BarAndGrill does not define make_reservation.
# 2. Steakhouse does not define make_reservation.
# 3. Restaurant defines it, so Python selects that implementation.
#
# Python does not also call Bar.make_reservation automatically.
# self inside Restaurant.make_reservation refers to bag, which is still
# a BarAndGrill instance.


# ============================================================
# SECTION 3 — INSPECT THE MRO
# ============================================================
print([cls.__name__ for cls in BarAndGrill.mro()])
# => ['BarAndGrill', 'Steakhouse', 'Restaurant', 'Bar', 'object']

print(BarAndGrill.__mro__ == tuple(BarAndGrill.mro()))  # => True
# .mro() returns class objects. The comprehension extracts their names
# to keep the output readable and independent of the module's name.
# Uncomment to see the class objects themselves:
# print(BarAndGrill.mro())
# print(BarAndGrill.__mro__)


# ============================================================
# SECTION 4 — DEPTH-FIRST VERSUS BREADTH-FIRST SEARCH
# ============================================================
# These are general tree/graph search concepts, illustrated by this tree:
#
# A
# |-- B
# |   |-- E
# |   |-- F
# |   `-- G
# |-- C
# |   |-- H
# |   `-- I
# `-- D
#     `-- J
#
# Assuming children are visited from left to right:
#
# Depth-first traversal (preorder):
# A, B, E, F, G, C, H, I, D, J
#
# Explore a branch deeply before returning to another branch.
#
# Breadth-first traversal:
# A, B, C, D, E, F, G, H, I, J
#
# Explore all nodes at one depth before moving to the next depth.
#
# These concepts help describe search strategies, but neither traversal
# is a complete description of Python's C3 method resolution order.
# Inheritance can form a graph with shared ancestors, not just a tree.


# ============================================================
# SECTION 5 — REVERSE THE DIRECT BASE CLASSES
# ============================================================
class BarFirstGrill(Bar, Steakhouse):
    pass


bar_first = BarFirstGrill()
bar_first.make_reservation(4)  # => Booked a lounge for 4

print([cls.__name__ for cls in BarFirstGrill.mro()])
# => ['BarFirstGrill', 'Bar', 'Steakhouse', 'Restaurant', 'object']
# Bar now appears before Restaurant and supplies the matching method.
# The original BarAndGrill class is unchanged.


# ============================================================
# SECTION 6 — AN OVERRIDE IN THE SUBCLASS TAKES PRIORITY
# ============================================================
class PrivateGrill(Steakhouse, Bar):
    def make_reservation(self, party_size):
        print(f"Booked a private room for {party_size}")


private_grill = PrivateGrill()
private_grill.make_reservation(6)  # => Booked a private room for 6
# PrivateGrill is first in its own MRO, so its definition is selected.


# ============================================================
# SECTION 7 — A SHARED ANCESTOR SHOWS WHY C3 MATTERS
# ============================================================
class Venue:
    def describe(self):
        return "General venue"


class DiningVenue(Venue):
    pass


class MusicVenue(Venue):
    def describe(self):
        return "Music venue"


class DinnerClub(DiningVenue, MusicVenue):
    pass


# Both direct parents inherit from Venue, forming a diamond:
#
#          Venue
#         /     \
# DiningVenue  MusicVenue
#         \     /
#        DinnerClub
#
# C3 keeps Venue after both of its subclasses in this hierarchy.
print([cls.__name__ for cls in DinnerClub.mro()])
# => ['DinnerClub', 'DiningVenue', 'MusicVenue', 'Venue', 'object']

club = DinnerClub()
print(club.describe())  # => Music venue
# A naive search all the way up DiningVenue's branch would find Venue
# too early. The actual MRO checks MusicVenue before the shared Venue.
# Venue appears only once in the MRO.


# ============================================================
# SECTION 8 — PRACTICE: PREDICT, EXPLAIN, THEN RUN
# ============================================================
# Write predictions in ANSWER comments before uncommenting the examples.

# EXERCISE 1 — IDENTIFY THE IMPLEMENTATION
# Predict each message and name the class that defines the chosen method.
# Restaurant().make_reservation(3)
# Steakhouse().make_reservation(3)
# Bar().make_reservation(3)
# BarAndGrill().make_reservation(3)
# ANSWER:


# EXERCISE 2 — TRACE THE LOOKUP
# Write the complete MRO for BarAndGrill.
# Where does lookup stop when finding make_reservation?
# What object does self refer to when bag.make_reservation(2) runs?
# ANSWER:


# EXERCISE 3 — CHANGE THE BASE ORDER
# Why do these objects select different implementations?
# BarAndGrill().make_reservation(5)
# BarFirstGrill().make_reservation(5)
# ANSWER:


# EXERCISE 4 — DISTINGUISH SEARCH STRATEGIES
# Using the tree in Section 4, list the nodes visited before H is reached:
# Depth-first:
# Breadth-first:
# Why should neither strategy be used as a universal rule for Python MRO?
# ANSWER:


# EXERCISE 5 — TRACE THE DIAMOND
# Predict club.describe() and explain why Venue.describe is not selected.
# How many times does Venue appear in DinnerClub.mro()?
# ANSWER:


# EXERCISE 6 — WRITE AN OVERRIDE
# Create a ReservedSteakhouse subclass of Steakhouse.
# Override make_reservation to print "Booked a booth for {party_size}".
# Create a BoothGrill class inheriting from ReservedSteakhouse and Bar.
# Instantiate BoothGrill, call make_reservation, and print its MRO names.
# Write your code below:


# OPTIONAL CHALLENGE — REVERSE A DIAMOND'S BASES
# Create MusicFirstClub(MusicVenue, DiningVenue).
# Predict its complete MRO, then inspect it using .mro().
# Does reversing these parents change the result of describe()? Why?
# ANSWER:


# ============================================================
# SECTION 9 — FINAL REVIEW
# ============================================================
# 1. MRO stands for __________________________________________.
# 2. Python's MRO algorithm is called ________________________.
# 3. .mro() returns a list of strings or class objects?
# 4. __mro__ stores the order as a ____________________________.
# 5. Why does Restaurant appear before Bar in BarAndGrill's MRO?
# 6. Does finding a method automatically call every parent's version?
# 7. Which search strategy explores one level at a time?
# 8. In DinnerClub's MRO, why is Venue after MusicVenue?
# ANSWER:
