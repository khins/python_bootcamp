# ============================================================
# FILE: 01_search-text-with-a-pattern-object.py
# TOPIC: Searching with a Compiled Pattern
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.

import re


# LESSON OBJECTIVES
# 1. Compile a regular expression into a reusable pattern object.
# 2. Search for the first matching substring.
# 3. Inspect a Match object and handle a missing match.


# ============================================================
# SECTION 1 — A PATTERN DESCRIBES TEXT TO FIND
# ============================================================
# A regular expression (regex) describes a text pattern.
# Start with literal characters: "cat" searches for those letters.
# re is Python's standard-library regular-expression module.
# re.compile() creates a reusable Pattern object, not a search result.

def example_compile_and_search():
    pattern = re.compile(r"cat")
    match = pattern.search("A cat naps.")
    if match is not None:
        print(match.group()) # => cat
        print(match.start()) # => 2
        print(match.end())   # => 5
        print(match.span())  # => (2, 5)


# example_compile_and_search()
# search() scans for the first match anywhere in the string.
# start is included; end is excluded, like ordinary slicing.
# group() and group(0) both return the complete matched text.


# ============================================================
# SECTION 2 — A MISSING MATCH RETURNS None
# ============================================================
def example_missing_match():
    pattern = re.compile(r"cat")
    match = pattern.search("A dog naps.")
    print(match is None) # => True
    if match is not None:
        print(match.group())
    else:
        print("No match") # => No match


# example_missing_match()
# Calling .group() on None raises AttributeError. Check first.
# Do not compare str(match) with your expected text; use match.group().


# ============================================================
# SECTION 3 — LITERAL SEARCH IS CASE-SENSITIVE BY DEFAULT
# ============================================================
def example_reuse_pattern():
    pattern = re.compile(r"cat")
    print(pattern.search("Cat") is None) # => True
    print(pattern.search("catalog").group()) # => cat
    print(pattern.search("cat cat").span())  # => (0, 3)


# example_reuse_pattern()
# A literal pattern can match part of a larger word. Word boundaries
# are introduced later. search() returns one Match, not all matches.
# For plain literal membership, "cat" in text may be simpler than regex.


# ============================================================
# SECTION 4 — PRACTICE
# ============================================================
# EXERCISE: What span does re.compile(r"dog").search("my dog") report?
# ANSWER: ____________________________________________________
# CHALLENGE: Compile "Python" once. Search three strings, including
# one without a match. Print the matched text and span, or "Not found".
# Write your code here:


# ============================================================
# SECTION 5 — FINAL REVIEW
# ============================================================
# 1. What does compile() return? _______________________________
# 2. What does search() return on success? On failure? __________
# 3. Is the end index included in the matched slice? ____________
# KEY TAKEAWAY: Compile a pattern, search the text, and inspect the
# Match only after confirming a match exists.

# ============================================================
# END OF LESSON
# ============================================================

