# String representation with __str__ and __repr__ — Study Summary
# Instructor summary:
# - Customize an object's string representations by defining special methods.
# - __str__(self) returns a readable, user-friendly description.
# - __repr__(self) returns a technical description useful to developers.
# - Both methods must return strings, rather than print their descriptions.
# - print(object) and str(object) use the object's string representation.
# - repr(object) requests its developer-facing representation.
# - When practical, __repr__ should resemble Python code that could recreate
#   an object with the same values.
# - If no custom __str__ is provided, the inherited default uses __repr__.
# - Choose the attributes that make the representation useful and meaningful.
#
# Clarifications to the transcript:
# - These methods represent an instance, not the class object itself.
# - _rank and _suit are non-public by convention, not access-protected by Python.
# - A default representation typically includes the module, class, and an
#   identity-related hexadecimal value. Its exact form is implementation-dependent;
#   a memory address is not a portable guarantee, nor must it change every run.
# - repr() does not fall back to a custom __str__. The default fallback works
#   in the other direction: object.__str__ uses the object's __repr__.
# - An invalid __str__ result raises TypeError; it does not trigger a repr fallback.
# - A reconstructible repr is a goal when feasible, not a requirement for all objects.
# - Returning code-like text does not execute it or create another instance.
# - !r in an f-string applies repr() to a value, handling string quotes and escapes.
#   It is more robust than manually placing quote characters around attributes.
# - The built-in function is repr(), not __repr__(); __repr__ is the method name.


# --- 1. Inspect the default representation ---
class PlainCard:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit


plain_card = PlainCard("Ace", "Spades")
print(plain_card)  # Example shape: <__main__.PlainCard object at 0x...>
# The exact output varies. Python does not automatically display our attributes.
# __main__ is the module name when this file is run as a script.


# --- 2. Define user-friendly and developer-facing representations ---
class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def __str__(self):
        return f"{self._rank} of {self._suit}"

    def __repr__(self):
        return f"Card({self._rank!r}, {self._suit!r})"


card = Card("Ace", "Spades")
print(card)        # => Ace of Spades
print(str(card))   # => Ace of Spades
print(repr(card))  # => Card('Ace', 'Spades')
# str(card) requests the readable description; repr(card) requests the technical one.
# The quotes inside the repr result are actual characters in the returned string.
# Single or double quotes can both represent a Python string literal.


# --- 3. Return a string; let the caller decide what to do with it ---
description = str(card)
technical_description = repr(card)
print(type(description))            # => <class 'str'>
print(type(technical_description))  # => <class 'str'>
print("Your card: " + description)  # => Your card: Ace of Spades
# Neither method prints anything itself. Each returns a reusable string.
# Direct calls illustrate the hooks, but prefer str(card) and repr(card).
print(card.__str__())   # => Ace of Spades
print(card.__repr__())  # => Card('Ace', 'Spades')


# --- 4. Use !r to preserve quotes and escape characters ---
rank = "Ace"
print(f"{rank}")   # => Ace
print(f"{rank!r}") # => 'Ace'
# In Card.__repr__, !r applies repr() separately to each attribute.
# That produces suitable string literals even when a value contains a quote.
novelty_card = Card('The "Ace"', "Spades")
print(novelty_card)        # => The "Ace" of Spades
print(repr(novelty_card))  # => Card('The "Ace"', 'Spades')
# The returned text describes a constructor call; it does not execute one.


# --- 5. Fall back to __repr__ when no custom __str__ exists ---
class ReprOnlyCard:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def __repr__(self):
        return f"ReprOnlyCard({self._rank!r}, {self._suit!r})"


repr_only_card = ReprOnlyCard("King", "Hearts")
print(repr_only_card)        # => ReprOnlyCard('King', 'Hearts')
print(str(repr_only_card))   # => ReprOnlyCard('King', 'Hearts')
print(repr(repr_only_card))  # => ReprOnlyCard('King', 'Hearts')
# This class inherits object.__str__, which uses our __repr__ implementation.
# A class defining only __str__ would still have the default object.__repr__.


# --- 6. Containers and f-strings can request different representations ---
hand = [card, Card("Queen", "Hearts")]
print(hand)  # => [Card('Ace', 'Spades'), Card('Queen', 'Hearts')]
# A list's representation uses repr() for its elements, even when printed.
print(f"Selected: {card}")     # => Selected: Ace of Spades
print(f"Selected: {card!s}")   # => Selected: Ace of Spades
print(f"Debug: {card!r}")      # => Debug: Card('Ace', 'Spades')
# For this class, an empty f-string format uses its string representation.
# !s explicitly applies str(); !r explicitly applies repr().


# --- 7. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# The Card and ReprOnlyCard classes above are available to these exercises.
# Keep intentional-error examples commented out.

# Exercise 1 — Choose the representation
# Predict all three outputs. Identify the special method used for each.
# queen = Card("Queen", "Diamonds")
# print(queen)
# print(str(queen))
# print(repr(queen))
# ANSWER:


# Exercise 2 — Explain the fallback
# Predict both outputs and explain why they match.
# king = ReprOnlyCard("King", "Clubs")
# print(king)
# print(repr(king))
# Would defining only __str__ make repr(king) use that method? Explain.
# ANSWER:


# Exercise 3 — A card inside a list
# Predict both outputs. Explain why the descriptions differ.
# ace = Card("Ace", "Hearts")
# print(ace)
# print([ace])
# ANSWER:


# Exercise 4 — Return, do not print
# Explain what is wrong with this implementation and write a corrected version.
# Leave the failing example commented out.
# class BrokenCard:
#     def __str__(self):
#         print("Ace of Spades")
#
# print(BrokenCard())  # Prints inside the method, then raises TypeError.
# What does a method return when it has no return statement?
# ANSWER:


# Exercise 5 — Explain !r
# Predict both outputs. Explain why !r is helpful in Card.__repr__.
# suit = "Clubs"
# print(f"Suit: {suit}")
# print(f"Suit: {suit!r}")
# ANSWER:


# Exercise 6 — Write your own representations
# Define a Book class with title and author stored as _title and _author.
# Make str(book) return: The Hobbit by J. R. R. Tolkien
# Make repr(book) return: Book('The Hobbit', 'J. R. R. Tolkien')
# Use the instance's actual attribute values, not hard-coded descriptions.
# Use !r for the attribute values in __repr__.
# Write your code below:


# Uncomment these checks after defining your class:
# book = Book("The Hobbit", "J. R. R. Tolkien")
# print(book)        # => The Hobbit by J. R. R. Tolkien
# print(repr(book))  # => Book('The Hobbit', 'J. R. R. Tolkien')
# print([book])      # => [Book('The Hobbit', 'J. R. R. Tolkien')]


# Optional challenge — Same description, separate objects
# Work through this one together when you are ready.
# Predict all three outputs and explain the difference between an object's
# representation and its identity. No custom equality method is needed here.
# first = Card("Ace", "Spades")
# second = Card("Ace", "Spades")
# print(str(first) == str(second))
# print(repr(first) == repr(second))
# print(first is second)
# ANSWER:
