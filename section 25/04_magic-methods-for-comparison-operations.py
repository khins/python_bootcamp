# magic-methods-for-comparison-operations.py

# ============================================================
# Magic Methods for Comparison and Mathematical Operations
# ============================================================

# In the previous lesson, we learned how __eq__ allows us to
# define what equality means between our custom objects.
#
# Python provides additional magic methods that allow us to
# define how our objects behave with comparison operators:
#
# __gt__  -> greater than >
# __ge__  -> greater than or equal to >=
# __lt__  -> less than <
# __le__  -> less than or equal to <=
#
# We can also define how mathematical operators work:
#
# __add__ -> addition +
# __sub__ -> subtraction -
#
# The logic used by these methods is OUR decision.
# We decide what "greater than", "addition", etc. mean for
# objects created from our class.


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

    def __gt__(self, other_student):
        return self.grades > other_student.grades

    def __le__(self, other_student):
        return self.grades <= other_student.grades

    def __add__(self, other_student):
        return self.grades + other_student.grades

    def __sub__(self, other_student):
        return self.grades - other_student.grades


# ============================================================
# 2. Create Student objects
# ============================================================

bob = Student(90, 90, 90)

moe = Student(100, 90, 80)

joe = Student(40, 45, 50)


# ============================================================
# 3. Practice — Calculate total grades
# ============================================================

# Predict each value BEFORE running.
#
# ANSWER:
#
# bob.grades =>
#
# moe.grades =>
#
# joe.grades =>


print(bob.grades)
print(moe.grades)
print(joe.grades)


# ============================================================
# 4. Understanding __gt__
# ============================================================

# __gt__ means:
#
# greater than
#
# It controls the behavior of:
#
# >
#
# Our method:
#
# def __gt__(self, other_student):
#     return self.grades > other_student.grades
#
#
# Therefore:
#
# moe > joe
#
# conceptually causes Python to use:
#
# moe.__gt__(joe)
#
#
# Inside the method:
#
# self          -> moe
# other_student -> joe


# ============================================================
# 5. Practice — Greater Than
# ============================================================

# Predict the output BEFORE running.
#
# ANSWER:
#
# moe > joe =>
#
# joe > moe =>
#
# bob > joe =>


print(moe > joe)
print(joe > moe)
print(bob > joe)


# ============================================================
# 6. Understanding __le__
# ============================================================

# __le__ means:
#
# less than or equal to
#
# It controls:
#
# <=
#
# Our method:
#
# def __le__(self, other_student):
#     return self.grades <= other_student.grades
#
#
# Therefore:
#
# joe <= bob
#
# compares:
#
# joe.grades <= bob.grades


# ============================================================
# 7. Practice — Less Than or Equal To
# ============================================================

# Predict each result.
#
# ANSWER:
#
# joe <= bob =>
#
# bob <= moe =>
#
# moe <= joe =>


print(joe <= bob)
print(bob <= moe)
print(moe <= joe)


# ============================================================
# 8. Practice — Trace a comparison
# ============================================================

# Consider:
#
# moe > joe
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
# The comparison being performed is:
#
# __________________ > __________________
#
# Therefore __gt__ returns: __________________


# ============================================================
# 9. Understanding __add__
# ============================================================

# Magic methods can also control mathematical operators.
#
# __add__ controls:
#
# +
#
# Our method:
#
# def __add__(self, other_student):
#     return self.grades + other_student.grades
#
#
# Therefore:
#
# bob + moe
#
# conceptually uses:
#
# bob.__add__(moe)
#
#
# In this class, adding students means:
#
# add their TOTAL grades together.


# ============================================================
# 10. Practice — Addition
# ============================================================

# Predict each result BEFORE running.
#
# ANSWER:
#
# bob + moe =>
#
# bob + joe =>
#
# moe + joe =>


print(bob + moe)
print(bob + joe)
print(moe + joe)


# ============================================================
# 11. Understanding __sub__
# ============================================================

# __sub__ controls:
#
# -
#
# Our method:
#
# def __sub__(self, other_student):
#     return self.grades - other_student.grades
#
#
# Therefore:
#
# moe - joe
#
# conceptually uses:
#
# moe.__sub__(joe)


# ============================================================
# 12. Practice — Subtraction
# ============================================================

# Predict each result.
#
# ANSWER:
#
# moe - joe =>
#
# joe - moe =>
#
# bob - moe =>


print(moe - joe)
print(joe - moe)
print(bob - moe)


# ============================================================
# 13. Practice — Direction Matters
# ============================================================

# Compare:
#
# moe - joe
#
# with:
#
# joe - moe
#
#
# ANSWER:
#
# Are the results the same?
#
# ________________________________
#
# Why or why not?
#
# ____________________________________________________________
# ____________________________________________________________


# ============================================================
# 14. Practice — Add __ge__
# ============================================================

