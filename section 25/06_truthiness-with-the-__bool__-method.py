# Truthiness with __bool__ — Study Summary
# Instructor summary:
# - __bool__ defines how a custom object behaves in a Boolean context.
# - Boolean contexts include if statements and while loop conditions.
# - Python calls this special method when it needs the object's truth value.
# - Define __bool__(self) in the class and return True or False.
# - The result can depend on the object's current attributes.
# - Changing those attributes can change the same object's truthiness.
# - bool(object) explicitly asks Python for the object's truth value.
#
# Clarifications and connections:
# - __bool__ must return an actual bool, not just a truthy or falsy value.
#   Returning 1, 0, a string, or None raises TypeError during truth testing.
# - Without __bool__, Python falls back to __len__ if it is defined.
#   A length of zero is falsy; a positive length is truthy.
# - If neither method is defined, an ordinary custom object is truthy.
# - A truthy object does not become the Boolean True; it is still an object.
# - if object checks truthiness; object == True checks equality instead.
# - Prefer if object or bool(object) over directly calling __bool__.
# - The Emotion rule below is an example chosen for this class, not a
#   general rule Python applies to every object.


# --- 1. Define truthiness for an Emotion object ---
class Emotion:

    def __init__(self, positivity, negativity):
        self.positivity = positivity
        self.negativity = negativity

    def __bool__(self):
        return self.positivity > self.negativity


# The comparison returns a Boolean:
# True  -> positivity is greater than negativity.
# False -> positivity is less than or equal to negativity.
# self refers to the Emotion object whose truth value is being checked.


# --- 2. Start with a falsy object ---
my_emotional_state = Emotion(50, 75)

print(bool(my_emotional_state))  # => False

if my_emotional_state:
    print("This will not print because positivity is lower than negativity.")

# The if body is skipped because __bool__ returns False:
# self.positivity > self.negativity
# 50 > 75
# False
# The object still exists; being falsy does not mean it is None.
print(my_emotional_state is None)  # => False


# --- 3. Change the same object's truthiness ---
my_emotional_state.positivity = 100

print(bool(my_emotional_state))  # => True

if my_emotional_state:
    print("This will print because positivity is greater than negativity.")
# => This will print because positivity is greater than negativity.

# Python checks the current attribute values each time:
# self.positivity > self.negativity
# 100 > 75
# True
# We changed an attribute; we did not create a new Emotion object.


# --- 4. Equal values are falsy under this rule ---
balanced_state = Emotion(75, 75)

print(bool(balanced_state))  # => False

if balanced_state:
    print("Positivity is greater.")
else:
    print("Positivity is not greater.")
# => Positivity is not greater.

# The rule uses >, not >=. Equal values therefore produce False.


# --- 5. Use bool(), not, and ordinary if syntax ---
hopeful_state = Emotion(90, 20)

print(bool(hopeful_state))  # => True
print(not hopeful_state)   # => False
print(not balanced_state)  # => True

# A direct call illustrates the method, but bool() is the usual approach.
print(hopeful_state.__bool__())  # => True
# Truth testing does not replace the object with True or False.
print(hopeful_state.positivity)  # => 90


# --- 6. What happens without __bool__? ---
class OrdinaryObject:
    pass


ordinary_object = OrdinaryObject()
print(bool(ordinary_object))  # => True
# No __bool__ or __len__ is defined, so the object is truthy by default.


class Basket:

    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


print(bool(Basket([])))         # => False
print(bool(Basket(["apple"])))  # => True
# Basket has no __bool__, so Python uses __len__ for truth testing.
# If a class defines both methods, __bool__ controls its truth value.


# --- 7. Return a Boolean, not a number ---
# Keep this intentional-error example commented out:
#
# class InvalidEmotion:
#
#     def __bool__(self):
#         return 1
#
# print(bool(InvalidEmotion()))
# TypeError: __bool__ should return bool, returned int
#
# Although bool(1) is True, returning 1 from __bool__ is invalid.
# Return True, False, or an expression that produces a bool.


# --- 8. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Keep intentional-error examples commented out.

# Exercise 1 — Predict truthiness
# Predict each output using the Emotion class's rule.
# print(bool(Emotion(80, 30)))
# print(bool(Emotion(20, 60)))
# print(bool(Emotion(40, 40)))
# ANSWER:


# Exercise 2 — Trace self
# For the following truth test, identify what self refers to and the
# values compared inside __bool__.
# mood = Emotion(15, 25)
# print(bool(mood))
# ANSWER:
# self refers to:
# self.positivity:
# self.negativity:
# __bool__ returns:


# Exercise 3 — Change the state
# Predict all three outputs. Explain why one object can produce
# different truth values at different times.
# mood = Emotion(10, 20)
# print(bool(mood))
# mood.positivity = 30
# print(bool(mood))
# mood.negativity = 30
# print(bool(mood))
# ANSWER:


# Exercise 4 — Choose the branch
# Which message prints? What would change if positivity became 6?
# mood = Emotion(5, 5)
# if mood:
#     print("More positivity")
# else:
#     print("Not more positivity")
# ANSWER:


# Exercise 5 — Explain the return type
# Why is return 1 invalid inside __bool__, even though 1 is truthy?
# What does the expression self.positivity > self.negativity return?
# ANSWER:


# Exercise 6 — Write your own rule
# Create a Battery class with a charge attribute.
# Define __bool__ so a battery is truthy only when charge is greater than 0.
# Test Battery(0) and Battery(50) with bool() and an if statement.
# Write your code below:


# Optional challenge — Change the boundary
# Create a separate InclusiveEmotion class whose truthiness rule uses >=.
# Compare Emotion(50, 50) with InclusiveEmotion(50, 50) using bool().
# Explain how the choice of comparison changes the result.
# ANSWER:


# --- 9. Final review ---
# 1. The __________ method defines a custom object's truthiness.
# 2. __bool__ must return a value of type __________.
# 3. The built-in __________ function explicitly checks truthiness.
# 4. Without __bool__, Python tries __________ if it is defined.
# 5. An object with neither truth-testing method is __________ by default.
# 6. Does a falsy object necessarily equal None?
# 7. Why is Emotion(75, 75) falsy under the original rule?
# ANSWER:
