# ============================================================
# FILE: name-mangling-for-privacy.py
# TOPIC: Name Mangling and Avoiding Subclass Name Collisions
# ============================================================

# LESSON OBJECTIVES
# 1. Distinguish public, single-underscore, and double-underscore names.
# 2. Observe how Python mangles names defined inside classes.
# 3. Access mangled attributes and methods for demonstration.
# 4. Explain why mangling reduces accidental subclass overrides.
# 5. Complete prediction and coding exercises independently.

# ============================================================
# SECTION 1 — THE BIG IDEA
# ============================================================
# Python does not enforce truly private instance attributes.
# A single leading underscore (_value) signals internal use by convention.
# Two leading underscores (__value) trigger name mangling when the name
# does not also end with two or more underscores.
#
# Within class Nonsense, __some_attribute becomes
# _Nonsense__some_attribute. This reduces accidental name collisions
# between a superclass and a subclass; it is NOT a security boundary.
#
# Contrast: __init__ is a special (dunder) name and is NOT mangled.

# ============================================================
# SECTION 2 — DEFINE THE SUPERCLASS AND SUBCLASS
# ============================================================
class Nonsense:
    def __init__(self):
        self.__some_attribute = "Hello"

    def __some_method(self):
        print("This is coming from some method")


class SpecialNonsense(Nonsense):
    pass


# EXAMPLE — Create one object of each class.
# Uncomment the lines to explore.
# n = Nonsense()
# sn = SpecialNonsense()

# ============================================================
# SECTION 3 — PREDICT ATTRIBUTE LOOKUP
# ============================================================
# EXERCISE 1: In a fresh run, uncomment one line at a time.
# Predict whether each expression prints a value or raises AttributeError.
#
# n = Nonsense()
# sn = SpecialNonsense()
# print(n.__some_attribute)
# print(n.some_attribute)
# print(sn.__some_attribute)
# print(sn.some_attribute)
#
# ANSWERS:
# 1. ____________________________________________
# 2. ____________________________________________
# 3. ____________________________________________
# 4. ____________________________________________
#
# Why can't ordinary dot lookup find these spellings?
# __________________________________________________

# ============================================================
# SECTION 4 — ACCESS THE MANGLED ATTRIBUTE
# ============================================================
# Python rewrites names beginning with __ inside a class definition.
# For this example, the resulting name is _Nonsense__some_attribute.
#
# EXERCISE 2: Predict the outputs before uncommenting.
# n = Nonsense()
# sn = SpecialNonsense()
# print(n._Nonsense__some_attribute)
# print(sn._Nonsense__some_attribute)
#
# ANSWER:
# 1. ____________________________________________
# 2. ____________________________________________
#
# Does the subclass object still have access to the inherited attribute?
# __________________________________________________

# ============================================================
# SECTION 5 — ACCESS THE MANGLED METHOD
# ============================================================
# EXERCISE 3: Predict what these calls do.
# n = Nonsense()
# sn = SpecialNonsense()
# n._Nonsense__some_method()
# sn._Nonsense__some_method()
#
# ANSWER:
# 1. ____________________________________________
# 2. ____________________________________________
#
# Why do we use parentheses for this method but not for the attribute?
# __________________________________________________

# ============================================================
# SECTION 6 — ACCIDENTAL OVERRIDES AND NAME COLLISIONS
# ============================================================
# The main reason for name mangling is to protect implementation details
# against ACCIDENTAL naming collisions in subclasses.
#
# A subclass's own __some_method is mangled using the SUBCLASS name,
# so it does not automatically replace Nonsense's __some_method.

class SpecialNonsenseWithMethod(Nonsense):
    def __some_method(self):
        print("This is coming from the subclass")

    def run_subclass_method(self):
        self.__some_method()


# EXERCISE 4 — Predict each line's output.
# obj = SpecialNonsenseWithMethod()
# obj.run_subclass_method()
# obj._Nonsense__some_method()
# obj._SpecialNonsenseWithMethod__some_method()
#
# ANSWER:
# 1. ____________________________________________
# 2. ____________________________________________
# 3. ____________________________________________
#
# Why do the parent and child methods coexist?
# __________________________________________________

# ============================================================
# SECTION 7 — INSPECT AN OBJECT'S NAMES
# ============================================================
# vars(obj) returns its instance attribute dictionary when available.
# dir(obj) lists accessible attribute names, including mangled ones.
#
# EXERCISE 5:
# n = Nonsense()
# print(vars(n))
# print([name for name in dir(n) if "some" in name])
#
# Which names reveal the class prefix added by name mangling?
# ANSWER: __________________________________________

# ============================================================
# SECTION 8 — CODING CHALLENGE 1: PRIVATE-STYLE ATTRIBUTE
# ============================================================
# Define a class called LibraryAccount.
# 1. __init__ accepts owner and balance.
# 2. Save owner as a public attribute.
# 3. Save balance as a double-underscore attribute.
# 4. Add get_balance() that returns the balance.
# 5. Instantiate an account and test its public method.

class LibraryAccount:
    # Write your code below.
    pass


# ============================================================
# SECTION 9 — CODING CHALLENGE 2: SUBCLASS COLLISION
# ============================================================
# Define a parent class called BaseProcessor with a name-mangled
# __setup() method that prints "Base setup".
# Add a public start() method that invokes self.__setup().
#
# Define a child class called CustomProcessor that also defines
# its own __setup() printing "Custom setup".
#
# Instantiate CustomProcessor and call start().
# Predict which implementation is invoked and explain why.

class BaseProcessor:
    # Write your code below.
    pass


class CustomProcessor(BaseProcessor):
    # Write your code below.
    pass


# PREDICTION: _______________________________________
# EXPLANATION: ______________________________________

# ============================================================
# SECTION 10 — CODING CHALLENGE 3: COMPARE UNDERSCORES
# ============================================================
# Write a class called ExampleNames with three instance attributes:
# public_value, _internal_value, and __mangled_value.
#
# Create an instance and try accessing each value from outside.
# Which one requires a class-prefixed mangled spelling?

class ExampleNames:
    # Write your code below.
    pass


# ============================================================
# SECTION 11 — FINAL REVIEW
# ============================================================
# Fill in the blanks without looking back.
#
# 1. A single leading underscore is a naming __________.
# 2. A double leading underscore can trigger name __________.
# 3. __some_attribute defined in class Nonsense becomes __________.
# 4. Name mangling helps avoid accidental __________ in subclasses.
# 5. Name mangling does NOT provide true __________.
# 6. A method called __init__ is / is not name-mangled: __________.
# 7. A subclass's __setup method uses the __________ class name.
# 8. The built-in __________ function can reveal instance attributes.
#
# KEY TAKEAWAY:
# Mangling changes how Python stores and looks up certain names;
# it doesn't prevent deliberate access to them.
# ============================================================
# END OF LESSON
# ============================================================
