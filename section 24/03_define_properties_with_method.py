# Define properties with methods — Study Summary
# Instructor summary:
# - A getter (reader) retrieves a value; a setter (writer) assigns a value.
# - Properties expose method logic through ordinary attribute syntax.
# - Reading object.feet invokes the property's getter.
# - Assigning object.feet = value invokes its setter with that value.
# - A getter can convert stored data without storing a duplicate value.
# - A setter can validate input before changing internal state.
# - Define a property in the class body with property(getter, setter).
# - Pass the functions themselves, without calling them with parentheses.
# - Use a different name for the property and its backing storage.
#
# Clarifications to the transcript:
# - A property IS an attribute managed by a descriptor, not a separate category
#   outside attributes. The property object lives on the class.
# - Plain attributes are often sufficient; explicit getter/setter methods are
#   not universally wrong. Properties suit operations that feel like data access.
# - property(fget=None, fset=None, fdel=None, doc=None) accepts a getter, setter,
#   deleter, and documentation. All four arguments are optional.
# - A leading underscore marks internal names by convention, not access control.
# - The lesson's setter silently ignores negative values; it raises no error.
# - Its initializer writes _inches directly, bypassing the setter's validation.
# - These examples assume ordinary numeric inputs; they do not fully validate
#   types or handle every possible numeric value.
# - Recursion occurs when an accessor accesses its OWN property again instead
#   of separate storage, not merely because a name appears in two places.
# - The / operator returns a float for the integer inputs used in this lesson.


# --- 1. Store inches and expose feet through a property ---
class Height:
    def __init__(self, feet):
        self._inches = feet * 12

    def _get_feet(self):
        return self._inches / 12

    def _set_feet(self, feet):
        if feet >= 0:
            self._inches = feet * 12

    feet = property(_get_feet, _set_feet)


# Define the accessors before referring to them in the property call.
# feet is the public name; _inches is the single stored measurement.
# _get_feet and _set_feet are internal methods used by the property.
# The equivalent keyword form is:
# feet = property(fget=_get_feet, fset=_set_feet)


# --- 2. Read the property without method-call parentheses ---
height = Height(5)
print(height.feet)     # => 5.0
print(height._inches)  # => 60
# height.feet runs _get_feet with height supplied as self.
# The getter converts 60 inches to 5.0 feet without changing stored state.
# Reading _inches here illustrates storage; normal callers should use feet.
# Keep this intentional error commented out:
# height.feet()  # TypeError: the returned float is not callable.


# --- 3. Assignment invokes the setter ---
height.feet = 6
print(height.feet)     # => 6.0
print(height._inches)  # => 72
# Python passes 6 to _set_feet as the feet argument.
# The setter stores 72 inches; it does not create a second stored feet value.
# A later read runs the getter again using the updated _inches.


# --- 4. Validate an update before changing storage ---
height.feet = -10
print(height.feet)     # => 6.0
print(height._inches)  # => 72
# The condition is false, so the setter leaves the previous value unchanged.
# Silently ignoring invalid input is this lesson's design choice. A different
# interface could raise ValueError to tell callers that their input is invalid.

height.feet = 0
print(height.feet)  # => 0.0
# Zero passes the >= 0 check: this setter accepts nonnegative values.


# --- 5. Notice the initializer's validation gap ---
negative_height = Height(-2)
print(negative_height.feet)  # => -2.0
# __init__ assigns _inches directly, so _set_feet never checks this input.
# Adding validation to a setter does not validate every assignment automatically.
# Direct external assignment to _inches would also bypass that validation.


class ValidatedHeight:
    def __init__(self, feet):
        self.feet = feet

    def _get_feet(self):
        return self._inches / 12

    def _set_feet(self, feet):
        if feet < 0:
            raise ValueError("Height cannot be negative.")
        self._inches = feet * 12

    feet = property(_get_feet, _set_feet)


validated = ValidatedHeight(5)
validated.feet = 6
print(validated.feet)  # => 6.0
# Assigning self.feet inside __init__ invokes the same setter as later updates.
# This version raises an error for negative input during either operation.
# Simply routing initialization through the original silent setter could leave
# _inches missing when the initial value is negative.
# Keep these intentional errors commented out:
# ValidatedHeight(-2)  # ValueError: Height cannot be negative.
# validated.feet = -1 # ValueError; the existing height remains unchanged.


