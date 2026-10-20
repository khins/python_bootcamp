# ============================================================
# FILE: 09_search-word-boundaries.py
# TOPIC: Word Boundaries with \b
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.

import re


# LESSON OBJECTIVES
# 1. Match whole regex words using zero-width boundaries.
# 2. Explain the relationship between \b and \w.
# 3. Avoid the ordinary-string backspace escape trap.


# ============================================================
# SECTION 1 — A BOUNDARY IS A POSITION, NOT A CHARACTER
# ============================================================
def example_whole_word():
    text = "cat scatter cat! cat_2"
    print(re.findall(r"cat", text))       # => ['cat', 'cat', 'cat', 'cat']
    print(re.findall(r"\bcat\b", text)) # => ['cat', 'cat']


# example_whole_word()
# \b matches the boundary between a \w and a \W character, or a
# string edge next to a \w character. It consumes no characters.
# Word classification follows Unicode rules unless re.ASCII is used.


# ============================================================
# SECTION 2 — UNDERSCORES AND DIGITS AFFECT BOUNDARIES
# ============================================================
def example_boundaries():
    text = "cat-cat cat_2 cat2"
    print(re.findall(r"\bcat\b", text)) # => ['cat', 'cat']
    print([m.span() for m in re.finditer(r"\b", "hi!")])
    # => [(0, 0), (2, 2)]


# example_boundaries()
# Hyphens are non-word characters, but underscores and digits are word
# characters. Thus cat_2 and cat2 have no word boundary after cat.
# Zero-width matches have equal start/end positions; they still exist.
# Testing match.group() for truthiness can miss a valid empty match.


# ============================================================
# SECTION 3 — RAW STRINGS MATTER HERE
# ============================================================
def example_backspace_trap():
    print(re.search("\bcat\b", "cat") is None) # => True
    print(re.search(r"\bcat\b", "cat").group()) # => cat
    print(re.findall(r"\Bcat\B", "scatter cat")) # => ['cat']


# example_backspace_trap()
# In an ordinary Python string, \b becomes a backspace character.
# In a raw regex string, it reaches re as the boundary escape.
# Inside a bracket character class, [\b] means a backspace, not a boundary.
# \B matches a position that is not a word boundary, as inside scatter.


# ============================================================
# SECTION 4 — PRACTICE AND FINAL REVIEW
# ============================================================
# EXERCISE: Does \bcar\b match "car2", "car!", and "scar"? _____
# CHALLENGE: Find standalone "Python" case-insensitively, excluding
# "Python3" and "myPython". Include punctuation around valid matches.
# Write your code here:
#
# 1. Does \b consume a space or any other character? ____________
# 2. Why isn't an underscore a word separator here? _____________
# 3. Why use r"\bword\b" instead of "\bword\b"? _______________
# KEY TAKEAWAY: Boundaries test positions defined by word-character
# rules; they are not literal spaces or natural-language word parsing.

# ============================================================
# END OF LESSON
# ============================================================

