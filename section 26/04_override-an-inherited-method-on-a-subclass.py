# ============================================================
# FILE: override-an-inherited-method-on-a-subclass.py
# TOPIC: Method overriding in Python inheritance
# ============================================================
# LESSON OBJECTIVES
# - Explain method overriding.
# - Distinguish inherited methods from subclass-specific methods.
# - Predict which method Python invokes on each instance.
# - Practice overriding methods in your own subclasses.
#
# HOW TO STUDY:
# Read each section, predict output before running, and complete
# the TODO challenges yourself. Uncomment example calls to test.


# ============================================================
# SECTION 1 — WHAT IS METHOD OVERRIDING?
# ============================================================
# A subclass can define a method with the same name as a method
# in its superclass. This is called method overriding.
#
# When an instance calls a method, Python looks for the method
# through the class inheritance hierarchy. A subclass's own
# implementation takes precedence over an inherited one.
#
# A subclass can also define entirely NEW methods.


# ============================================================
# SECTION 2 — THE PARENT CLASS: Teacher
# ============================================================
class Teacher:
    def teach_class(self):
        print("Teaching stuff")

    def grab_lunch(self):
        print("Yum, yum, yum")

    def grade_tests(self):
        print("F, F, F")


# EXERCISE 1 — PREDICT BEFORE RUNNING
# teacher = Teacher()
# teacher.teach_class()
# teacher.grab_lunch()
# teacher.grade_tests()
#
# ANSWER:
# 1. ______________________________________
# 2. ______________________________________
# 3. ______________________________________


# ============================================================
# SECTION 3 — A SUBCLASS: CollegeProfessor
# ============================================================
class CollegeProfessor(Teacher):
    def publish_book(self):
        print("Hooray, I'm an author")

    def grade_tests(self):
        print("A, A, A")


# CollegeProfessor inherits teach_class() and grab_lunch().
# It defines publish_book() as a new method.
# It OVERRIDES grade_tests() with its own implementation.
#
# EXERCISE 2 — PREDICT BEFORE RUNNING
# professor = CollegeProfessor()
# professor.publish_book()
# professor.grab_lunch()
# professor.teach_class()
# professor.grade_tests()
#
# ANSWER:
# 1. ______________________________________
# 2. ______________________________________
# 3. ______________________________________
# 4. ______________________________________


# ============================================================
# SECTION 4 — SAME METHOD NAME, DIFFERENT BEHAVIOR
# ============================================================
# teacher = Teacher()
# professor = CollegeProfessor()
# teacher.grade_tests()
# professor.grade_tests()
#
# QUESTION 1:
# Which class provides the method used by teacher.grade_tests()?
# ANSWER: _________________________________________________
#
# QUESTION 2:
# Which class provides the method used by professor.grade_tests()?
# ANSWER: _________________________________________________
#
# QUESTION 3:
# Does defining grade_tests() in CollegeProfessor change the
# implementation in Teacher?
# ANSWER: _________________________________________________


# ============================================================
# SECTION 5 — METHOD LOOKUP
# ============================================================
# Simplified lookup for this example:
#
# professor.grade_tests()
#      |
#      v
# CollegeProfessor defines grade_tests()? YES -> use it
#      |
#      +-- If NO, search Teacher
#
# professor.grab_lunch()
#      |
#      v
# CollegeProfessor defines grab_lunch()? NO
#      |
#      v
# Teacher defines grab_lunch()? YES -> use it
#
# QUESTION 4:
# Why can professor.grab_lunch() work without a definition
# of grab_lunch() in CollegeProfessor?
# ANSWER: _________________________________________________
# _________________________________________________________


# ============================================================
# SECTION 6 — INHERITANCE DOES NOT WORK BACKWARD
# ============================================================
# A Teacher instance does not gain publish_book(), which is
# defined only in CollegeProfessor.
#
# EXERCISE 3 — PREDICT THE RESULT
# teacher = Teacher()
# teacher.publish_book()
#
# What exception do you expect?
# ANSWER: _________________________________________________
#
# Leave the failing call commented out while running other work.


# ============================================================
# SECTION 7 — CODING CHALLENGE: Employee AND Manager
# ============================================================
# TODO:
# 1. Create an Employee class with work() that prints "Working".
# 2. Create Manager(Employee).
# 3. Override work() in Manager to print "Managing work".
# 4. Add a new Manager method approve_budget() that prints
#    "Budget approved".
# 5. Create one object of each class and call their methods.
#
# YOUR CODE BELOW:
#
# class Employee:
#     pass
#
# class Manager(Employee):
#     pass
#
# Predict output before testing:
# ANSWER: _________________________________________________


# ============================================================
# SECTION 8 — CODING CHALLENGE: MULTIPLE OVERRIDES
# ============================================================
# TODO:
# Create a subclass FriendlyProfessor(Teacher).
# Override BOTH grade_tests() and grab_lunch().
# Keep teach_class() inherited without redefining it.
#
# Suggested messages:
# grade_tests() -> "Everyone gets feedback"
# grab_lunch() -> "Lunch with students"
#
# YOUR CODE BELOW:
#
# class FriendlyProfessor(Teacher):
#     pass
#
# Test all three methods and explain where each comes from.
# ANSWER: _________________________________________________
# _________________________________________________________


# ============================================================
# SECTION 9 — TRACE THE METHOD SOURCE
# ============================================================
# For each call, write either Teacher or CollegeProfessor.
#
# professor = CollegeProfessor()
#
# professor.teach_class()  -> ___________________________
# professor.grab_lunch()   -> ___________________________
# professor.grade_tests()  -> ___________________________
# professor.publish_book() -> ___________________________
#
# Which of these methods is OVERRIDDEN?
# ANSWER: _________________________________________________
#
# Which method is NEW to the subclass?
# ANSWER: _________________________________________________


# ============================================================
# SECTION 10 — FINAL REVIEW
# ============================================================
# Fill in the blanks:
#
# 1. Defining a different implementation of a parent method
#    on a subclass is called method ____________________.
#
# 2. A class that is inherited from is called the __________
#    or superclass.
#
# 3. A more specialized class is called a __________________.
#
# 4. Python checks the subclass's implementation before
#    continuing to its __________________ in this example.
#
# 5. A subclass can both inherit existing methods and define
#    __________________ methods.
#
# 6. An object of the superclass does NOT automatically gain
#    methods defined only on a __________________.
#
# 7. In this lesson, CollegeProfessor overrides ____________.
#
# 8. The method unique to CollegeProfessor is ______________.


# ============================================================
# SECTION 11 — KEY TAKEAWAYS
# ============================================================
# - Inheritance lets a subclass reuse superclass behavior.
# - A subclass can add new methods.
# - A subclass can override inherited methods by defining
#   a method with the same name.
# - Teacher.grade_tests and CollegeProfessor.grade_tests are
#   separate implementations.
# - Method overriding does not modify the parent class.
# - Inheritance is useful when the subclass IS A more
#   specialized kind of the superclass.
#
# NEXT TOPIC TO WATCH FOR:
# Python's super() can help a subclass call behavior from
# a superclass. It is not required for this introductory lesson.
# ============================================================
# END OF LESSON
# ============================================================