# __ge__ means:
#
# greater than or equal to
#
# It controls:
#
# >=
#
# Add the __ge__ method to the class below.


class StudentGE:

    def __init__(self, math, history, writing):
        self.math = math
        self.history = history
        self.writing = writing

    @property
    def grades(self):
        return self.math + self.history + self.writing

    def __ge__(self, other_student):

        # Write your comparison here:
        pass


# ============================================================
# 15. Test __ge__
# ============================================================

student1 = StudentGE(90, 90, 90)
student2 = StudentGE(100, 90, 80)
student3 = StudentGE(40, 45, 50)


# Predict BEFORE running.
#
# ANSWER:
#
# student1 >= student2 =>
#
# student1 >= student3 =>
#
# student3 >= student1 =>


print(student1 >= student2)
print(student1 >= student3)
print(student3 >= student1)


# ============================================================
# 16. Practice — Add __lt__
# ============================================================

# __lt__ means:
#
# less than
#
# It controls:
#
# <
#
# Complete the method below.


class StudentLT:

    def __init__(self, math, history, writing):
        self.math = math
        self.history = history
        self.writing = writing

    @property
    def grades(self):
        return self.math + self.history + self.writing

    def __lt__(self, other_student):

        # Write your comparison here:
        pass


# ============================================================
# 17. Test __lt__
# ============================================================

student1 = StudentLT(90, 90, 90)
student2 = StudentLT(40, 45, 50)


# Predict:
#
# ANSWER:
#
# student1 < student2 =>
#
# student2 < student1 =>


print(student1 < student2)
print(student2 < student1)


# ============================================================
# 18. Practice — Create your own comparison
# ============================================================

# Create two Student objects with different total grades.
#
# Write your code below:




# Use > to compare them.




# ANSWER:
#
# Which student is considered greater?
#
# ___________________________________
#
# Why?
#
# ____________________________________________________________
# ____________________________________________________________


# ============================================================
# 19. Practice — Multiplication
# ============================================================

# The lesson mentions that Python also provides magic methods
# for operations such as multiplication and division.
#
# Research/challenge:
#
# Determine the name of the magic method that controls:
#
# *
#
# ANSWER:
#
# ________________________________
#
#
# Then complete the class below so multiplying two students
# multiplies their total grades.


class MultiplicationStudent:

    def __init__(self, math, history, writing):
        self.math = math
        self.history = history
        self.writing = writing

    @property
    def grades(self):
        return self.math + self.history + self.writing

    # Define the appropriate magic method below:




# ============================================================
# 20. Practice — Division
# ============================================================

# Determine the magic method that controls:
#
# /
#
# ANSWER:
#
# ________________________________
#
#
# How could we define division between two Student objects?
#
# Write your idea below:
#
# ____________________________________________________________
# ____________________________________________________________


# ============================================================
# 21. Operator to Magic Method Review
# ============================================================

# Fill in the missing magic methods:
#
#
# Operator       Magic Method
# --------       ------------
#
# ==             __eq__
#
# >              ______________
#
# >=             ______________
#
# <              ______________
#
# <=             ______________
#
# +              ______________
#
# -              ______________
#
# *              ______________
#
# /              ______________


# ============================================================
# 22. Final Review
# ============================================================

# Fill in the blanks:
#
# 1. __gt__ controls the ______ operator.
#
#
# 2. __le__ controls the ______ operator.
#
#
# 3. __add__ controls the ______ operator.
#
#
# 4. __sub__ controls the ______ operator.
#
#
# 5. Comparison magic methods return a:
#
#    ________________________________
#
#
# 6. When Python evaluates:
#
#       moe > joe
#
#    Python uses the __________________ magic method.
#
#
# 7. When Python evaluates:
#
#       bob + moe
#
#    Python uses the __________________ magic method.
#
#
# 8. In our Student class, "greater than" means that one
#    student's ________________________________ are higher
#    than another student's.
#
#
# 9. In our Student class, adding two students means adding
#    their ________________________________ together.
#
#
# 10. Who decides what addition, subtraction, or comparison
#     means for our custom Student objects?
#
#     ________________________________


# ============================================================
# KEY CONCEPT
# ============================================================

# Magic methods allow our custom Python objects to work with
# Python's normal operators.
#
#
# When we write:
#
#     moe > joe
#
# Python can use:
#
#     moe.__gt__(joe)
#
#
# When we write:
#
#     bob + moe
#
# Python can use:
#
#     bob.__add__(moe)
#
#
# The IMPORTANT idea:
#
# WE define what these operations mean for our objects.
#
# For Student:
#
#     >   compares total grades
#
#     <=  compares total grades
#
#     +   adds total grades
#
#     -   subtracts total grades
#
#
# By defining magic methods, our custom objects can work with
# familiar Python operators such as:
#
# ==   >   <   >=   <=   +   -   *   /