# equality-with-the-__eq__-method.py

# ============================================================
# __eq__ — Defining Equality Between Custom Objects
# ============================================================

# Python does not automatically know which attributes of our
# custom objects should determine whether two objects are equal.
#
# We can define our own equality rules using:
#
# __eq__()
#
# __eq__ is a "dunder" (double underscore) method.
#
# It should return a Boolean:
#
# True  -> the objects are considered equal
# False -> the objects are considered unequal


# ============================================================
# 1. Create the Student class
# ============================================================

class Student:

    def __init__(self, math, history, writing):
        self.math = math
        self.history = history
        self.writing = writing

    @property
    def grades(self):
        return self.math + self.history + self.writing

    def __eq__(self, other_student):
        return self.grades == other_student.grades


# ============================================================
# 2. Create Student objects
# ============================================================

bob = Student(90, 90, 90)
moe = Student(100, 90, 80)
joe = Student(40, 45, 50)


# ============================================================
# 3. Practice — Calculate the grades
# ============================================================

# Before running these, predict the output.
#
# ANSWER:
# bob.grades =>
# moe.grades =>
# joe.grades =>

print(bob.grades)
print(moe.grades)
print(joe.grades)


# ============================================================
# 4. Understanding __eq__
# ============================================================

# When Python sees:
#
# bob == moe
#
# Python uses the __eq__ method that we defined.
#
# Conceptually:
#
# bob.__eq__(moe)
#
# Inside __eq__:
#
# self          -> bob
# other_student -> moe
#
# The method compares:
#
# bob.grades == moe.grades


# ============================================================
# 5. Practice — Predict equality
# ============================================================

# Predict each result BEFORE running the code.

# ANSWER:
# bob == moe =>
# moe == bob =>
# bob == joe =>
# moe == joe =>

print(bob == moe)
print(moe == bob)
print(bob == joe)
print(moe == joe)


# ============================================================
# 6. Practice — Predict inequality
# ============================================================

# Defining equality also allows us to test inequality.
#
# Predict the results.

# ANSWER:
# bob != joe =>
# joe != moe =>
# bob != moe =>

print(bob != joe)
print(joe != moe)
print(bob != moe)


# ============================================================
# 7. Practice — Trace __eq__
# ============================================================

# Consider:
#
# bob == moe
#
# Fill in the blanks:
#
# ANSWER:
#
# self refers to: __________________
#
# other_student refers to: __________________
#
# self.grades equals: __________________
#
# other_student.grades equals: __________________
#
# Therefore __eq__ returns: __________________


# ============================================================
# 8. Practice — Different grades, equal students?
# ============================================================

# Bob:
#
# Math    = 90
# History = 90
# Writing = 90
#
# Moe:
#
# Math    = 100
# History = 90
# Writing = 80
#
# Their individual grades are different.
#
# Why does the __eq__ method still consider them equal?
#
# ANSWER:
#
# ____________________________________________________________
# ____________________________________________________________
# ____________________________________________________________


# ============================================================
# 9. Practice — Create your own students
# ============================================================

# Create two Student objects with DIFFERENT individual grades
# but the SAME total grade.

# Write your code below:




# Print both students' grades.




# Compare the students using ==.




# ANSWER:
# Are they equal? __________________
#
# Why?
# ____________________________________________________________
# ____________________________________________________________


# ============================================================
# 10. Practice — Create unequal students
# ============================================================

# Create two students whose total grades are different.

# Write your code below:




# Compare them using ==.




# ANSWER:
# Expected result: __________________


# ============================================================
# 11. Practice — Change the equality rule
# ============================================================

# Currently students are equal when their TOTAL grades are equal:
#
# return self.grades == other_student.grades
#
# Imagine instead that students should only be equal when ALL
# three individual grades match.
#
# Complete the new __eq__ method below.
#
# Do not change the original Student class above.


class ExactStudent:

    def __init__(self, math, history, writing):
        self.math = math
        self.history = history
        self.writing = writing

    def __eq__(self, other_student):

        # Write your equality comparison here:
        pass


# ============================================================
# 12. Test ExactStudent
# ============================================================

student1 = ExactStudent(90, 90, 90)
student2 = ExactStudent(100, 90, 80)
student3 = ExactStudent(90, 90, 90)

# Predict BEFORE running.

# ANSWER:
# student1 == student2 =>
# student1 == student3 =>

print(student1 == student2)
print(student1 == student3)


# ============================================================
# 13. Final Review
# ============================================================

# Fill in the blanks:
#
# 1. __eq__ is used to define _______________________________.
#
# 2. The first parameter, self, represents _________________.
#
# 3. The second parameter represents _______________________.
#
# 4. __eq__ should return a ________________________________.
#
# 5. If __eq__ returns True, the objects are considered
#    ________________________________.
#
# 6. If __eq__ returns False, the objects are considered
#    ________________________________.
#
# 7. When Python evaluates:
#
#       bob == moe
#
#    Python uses the __________________ method defined
#    in the Student class.
#
# 8. In this lesson, two Student objects are considered equal
#    when their __________________________________ are equal.


# ============================================================
# KEY CONCEPT
# ============================================================

# __eq__ allows OUR CLASS to define what "equal" means.
#
# For the Student class:
#
#     bob == moe
#
# eventually compares:
#
#     bob.grades == moe.grades
#
# Therefore, two Student objects can contain different individual
# grades and still be considered equal if their total grades are
# the same.