# Class attributes — Study Summary
# Instructor summary:
# - An assignment in the class body creates a class attribute.
# - Access it through ClassName.attribute without creating an instance first.
# - Class attributes hold data associated with the class rather than one instance.
# - A shared counter can record how many instances have been initialized.
# - Use Counter.count inside an instance method to update this class's counter.
# - A class method receives cls and can access class attributes through cls.
# - Creating instances inside a factory runs __init__ for each new instance.
# - Instances can read class attributes through ordinary attribute lookup.
# - A shared mutable class attribute is one object, not a copy per instance.
#
# Clarifications to the transcript:
# - Class attributes are not module-level global variables; they belong to a class.
# - For the ordinary data attributes here, an instance's own attribute takes
#   precedence over an attribute of the same name found on its class.
# - Assigning instance.count normally creates or updates an instance attribute;
#   it does not reassign Counter.count.
# - Counter.count += 1 reassigns the class attribute to a new integer value;
#   integers themselves are immutable.
# - Bare count += 1 inside __init__ treats count as local and would raise
#   UnboundLocalError when that local value has not been assigned.
# - This counter records initializer calls, not the number of currently living
#   objects. Deleting an instance does not automatically decrease it.
# - Explicitly calling __init__ again would also increment this simple counter.
# - An instance method can use type(self) to obtain its class, but updating
#   type(self).count can behave differently for subclasses than Counter.count.
# - Counter.count below deliberately updates the named Counter class. It is
#   not a separate counter for every subclass.
# - Shared mutable data is useful when intentional; use instance attributes
#   when each object should have its own list or dictionary.


# --- 1. Define a class attribute and update it during initialization ---
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def create_two(cls):
        two_counters = [cls(), cls()]
        print(f"New number of counter objects created: {cls.count}")
        return two_counters


print(Counter.count)  # => 0
# count is already available on the class; no Counter instance exists yet.
# The assignment count = 0 runs when the class body is executed, not each time
# an instance is created.

c1 = Counter()
print(Counter.count)  # => 1
# __init__ updates the class attribute rather than assigning self.count.


# --- 2. Create two instances through a class method ---
c2, c3 = Counter.create_two()
# => New number of counter objects created: 3
print(Counter.count)  # => 3
print(c2 is c3)      # => False
# cls() runs twice, so the initializer increments the counter twice.
# Do not increment count again in create_two: that would double-count creation.
# The returned list contains two separate instances, unpacked into c2 and c3.
# cls.count reads the attribute through the class supplied to the factory.


# --- 3. Read the class attribute through instances ---
print(c1.count)  # => 3
print(c2.count)  # => 3
print(c3.count)  # => 3
print(vars(c1))  # => {}
# None of these instances has its own count attribute, so lookup finds the
# class attribute. Reading c1.count does not copy count into the instance.
# vars(c1) shows this ordinary instance's stored attributes, not class data.

c4 = Counter()
print(Counter.count)  # => 4
print(c1.count)       # => 4
print(c2.count)       # => 4
# Existing instances see the updated class value when they look it up again.


# --- 4. Preview: instance assignment can shadow a class attribute ---
c1.count = 99
print(c1.count)       # => 99
print(Counter.count)  # => 4
print(c2.count)       # => 4
print(vars(c1))       # => {'count': 99}
# c1 now has its own count, which hides the class value during ordinary lookup.
# This assignment did not change the shared counter.

del c1.count
print(c1.count)  # => 4
# Removing the instance attribute reveals the class attribute again.
# This is a preview of attribute lookup, explored further in the next lesson.
# Using self.count += 1 in __init__ would likewise assign an instance attribute
# for this integer example, rather than updating Counter.count.


# --- 5. A shared mutable class attribute refers to one object ---
class SharedNotebook:
    notes = []


first_notebook = SharedNotebook()
second_notebook = SharedNotebook()
first_notebook.notes.append("Review class attributes")
print(second_notebook.notes)  # => ['Review class attributes']
print(SharedNotebook.notes)  # => ['Review class attributes']
print(first_notebook.notes is second_notebook.notes)  # => True
# append mutates the shared list found through lookup; it does not assign a
# new notes attribute to first_notebook.

