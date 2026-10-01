# The hasattr and delattr functions — Study Summary
# Instructor summary:
# - hasattr(object, name) checks whether an attribute can be accessed.
# - It returns True or False, making it useful in an if statement.
# - delattr(object, name) removes the named attribute when deletion is supported.
# - Both functions take an object and an attribute name supplied as a string.
# - Use names stored in variables to check or delete attributes dynamically.
# - Deleting a missing ordinary instance attribute raises AttributeError.
# - For the lesson's Pizza objects, check with hasattr before deleting each name.
# - Removing an attribute makes subsequent ordinary access to that name fail.
#
# Clarifications to the transcript:
# - hasattr performs attribute lookup; it returns False if lookup raises
#   AttributeError. Other exceptions raised during lookup propagate.
# - Lookup can invoke a property getter or custom attribute-access code.
# - True does not guarantee that deletion is allowed: an attribute may be
#   inherited or may be a property without a deleter.
# - Checking and then deleting works for the simple instance data shown here;
#   it is not a universal guarantee that delattr cannot raise an exception.
# - delattr returns None, not the removed value or the modified object.
# - delattr(obj, "size") corresponds to del obj.size for a fixed attribute name.
# - Removing an attribute does not delete the entire object or other references
#   to the value that the attribute held.
# - An attribute whose value is None, False, or 0 still exists.


# --- 1. Recreate the Pizza example from the previous lesson ---
stats = {
    "name": "BBQ Chicken",
    "price": 19.99,
    "size": "Extra Large",
    "ingredients": ["chicken", "onions", "BBQ sauce"],
}


class Pizza:
    def __init__(self, stats):
        for key, value in stats.items():
            setattr(self, key, value)


bbq = Pizza(stats)
print(bbq.size)  # => Extra Large
# Each dictionary key becomes an ordinary instance attribute.
# This lesson is self-contained; it does not need to import the previous file.


# --- 2. Check whether attributes can be accessed ---
print(hasattr(bbq, "size"))      # => True
print(hasattr(bbq, "diameter"))  # => False

attribute_name = "ingredients"
print(hasattr(bbq, attribute_name))  # => True
# Pass the variable to use its string value as the attribute name.
# hasattr(bbq, "attribute_name") would check that literal name instead.

if hasattr(bbq, "size"):
    print(bbq.size)  # => Extra Large
# For a simple read with a fallback, getattr is another option:
print(getattr(bbq, "diameter", "Unknown"))  # => Unknown


# --- 3. Delete only the requested attributes that exist ---
stats_to_delete = ["size", "diameter", "spiciness", "ingredients"]

for stat in stats_to_delete:
    if hasattr(bbq, stat):
        delattr(bbq, stat)
        print(f"Deleted {stat}")
# => Deleted size
# => Deleted ingredients
# diameter and spiciness are absent, so their deletion calls are skipped.

print(hasattr(bbq, "size"))         # => False
print(hasattr(bbq, "ingredients"))  # => False
print(bbq.name)                     # => BBQ Chicken
print(bbq.price)                    # => 19.99
# The object still exists, and its other attributes remain available.
# Keep these intentional errors commented out:
# print(bbq.size)       # AttributeError: size was removed.
# delattr(bbq, "size")  # AttributeError: size is already absent.


# --- 4. Compare dynamic deletion with del syntax ---
sample = Pizza({"name": "Cheese", "size": "Small", "price": 10})
result = delattr(sample, "size")
print(result)                   # => None
print(hasattr(sample, "size"))   # => False

del sample.price
print(hasattr(sample, "price"))  # => False
# Use del sample.price when the name is fixed in the source code.
# Use delattr(sample, field) when field contains the name chosen at runtime.
# Do not assign sample = delattr(...): the return value would replace sample
# with None instead of preserving your reference to the Pizza instance.

setattr(sample, "size", "Large")
print(sample.size)  # => Large
# An ordinary instance attribute can be created again after deletion.


# --- 5. Distinguish existence from truthiness ---
plain = Pizza({"discounted": False, "rating": None, "stock": 0})
print(hasattr(plain, "discounted"))  # => True
print(hasattr(plain, "rating"))      # => True
print(hasattr(plain, "stock"))       # => True
print(hasattr(plain, "diameter"))    # => False
# hasattr does not test whether an attribute's value is truthy.
# Setting rating to None does not remove rating; delattr does.
delattr(plain, "rating")
print(hasattr(plain, "rating"))  # => False


