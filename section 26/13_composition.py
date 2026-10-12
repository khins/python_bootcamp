# ============================================================
# FILE: 13_composition.py
# TOPIC: Composition and Delegating Responsibilities
# ============================================================
# OBJECTIVES
# - Distinguish "is a" relationships from "has a" relationships.
# - Store custom objects in another object's attributes.
# - Delegate work through methods instead of reaching into storage details.
# - Separate responsibilities among Paper, Briefcase, and Lawyer.
# - Trace how collaborating objects create, store, and retrieve notes.
#
# STUDY SUMMARY
# - Inheritance models "is a": a Superhero is a Person.
# - Composition models "has a": a Lawyer has a Briefcase.
# - An attribute can refer to another custom object, not just built-in values.
# - Delegation means asking another object to carry out some responsibility.
# - A Paper holds note text and its associated case identifier.
# - A Briefcase stores papers and retrieves their text.
# - A Lawyer creates notes and delegates their storage to a briefcase.
# - A consistent method interface lets storage details change independently.
#
# CLARIFICATIONS TO THE TRANSCRIPT
# - Passing an object into __init__ stores a reference here, not a copy.
# - self.papers = [] creates a new, mutable list for each Briefcase instance;
#   the list is not a constant or a list shared by all briefcases.
# - Lawyer.view_notes must RETURN the briefcase's result to pass it back
#   to the caller. Calling the method without return would yield None.
# - Lawyer still knows about Paper because write_note constructs one.
#   It does not need to know how Briefcase stores those Paper objects.
# - Composition reduces dependence on implementation details; it does not
#   remove all dependencies between the collaborating classes.
# - "Prefer composition" is guidance, not a ban on inheritance. Choose the
#   relationship that matches the model and the behavior callers need.
# - Small classes help when they have clear responsibilities; size alone
#   does not guarantee a good design.
# - This lesson uses composition broadly for objects working through stored
#   references. Python does not enforce exclusive ownership or shared lifetimes.


# ============================================================
# SECTION 1 — A PAPER STORES ONE NOTE
# ============================================================
class Paper:
    def __init__(self, text, case):
        self.text = text
        self.case = case


# text holds the note's contents.
# case holds the identifier of the legal case associated with the note.
# Paper does not decide where papers are stored or who owns the briefcase.


# ============================================================
# SECTION 2 — A BRIEFCASE MANAGES ITS PAPERS
# ============================================================
class Briefcase:
    def __init__(self, price):
        self.price = price
        self.papers = []

    def add_paper(self, paper):
        self.papers.append(paper)

    def view_notes(self):
        return [paper.text for paper in self.papers]


# add_paper expects an object with the Paper interface used in this example.
# view_notes returns a new list of text values in the papers' stored order.
# It returns text, not the Paper objects or their case identifiers.
# With no papers, the comprehension returns an empty list.
#
# Briefcase itself delegates ordered storage to a built-in list.
# The list already knows how to append and iterate over items.


# ============================================================
# SECTION 3 — A LAWYER DELEGATES TO A BRIEFCASE
# ============================================================
class Lawyer:
    def __init__(self, name, briefcase):
        self.name = name
        self.briefcase = briefcase

    def write_note(self, text, case):
        paper = Paper(text, case)
        self.briefcase.add_paper(paper)

    def view_notes(self):
        return self.briefcase.view_notes()


# Lawyer has a Briefcase; it does not inherit from Briefcase.
# A lawyer is not a kind of briefcase.
#
# Lawyer uses these methods on its collaborator:
# - add_paper(paper)
# - view_notes()
#
# It does not append directly to self.briefcase.papers.
# Keeping that operation inside Briefcase lets Briefcase manage its storage.


# ============================================================
# SECTION 4 — CONNECT THE OBJECTS
# ============================================================
cheap_briefcase = Briefcase(19.99)
vinnie = Lawyer("Vincent", cheap_briefcase)

print(vinnie.name)                         # => Vincent
print(vinnie.briefcase.price)              # => 19.99
print(vinnie.briefcase is cheap_briefcase)  # => True
print(vinnie.view_notes())                 # => []

# The two references point to the SAME Briefcase object.
# Lawyer.__init__ did not create or copy a briefcase.
#
# Object relationships:
# vinnie (Lawyer)
#     briefcase -> cheap_briefcase (Briefcase)
#                      papers -> list of Paper objects


# ============================================================
# SECTION 5 — WRITE AND VIEW NOTES
# ============================================================
vinnie.write_note("My client is innocent.", "AS2ZK1")
vinnie.write_note("There is no evidence of a crime.", "AS2ZK1")

print(vinnie.view_notes())
# => ['My client is innocent.', 'There is no evidence of a crime.']

# Writing a note:
# 1. Lawyer.write_note receives the text and case identifier.
# 2. It creates a Paper object.
# 3. It passes that object to Briefcase.add_paper.
# 4. Briefcase appends the paper to its internal list.
#
# Viewing notes:
# 1. Lawyer.view_notes calls Briefcase.view_notes.
# 2. Briefcase collects each stored paper's text into a new list.
# 3. Lawyer returns that list to the caller.
# 4. print() displays the list.
#
# The case identifier is stored but not used to filter notes yet.


# ============================================================
# SECTION 6 — KEEP STORAGE DETAILS INSIDE THE BRIEFCASE
# ============================================================
# Inside Lawyer.write_note, use the collaborator's method:
# self.briefcase.add_paper(paper)
#
# Reaching through to the storage would look like this:
# self.briefcase.papers.append(paper)
#
# That second version assumes the briefcase exposes a list named papers.
# If its storage changes, Lawyer would also need to change.
# Delegating through add_paper lets Briefcase handle that change internally.
#
# Likewise, Lawyer asks for view_notes() instead of building its own
# comprehension over the briefcase's internal collection.
# Any replacement must preserve the behavior callers expect, including
# storing multiple notes for the same case and returning their text.


# ============================================================
# SECTION 7 — SEPARATE BRIEFCASES HAVE SEPARATE CONTENTS
# ============================================================
second_briefcase = Briefcase(49.99)
maya = Lawyer("Maya", second_briefcase)

maya.write_note("Review the witness statement.", "BX104")

print(maya.view_notes())
# => ['Review the witness statement.']
print(vinnie.view_notes())
# => ['My client is innocent.', 'There is no evidence of a crime.']
print(maya.briefcase is vinnie.briefcase)  # => False
# Each Briefcase created its own list in __init__.


# ============================================================
# SECTION 8 — SHARED REFERENCES MEAN SHARED CONTENTS
# ============================================================
shared_briefcase = Briefcase(29.99)
alex = Lawyer("Alex", shared_briefcase)
sam = Lawyer("Sam", shared_briefcase)

alex.write_note("Prepare the case timeline.", "CX200")

print(sam.view_notes())  # => ['Prepare the case timeline.']
print(alex.briefcase is sam.briefcase)  # => True
# Both lawyers refer to the same briefcase, so both see its notes.
# Whether sharing is appropriate is a choice for the program's design.
# Passing a collaborator into __init__ does not automatically make it private.


# ============================================================
# SECTION 9 — PRACTICE: PREDICT, EXPLAIN, THEN RUN
# ============================================================
# Write predictions in ANSWER comments before uncommenting the examples.

# EXERCISE 1 — IS A OR HAS A?
# Classify each relationship as inheritance or composition:
# 1. A Lawyer has a Briefcase.
# 2. A Superhero is a Person.
# 3. A Briefcase has a list of Paper objects.
# 4. A GuideDog is a Dog.
# ANSWER:


# EXERCISE 2 — MATCH RESPONSIBILITIES
# Which class handles each task in this lesson?
# 1. Stores text and a case identifier for one note.
# 2. Appends a paper to the storage collection.
# 3. Creates a paper when someone writes a note.
# 4. Extracts the text from all stored papers.
# ANSWER:


# EXERCISE 3 — PREDICT THE NOTES
# bag = Briefcase(10.00)
# lawyer = Lawyer("Taylor", bag)
# print(lawyer.view_notes())
# lawyer.write_note("Call the witness.", "D100")
# lawyer.write_note("Check the dates.", "D200")
# print(lawyer.view_notes())
# Does view_notes filter by case identifier?
# ANSWER:


# EXERCISE 4 — EXPLAIN THE RETURN
# What would print(vinnie.view_notes()) display if Lawyer.view_notes
# called self.briefcase.view_notes() but omitted the return keyword?
# Would that omission remove the notes from the briefcase?
# ANSWER:


# EXERCISE 5 — TRACE A SHARED OBJECT
# bag = Briefcase(20.00)
# first = Lawyer("First", bag)
# second = Lawyer("Second", bag)
# second.write_note("Bring the documents.", "E300")
# print(first.view_notes())
# Why can first see a note written through second?
# ANSWER:


# EXERCISE 6 — ADD CASE FILTERING
# Add a notes_for_case(case) method to Briefcase that returns only the
# text of papers whose case attribute matches the argument.
# Add a Lawyer method with the same name that delegates to the briefcase.
# Test with notes for two case identifiers and one identifier with no notes.
# Keep the filtering logic inside Briefcase.
# Write your code below:


# OPTIONAL CHALLENGE — REUSE THE COLLABORATOR
# Create a Reporter class with a name and a Briefcase object.
# Give it methods to create and view notes using the existing Paper and
# Briefcase classes. Use story identifiers in the case field for this exercise.
# Do not copy the briefcase's storage or note-extraction logic into Reporter.
# Explain which behavior was reused through composition.
# ANSWER:


# ============================================================
# SECTION 10 — FINAL REVIEW
# ============================================================
# 1. Inheritance models an "__________" relationship.
# 2. Composition models a "__________" relationship.
# 3. Asking a stored object to perform work is called __________.
# 4. Which two Briefcase methods does Lawyer rely on?
# 5. Why should Lawyer avoid calling briefcase.papers.append directly?
# 6. Does assigning self.briefcase = briefcase copy the object?
# 7. What happens when two lawyers share the same briefcase?
# 8. Does composition remove every dependency between classes?
# ANSWER:
