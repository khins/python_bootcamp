# ============================================================
# FILE: 11_multiple-inheritance-III.py
# TOPIC: Diamond Inheritance and Shared Ancestors
# ============================================================
# OBJECTIVES
# - Recognize a diamond-shaped inheritance hierarchy.
# - Trace method lookup when two parents share a common ancestor.
# - Explain why a sibling's override can precede an inherited method.
# - Inspect the MRO and predict the effect of reversing direct bases.
#
# STUDY SUMMARY
# - Diamond inheritance occurs when two branches share a common ancestor.
# - Director and Screenwriter both inherit from Filmmaker.
# - JackOfAllTrades inherits from both Director and Screenwriter.
# - Python computes one method resolution order (MRO) for the class.
# - Each ancestor appears only once in that order.
# - For the ordinary methods here, lookup selects the first definition
#   found along the instance's class MRO.
# - Changing base-class order can change the MRO without changing the output.
#
# CLARIFICATIONS TO THE TRANSCRIPT
# - Python uses C3 linearization, not depth-first search followed by
#   deleting earlier occurrences of duplicate classes.
# - That duplicate-removal shortcut happens to predict this example,
#   but it is not a general algorithm for Python's MRO.
# - C3 preserves the declared order of direct bases and the relative
#   order established by the parents' MROs.
# - Here, Filmmaker must come after both Director and Screenwriter.
# - Shared ancestors are not simply moved to the very end; they occupy
#   positions consistent with the inheritance ordering requirements.
# - The MRO is computed when the class is created, not rebuilt for each call.
# - .mro() returns class objects, not strings. __mro__ is a tuple of classes.


# ============================================================
# SECTION 1 — DEFINE THE COMMON ANCESTOR
# ============================================================
class Filmmaker:
    def give_interview(self):
        print("I love making movies.")


# Filmmaker provides the general version of give_interview.
# Both branches below inherit from this same class.


# ============================================================
# SECTION 2 — DEFINE THE TWO BRANCHES
# ============================================================
class Director(Filmmaker):
    pass


class Screenwriter(Filmmaker):
    def give_interview(self):
        print("I love writing scripts.")


Director().give_interview()      # => I love making movies.
Screenwriter().give_interview()  # => I love writing scripts.
# Director inherits the general method without overriding it.
# Screenwriter defines its own version.


# ============================================================
# SECTION 3 — COMPLETE THE DIAMOND
# ============================================================
class JackOfAllTrades(Director, Screenwriter):
    pass


#             Filmmaker
#             /       \
#       Director     Screenwriter
#             \       /
#           JackOfAllTrades
#
# The diagram shows direct inheritance relationships.
# Filmmaker also inherits from object, omitted here for readability.
# There is one shared Filmmaker class, not a separate copy for each branch.

stallone = JackOfAllTrades()
stallone.give_interview()  # => I love writing scripts.


# ============================================================
# SECTION 4 — TRACE THE ACTUAL MRO
# ============================================================
print([cls.__name__ for cls in JackOfAllTrades.mro()])
# => ['JackOfAllTrades', 'Director', 'Screenwriter', 'Filmmaker', 'object']

# Lookup for stallone.give_interview proceeds as follows:
# 1. JackOfAllTrades has no definition of give_interview.
# 2. Director has no definition of give_interview.
# 3. Screenwriter defines it, so that implementation is selected.
#
# Python does not perform a separate lookup through Director's ancestors
# before returning to the rest of JackOfAllTrades' MRO.
# Director inherits Filmmaker's method, but does not define its own copy.
#
# self inside Screenwriter.give_interview refers to stallone.
# That object is still a JackOfAllTrades instance.
print(isinstance(stallone, Director))      # => True
print(isinstance(stallone, Screenwriter))  # => True
print(isinstance(stallone, Filmmaker))     # => True


# ============================================================
# SECTION 5 — WHY FILMMAKER COMES AFTER BOTH BRANCHES
# ============================================================
print([cls.__name__ for cls in Director.mro()])
# => ['Director', 'Filmmaker', 'object']
print([cls.__name__ for cls in Screenwriter.mro()])
# => ['Screenwriter', 'Filmmaker', 'object']

