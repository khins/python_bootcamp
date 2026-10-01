# Attribute lookup order — Study Summary
# Instructor summary:
# - For ordinary data attributes, Python checks an instance's own attributes
#   before falling back to attributes on its class.
# - Instances can read a class attribute without storing their own copy.
# - Assigning an ordinary attribute on one instance can hide the class value
#   for that instance. This is called shadowing.
# - Other instances still use the class value unless they have their own value.
# - Deleting the instance attribute reveals the class attribute again.
# - Deleting instance.data does not delete ClassName.data.
# - If the requested name cannot be found, ordinary lookup raises AttributeError.
#
# Clarifications to the transcript:
# - "Instance first, then class" describes these ordinary data attributes, not
#   every possible lookup. Properties are an important exception.
# - Under normal instance lookup, a data descriptor found on the class (such as
#   a property) takes precedence over an entry in the instance dictionary.
# - Class lookup also searches base classes in method resolution order (MRO).
# - Classes can customize attribute access with __getattribute__ and __getattr__;
#   the simple Example class below does neither.
# - Adding attributes after construction is valid Python. Whether it is useful
#   depends on the interface; __init__ is a convenient place for consistent state.
# - Reassigning one instance attribute does not reassign another instance's
#   attribute. Mutating an object shared by instances can still affect both.
# - The deletion statement is spelled del, not delete or dl.
# - An instance value of None, False, or 0 still takes precedence over an
#   ordinary class attribute. Fallback depends on absence, not truthiness.


# --- 1. Fall back to a class attribute ---
class Example:
    data = "class attribute"


e1 = Example()
e2 = Example()
print(e1.data)       # => class attribute
print(e2.data)       # => class attribute
print(Example.data)  # => class attribute
print(vars(e1))      # => {}
# Neither instance stores data, so both reads find Example.data.
# Reading the value does not create an instance attribute.
# vars(e1) shows this ordinary instance's own stored attributes.


# --- 2. Shadow the class value on one instance ---
e1.data = "instance attribute"
print(e1.data)       # => instance attribute
print(e2.data)       # => class attribute
print(Example.data)  # => class attribute
print(vars(e1))      # => {'data': 'instance attribute'}
print(vars(e2))      # => {}
# e1.data now finds e1's own value first. e2 still falls back to the class.
# Assignment to e1.data did not overwrite Example.data or change e2.


# --- 3. Delete the instance value to reveal the class value ---
del e1.data
print(e1.data)       # => class attribute
print(e2.data)       # => class attribute
print(Example.data)  # => class attribute
print(vars(e1))      # => {}
# Only e1's own data attribute was removed. The class value remains available.
# delattr(e1, "data") would perform the same deletion if that instance attribute
# existed. Deletion does not automatically remove a value found on the class.
# Keep this intentional error commented out:
# del e1.data  # AttributeError: e1 no longer has its own data to delete.
# Even though deletion would fail, reading e1.data still succeeds.


# --- 4. Distinguish a missing attribute from an existing false-like value ---
e1.data = None
print(e1.data)               # => None
print(e2.data)               # => class attribute
print(hasattr(e1, "data"))   # => True
print(hasattr(e1, "nonsense"))  # => False
print(getattr(e1, "nonsense", "Unknown"))  # => Unknown
# None is an actual instance value, so Python does not fall back to Example.data.
# Keep this intentional error commented out:
# print(e1.nonsense)  # AttributeError: neither instance nor class provides it.
del e1.data


# --- 5. Class updates affect instances that use the fallback ---
e1.data = "personal value"
Example.data = "updated class attribute"
print(e1.data)       # => personal value
print(e2.data)       # => updated class attribute
print(Example.data)  # => updated class attribute
# e1 keeps its own value; e2 reads the new class value on its next lookup.

del e1.data
print(e1.data)  # => updated class attribute
# Deletion reveals the current class value, not a remembered original value.


# --- 6. Properties are an exception to the simple instance-first rule ---
class PropertyExample:
    @property
    def data(self):
        return "property value"


managed = PropertyExample()
# Direct dictionary manipulation is only for demonstrating lookup precedence.
vars(managed)["data"] = "dictionary value"
print(vars(managed))  # => {'data': 'dictionary value'}
print(managed.data)   # => property value
# A property is a data descriptor even when no setter was provided. Its getter
# takes precedence over the same name stored in the instance dictionary.
# Keep this intentional error commented out:
# managed.data = "new value"  # AttributeError: this property has no setter.
# Ordinary assignment does not bypass the property to create a shadowing value.


# --- 7. Preview: class lookup includes inherited attributes ---
class Parent:
    label = "parent value"


class Child(Parent):
    pass


child = Child()
print(child.label)  # => parent value
# Neither the instance nor Child provides an ordinary label value of its own,
# so lookup finds the inherited value on Parent.
child.label = "child instance value"
print(child.label)   # => child instance value
print(Parent.label)  # => parent value
# Inheritance extends class lookup; it does not change the shadowing behavior
# demonstrated for these ordinary attributes.


# --- 8. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Use the separate classes below so their values do not depend on the earlier
# changes to Example.data. Keep intentional-error lines commented out.

# Exercise 1 — Find the source of each value
# Predict all three outputs and identify which object supplies each value.
# class Setting:
#     theme = "light"
#
# first = Setting()
# second = Setting()
# first.theme = "dark"
# print(first.theme)
# print(second.theme)
# print(Setting.theme)
# ANSWER:


# Exercise 2 — Reveal the fallback
# Predict both outputs. What does del remove here?
# class Item:
#     status = "available"
#
# item = Item()
# item.status = "reserved"
# print(item.status)
# del item.status
# print(item.status)
# ANSWER:


# Exercise 3 — Change the class after shadowing
# Predict all three outputs. Does the instance remember the old class value?
# class Label:
#     text = "original"
#
# first = Label()
# second = Label()
# first.text = "custom"
# Label.text = "updated"
# print(first.text)
# print(second.text)
# del first.text
# print(first.text)
# ANSWER:


# Exercise 4 — False-like values still shadow
# Predict all three outputs. Explain why neither read returns the class value.
# class Score:
#     points = 100
#
# first = Score()
# second = Score()
# first.points = 0
# second.points = None
# print(first.points)
# print(second.points)
# print(Score.points)
# ANSWER:


# Exercise 5 — Readable does not mean deletable from the instance
# Explain why the read succeeds but the deletion raises AttributeError.
# class Menu:
#     title = "Lunch"
#
# menu = Menu()
# print(menu.title)
# del menu.title
# Keep the failing deletion commented out.
# How could you first create, then delete, an instance-specific title?
# ANSWER:


# Exercise 6 — Write your own default and override
# 1. Define Player with a class attribute volume = 5.
# 2. Create two instances and print their volume values.
# 3. Assign volume = 8 on only the first instance.
# 4. Change Player.volume to 3 and print both instances' values.
# 5. Delete the first instance's volume and print its value again.
# 6. Explain which reads use instance storage and which use class storage.
# Write your code below:

# ANSWER:


# Optional challenge — Remove both levels of an ordinary attribute
# Work through this one together when you are ready.
# Predict the outputs before uncommenting. Explain each successful lookup and
# why the final lookup uses its default instead of finding a stored value.
# class Message:
#     text = "shared"
#
# first = Message()
# second = Message()
# first.text = "personal"
# del Message.text
# print(first.text)                    # Predict this output.
# print(hasattr(second, "text"))       # Predict this output.
# del first.text
# print(getattr(first, "text", "missing"))  # Predict this output.
# Explain why deleting Message.text did not delete first.text.
# ANSWER:
