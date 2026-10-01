# Class methods — Study Summary
# Instructor summary:
# - Define a class method by placing @classmethod above a method definition.
# - Use cls as its first parameter to represent the class receiving the call.
# - Python supplies the class automatically when the method is called normally.
# - Call a class method using ClassName.method_name(arguments).
# - Callers supply arguments for parameters that come after cls.
# - Class methods can create instances with predefined settings.
# - Return cls(...) to construct an instance of the receiving class.
# - Named factory methods make common configurations easy to request.
# - Direct construction remains available for custom configurations.
#
# Clarifications to the transcript:
# - cls is a naming convention, not a keyword. Naming a parameter cls alone
#   does not make a method a class method; @classmethod changes its binding.
# - Class methods can also be accessed through instances. They still receive
#   the class, not the individual instance, as their first argument.
# - Ordinary instance methods are also defined on the class; the key distinction
#   is whether normal method binding supplies an instance or a class.
# - A decorator returns a replacement object, not necessarily a function.
#   classmethod wraps a function to provide class-based method binding.
# - Factory methods are a common use of class methods, not their only purpose.
# - cls(...) supports inherited factories: a subclass receives itself as cls.
#   Its initializer must still accept the arguments passed by the factory.
# - Returning SushiPlatter(...) directly would always construct that base class.
# - A class method does not automatically create or return an instance. The
#   return cls(...) statement is what gives these factories that behavior.
# - These examples assume sensible piece counts and perform no validation.


# --- 1. Define custom construction and named factories ---
class SushiPlatter:
    def __init__(self, salmon, tuna, shrimp, squid):
        self.salmon = salmon
        self.tuna = tuna
        self.shrimp = shrimp
        self.squid = squid

    @classmethod
    def lunch_special_a(cls):
        return cls(salmon=2, tuna=2, shrimp=2, squid=0)

    @classmethod
    def tuna_lover(cls):
        return cls(salmon=0, tuna=10, shrimp=0, squid=1)

    @classmethod
    def salmon_special(cls, pieces):
        return cls(salmon=pieces, tuna=0, shrimp=0, squid=0)

    def total_pieces(self):
        return self.salmon + self.tuna + self.shrimp + self.squid


boris = SushiPlatter(8, 4, 5, 10)
print(boris.salmon)          # => 8
print(boris.total_pieces())  # => 27
# The initializer stores the counts on each new instance.
# total_pieces is an instance method: self refers to the particular platter.
# The factories are class methods: cls refers to the class used to call them.


# --- 2. Request a predefined lunch special ---
lunch_eater = SushiPlatter.lunch_special_a()
print(lunch_eater.salmon)          # => 2
print(lunch_eater.tuna)            # => 2
print(lunch_eater.shrimp)          # => 2
print(lunch_eater.squid)           # => 0
print(lunch_eater.total_pieces())  # => 6
# Python supplies SushiPlatter as cls; the caller supplies no arguments here.
# cls(...) creates a new platter and runs its initializer with the preset counts.
# return sends that instance back to the caller for assignment to lunch_eater.


# --- 3. Offer another named configuration ---
tuna_fan = SushiPlatter.tuna_lover()
print(tuna_fan.salmon)        # => 0
print(tuna_fan.tuna)          # => 10
print(tuna_fan.squid)         # => 1
print(tuna_fan.total_pieces())  # => 11
# The method name explains which combination the customer wants.
# The returned object supports the same instance methods as a custom platter.


# --- 4. Accept caller-supplied arguments after cls ---
salmon_fan = SushiPlatter.salmon_special(6)
print(salmon_fan.salmon)          # => 6
print(salmon_fan.total_pieces())  # => 6

larger_order = SushiPlatter.salmon_special(pieces=12)
print(larger_order.salmon)  # => 12
# Only pieces comes from the caller. Python still supplies cls automatically.
# Both positional and keyword arguments work for this ordinary parameter.
# Keep these intentional errors commented out:
# SushiPlatter.salmon_special()  # TypeError: required pieces argument missing.
# SushiPlatter.lunch_special_a(SushiPlatter)  # TypeError: extra argument.
# Do not manually pass the class when calling these bound class methods.


# --- 5. Each factory call creates a separate instance ---
first = SushiPlatter.lunch_special_a()
second = SushiPlatter.lunch_special_a()
print(first is second)  # => False

first.salmon = 20
print(first.salmon)   # => 20
print(second.salmon)  # => 2
# Each call executes cls(...) again, so it creates a new object.
# Changing one platter's numeric attribute does not change the other platter.
# The class method does not cache or reuse an earlier order in this example.


# --- 6. Calling through an instance still supplies the class ---
custom = SushiPlatter(1, 2, 3, 4)
another_order = custom.tuna_lover()
print(another_order.tuna)  # => 10
print(custom.tuna)         # => 2
print(another_order is custom)  # => False
# This is allowed, but SushiPlatter.tuna_lover() makes the factory's role clearer.
# custom is not passed as self. Its class is passed as cls instead.
# The factory creates a new platter rather than changing the existing one.


# --- 7. Preview: cls preserves the receiving subclass ---
class PartyPlatter(SushiPlatter):
    pass


party_order = PartyPlatter.lunch_special_a()
print(type(party_order) is PartyPlatter)  # => True
print(party_order.total_pieces())         # => 6
# PartyPlatter inherits the initializer and methods from SushiPlatter.
# During this factory call, cls is PartyPlatter, so cls(...) creates that type.
# Hard-coding return SushiPlatter(...) would create a SushiPlatter instead.
# This is a brief inheritance preview; no new subclass behavior is needed here.


# --- 8. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Exercises using SushiPlatter refer to the class defined in section 1 above.
# Keep intentional-error lines commented out.

# Exercise 1 — Trace a preset
# Predict all three outputs. What does cls refer to inside tuna_lover?
# order = SushiPlatter.tuna_lover()
# print(order.salmon)
# print(order.tuna)
# print(order.total_pieces())
# ANSWER:


# Exercise 2 — Supply arguments after cls
# Predict both outputs. How many arguments does the caller supply?
# order = SushiPlatter.salmon_special(pieces=9)
# print(order.salmon)
# print(order.squid)
# Explain why the caller does not pass SushiPlatter explicitly.
# ANSWER:


# Exercise 3 — Independent orders
# Predict all three outputs and explain why the objects have different counts.
# first = SushiPlatter.lunch_special_a()
# second = SushiPlatter.lunch_special_a()
# first.tuna = 7
# print(first.tuna)
# print(second.tuna)
# print(first is second)
# ANSWER:


# Exercise 4 — Diagnose a missing decorator
# Consider this separate class. Explain why cls alone is not enough.
# class Snack:
#     def special(cls):
#         return cls()
#
# Snack.special()
# Why does this call raise TypeError? Add the decorator that makes it work.
# Keep the failing call commented out until the definition is fixed.
# ANSWER:


# Exercise 5 — A factory called through an instance
# Predict all three outputs. Is original passed into tuna_lover as an instance?
# original = SushiPlatter(3, 4, 5, 6)
# new_order = original.tuna_lover()
# print(original.tuna)
# print(new_order.tuna)
# print(original is new_order)
# ANSWER:


# Exercise 6 — Write your own named factory
# 1. Define Sandwich with __init__(self, bread, filling, toasted=False).
# 2. Store all three values as instance attributes.
# 3. Add a class method named cheese_special with cls as its first parameter.
# 4. Return a new instance using cls("wheat", "cheese", True).
# 5. Create one custom sandwich directly and one through cheese_special().
# 6. Print their attributes and explain what the factory returns.
# 7. Call cheese_special() twice and verify that it returns separate objects.
# Write your code below:

# ANSWER:


# Optional challenge — Scale a preset with an argument
# Work through this one together when you are ready.
# Add a class method named group_special(cls, people) to SushiPlatter.
# Return a new platter with 2 salmon, 2 tuna, and 2 shrimp per person, and 0 squid.
# Assume people is a positive integer; no validation is required.
# Construct the result using cls rather than the literal class name.
# Write your method inside SushiPlatter above.


# Uncomment these checks after adding your method:
# group = SushiPlatter.group_special(3)
# print(group.salmon)          # => 6
# print(group.tuna)            # => 6
# print(group.shrimp)          # => 6
# print(group.squid)           # => 0
# print(group.total_pieces())  # => 18
# party = PartyPlatter.group_special(2)
# print(type(party) is PartyPlatter)  # => True
# print(party.total_pieces())         # => 12
# Explain how the inherited factory knows which type of platter to construct.