first_notebook.notes = ["Personal note"]
print(first_notebook.notes)   # => ['Personal note']
print(second_notebook.notes)  # => ['Review class attributes']
# Reassignment creates an instance attribute here. Mutation and reassignment
# are different operations, even though both can use instance.notes syntax.


# --- 6. Use instance attributes for independent mutable data ---
class PersonalNotebook:
    def __init__(self):
        self.notes = []


first_personal = PersonalNotebook()
second_personal = PersonalNotebook()
first_personal.notes.append("Practice Python")
print(first_personal.notes)   # => ['Practice Python']
print(second_personal.notes)  # => []
print(first_personal.notes is second_personal.notes)  # => False
# Each initializer call evaluates [] again and stores a new list on that instance.
# Choose class or instance storage based on whether the data should be shared.


# --- 7. Distinguish total creations from currently referenced objects ---
print(Counter.count)  # => 4
c5 = Counter()
print(Counter.count)  # => 5

del c5
print(Counter.count)  # => 5
# del removes the variable binding; it does not undo the initializer's increment.
# This counter is not a live-object tracker and has no automatic decrement.
# Manually assigning Counter.count = 0 would reset the stored number without
# removing any existing instances, so it would no longer be a lifetime total.


# --- 8. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Use the separate classes below so answers do not depend on Counter's running
# total from earlier examples. Keep intentional-error lines commented out.

# Exercise 1 — Read a shared class attribute
# Predict all three outputs. Does reading kind create an instance attribute?
# class Pet:
#     kind = "animal"
#
# first = Pet()
# second = Pet()
# print(Pet.kind)
# print(first.kind)
# print(vars(second))
# ANSWER:


# Exercise 2 — Trace a creation counter
# Predict all three outputs. How often does the initializer run?
# class Ticket:
#     count = 0
#
#     def __init__(self):
#         Ticket.count += 1
#
# print(Ticket.count)
# first = Ticket()
# second = Ticket()
# print(Ticket.count)
# print(first.count)
# ANSWER:


# Exercise 3 — Class assignment versus instance assignment
# Predict all three outputs. Which object owns each label after assignment?
# class Label:
#     text = "default"
#
# first = Label()
# second = Label()
# first.text = "personal"
# Label.text = "updated"
# print(first.text)
# print(second.text)
# del first.text
# print(first.text)
# ANSWER:


# Exercise 4 — Shared list or separate lists?
# Predict both outputs. Rewrite the class to give each instance its own list.
# class Team:
#     members = []
#
# first = Team()
# second = Team()
# first.members.append("Ada")
# print(first.members)
# print(second.members)
# ANSWER:


# Exercise 5 — Diagnose the wrong counter target
# Predict both outputs. Explain why self.count += 1 does not update the class.
# class LocalCounter:
#     count = 0
#
#     def __init__(self):
#         self.count += 1
#
# first = LocalCounter()
# second = LocalCounter()
# print(LocalCounter.count)
# print(first.count, second.count)
# Rewrite the initializer to increment the class attribute instead.
# ANSWER:


# Exercise 6 — Combine a class attribute and a factory
# 1. Define Book with a class attribute created = 0.
# 2. In __init__(self, title), store title on the instance and increment
#    Book.created by one.
# 3. Add @classmethod above sample_pair(cls).
# 4. Return [cls("Sample A"), cls("Sample B")].
# 5. Create one book directly, then unpack the result of Book.sample_pair().
# 6. Print Book.created and all three titles.
# 7. Explain why the factory does not need an additional counter increment.
# Write your code below:

# ANSWER:


# Optional challenge — Assign each instance an identifier
# Work through this one together when you are ready.
# Define Order with a class attribute next_id = 1.
# Its initializer should accept item, store it on the instance, and copy the
# current Order.next_id into self.order_id. Then increment Order.next_id.
# Create three orders and verify that each retains its own identifier even
# after the class counter changes. No inheritance is required for this exercise.
# Write your code below:


# Uncomment these checks after defining your class:
# first = Order("tea")
# second = Order("coffee")
# third = Order("juice")
# print(first.order_id)   # => 1
# print(second.order_id)  # => 2
# print(third.order_id)   # => 3
# print(Order.next_id)    # => 4
# print(first.order_id)   # => 1
# Explain why order_id belongs on each instance while next_id belongs on Order.