# --- 6. Deleting an attribute does not erase its referenced value ---
shared_stats = {"ingredients": ["cheese", "tomato"]}
pizza = Pizza(shared_stats)
saved_ingredients = pizza.ingredients

delattr(pizza, "ingredients")
print(hasattr(pizza, "ingredients"))  # => False
print(saved_ingredients)              # => ['cheese', 'tomato']
print(shared_stats["ingredients"])   # => ['cheese', 'tomato']
# The dictionary and saved variable still refer to the original list.
# Removing the instance attribute does not remove the dictionary's key.


# --- 7. Understand the limits of an existence check ---
class MenuItem:
    @property
    def name(self):
        return "Pizza"


item = MenuItem()
print(hasattr(item, "name"))  # => True
# hasattr runs the getter, which returns successfully.
# Keep this intentional error commented out:
# delattr(item, "name")  # AttributeError: the property has no deleter.
# An accessible attribute is not necessarily a deletable instance attribute.
# Similarly, methods or class attributes can be found through an instance even
# though they are not stored on that instance for delattr to remove.
# The guarded deletion loop above is intended for Pizza's ordinary stored data.


# --- 8. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Exercises using Pizza refer to the class defined in section 1 above.
# Keep intentional-error lines commented out.

# Exercise 1 — Present or missing?
# Predict all three outputs. Does None mean an attribute is absent?
# pizza = Pizza({"name": "Cheese", "size": None})
# print(hasattr(pizza, "name"))
# print(hasattr(pizza, "size"))
# print(hasattr(pizza, "price"))
# ANSWER:


# Exercise 2 — Trace a guarded deletion loop
# Predict all three outputs. Explain why diameter causes no error.
# pizza = Pizza({"name": "Veggie", "size": "Large", "price": 15})
# for field in ["size", "diameter", "price"]:
#     if hasattr(pizza, field):
#         delattr(pizza, field)
# print(hasattr(pizza, "size"))
# print(hasattr(pizza, "price"))
# print(pizza.name)
# ANSWER:


# Exercise 3 — Delete the same attribute twice
# Explain which call fails and which exception it raises.
# Rewrite the calls using an existence check so a missing size is skipped.
# pizza = Pizza({"size": "Small"})
# delattr(pizza, "size")
# delattr(pizza, "size")
# Keep the failing call commented out.
# ANSWER:


# Exercise 4 — Dynamic names and return values
# Predict all three outputs. Which attribute does field identify?
# pizza = Pizza({"size": "Medium", "field": "Keep me"})
# field = "size"
# result = delattr(pizza, field)
# print(result)
# print(hasattr(pizza, "size"))
# print(pizza.field)
# ANSWER:


# Exercise 5 — Attribute removal versus list mutation
# Predict both outputs. Explain why the saved list still exists.
# pizza = Pizza({"ingredients": ["cheese"]})
# saved = pizza.ingredients
# delattr(pizza, "ingredients")
# saved.append("olives")
# print(saved)
# print(hasattr(pizza, "ingredients"))
# ANSWER:


# Exercise 6 — Write a reusable removal function
# 1. Define remove_stats(pizza, names).
# 2. Loop over names and check each one with hasattr.
# 3. Delete each existing attribute with delattr.
# 4. Return a list of the names successfully removed, in removal order.
# 5. Test with both present and missing names.
# Assume names refer only to ordinary Pizza instance data, not methods or
# properties. Do not generalize the existence check to all possible objects.
# Write your code below:

# ANSWER:


# Optional challenge — Report removed and skipped names
# Work through this one together when you are ready.
# Extend remove_stats to return a dictionary with "removed" and "skipped" lists.
# Put each requested name in the appropriate list and preserve request order
# within each list. Use the same ordinary-instance-data assumption as above.
# Repeated names should be checked again after any earlier deletion.
# Write your code below:


# Uncomment these checks after defining your function:
# pizza = Pizza({"name": "Cheese", "size": "Large"})
# report = remove_stats(pizza, ["size", "diameter", "size"])
# print(report["removed"])      # => ['size']
# print(report["skipped"])      # => ['diameter', 'size']
# print(pizza.name)             # => Cheese
# print(hasattr(pizza, "size")) # => False
# Explain why the second request for size is skipped.