# --- 6. Keep property access separate from backing storage ---
# These accessor bodies would recursively invoke themselves:
# def _get_feet(self):
#     return self.feet
#
# def _set_feet(self, value):
#     self.feet = value
#
# If wired to the feet property, each read or write repeats until RecursionError.
# The lesson avoids this by reading and writing self._inches instead.
# A property named feet could also use self._feet as its backing attribute.
# self.feet = feet in ValidatedHeight.__init__ is fine: it enters the setter,
# whose body writes _inches rather than entering the same setter again.


# --- 7. Omit a setter to expose a read-only property ---
class ReadOnlyHeight:
    def __init__(self, feet):
        self._inches = feet * 12

    def _get_feet(self):
        return self._inches / 12

    feet = property(_get_feet)


fixed_height = ReadOnlyHeight(5)
print(fixed_height.feet)  # => 5.0
# Keep these intentional errors commented out:
# fixed_height.feet = 6  # AttributeError: no setter was supplied.
# del fixed_height.feet # AttributeError: no deleter was supplied.
# Read-only describes this public property, not an immutable object.
# _inches can still be changed directly, though callers should avoid doing so.


# --- 8. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Exercises using Height refer to the class defined in section 1 above.
# Keep intentional-error lines commented out.

# Exercise 1 — Convert on read
# Predict both outputs. Which value is actually stored on the instance?
# measurement = Height(5.5)
# print(measurement.feet)
# print(measurement._inches)
# ANSWER:


# Exercise 2 — Trace accepted and ignored assignments
# Predict all three outputs and explain which accessor each operation invokes.
# measurement = Height(5)
# measurement.feet = 7
# print(measurement.feet)
# measurement.feet = -3
# print(measurement.feet)
# measurement.feet = 0
# print(measurement.feet)
# ANSWER:


# Exercise 3 — Initialization versus property assignment
# Predict both outputs. Why is the initial negative value stored?
# measurement = Height(-4)
# print(measurement.feet)
# measurement.feet = -2
# print(measurement.feet)
# How would ValidatedHeight(-4) behave instead?
# ANSWER:


# Exercise 4 — Pass a function or call it?
# Explain why the first definition is correct inside the Height class body.
# feet = property(_get_feet, _set_feet)
# feet = property(_get_feet(), _set_feet())
# What would the parentheses attempt to do before property is constructed?
# ANSWER:


# Exercise 5 — Diagnose recursive access
# A feet property's getter contains return self.feet.
# Explain what happens when a caller reads measurement.feet.
# Rewrite the getter to read _inches and return the measurement in feet.
# ANSWER:


# Exercise 6 — Write your own converted property
# 1. Define Distance with __init__(self, meters).
# 2. Store the measurement internally as _centimeters = meters * 100.
# 3. Define _get_meters to return _centimeters / 100.
# 4. Define _set_meters to update _centimeters only when meters >= 0.
# 5. Create meters with property(_get_meters, _set_meters).
# 6. Create a distance, read meters, and assign a new positive measurement.
# 7. Assign a negative measurement and verify that the prior value remains.
# Assume numeric inputs and preserve the lesson's direct initialization style.
# Write your code below:

# ANSWER:


# Optional challenge — Apply one validation rule at both entry points
# Work through this one together when you are ready.
# Define ValidatedDistance with a meters property and _centimeters storage.
# Reject negative meters with ValueError in the setter.
# Route initialization through the property so the same rule applies there.
# Use property(...) rather than decorators for this exercise.
# Assume ordinary numeric inputs.
# Write your code below:


# Uncomment these checks after defining your class:
# distance = ValidatedDistance(2)
# print(distance.meters)  # => 2.0
# distance.meters = 3.5
# print(distance.meters)  # => 3.5
# distance.meters = 0
# print(distance.meters)  # => 0.0
# Try each invalid operation separately and explain why it raises ValueError:
# ValidatedDistance(-1)
# distance.meters = -1
# Explain why assigning self.meters in __init__ does not cause recursion,
# while assigning self.meters inside its own setter would.
