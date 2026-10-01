# Default values in attributes — Study Summary
# Instructor summary:
# - Instance attributes can receive argument values or fixed initial values.
# - Assign a fixed value in __init__ when callers do not need to supply it.
# - A default parameter value lets callers omit a commonly used argument.
# - In def __init__(self, title, author, price=14.99), price is optional.
# - self.price = price stores the supplied price or its default on the instance.
# - An explicit argument overrides the default for that call.
# - Required title and author arguments still need to be supplied.
# - Keyword arguments identify parameters by name and can be reordered.
# - Python supplies self automatically during the normal class call.
#
# Clarifications to the transcript:
# - A fixed INITIAL value does not make an ordinary attribute read-only.
# - A parameter default does not create an attribute by itself; the assignment
#   self.price = price is what stores that value on the instance.
# - Omitting an argument uses its default. Explicit values such as 0 or None
#   are passed through; they do not automatically trigger the default.
# - In the signatures here, required parameters precede defaulted parameters.
# - In ordinary calls mixing both styles, positional arguments go before
#   keyword arguments. Do not supply the same parameter twice.
# - Keywords must match parameter names, not necessarily attribute names.
# - Defaults are evaluated when the function is defined, not on every call.
#   Avoid mutable defaults such as [] for independent per-instance collections.
# - These examples preserve the lesson's float prices to focus on initialization.
# - Passing every value explicitly is valid; defaults are useful when a common
#   fallback makes sense for the requirements.


# --- 1. Require every value from the caller ---
class ExplicitPriceBook:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


first = ExplicitPriceBook("Animal Farm", "George Orwell", 14.99)
second = ExplicitPriceBook("The Great Gatsby", "F. Scott Fitzgerald", 14.99)
print(first.author)  # => George Orwell
print(first.price)   # => 14.99
print(second.price)  # => 14.99
# This works, but the caller must repeat the price even when it is always 14.99.
# Separate class names keep all three approaches available for comparison.


# --- 2. Assign a fixed initial value inside __init__ ---
class FixedPriceBook:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.price = 14.99


fixed_first = FixedPriceBook("Animal Farm", "George Orwell")
fixed_second = FixedPriceBook("The Great Gatsby", "F. Scott Fitzgerald")
print(fixed_first.price)   # => 14.99
print(fixed_second.price)  # => 14.99
# There is no price parameter, so each book starts with the hard-coded price.
# Keep this intentional error commented out:
# invalid = FixedPriceBook("Animal Farm", "George Orwell", 19.99)  # TypeError

fixed_first.price = 9.99
print(fixed_first.price)   # => 9.99
print(fixed_second.price)  # => 14.99
# Fixed initialization does not prevent later reassignment of the attribute.


# --- 3. Use a default parameter for flexible initialization ---
class Book:
    def __init__(self, title, author, price=14.99):
        self.title = title
        self.author = author
        self.price = price


animal_farm = Book("Animal Farm", "George Orwell", 19.99)
gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald")
print(animal_farm.price)  # => 19.99
print(gatsby.price)       # => 14.99
# The caller provides two or three explicit arguments; Python supplies self.
# Omitting price uses 14.99. Supplying price uses that value for this instance.
# A custom price does not change the default used by later calls.


# --- 4. Use keyword arguments for clarity and flexible order ---
atlas = Book(title="Atlas Shrugged", author="Ayn Rand")
jude = Book(author="Thomas Hardy", price=24.99, title="Jude the Obscure")
print(atlas.title)   # => Atlas Shrugged
print(atlas.price)   # => 14.99
print(jude.author)   # => Thomas Hardy
print(jude.price)    # => 24.99

mixed = Book("Animal Farm", author="George Orwell", price=12.99)
print(mixed.price)  # => 12.99
# Positional arguments go first in this mixed call; keyword arguments follow.
# Keywords match the names in __init__: title, author, and price.


# --- 5. Omitted values, explicit values, and independent instances ---
free_book = Book("Sample", "Bookshop", price=0)
unspecified = Book("Catalog", "Bookshop", price=None)
print(free_book.price)    # => 0
print(unspecified.price)  # => None
# This class does not validate prices. Both explicit values are stored as given.
# None does not mean "use the default" unless we write code to give it that meaning.

gatsby.price = 10.99
another_gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald")
print(gatsby.price)          # => 10.99
print(another_gatsby.price)  # => 14.99
print(gatsby is another_gatsby)  # => False
# Changing an instance attribute does not change the initializer's default.


# --- 6. Diagnose argument mistakes ---
# Keep these intentional errors commented out:
# Book("Animal Farm")  # TypeError: required author argument missing.
# Book("Animal Farm", "George Orwell", cost=9.99)  # TypeError: unknown keyword.
# Book("Animal Farm", "George Orwell", 19.99, price=9.99)
# TypeError: price received both a positional value and a keyword value.
# Book(title="Animal Farm", "George Orwell")
# SyntaxError: positional argument follows keyword argument.
#
# This definition would also be invalid:
# def __init__(self, price=14.99, title, author):
#     pass
# SyntaxError: a non-default parameter follows a default parameter here.
# Use required title and author first, followed by optional price.


# --- 7. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Exercises using Book refer to the class defined in section 3 above.
# Keep intentional-error lines commented out.

# Exercise 1 — A fixed initial attribute
# Predict all three outputs. Explain why pages is not an argument to Notebook().
# class Notebook:
#     def __init__(self, color):
#         self.color = color
#         self.pages = 100
#
# first = Notebook("blue")
# second = Notebook("red")
# first.pages = 80
# print(first.color)
# print(first.pages)
# print(second.pages)
# ANSWER:


# Exercise 2 — Default or custom price?
# Predict all three outputs. Does the second call affect the third call's price?
# first = Book("First", "Author A")
# second = Book("Second", "Author B", 29.99)
# third = Book("Third", "Author C")
# print(first.price)
# print(second.price)
# print(third.price)
# ANSWER:


# Exercise 3 — Match keyword arguments to parameters
# Predict all three outputs. Explain why the argument order works.
# book = Book(price=8.99, author="George Orwell", title="Animal Farm")
# print(book.title)
# print(book.author)
# print(book.price)
# ANSWER:


# Exercise 4 — Diagnose the calls
# Consider each call separately. Which succeed, and which raise TypeError?
# For successful calls, state the stored price. Explain each failure.
# A. Book("Title", "Author")
# B. Book(title="Title", price=9.99)
# C. Book("Title", "Author", price=0)
# D. Book("Title", "Author", 19.99, price=9.99)
# E. Book("Title", "Author", cost=9.99)
# Keep invalid calls commented out.
# ANSWER:


# Exercise 5 — An explicit value is not an omitted value
# Predict all three outputs. Explain why None does not become 14.99.
# first = Book("First", "Author", price=None)
# second = Book("Second", "Author")
# first.price = 4.99
# print(first.price)
# print(second.price)
# print(Book("Third", "Author", price=None).price)
# ANSWER:


# Exercise 6 — Write your own class with a default
# 1. Define a class named MusicPlayer.
# 2. Give __init__ a required brand parameter and a volume parameter defaulting to 5.
# 3. Store both values as instance attributes.
# 4. Create one player using the default volume and another with a custom volume.
# 5. Create a third using keyword arguments in a different order.
# 6. Print all three volumes. Explain why callers do not pass self and why
#    the default must appear in the parameter list as well as being stored
#    through an attribute assignment in the method body.
# Write your code below:

# ANSWER:


# Optional challenge — Combine required, default, and fixed initial values
# Work through this one together when you are ready.
# Define a class named BookOrder.
# Its __init__ should accept required title and author parameters, followed by
# price=14.99 and quantity=1. Store all four as instance attributes.
# Also set self.status to "pending" inside __init__; do not accept status
# as a parameter. This gives every order the same initial status.
# Create orders with defaults, custom values, and reordered keyword arguments.
# No additional methods or input validation are needed for this challenge.
# Write your code below:


# Uncomment these checks after defining your class:
# standard = BookOrder("Animal Farm", "George Orwell")
# custom = BookOrder("The Great Gatsby", "F. Scott Fitzgerald", 19.99, 2)
# bulk = BookOrder(quantity=3, author="Thomas Hardy", title="Jude the Obscure")
# print(standard.price, standard.quantity, standard.status)  # => 14.99 1 pending
# print(custom.price, custom.quantity)                      # => 19.99 2
# print(bulk.price, bulk.quantity)                          # => 14.99 3
# standard.status = "paid"
# print(custom.status)                                     # => pending
# Explain the difference between the fixed initial status and the default price.
# Would BookOrder("Sample", "Author", status="paid") work with this signature?
# Would explicitly passing quantity=0 use the default of 1? Explain why.
