# ============================================================
# FILE: 02_search-at-the-beginning-with-match.py
# TOPIC: Matching at the Beginning with match()
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.

import re


# LESSON OBJECTIVES
# 1. Distinguish match() from search().
# 2. Recognize prefix matching versus full-string matching.
# 3. Use fullmatch() when the entire input must satisfy a pattern.


# ============================================================
# SECTION 1 — match() STARTS AT THE BEGINNING
# ============================================================
def example_match_vs_search():
    pattern = re.compile(r"cat")
    print(pattern.match("cat naps").group()) # => cat
    print(pattern.match("a cat") is None)   # => True
    print(pattern.search("a cat").span())   # => (2, 5)


# example_match_vs_search()
# With no position arguments, match() tries only at index zero.
# search() scans forward to find the first match anywhere.
# A successful match() need not consume the entire string.


# ============================================================
# SECTION 2 — PREFIX CHECKS ARE NOT COMPLETE VALIDATION
# ============================================================
def example_fullmatch():
    pattern = re.compile(r"cat")
    print(pattern.match("catalog").group())       # => cat
    print(pattern.fullmatch("catalog") is None)   # => True
    print(pattern.fullmatch("cat").group())       # => cat
    print(pattern.fullmatch("cat ") is None)      # => True


# example_fullmatch()
# fullmatch() requires the whole supplied string to match.
# Whitespace is still part of the input unless the pattern allows it
# or you intentionally normalize the string before validation.


# ============================================================
# SECTION 3 — COMPILED PATTERNS CAN TAKE A START POSITION
# ============================================================
def example_position():
    pattern = re.compile(r"cat")
    text = "a cat"
    match = pattern.match(text, 2)
    print(match.span()) # => (2, 5)


# example_position()
# The optional pos argument changes where a compiled pattern's match()
# starts checking. It does not scan forward from there like search().
# re.MULTILINE does not make match() search each line automatically.


# ============================================================
# SECTION 4 — PRACTICE
# ============================================================
# EXERCISE: Which succeed for "catfish": search, match, fullmatch,
# when the pattern is r"cat"?
# ANSWER: ____________________________________________________
# CHALLENGE: Classify "ERROR disk", "INFO ERROR", and "ERROR"
# using a compiled "ERROR" pattern and match(). Then compare fullmatch().
# Write your code here:


# ============================================================
# SECTION 5 — FINAL REVIEW
# ============================================================
# 1. Does match() scan the whole string? _______________________
# 2. Does a successful match() prove the entire input matches? ___
# 3. Which method is best for full-input validation? ____________
# KEY TAKEAWAY: search finds a match anywhere, match checks a
# starting position, and fullmatch checks the entire input.

# ============================================================
# END OF LESSON
# ============================================================

