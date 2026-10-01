# getattr and setattr functions — Study Summary
# Instructor summary:
# - getattr and setattr access attributes using names supplied as strings.
# - Use them when an attribute name comes from a variable or is chosen at runtime.
# - setattr(object, name, value) assigns a value to the named attribute.
# - getattr(object, name) retrieves the named attribute's value.
# - getattr(object, name, default) supplies a fallback for a missing attribute.
# - Iterate over dictionary items to build attributes from key/value pairs.
# - Use attribute names and getattr to build a dictionary from an object.
# - Dot syntax remains the simpler choice when the attribute name is known.
#
# Clarifications to the transcript:
# - getattr's third argument is OPTIONAL, not mandatory.
# - Without a default, a missing attribute raises AttributeError.
# - setattr can update an existing attribute as well as create a new one.
# - setattr returns None; it does not return the assigned value or the object.
# - Both functions require the attribute name to be a string.
# - Dictionaries preserve insertion order in Python 3.7 and later.
# - self.key means the literal attribute named key, not the value of key.
# - Dynamic access follows normal attribute behavior, including property getters
#   and setters; these functions do not bypass validation or access restrictions.
# - Not all objects allow arbitrary new attributes, for example some built-in
#   types, classes using __slots__, or properties without setters.
# - dir returns a useful list of names, not a guaranteed complete inventory.
#   It can include inherited names, methods, and properties, not just stored data.
# - Assigning mutable values stores references; it does not copy those values.


# --- 1. Build instance attributes from a dictionary ---
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
print(bbq.name)         # => BBQ Chicken
print(bbq.price)        # => 19.99
print(bbq.size)         # => Extra Large
print(bbq.ingredients)  # => ['chicken', 'onions', 'BBQ sauce']
# Each key supplies an attribute name; its associated value becomes the value.
# This simple class assumes suitable string keys and performs no validation.


# --- 2. Distinguish a dynamic name from a literal attribute ---
attribute_name = "size"
setattr(bbq, attribute_name, "Medium")
print(bbq.size)  # => Medium
# setattr(bbq, "size", "Medium") has the same effect as bbq.size = "Medium".

bbq.attribute_name = "This is a separate attribute."
print(bbq.attribute_name)  # => This is a separate attribute.
print(bbq.size)            # => Medium
# Dot syntax does not substitute the string stored in attribute_name.
# Likewise, self.key = value in the initializer would repeatedly assign key
# rather than creating name, price, size, and ingredients attributes.

result = setattr(bbq, "discounted", False)
print(result)          # => None
print(bbq.discounted)  # => False
# Do not write bbq = setattr(...): that would replace the variable with None.


# --- 3. Retrieve values using dynamic names ---
print(getattr(bbq, "name"))  # => BBQ Chicken
print(getattr(bbq, "size"))  # => Medium
# These reads are equivalent to bbq.name and bbq.size.

sample = Pizza(stats)
for attr in ["price", "name", "diameter", "discounted"]:
    print(getattr(sample, attr, "Unknown"))
# => 19.99
# => BBQ Chicken
# => Unknown
# => Unknown
# This fresh instance has neither diameter nor discounted.
# Supplying a fallback does not create the missing attribute on the object.
# Keep this intentional error commented out:
# getattr(sample, "diameter")  # AttributeError: no default was supplied.


# --- 4. A fallback does not replace existing false-like values ---
sample.discounted = False
sample.rating = None
sample.stock = 0
print(getattr(sample, "discounted", "Unknown"))  # => False
print(getattr(sample, "rating", "Unknown"))      # => None
print(getattr(sample, "stock", "Unknown"))       # => 0
print(getattr(sample, "diameter", "Unknown"))    # => Unknown
# The default handles missing attributes, not values such as False, None, or 0.
# If None is a valid value, a default of None alone cannot tell you whether
# that value was stored or the requested attribute was missing.


# --- 5. Build a dictionary from selected attributes ---
selected_names = ["name", "price", "size"]
selected_stats = {
    name: getattr(sample, name)
    for name in selected_names
}
print(selected_stats)
# => {'name': 'BBQ Chicken', 'price': 19.99, 'size': 'Extra Large'}
# This reverses the earlier direction: object attributes become dictionary data.
# Explicitly selecting names makes it clear which values belong in the result.
# The transcript's library example illustrates the broader pattern:
# params = {name: getattr(sample, name) for name in dir(sample)}
# That broader form may include methods and internal names, and reading a
# property may run code or raise an exception. It is not a general serializer.
# vars(sample) exposes this ordinary instance's stored attribute dictionary;
# it does not include every inherited attribute or calculated property.


# --- 6. Attribute assignment keeps references to mutable values ---
first = Pizza(stats)
second = Pizza(stats)
print(first.ingredients is stats["ingredients"])  # => True
print(first.ingredients is second.ingredients)    # => True
# Both instances refer to the same list supplied in stats.
# Use a separate dictionary here to demonstrate mutation without changing stats.
shared_stats = {"ingredients": ["cheese"]}
plain = Pizza(shared_stats)
plain.ingredients.append("tomato")
print(shared_stats["ingredients"])  # => ['cheese', 'tomato']
# setattr does not create an independent copy of a list or other mutable value.
# Replacing an attribute is different from mutating its existing value:
plain.ingredients = ["mushrooms"]
print(shared_stats["ingredients"])  # => ['cheese', 'tomato']
print(plain.ingredients)             # => ['mushrooms']


# --- 7. Dynamic access also invokes property methods ---
class PizzaOrder:
    def __init__(self, quantity):
        self.quantity = quantity

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = value


order = PizzaOrder(1)
setattr(order, "quantity", 3)
print(getattr(order, "quantity"))  # => 3
# setattr invokes the setter; getattr invokes the getter.
# Assume integer inputs for this example.
# Keep these intentional errors commented out:
# setattr(order, "quantity", -1)  # ValueError from the property's setter.
# setattr(order, 123, "value")    # TypeError: attribute name must be a string.
# getattr(order, 123)             # TypeError: attribute name must be a string.
# When names come from external input, select allowed fields before assigning:
# arbitrary names could replace methods or other important attributes.


# --- 8. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Exercises using Pizza refer to the class defined in section 1 above.
# Keep intentional-error lines commented out.

# Exercise 1 — Create and update attributes
# Predict both outputs. Which call creates an attribute and which updates one?
# pizza = Pizza({"name": "Margherita"})
# setattr(pizza, "size", "Small")
# setattr(pizza, "name", "Cheese")
# print(pizza.name)
# print(pizza.size)
# ANSWER:


# Exercise 2 — A name stored in a variable
# Predict both outputs. Explain why the assignments target different names.
# pizza = Pizza({"size": "Large"})
# field = "size"
# pizza.field = "Medium"
# setattr(pizza, field, "Small")
# print(pizza.field)
# print(pizza.size)
# ANSWER:


# Exercise 3 — Missing versus false-like values
# Predict all four outputs. Explain when the fallback is used.
# pizza = Pizza({"price": 0, "discounted": False, "rating": None})
# for field in ["price", "discounted", "rating", "diameter"]:
#     print(getattr(pizza, field, "Unknown"))
# What happens if getattr(pizza, "diameter") is called without a default?
# ANSWER:


# Exercise 4 — Return value and stored value
# Predict both outputs. Why should the result not replace the pizza variable?
# pizza = Pizza({})
# result = setattr(pizza, "price", 12)
# print(result)
# print(getattr(pizza, "price"))
# ANSWER:


# Exercise 5 — Shared mutable data
# Predict both lists. Explain why changing first also affects second.
# details = {"ingredients": ["cheese"]}
# first = Pizza(details)
# second = Pizza(details)
# first.ingredients.append("olives")
# print(first.ingredients)
# print(second.ingredients)
# Would replacing first.ingredients with a new list also replace second's list?
# ANSWER:


# Exercise 6 — Write a small attribute exporter
# 1. Define export_attributes(obj, names).
# 2. Build and return a dictionary using each name as a key.
# 3. Get each value with getattr, using "Unknown" when the attribute is missing.
# 4. Test it on a Pizza using names ["name", "price", "diameter"].
# 5. Explain why exporting selected names is different from exporting dir(obj).
# Write your code below:

# ANSWER:


# Optional challenge — Limit dynamic updates to allowed fields
# Work through this one together when you are ready.
# Define update_pizza(pizza, changes) where changes is a dictionary.
# Permit only the names "name", "price", and "size".
# Loop over changes.items(), using setattr only for permitted names.
# Ignore other names and return the number of permitted assignments made.
# No value validation is required for this exercise.
# Write your code below:


# Uncomment these checks after defining your function:
# pizza = Pizza({"name": "Cheese", "price": 10, "size": "Small"})
# count = update_pizza(pizza, {"price": 12, "size": "Large", "rating": 5})
# print(count)                               # => 2
# print(pizza.price)                         # => 12
# print(pizza.size)                          # => Large
# print(getattr(pizza, "rating", "Unknown"))  # => Unknown
# Explain how choosing permitted names limits what a dynamic update can change.
