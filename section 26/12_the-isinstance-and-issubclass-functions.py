# ============================================================
# FILE: 12_the-isinstance-and-issubclass-functions.py
# TOPIC: Checking Instances and Inheritance Relationships
# ============================================================
# OBJECTIVES
# - Use type() to identify an object's exact class.
# - Use isinstance() to check an object against a class or its ancestors.
# - Use issubclass() to check inheritance relationships between classes.
# - Check against multiple candidate classes with a tuple.
# - Distinguish class objects from instances and choose appropriate checks.
#
# STUDY SUMMARY
# - type(value) returns the class object representing value's exact type.
# - isinstance(value, ClassName) returns True for instances of that class
#   or its subclasses.
# - issubclass(Child, Parent) checks the relationship between classes.
# - Inheritance checks include indirect ancestors, not just direct parents.
# - A tuple of classes in the second argument checks for ANY match.
# - Built-in types and user-defined classes both support these functions.
#
# CLARIFICATIONS TO THE TRANSCRIPT
# - Pass actual class objects, such as int or dict, not strings like "int".
# - isinstance() accepts any object as its first argument, including a class.
#   Classes are objects too; that does not turn it into an inheritance check.
# - issubclass() requires a class as its first argument, not a normal instance.
# - issubclass(SomeClass, SomeClass) is True: a class counts as its own subclass
#   for this function.
# - issubclass() also accepts a tuple of candidate classes as its second argument.
# - Type checks can be appropriate for validation and other explicit contracts.
#   They are not automatically a design flaw.
# - When objects already share the behavior you need, polymorphism often
#   avoids unnecessary branches based on their concrete types.


# ============================================================
# SECTION 1 — REVIEW type()
# ============================================================
print(type({"a": 1}))  # => <class 'dict'>
print(type(1))         # => <class 'int'>
print(type([1, 2]))    # => <class 'list'>
print(type("hello"))   # => <class 'str'>

# These are class objects, not strings containing class names.
print(type({"a": 1}) is dict)  # => True
# Common class names: int, float, str, list, tuple, dict, set, bool.
# Use the lowercase built-in names exactly as written.


# ============================================================
# SECTION 2 — CHECK BUILT-IN INSTANCES
# ============================================================
print(isinstance(1, int))          # => True
print(isinstance({"a": 1}, dict))  # => True
print(isinstance([1, 2], list))    # => True
print(isinstance([1, 2], int))     # => False
print(isinstance("1", int))       # => False
# A string containing a digit is still a string.
# isinstance() checks the object; it does not convert it.

# Keep this intentional error commented out:
# isinstance(1, "int")  # TypeError: the second argument is not a type.


# ============================================================
# SECTION 3 — EVERYTHING HERE IS AN OBJECT
# ============================================================
print(isinstance(1, object))     # => True
print(isinstance(3.14, object))  # => True
print(isinstance(str, object))   # => True
print(isinstance(len, object))   # => True
print(isinstance(None, object))  # => True

# Numbers, classes, functions, and None are all objects.
# Checking against object is therefore too broad to distinguish these values.
# str without parentheses refers to the class; "hello" is a string instance.


# ============================================================
# SECTION 4 — CHECK AGAINST MULTIPLE CLASSES
# ============================================================
print(isinstance([], (list, dict)))       # => True
print(isinstance({}, (list, dict)))       # => True
print(isinstance(10, (list, dict)))       # => False
print(isinstance(10, (list, dict, int)))  # => True

# The tuple means OR: matching any candidate is enough.
# It does not mean the value must be an instance of every listed class.
# Use a tuple of classes, not a list of class names.


# ============================================================
# SECTION 5 — DEFINE A CUSTOM INHERITANCE HIERARCHY
# ============================================================
class Person:
    pass


class Superhero(Person):
    pass


arnold = Person()
boris = Superhero()

print(isinstance(boris, Superhero))  # => True
print(isinstance(boris, Person))     # => True
print(isinstance(boris, object))     # => True
print(isinstance(arnold, Person))    # => True
print(isinstance(arnold, Superhero)) # => False

# Every Superhero is a Person, but not every Person is a Superhero.
# isinstance() recognizes superclass relationships, not only exact types.


# ============================================================
# SECTION 6 — EXACT TYPE VERSUS INHERITANCE-AWARE CHECKS
# ============================================================
print(type(boris) is Superhero)  # => True
print(type(boris) is Person)     # => False
print(isinstance(boris, Person)) # => True

# type(boris) identifies the exact class: Superhero.
# isinstance(boris, Person) also accepts instances of Person's subclasses.
# Choose an exact-type check only when excluding subclasses is intentional.

# A built-in example that can be surprising:
print(type(True) is bool)        # => True
print(type(True) is int)         # => False
print(isinstance(True, int))     # => True
# bool is a subclass of int, so isinstance(True, int) returns True.