# The combined order must respect these relationships:
# - Director precedes Screenwriter in the declared direct bases.
# - Director precedes Filmmaker in Director's MRO.
# - Screenwriter precedes Filmmaker in Screenwriter's MRO.
# - Filmmaker precedes object.
#
# Therefore, this hierarchy gives:
# JackOfAllTrades -> Director -> Screenwriter -> Filmmaker -> object
#
# C3 combines compatible ordering requirements into one sequence.
# This is neither a general depth-first nor breadth-first traversal.
print(JackOfAllTrades.mro().count(Filmmaker))  # => 1
print(JackOfAllTrades.mro().count(object))     # => 1


# ============================================================
# SECTION 6 — REVERSE THE DIRECT BASES
# ============================================================
class WriterFirst(Screenwriter, Director):
    pass


writer_first = WriterFirst()
writer_first.give_interview()  # => I love writing scripts.

print([cls.__name__ for cls in WriterFirst.mro()])
# => ['WriterFirst', 'Screenwriter', 'Director', 'Filmmaker', 'object']
# The MRO changes, but Screenwriter still supplies the first definition.
# In JackOfAllTrades, lookup passes through Director first.
# In WriterFirst, lookup reaches Screenwriter immediately after the subclass.
# The original JackOfAllTrades class remains unchanged.


# ============================================================
# SECTION 7 — WHEN NEITHER BRANCH OVERRIDES THE METHOD
# ============================================================
class QuietScreenwriter(Filmmaker):
    pass


class GeneralFilmmaker(Director, QuietScreenwriter):
    pass


general = GeneralFilmmaker()
general.give_interview()  # => I love making movies.

print([cls.__name__ for cls in GeneralFilmmaker.mro()])
# => ['GeneralFilmmaker', 'Director', 'QuietScreenwriter', 'Filmmaker', 'object']
# Neither branch defines give_interview, so lookup reaches Filmmaker.
# Sharing an ancestor does not mean calling its method twice.
# An ordinary method call selects one implementation; additional method
# calls would need to be written explicitly in the selected method's body.


# ============================================================
# SECTION 8 — PRACTICE: PREDICT, EXPLAIN, THEN RUN
# ============================================================
# Write predictions in ANSWER comments before uncommenting the examples.

# EXERCISE 1 — IDENTIFY THE DIAMOND
# Which class is the shared ancestor?
# Which two classes are the branches?
# Which class inherits from both branches?
# ANSWER:


# EXERCISE 2 — PREDICT THE OUTPUT
# Director().give_interview()
# Screenwriter().give_interview()
# JackOfAllTrades().give_interview()
# WriterFirst().give_interview()
# ANSWER:


# EXERCISE 3 — EXPLAIN THE INHERITED METHOD
# Director().give_interview() uses Filmmaker's implementation.
# Why does JackOfAllTrades().give_interview() use Screenwriter's instead,
# even though Director is the first direct base?
# ANSWER:


# EXERCISE 4 — WRITE BOTH ORDERS
# Write the complete MRO for each class, including object.
# JackOfAllTrades:
# WriterFirst:
# Why does the different order produce the same interview message?
# ANSWER:


# EXERCISE 5 — ADD AN OVERRIDE TO A BRANCH
# Create a VocalDirector subclass of Director.
# Override give_interview to print "I love directing actors.".
# Create DirectorFirst(VocalDirector, Screenwriter).
# Predict its interview message and MRO, then instantiate it and check.
# Write your code below:


# EXERCISE 6 — OVERRIDE IN THE FINAL SUBCLASS
# Create InterviewStar(Director, Screenwriter).
# Define give_interview directly in InterviewStar with your own message.
# Explain why this definition takes priority over all inherited versions.
# Write your code below:


# OPTIONAL CHALLENGE — BUILD ANOTHER DIAMOND
# Create Artist with a describe method, then Painter and Musician
# subclasses. Override describe only in Musician.
# Create MultiArtist(Painter, Musician) and inspect its MRO.
# Predict the result of describe before running it.
# Explain how your example corresponds to the filmmaker hierarchy.
# ANSWER:


# ============================================================
# SECTION 9 — FINAL REVIEW
# ============================================================
# 1. Diamond inheritance involves branches sharing a common __________.
# 2. Python calculates the MRO using __________ linearization.
# 3. How many times does Filmmaker appear in JackOfAllTrades' MRO?
# 4. Which class defines the method selected for stallone.give_interview()?
# 5. Why must Screenwriter come before Filmmaker in this diamond's MRO?
# 6. Can changing the MRO leave a method call's output unchanged?
# 7. Is "depth-first, then remove earlier duplicates" Python's MRO algorithm?
# 8. Does inheriting a method create a new definition in the subclass?
# ANSWER:
