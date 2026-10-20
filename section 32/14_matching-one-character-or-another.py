# ============================================================
# FILE: 14_matching-one-character-or-another.py
# TOPIC: Alternatives with Character Classes and |
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.

import re


# LESSON OBJECTIVES
# 1. Choose between individual characters or complete patterns.
# 2. Group alternatives to control their scope.
# 3. Understand left-to-right alternative selection.


# ============================================================
# SECTION 1 — CHOOSE ONE CHARACTER WITH A CLASS
# ============================================================
def example_character_alternatives():
    print(re.findall(r"gr[ae]y", "gray grey groy")) # => ['gray', 'grey']
    print(re.findall(r"[ab]", "abc")) # => ['a', 'b']
    print(re.findall(r"a|b", "abc"))  # => ['a', 'b']


# example_character_alternatives()
# [ae] is a concise way to choose one character: a or e.
# | expresses alternation between patterns, which may contain more
# than one character. It does not mean Boolean 'or' in Python code.


# ============================================================
# SECTION 2 — CHOOSE BETWEEN COMPLETE WORDS
# ============================================================
def example_word_alternatives():
    text = "cat dog catalog dogma"
    print(re.findall(r"cat|dog", text)) # => ['cat', 'dog', 'cat', 'dog']
    print(re.findall(r"\b(?:cat|dog)\b", text)) # => ['cat', 'dog']


# example_word_alternatives()
# The noncapturing group (?:...) keeps both alternatives between the
# boundaries without adding a capture that changes findall's return shape.
# [cat|dog] means ONE character from c, a, t, |, d, o, g. Inside that
# class, | is literal; it does not separate words.


# ============================================================
# SECTION 3 — GROUPING CONTROLS THE SCOPE OF ALTERNATION
# ============================================================
def example_group_scope():
    print(re.findall(r"red cat|dog", "red cat dog red dog"))
    # => ['red cat', 'dog', 'dog']
    print(re.findall(r"red (?:cat|dog)", "red cat dog red dog"))
    # => ['red cat', 'red dog']


# example_group_scope()
# Without grouping, red cat|dog means "red cat" OR "dog".
# With grouping, the shared prefix red applies to both alternatives.


# ============================================================
# SECTION 4 — ALTERNATIVES ARE TRIED LEFT TO RIGHT
# ============================================================
def example_alternative_order():
    print(re.search(r"cat|catalog", "catalog").group()) # => cat
    print(re.search(r"catalog|cat", "catalog").group()) # => catalog
    print(re.fullmatch(r"cat|catalog", "catalog").group()) # => catalog


# example_alternative_order()
# At a candidate position, the first branch that lets the entire pattern
# succeed wins; alternation does not automatically choose the longest.
# fullmatch rejects the short branch if it leaves unconsumed input and
# can then succeed with the longer branch.
# To find a literal pipe outside a class, escape it as \|.


# ============================================================
# SECTION 5 — PRACTICE AND FINAL REVIEW
# ============================================================
# EXERCISE: Why isn't [yes|no] a pattern for the words yes or no? __
# CHALLENGE: Validate exactly "yes", "no", or "maybe" using fullmatch,
# ignoring case. Reject longer strings and leading/trailing whitespace.
# Write your code here:
#
# 1. When is a character class simpler than alternation? ________
# 2. Why group alternatives that share a prefix or boundary? ____
# 3. Does | always select the longest matching alternative? _____
# KEY TAKEAWAY: Use classes for one-character choices, alternation
# for full-pattern choices, and grouping to make their scope explicit.

# ============================================================
# END OF LESSON
# ============================================================