# ============================================================
# SECTION 7 — CHECK CLASS RELATIONSHIPS WITH issubclass()
# ============================================================
print(issubclass(Superhero, Person))     # => True
print(issubclass(Person, Superhero))     # => False
print(issubclass(Superhero, object))     # => True
print(issubclass(Person, object))        # => True
print(issubclass(Superhero, Superhero))  # => True
print(issubclass(bool, int))            # => True

# Read issubclass(A, B) as: "Is A a subclass of B, including B itself?"
# The direction matters. Reversing arguments can change the result.
# Unlike isinstance(), this function checks a CLASS as the first argument.

# Keep this intentional error commented out:
# issubclass(boris, Person)  # TypeError: boris is an instance, not a class.

print(issubclass(Superhero, (dict, Person)))  # => True
# As with isinstance(), a tuple in the second argument means ANY match.


# ============================================================
# SECTION 8 — INDIRECT INHERITANCE COUNTS TOO
# ============================================================
class FlyingSuperhero(Superhero):
    pass


flyer = FlyingSuperhero()

print(isinstance(flyer, FlyingSuperhero))   # => True
print(isinstance(flyer, Superhero))         # => True
print(isinstance(flyer, Person))            # => True
print(issubclass(FlyingSuperhero, Person))  # => True
# FlyingSuperhero -> Superhero -> Person -> object.
# Person does not need to be a direct base for either check to succeed.


# ============================================================
# SECTION 9 — CLASSES ARE OBJECTS, BUT CHECKS ASK DIFFERENT QUESTIONS
# ============================================================
print(isinstance(Superhero, Person))  # => False
print(issubclass(Superhero, Person))  # => True
print(isinstance(Superhero, type))    # => True

# Superhero is a class object, not a Person instance.
# In this ordinary class definition, its type is the built-in class type.
# To check whether a particular superhero object is a Person, use:
print(isinstance(boris, Person))      # => True

# Practical guidance:
# - Use isinstance(value, ClassName) for an object-level type check.
# - Use issubclass(ClassName, BaseClass) for a class relationship check.
# - If callers only need shared behavior, such as a speak() method, let
#   each object provide that behavior instead of adding a branch per class.


# ============================================================
# SECTION 10 — PRACTICE: PREDICT, EXPLAIN, THEN RUN
# ============================================================
# Write predictions in ANSWER comments before uncommenting the examples.
# Keep intentional-error examples commented out.

# EXERCISE 1 — BUILT-IN TYPES
# print(isinstance("42", str))
# print(isinstance("42", int))
# print(isinstance(42.0, int))
# print(isinstance(42.0, (int, float)))
# ANSWER:


# EXERCISE 2 — FOLLOW THE INHERITANCE DIRECTION
# print(isinstance(arnold, Superhero))
# print(isinstance(boris, Person))
# print(issubclass(Superhero, Person))
# print(issubclass(Person, Superhero))
# ANSWER:


# EXERCISE 3 — EXACT TYPE OR ANCESTOR?
# Predict both results and explain the difference.
# print(type(flyer) is Person)
# print(isinstance(flyer, Person))
# ANSWER:


# EXERCISE 4 — CHOOSE THE FUNCTION
# Write one expression for each question:
# 1. Is boris an instance of Superhero or one of its subclasses?
# 2. Is FlyingSuperhero a subclass of Person?
# 3. Is arnold's exact type Person?
# 4. Is a value named data either a list or a dictionary?
# ANSWER:


# EXERCISE 5 — FIND THE INVALID ARGUMENTS
# Which calls are valid? Predict results or identify the argument problem.
# isinstance(boris, Person)
# isinstance(boris, "Person")
# issubclass(boris, Person)
# issubclass(Superhero, (Person, dict))
# ANSWER:


# EXERCISE 6 — CREATE YOUR OWN HIERARCHY
# Define Animal, Dog(Animal), and GuideDog(Dog).
# Instantiate each class and use isinstance() to check their relationships.
# Use issubclass() to check direct, indirect, reversed, and same-class cases.
# Write your code below:


# OPTIONAL CHALLENGE — EXCLUDE BOOLEANS
# isinstance(True, int) is True because bool inherits from int.
# Write an expression that accepts int instances (including subclasses)
# but rejects bool instances. Test it with 5, True, and "5".
# ANSWER:


# ============================================================
# SECTION 11 — FINAL REVIEW
# ============================================================
# 1. type(value) returns value's exact __________.
# 2. isinstance() checks an __________ against a class or classes.
# 3. issubclass() checks a __________ against another class or classes.
# 4. Does isinstance() recognize indirect superclass relationships?
# 5. A tuple of candidate classes means ANY match or ALL matches?
# 6. What does issubclass(Person, Person) return?
# 7. Why should you pass dict rather than "dict" as a candidate type?
# 8. Are type checks always a design flaw? Explain an appropriate use.
# ANSWER:
