# ============================================================
# FILE: 08_search-for-whitespace-and-non-whitespace.py
# TOPIC: Whitespace and Non-Whitespace: \s and \S
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.

import re


# LESSON OBJECTIVES
# 1. Match spaces, tabs, newlines, and other whitespace.
# 2. Extract non-whitespace runs.
# 3. Recognize when whitespace normalization changes meaning.


# ============================================================
# SECTION 1 — \s MATCHES MORE THAN A SPACE
# ============================================================
def example_whitespace():
    text = "a b\tc\nd"
    print(re.findall(r"\s", text)) # => [' ', '\t', '\n']
    print(re.findall(r"\S+", text)) # => ['a', 'b', 'c', 'd']


# example_whitespace()
# \s matches one whitespace character; \S matches one non-whitespace.
# + collects adjacent characters into a run.
# Non-whitespace includes punctuation; \S+ does not mean letters only.


# ============================================================
# SECTION 2 — NORMALIZE WHITESPACE INTENTIONALLY
# ============================================================
def example_normalize():
    text = "  hello\t\tworld\nagain  "
    normalized = re.sub(r"\s+", " ", text).strip()
    print(normalized) # => hello world again
    print(re.findall(r"\S+", "hello, world!")) # => ['hello,', 'world!']


# example_normalize()
# Replacing \s+ also replaces line breaks. That is useful for a single
# display line, but may destroy meaningful paragraph/code formatting.
# str.split() without arguments often suffices for whitespace tokenization.


# ============================================================
# SECTION 3 — UNICODE WHITESPACE
# ============================================================
def example_unicode_space():
    text = "a\u00a0b" # A non-breaking space between the letters.
    print(re.search(r"\s", text) is not None) # => True
    print(re.search(r"\s", text, flags=re.ASCII) is None) # => True


# example_unicode_space()
# Unicode str matching recognizes more whitespace than ASCII does.
# ASCII \s includes space, tab, newline, carriage return, form feed,
# and vertical tab. To match ONLY a literal space, write a literal space.
# To match spaces or tabs but not newlines, use [ \t]+.


# ============================================================
# SECTION 4 — PRACTICE AND FINAL REVIEW
# ============================================================
# EXERCISE: Does \S+ keep the comma in "hello,"? ________________
# CHALLENGE: Normalize repeated spaces/tabs while preserving newlines.
# Compare the result of [ \t]+ with \s+ on the same multiline input.
# Write your code here:
#
# 1. Is a newline whitespace? _________________________________
# 2. Does \s match only ASCII by default for str? _______________
# 3. Why can whitespace replacement alter meaning? _____________
# KEY TAKEAWAY: Choose whether you mean all whitespace or only
# specific separators before extracting or normalizing text.

# ============================================================
# END OF LESSON
# ============================================================

