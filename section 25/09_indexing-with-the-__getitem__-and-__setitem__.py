# Indexing with __getitem__ and __setitem__ — Study Summary
# Instructor summary:
# - __getitem__ defines how a custom object retrieves a value with brackets.
# - __setitem__ defines how it assigns a value with brackets.
# - Lists use positions; dictionaries use keys to identify stored values.
# - A custom class decides what the value inside its brackets means.
# - CrayonBox delegates reading and writing to an internal crayons list.
# - __getitem__(self, index) returns the requested value.
# - __setitem__(self, index, value) updates the stored value.
# - These methods let custom objects work with familiar Python syntax.
#
# Clarifications to the transcript:
# - The error says "not subscriptable", not "not scriptable".
# - Reading an item and assigning an item are separate operations.
#   Defining __getitem__ alone does not enable bracket assignment.
# - The parameter name index is our choice; a mapping might call it key.
# - Our implementation forwards indexes to a list, so it supports integer
#   positions, negative indexes, and slices, but not string keys.
# - __setitem__ changes state; its return value is ignored by assignment.
# - Without __iter__, Python can fall back to sequence-style __getitem__
#   for iteration: it requests indexes 0, 1, 2, ... until IndexError.
# - Having __getitem__ is not enough for useful iteration unless that
#   sequence-style behavior is supported. Python does not inspect our list.
# - Neither item method automatically defines len() or item deletion.
#   Those operations need __len__ and __delitem__, respectively.


# --- 1. Read values from a built-in dictionary ---
pillows = {"soft": 79.99, "hard": 99.99}

print(pillows["soft"])              # => 79.99
print(pillows.__getitem__("soft"))  # => 79.99
# The direct call illustrates the method used for bracket lookup.
# Prefer pillows["soft"] in ordinary code.

pillows["soft"] = 69.99
print(pillows["soft"])  # => 69.99
# Bracket assignment uses __setitem__ instead of __getitem__.


# --- 2. Define a CrayonBox with readable and writable items ---
class CrayonBox:

    def __init__(self):
        self.crayons = []

    def add(self, crayon):
        self.crayons.append(crayon)

    def __getitem__(self, index):
        return self.crayons[index]

    def __setitem__(self, index, value):
        self.crayons[index] = value


# Each box starts with its own empty list.
# add() appends a crayon to the end.
# __getitem__ reads from the list at the supplied index.
# __setitem__ replaces the list item at the supplied index.
# Without the item methods, storing a list would not by itself make
# a CrayonBox support square brackets.


# --- 3. Add crayons and read them by position ---
cb = CrayonBox()
cb.add("blue")
cb.add("red")

print(cb[0])  # => blue
print(cb[1])  # => red

# For cb[0], Python uses CrayonBox.__getitem__:
# self  -> cb
# index -> 0
# return self.crayons[0] -> "blue"
#
# The caller indexes the CrayonBox object. The method handles the
# internal list access on the caller's behalf.


# --- 4. Replace a crayon with bracket assignment ---
cb[0] = "yellow"

# Python uses CrayonBox.__setitem__:
# self  -> cb
# index -> 0
# value -> "yellow"
#
# The method performs:
# self.crayons[0] = "yellow"

print(cb[0])       # => yellow
print(cb[1])       # => red
print(cb.crayons)  # => ['yellow', 'red']
# This replaces blue; it does not append a third crayon.
# No explicit return is needed in __setitem__.


# --- 5. Iterate using the sequence fallback ---
for crayon in cb:
    print(crayon)
# => yellow
# => red

# CrayonBox has no __iter__, so Python tries __getitem__ with:
# 0 -> "yellow"
# 1 -> "red"
# 2 -> IndexError from the internal list, which ends iteration.
#
# The loop iterates over cb, not an explicit cb.crayons expression.
# Do not replace the out-of-range IndexError with return None:
# the fallback needs that exception to know when to stop.


# --- 6. Negative indexes and slices also reach the list ---
print(cb[-1])  # => red
print(cb[:1]) # => ['yellow']

# For cb[:1], index receives a slice object rather than an integer.
# The internal list already understands slices, so delegation supports them.
# Slicing here returns a list, not another CrayonBox.
cb[-1] = "green"
print(cb.crayons)  # => ['yellow', 'green']

# Slice assignment works for the same reason:
cb[0:1] = ["blue", "purple"]
print(cb.crayons)  # => ['blue', 'purple', 'green']
# Unlike assignment to one integer index, slice assignment can change
# the number of items when the slice has no extended step.


# --- 7. Keep unsupported operations explicit ---
# Keep these intentional-error examples commented out:
#
# print(cb[99])       # IndexError: list index out of range.
# cb[99] = "orange"   # IndexError: assignment does not append at a new index.
# print(cb["blue"])   # TypeError: this list does not accept string keys.
# print(len(cb))      # TypeError: CrayonBox has no __len__.
# del cb[0]           # TypeError: CrayonBox has no __delitem__.
#
# Use the existing add() method to append a new crayon:
cb.add("orange")
print(cb.crayons)  # => ['blue', 'purple', 'green', 'orange']
# We could add other special methods later if those operations are useful.


# --- 8. Practice: predict, explain, then run ---
# Each exercise creates its own box so it does not depend on earlier edits.
# Write predictions in ANSWER comments before uncommenting each exercise.
# Keep intentional-error examples commented out.

# Exercise 1 — Read by index
# box = CrayonBox()
# box.add("pink")
# box.add("black")
# print(box[0])
# print(box[1])
# print(box[-1])
# ANSWER:


# Exercise 2 — Trace assignment
# Identify self, index, and value when the assignment below runs.
# Which special method handles it? What is the final list?
# box = CrayonBox()
# box.add("red")
# box.add("blue")
# box[1] = "white"
# ANSWER:
# Method:
# self:
# index:
# value:
# Final list:


# Exercise 3 — Append or replace?
# Predict the output. Explain the difference between add() and assignment.
# box = CrayonBox()
# box.add("red")
# box[0] = "yellow"
# box.add("green")
# print(box.crayons)
# ANSWER:


# Exercise 4 — Explain iteration
# What prints? Which index eventually raises IndexError to end the loop?
# box = CrayonBox()
# box.add("silver")
# box.add("gold")
# for color in box:
#     print(color)
# ANSWER:


# Exercise 5 — Predict a slice
# Predict the output and its type. What kind of object is passed as index?
# box = CrayonBox()
# box.add("red")
# box.add("green")
# box.add("blue")
# print(box[1:])
# ANSWER:


# Exercise 6 — Build your own indexable class
# Create a Playlist class that stores a list of song titles.
# Implement __getitem__ and __setitem__ by delegating to that list.
# Create a playlist, read its first song, replace that song, and iterate
# over the playlist to display the updated contents.
# Write your code below:


# Optional challenge — Connect indexing and length
# Create a separate SizedCrayonBox class with the same item behavior
# and a __len__ method that counts its crayons.
# Test len() on an empty box and after adding two crayons.
# Explain why __getitem__ alone did not provide len() for CrayonBox.
# ANSWER:


# --- 9. Final review ---
# 1. Reading box[0] uses the __________ method.
# 2. Assigning box[0] = "red" uses the __________ method.
# 3. In __setitem__, the new item is received by the __________ parameter.
# 4. Our CrayonBox forwards item operations to its internal __________.
# 5. Sequence-style fallback iteration starts at index __________.
# 6. The __________ exception signals the end of that iteration.
# 7. Does assigning to an out-of-range integer index append an item?
# 8. Which additional special method would support del box[0]?
# ANSWER:
