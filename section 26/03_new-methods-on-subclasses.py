# ============================================================
# FILE: new-methods-on-subclasses.py
# TOPIC: Extending a superclass with new subclass methods
# ============================================================
# LESSON OBJECTIVES
# - Recognize an "is-a" relationship: Manager is an Employee.
# - Inherit existing behavior without rewriting it.
# - Add methods that are available only to specialized subclasses.
# - Trace a three-level inheritance hierarchy.
# - Predict which method calls succeed or raise AttributeError.
#
# INSTRUCTIONS: Predict outputs before running each section.
# Uncomment one exercise at a time and complete the TODO challenges.

# ============================================================
# SECTION 1 — THE EMPLOYEE SUPERCLASS
# ============================================================
class Employee:
    def do_work(self):
        print("I'm working")


# Try this first:
# e = Employee()
# e.do_work()
#
# PREDICT THE OUTPUT:
# ANSWER: ___________________________________________

# ============================================================
# SECTION 2 — A MANAGER ADDS A NEW METHOD
# ============================================================
class Manager(Employee):
    def waste_time(self):
        print("Wow, this YouTube video looks fun")


# Manager inherits do_work() and defines waste_time().
# m = Manager()
# m.do_work()
# m.waste_time()
#
# PREDICT THE TWO OUTPUT LINES:
# 1. _________________________________________________
# 2. _________________________________________________
#
# EXPLAIN: Why does m.do_work() work when Manager does not
# define do_work() directly?
# ANSWER: ___________________________________________

# ============================================================
# SECTION 3 — INHERITANCE DOES NOT WORK IN REVERSE
# ============================================================
# e = Employee()
# e.waste_time()  # Uncomment ONLY to observe the exception.
#
# QUESTION: What exception type will this raise?
# ANSWER: ___________________________________________
#
# QUESTION: Why does an Employee not gain methods added
# specifically to Manager?
# ANSWER: ___________________________________________

# ============================================================
# SECTION 4 — A DIRECTOR IS A TYPE OF MANAGER
# ============================================================
class Director(Manager):
    def fire_employee(self):
        print("You're fired")


# Hierarchy:
# Employee
#    |
# Manager
#    |
# Director
#
# d = Director()
# d.do_work()
# d.waste_time()
# d.fire_employee()
#
# PREDICT ALL THREE OUTPUT LINES:
# 1. _________________________________________________
# 2. _________________________________________________
# 3. _________________________________________________
#
# QUESTION: Which class defines each method?
# do_work: ___________________________________________
# waste_time: ________________________________________
# fire_employee: _____________________________________

# ============================================================
# SECTION 5 — WHICH OBJECT CAN CALL WHICH METHOD?
# ============================================================
# Complete the table with YES or NO before testing.
#
#                        Employee    Manager    Director
# do_work()              ________    _______    ________
# waste_time()           ________    _______    ________
# fire_employee()        ________    _______    ________
#
# Uncomment to experiment with the valid calls:
# e = Employee()
# m = Manager()
# d = Director()
# e.do_work()
# m.do_work()
# m.waste_time()
# d.do_work()
# d.waste_time()
# d.fire_employee()
#
# These should fail; uncomment ONE at a time:
# e.waste_time()
# e.fire_employee()
# m.fire_employee()

# ============================================================
# SECTION 6 — TRACE METHOD LOOKUP
# ============================================================
# When Python evaluates d.do_work(), it searches for the
# attribute through the instance and class inheritance chain.
# In this example it can find do_work on Employee.
#
# FILL IN THE LOOKUP PATH:
# d.fire_employee():  Director -> _____________________
# d.waste_time():     Director -> _____________________
# d.do_work():        Director -> _________ -> _________
#
# QUESTION: Does Manager have to redefine do_work()?
# ANSWER: ___________________________________________

# ============================================================
# SECTION 7 — CODING CHALLENGE 1: ADD A TEAM LEAD
# ============================================================
# Create TeamLead as a subclass of Employee.
# Add an instance method assign_task() that prints:
# "Assigning a task"
# Do NOT copy do_work() into TeamLead.

class TeamLead(Employee):
    # TODO: define assign_task(self)
    pass


# After completing the class, uncomment:
# lead = TeamLead()
# lead.do_work()
# lead.assign_task()
#
# PREDICT THE OUTPUT:
# 1. _________________________________________________
# 2. _________________________________________________

# ============================================================
# SECTION 8 — CODING CHALLENGE 2: ANOTHER THREE-LEVEL CHAIN
# ============================================================
# Create a class named SeniorDirector that inherits Director.
# Give it a method approve_budget() that prints:
# "Budget approved"
# Then create an instance and call all FOUR available methods.
#
# TODO: Write SeniorDirector below.
#
# class SeniorDirector(...):
#     ...
#
# TODO: Instantiate it and call its methods.
#
# QUESTION: Which three methods should SeniorDirector inherit?
# ANSWER: ___________________________________________

# ============================================================
# SECTION 9 — CODING CHALLENGE 3: MUSIC CLASS HIERARCHY
# ============================================================
# Apply the same pattern to a different "is-a" relationship.
#
# 1. Define Instrument with a play() method that prints
#    "Playing an instrument".
# 2. Define Guitar(Instrument) with a tune() method that prints
#    "Tuning the guitar".
# 3. Define ElectricGuitar(Guitar) with a distortion() method
#    that prints "Distortion on".
# 4. Create an ElectricGuitar and call all three methods.
# 5. Explain why a plain Instrument cannot call distortion().
#
# WRITE YOUR CODE BELOW:


# ============================================================
# SECTION 10 — FINAL REVIEW
# ============================================================
# 1. A superclass is also called a ________ class.
# 2. A subclass is also called a ________ class.
# 3. Manager(Employee) means Manager ________ from Employee.
# 4. Inheritance models an "________-a" relationship.
# 5. A subclass can add ________ methods of its own.
# 6. Does Employee automatically inherit Manager methods? ______
# 7. Does Director inherit Employee.do_work()? ______
# 8. Calling a missing method typically raises ________.
# 9. What keyword can leave a class body empty? ________
# 10. What is the advantage of inheriting do_work() rather than
#     copying it into Manager and Director?
#     ___________________________________________________
#
# KEY TAKEAWAY:
# A subclass receives behavior from its parent class and can
# extend that behavior. The parent does not gain methods that
# are defined only in the child class.
# ============================================================
# END OF LESSON
# ============================================================
